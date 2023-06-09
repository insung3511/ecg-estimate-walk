from DataFiltering import DataFiltering
from scipy.signal import find_peaks
from ecgdetectors import Detectors

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import peakutils

class DataConcate:
    def dataconcate(self, *args):
        concated_data = np.concatenate(args, axis=0)
        return concated_data

class DataLoader:
    def __init__(self):
        self.filter = DataFiltering(sampling_rate=250)

    def dataload(self, data_path):
        if 'mobile' in data_path:   
            print("MOBILE", data_path)
            df = pd.read_csv(data_path, header=None, sep="\s+")

        else:   
            print("NON Mobile", data_path)
            df = pd.read_csv(data_path, header=None, sep="\t")

        # ECG
        ecg = df.loc[:, 11:60].to_numpy().flatten()

        # RSP
        rsp = df.loc[:, 61:65].to_numpy().flatten()

        # Accelerometer
        acc_x = df.loc[:, 66:70].to_numpy().flatten()
        acc_y = df.loc[:, 71:75].to_numpy().flatten()
        acc_z = df.loc[:, 76:80].to_numpy().flatten()

        # Heart Rate
        heart_rate = df.loc[:, 1].to_numpy().flatten()

        return ecg, rsp, acc_x, acc_y, acc_z, heart_rate

    def raw_export_ecg_30sec(self, org_signal, samp_rate: int = 250):
        thirty_sec = samp_rate * 30
        cnt = int(len(org_signal) / thirty_sec)

        exported_signal = list()
        for i in range(cnt):
            start = i * thirty_sec
            end = (i + 1) * thirty_sec

            if i == cnt - 1: 
                end = len(signal)
            
            if end - start == thirty_sec and org_signal[start:end].shape[0] == thirty_sec:
                signal = org_signal[start:end]
                exported_signal.append(signal)

            else: 
                break

        return exported_signal 
 
    def export_ecg_30sec(self, org_signal, samp_rate: int = 250):
        thirty_sec = samp_rate * 30
        cnt = int(len(org_signal) / thirty_sec)

        exported_signal = list()
        for i in range(cnt):
            start = i * thirty_sec
            end = (i + 1) * thirty_sec

            if i == cnt - 1: 
                end = len(signal)
            
            if end - start == thirty_sec and org_signal[start:end].shape[0] == thirty_sec:
                signal = org_signal[start:end]
                exported_signal.append(signal ** 2)

            else: 
                break

        return exported_signal 
    
    def export_acc_30sec(self, signal, samp_rate: int = 25):
        thirty_sec = samp_rate * 30
        cnt = int(len(signal) / thirty_sec)

        exported_signal = list()
        for i in range(cnt):
            start = i * thirty_sec
            end = (i + 1) * thirty_sec
            if i == cnt - 1: end = len(signal)

            if end - start == thirty_sec: exported_signal.append(signal[start:end])
            else: break

        return exported_signal