
#load packages

import neurokit2 as nk
import pandas as pd
import bioread
import matplotlib
import matplotlib.pyplot as plt

'''
Import the Data of two participants 
participant1 and data1 = primary 
participant2 and data2 = matched control 
note: all sampling rates are 2000hz
'''

plt.rcParams['figure.figsize'] = [15, 9]  # Bigger images
plt.rcParams['font.size']= 13

participant1 = "/Users/elise/PycharmProjects/MASMRanalysis/MASMRpractice/003ASMR.acq"
data1, sampling_rate = nk.read_acqknowledge(participant1)

#particpant2 = "/Users/elise/PycharmProjects/MASMRanalysis/MASMRpractice/004ASMR.acq"
#data2, sampling_rate = nk.read_acqknowledge(particpant2)

'''
TURN PPG INTO HEART RATE 
'''


ppg1signals, ppg1info = nk.ppg_process(data1['PPG, X, PPGED-R'])



'''
 Process EDA signal (unfinished)
'''

eda1signals, eda2info = nk.eda_process(data["EDA, Y, PPGED-R"], sampling_rate=2000) #cleans the signal

# Extract clean EDA and SCR features
cleaned = signal["EDA_Clean"]
features = [info["SCR_Onsets"], info["SCR_Peaks"], info["SCR_Recovery"]]

# Visualize - dont really need to do this

edaplot = nk.eda_plot(signal)
data["EDA_Raw"] = eda_signal
plt.show()

'''
FIND START 
check change in channels 
first channel to change within the first 30 seconds indicates start of epochs 
'''

events = {}

#UNFINISHED - create a dictionary of events and pass events into the events parameter
#epochs = nk.epochs_create(ecg_signals, events=[0, 15000], sampling_rate=100, epochs_start=0, epochs_end=150)

'''
EPOCHS - split into 3 second chunks 
'''

'''
RATING - assign epochs a rating and a stimuli type (control, baseline, asmr)   
'''

'''
MATCH epoch of same time value from start of the control period for participant2 (NOT same rating) 
iteration of the analysis will input data from experimental participant and
just baseline / control data from the yoked participant 

start time of experimental epoch 

'''