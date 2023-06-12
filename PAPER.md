# Deep Learning Approaches for Estimate Steps from RAW ECG Signals

Our project aims to estimate walking steps from raw electrocardiogram (ECG) signals obtained from wearable devices. The ECG signals collected during walking contain baseline wander, which the project hypothesizes can be converted to signals from an inertia measurement unit (IMU). This approach is relevant to monitoring physical performance during walking, jogging, and running, which are popular leisure activities for people pursuing fitness. Wearable devices with IMUs are commonly used to monitor physical performance during these activities. Additionally, other studies have investigated walking at different speeds and inclines, as well as climbing stairs, to better understand human locomotion.

## Data Collecting Method

The data in this project was collected using the [HiCardi Smartpatch](https://www.me-zoo.com/main/html.php?htmid=products/hicardisystem2.html) device. This device was provided during the "Healthcare Device" class at Hallym University, and the project was conducted using the Electrocardiogram, Accelerometer X, Y, Z 3-axis signals obtained from the device.

Three situations were assumed and measured during data collection:

- Signals generated during normal walking outdoors
- Signals generated during relatively intense walking indoors and outdoors
- Signals generated while sitting still indoors

The signals generated during normal walking are the most crucial signals for me. I collected data by focusing on the number of steps taken in daily life, and a total of 45 minutes of data was collected. To obtain data for various situations, I acquired signals while running on the on-campus track and using a treadmill at the on-campus gym, each for 10 minutes. Lastly, I obtained signals while sitting still.

I used a mobile device and a laptop for signal acquisition, and the acquisition software was provided during the class.

## Data Pre-processing

In order to view the data at 30-second intervals, I performed data preprocessing using `data_preprocessing.py`. The sampling rate is set to 250 samples for the ECG signal and 25 samples for the accelerometer 3-axis signal. First, I concatenated the signals generated in the same situation into one signal, and this process is described in `ecg_30sec.ipynb`. Then, I applied signal preprocessing using `data_preprocessing.py`.

For the ECG signal, I segmented the signal at 30-second intervals by moving a window, squared the segments, and applied MinMaxScaler. As for the accelerometer, I also extracted segments of the signal at 30-second intervals using a window, squared each axis of the accelerometer 3-axis signal, summed them up, and then applied the square root [(Ref link)](https://www.quora.com/How-do-I-calculate-total-acceleration-from-the-x-y-and-z-g-force-values-given-by-an-accelerometer). Through this process, all signals were prepared, and then I proceeded with Deep Learning Regression Modeling.

Note: It is recommended to provide more specific information about the Deep Learning Regression Modeling process, such as the architecture used and any specific techniques or libraries employed.

## Modeling

We have tried multiple models. The first one was using CNN + GRU. However, the model took too long to train, and the Mean Squared Error (MSE) loss showed values close to 20,000, which were not acceptable.

Next, you used a Transformer Encoder model, and the code for this model is written in `model_30sec.ipynb`. You constructed the model using a Transformer Encoder and added a Fully Connected Layer at the end. Although the training loss and validation loss of the model decreased nicely, the overall results were not satisfactory.

After that, you built a Deep Fully Connected Layer model. The code for this model is implemented in `model_30sec_fc.ipynb`. It provided faster results compared to the Transformer Encoder model, but it had a problem of quickly getting stuck in local minimums. To address this issue, you concluded that the model might not be performing proper feature extraction, so you added an RNN model.

Finally, you applied an LSTM + Fully Connected Layer model, and the code for this model is written in `model_30sec_rnn.ipynb`. Based on your understanding, the LSTM model captures the temporal characteristics of the time series data and assigns significant meaning to each data point. The Fully Connected Layer then relates the features extracted by the RNN to the regression task.

In conclusion, the LSTM + Fully Connected Layer model showed the best performance. It exhibited well-settled training and validation loss values, indicating its effectiveness in capturing the patterns in the data.