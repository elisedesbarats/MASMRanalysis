
#load packages

import neurokit2 as nk
import pandas as pd
import bioread
import  matplotlib.pyplot as plt


'''
Import the Data 
note: all sampling rates are 2000hz
'''

plt.rcParams['figure.figsize'] = [15, 9]  # Bigger images
plt.rcParams['font.size']= 13

filename = "/Users/elise/PycharmProjects/MASMRanalysis/MASMRpractice/003ASMR.acq"
eda_signal, sampling_rate = nk.read_acqknowledge(filename)


'''
 Process the raw EDA signal (unfinished)
'''

signal, info = nk.eda_process(eda_signal["EDA, Y, PPGED-R"], sampling_rate=2000)

'''
FIND EVENTS 
fill the dictionary with events as they happen (change in channels)
label them with a time and a name for which type of stimulus it was 
'''

events = {}


# Process ecg
#ecg_signals, info = nk.ecg_process(data["ECG"], sampling_rate=2000)
#plot = nk.ecg_plot(ecg_signals[:3000], sampling_rate=100)


#UNFINISHED - create a dictionary of events and pass events into the events parameter
#epochs = nk.epochs_create(ecg_signals, events=[0, 15000], sampling_rate=100, epochs_start=0, epochs_end=150)