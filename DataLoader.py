from ecgdetectors import Detectors

import pandas as pd
import numpy as np

class DataConcate:
    def dataconcate(self, *args):
        concated_data = np.concatenate(args, axis=0)
        return concated_data

class DataLoader:
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
    
    def is_over_1min(self, signal, one_min_samp_rate: int):
        if len(signal) >= one_min_samp_rate: return True
        else: return False

    def export_ecg_1min(self, signal, samp_rate: int = 250):
        one_min = samp_rate * 60
        cnt = int(len(signal) / one_min)
        detectors = Detectors(samp_rate)

        exported_signal = list()
        for i in range(cnt):
            start = i * one_min
            end = (i + 1) * one_min
            if i == cnt - 1: end = len(signal)
            
            if end - start == one_min: exported_signal.append(signal[start:end] ** 2)
            else: break

        return exported_signal

    def export_ecg_30sec(self, signal, samp_rate: int = 250):
        thirty_sec = samp_rate * 30
        cnt = int(len(signal) / thirty_sec)
        detectors = Detectors(samp_rate)

        exported_signal = list()
        for i in range(cnt):
            start = i * thirty_sec
            end = (i + 1) * thirty_sec
            if i == cnt - 1: end = len(signal)
            
            if end - start == thirty_sec: exported_signal.append(signal[start:end] ** 2)
            else: break

        return exported_signal 
    
    def export_acc_1min(self, signal, samp_rate: int = 25):
        one_min = samp_rate * 60
        cnt = int(len(signal) / one_min)

        exported_signal = list()
        for i in range(cnt):
            start = i * one_min
            end = (i + 1) * one_min
            if i == cnt - 1: end = len(signal)

            if end - start == one_min: exported_signal.append(signal[start:end])
            else: break

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