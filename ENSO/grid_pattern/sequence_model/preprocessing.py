'''
Desc: data preprocessing handler.
Author: Kris Peng
Copyright (c) 2018 - Kris Peng <kris.dacpc@gmail.com>
'''
import scipy.io as sio
import numpy as np

DATA_PATH = '../../../../dataset/sst_grid_1/convert_sst.mon.mean_185001_201512.mat'
# DATA_PATH = '../../data/sst_grid/convert_sst.mon.mean_1850_01_2015_12.mat'

len_train = 167
map_height, map_width = 10, 50
MAX = 31.18499947
MIN = 20.33499908
MEAN = 26.80007865

def normalization(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = (data[i][j]- MIN)/(MAX - MIN)
    return data

def inverse_normalization(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = data[i][j]*(MAX - MIN) + MIN
    return data

def load_data_convlstm():
    # load data
    sst_data = sio.loadmat(DATA_PATH)
    sst_data = sst_data['sst'][:,:,:]
    sst_data = np.array(sst_data, dtype=float)

    # (180 * 360 * 2004) --> (10 * 50 * 2004) NINO3.4 region (5W~5N, 170W~120W)
    sst_data = sst_data[85:95,190:240,:]

    min = sst_data.min()
    max = sst_data.max()
    print('=' * 10)
    print("min:", min, "max:", max)
    # todo
    # # 1850.01~2015.01 (train)
    # train_data = sst_data[::,::,0:-12]
    # # 2015.01~2015.12 (test)
    # test_data = sst_data[::,::,-12:]

    # sst min:20.33 / max:31.18
    convert_sst = np.zeros((len_train,12,map_height,map_width,1), dtype = np.float)
    for i in range(len_train):
        for k in range(12):
            # Year * 12 + currentMonth
            convert_sst[i,k,::,::,0] = normalization(sst_data[::,::,i*12+k])
    return convert_sst

def load_data_resnet():
    # load data
    sst_data = sio.loadmat(DATA_PATH)
    sst_data = sst_data['sst'][:,:,:]
    sst_data = np.array(sst_data, dtype=float)

    # (180 * 360 * 2004) --> (10 * 50 * 2004) NINO3.4 region (5W~5N, 170W~120W)
    sst_data = sst_data[85:95,190:240,:]

    min = sst_data.min()
    max = sst_data.max()
    print('=' * 10)
    print("min:", min, "max:", max)

    # sst min:20.33 / max:31.18
    convert_sst = np.zeros((len_train,12,map_height,map_width), dtype = np.float)
    for i in range(len_train):
        for k in range(12):
            # Year * 12 + currentMonth
            convert_sst[i,k,::,::] = normalization(sst_data[::,::,i*12+k])
    return convert_sst