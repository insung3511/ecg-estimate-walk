from DataFiltering import DataFiltering
from DataLoader import DataLoader
from tqdm import tqdm

import matplotlib.pyplot as plt
import polars as pl
import numpy as np
import pickle
import gzip
import os

DATA_PATH = "./data/"
print(f"[LOAD] Loading data from {DATA_PATH}")

file_list = os.listdir(DATA_PATH)
print("[LOAD] File list :")
for val in file_list:   print("\t", val)

# Load data
data = DataLoader()
data_filtering = DataFiltering(sampling_rate=250)

# Load data
for file_name in tqdm(file_list):
    if file_name == "README.md":    continue
    if file_name == ".gitignore":   continue

    # Load data
    ecg, rsp, acc_x, acc_y, acc_z = data.dataload(DATA_PATH + file_name)

    filtered_ecg = data_filtering.filtering_auto(ecg)