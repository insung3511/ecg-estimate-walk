import polars as pl
import numpy as np

class DataLoader:
    def dataload(self, data_path):
        df = pl.read_csv(data_path, has_header=False, separator="\t")

        # ECG
        ecg = df[:, 11:60].to_numpy().flatten()

        # RSP
        rsp = df[:, 61:65].to_numpy().flatten()

        # Accelerometer
        acc_x = df[:, 66:70].to_numpy().flatten()
        acc_y = df[:, 71:75].to_numpy().flatten()
        acc_z = df[:, 76:80].to_numpy().flatten()

        # Heart Rate
        heart_rate = df[:, 1].to_numpy().flatten()

        return ecg, rsp, acc_x, acc_y, acc_z, heart_rate
