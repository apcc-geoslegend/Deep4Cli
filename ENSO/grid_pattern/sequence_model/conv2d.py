'''
Desc: the Grid CNN model for ENSO Case
Author: Kris Peng
Data: https://www.esrl.noaa.gov/psd/data/gridded/data.cobe2.html
Copyright (c) 2018 - Kris Peng <kris.dacpc@gmail.com>
'''

from keras.models import Sequential
from keras.utils import multi_gpu_model
from keras.layers.convolutional import Conv3D
from keras.layers.convolutional_recurrent import ConvLSTM2D
from keras.layers.normalization import BatchNormalization
import pylab as plt
from matplotlib import pyplot
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib as mpl
# from parallel_model import ParallelModel
import scipy.io as sio


seq = Sequential()
seq.add(ConvLSTM2D(filters=40, kernel_size=(3, 3),
                   input_shape=(None, 10, 50, 1),
                   padding='same', return_sequences=True))
seq.add(BatchNormalization())

seq.add(ConvLSTM2D(filters=40, kernel_size=(3, 3),
                   padding='same', return_sequences=True))
seq.add(BatchNormalization())

seq.add(ConvLSTM2D(filters=40, kernel_size=(3, 3),
                   padding='same', return_sequences=True))
seq.add(BatchNormalization())

seq.add(ConvLSTM2D(filters=40, kernel_size=(3, 3),
                   padding='same', return_sequences=True))
seq.add(BatchNormalization())

seq.add(Conv3D(filters=1, kernel_size=(3, 3, 3),
               activation='sigmoid',
               padding='same', data_format='channels_last'))

seq = multi_gpu_model(seq, gpus=2)

seq.compile(loss='binary_crossentropy', optimizer='adadelta')


# data preprocessing
sst = '../../../../dataset/sst_grid_1/convert_sst.mon.mean_185001_201512.mat'
sst_data = sio.loadmat(sst)

sst_data = sst_data['sst'][:,:,:]
sst_data = np.array(sst_data, dtype=float)


# (180 * 360 * 2004)
# print(sst_data.shape)
# (180 * 360 * 2004) --> (10 * 50 * 2004)
sst_data = sst_data[85:95,190:240,:]

# temp_sst = sst_data.reshape((50*10*2004))
# series_sst_data = pd.Series(temp_sst)
# print(series_sst_data.describe())
# print(sst_data.shape)
# print(sst_data[::,::,0])
# print("Mean: %s" % sst_data.mean())
# print("Max: %s , Loc: %s" % (sst_data.max(), sst_data.argmax()))
# print("Min: %s , Loc: %s" % (sst_data.min(), sst_data.argmin()))
# 1850.01~2015.01 (train)
train_data = sst_data[::,::,0:-12]
# 2015.01~2015.12 (test)
test_data = sst_data[::,::,-12:]

# print(train_data.shape)
# print(test_data.shape)
convert_sst = np.zeros((166,12,10,50,1), dtype = np.float)
for i in range(166):
    for k in range(12):
        convert_sst[i,k,::,::,0] = train_data[::,::,i*12+k]

noisy_movies = convert_sst
shifted_movies = convert_sst

seq.fit(noisy_movies[:160], shifted_movies[:160], batch_size=10,
        epochs=300, validation_split=0.05)

# # Testing the network on one movie
# feed it with the first 7 positions and then
# predict the new positions
which = 100
track = noisy_movies[which][:7, ::, ::, ::]

for j in range(12):
    new_pos = seq.predict(track[np.newaxis, ::, ::, ::, ::])
    new = new_pos[::, -1, ::, ::, ::]
    track = np.concatenate((track, new), axis=0)


# # And then compare the predictions
# # to the ground truth
track2 = noisy_movies[165][::, ::, ::, ::]
for i in range(12):
    fig = plt.figure(figsize=(10, 5))

    ax = fig.add_subplot(121)

    if i >= 7:
        ax.text(1, 3, 'Predictions !', fontsize=20, color='w')
    else:
        ax.text(1, 3, 'Initial trajectory', fontsize=20)

    toplot = track[i, ::, ::, 0]

    plt.imshow(toplot)
    ax = fig.add_subplot(122)
    plt.text(1, 3, 'Ground truth', fontsize=12)

    toplot = track2[i, ::, ::, 0]
#     if i >= 2:
    toplot = shifted_movies[165][i - 1, ::, ::, 0]

    plt.imshow(toplot)
    cbar = plt.colorbar(plt.imshow(toplot), orientation='horizontal')
    cbar.set_label('°C',fontsize=12)
    cbar.set_ticks(np.linspace(20,32,13))
    cbar.set_ticklabels(('20','21','22','23','24','25','26','27','28','29','30','31','32'))
    plt.savefig('%i_animate.png' % (i + 1))
