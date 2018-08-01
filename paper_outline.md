# Time Series Forecasting With LSTM Networks for ENSO Case

***Manuscript Version***
School of Software Engineering, Tongji University, Shanghai 201804, China


Todo

The abstract should summarize the contents of the paper in short terms, i.e. 150-250 words.


time series prediction, LSTM, ARIMA, ENSO.


	* *"The dynamical models use physical equations of the ocean and atmosphere to forecast ENSO event, which are computationally very expensive and not available outside the atmospheric scientific community."*



	* "capturing long-term temporal dependencies" -- LSTM
	* CNN+LSTM has been applied on climate problem, like Sea Level Anomalies (SLA), which show great pontential for such kind of problem.[7]



	* only SST prediction, no specified climate problem analysis.[1]
	* only single nino index (NINO3.4) prediction, no spatio information (pattern) considered, and both network model and data input size can be improved.[2]
	* Todo


	* Single SST prediction (Bohai SST)

	* two aspects -- the structure of the model (different layers, memory cells in each layer) && machine learning algorithms (SVR, MLPR)

	* need more training data

2. 《El niño-southern oscillation forecasting using complex networks analysis of LSTM neural networks》 ***（highly related）***

	* Use climate network to construct input and LSTM network as model to predict ENSO, but just priedict single NINO3.4 index, no spatial information discussed, for the experiment, forecast the  NINO3.4 index from 6-month lead, 9-month lead and 12-month lead, use RMSE and MAE, no contrast experiment. the conclusion said that more data and more complex LSTM neural network is needed. 

	* Nino3.4 + Climate Network (Preprocessing)  --> predict Nino34 with different time leads, and no contrast experiment done.

	* *"We believe this approach has great potential performance skills to augment the ENSO forecasting activity of climate scientists and meteorologists. And our vision is to improve the model by increasing the data sample size and the complexity of the LSTM architecture."*

	* *"To the best of our knowledge, this is the first time this approach has been applied to forecast ENSO phenomenon."*

	* **pyunicorn** --> which is used for construct Climate Network in this paper.


	
	* [How Good Have ENSO Forecasts Been Lately?](https://www.climate.gov/news-features/blogs/enso/how-good-have-enso-forecasts-been-lately) (a good reference when inroduce the prediction situation of ENSO )

		* *"how well the forecasts have matched reality"*
		* lead time --> *" The month from which forecasts are made is often called the start month, and the season that the forecast is for is often called the target season."*
		* measurements (MAE && RMSE && Correlation Coefficient)
		* *"we have a long way to go in improving their performance and utility beyond that.  It is especially hard to predict the timing of ENSO transitions and the correct strength. "*

	* [EXPERT USER GUIDANCE](https://climatedataguide.ucar.edu/climate-data/nino-sst-indices-nino-12-3-34-4-oni-and-tni?qt-climatedatasetmaintabs=1#qt-climatedatasetmaintabs)







	* *"CNNs are particularly suitable for gridded data exploiting the spatial correlations"*
	* LSTM / CNN+ConvLSTM / Sequence LSTM
	* *"reoccuring spatial patterns" (ENSO)*
	* Both in single grid cell (get one grid on the whole region) and grid spatial pattern capture (predict a single img-like grid pattern)
	* *"All the used network designs outperform the regression."*













14. 《Sequence to Sequence Weather Forecasting with Long Short-Term Memory Recurrent Neural Networks》






***Outline:***




***Outline:***



* Single Variable Single Step ( SVSS )
* Single Variable Multi Step ( SVMS )
* Multi Variable Single Step ( MVSS )
* Multi Variable Multi Step ( MVMS )

	Evaluation: Walk-forward Model Validation

	* the single nino index predition with different LSTM networks ( Nino3 / Nino4 / Nino3.4 )
	* different LSTM cell && different LSTM layers && parameters setting
	* different training methods ( Adam / Rmsprop etc. )


	* Baseline prediction ( naive method ) [8]
	* Traditional Machine Learning ( SVR, Random Forecast, MLP etc. )
	* ARIMA model ( Statistics model ) [12]

3. Develop a Robust Result ( Randomness in Machine Learning ) 


	*  Four other index ( SOI, PNA, Nino3, precipitation，ONI ) --> SOI
	*  LSTM model, random forest, linear regression

2. [Nino3 / 4 / 3.4 index Data (1870~2018)](https://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Nino34/) （ Raw Data ）

3. [Time Series Forecasting with the Long Short-Term Memory Network in Python](https://machinelearningmastery.com/time-series-forecasting-long-short-term-memory-network-python/)

	* Raw data --> Difference (stationary) --> Transfer Time series to Supervised learning problem (a list of numbers --> a list of input and output pattern) --> Scale [-1~1] --> Model --> Output

4. [Multi-step Time Series Forecasting with Long Short-Term Memory Networks in Python](https://machinelearningmastery.com/multi-step-time-series-forecasting-long-short-term-memory-networks-python/) ( how to make multistep forecasting )
	* *"The LSTM is stateful; this means that we have to manually reset the state of the network at the end of each training epoch. The network will be fit for 1500 epochs."*

5. [Multivariate Time Series Forecasting with LSTMs in Keras](https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/) ( how to make multivariate forecasting )
	* figure out related ( seem related ) raw data
	* *"multvariate time series forecasting with multiple lag inputs"*


6. [NINO SST INDICES (NINO 1+2, 3, 3.4, 4; ONI AND TNI)](https://climatedataguide.ucar.edu/climate-data/nino-sst-indices-nino-12-3-34-4-oni-and-tni) ( different SST anomalies for different regions)

	* *"Usually the anomalies are computed relative to a base period of 30 years.  The Niño 3.4 index and the Oceanic Niño Index (ONI) are the most commonly used indices to define El Niño and La Niña events. Other indices are used to help characterize the unique nature of each event."*

7. [enso-forecast](https://github.com/lohancock/enso-forecast) ( GitHub, based on R ) 

	* [Trying Out a Planetary Ring System for ENSO Prediction](https://ams.confex.com/ams/98Annual/webprogram/Paper321391.html) (ensemble predict for [MEI](https://www.esrl.noaa.gov/psd/enso/mei/))


8. [How to Make Baseline Predictions for Time Series Forecasting with Python](https://machinelearningmastery.com/persistence-time-series-forecasting-with-python/) ( using current stage as the prediction of the next several steps )


9. [How To Backtest Machine Learning Models for Time Series Forecasting](https://machinelearningmastery.com/backtest-machine-learning-models-time-series-forecasting/)

	* *"A model that remembered the timestamps and value for each observation
would achieve perfect performance."*
	* Train-Test Split
	* Multiple Train-Test Splits
	* *"Walk-forward validation is the gold standard of model evaluation. It is the k-fold cross validation of the time series world and is recommended for your own projects."* 

10. [LSTM Climatological Time Series Analysis](https://github.com/danielefranceschi/lstm-climatological-time-series) ( GitHub )

11. Multivariate ENSO Index(MEI) [wiki](https://en.wikipedia.org/wiki/Multivariate_ENSO_index)

	* 6 variables -- sea-level pressure (P), zonal (U) and meridional (V) components of the surface wind, sea surface temperature (S), surface air temperature (A), and total cloudiness fraction of the sky (C)

12. [ARIMA Model](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)

	* [Time Series Forecast Study with Python: Monthly Sales of French Champagne](https://machinelearningmastery.com/time-series-forecast-study-python-monthly-sales-french-champagne/)


