
#load packages

import neurokit2 as nk
import pandas as pd
import  matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = [15, 9]  # Bigger images
plt.rcParams['font.size']= 13

filename = "/Users/elise/PycharmProjects/MASMRanalysis/MASMRpractice/003ASMR.acq"
data, sampling_rate = nk.read_acqknowledge(filename)
#note: all sampling rates are 2000hz



# Process ecg
#ecg_signals, info = nk.ecg_process(data["ECG"], sampling_rate=2000)
#plot = nk.ecg_plot(ecg_signals[:3000], sampling_rate=100)


#UNFINISHED - create a dictionary of events and pass events into the events parameter
#epochs = nk.epochs_create(ecg_signals, events=[0, 15000], sampling_rate=100, epochs_start=0, epochs_end=150)