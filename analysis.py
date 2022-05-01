
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

participant1 = "/Users/elise/PycharmProjects/MASMRanalysis/MASMRpractice/003ASMRcut.acq"
data1, sampling_rate = nk.read_acqknowledge(participant1)

#particpant2 = "/Users/elise/PycharmProjects/MASMRanalysis/MASMRpractice/004ASMR.acq"
#data2, sampling_rate = nk.read_acqknowledge(particpant2)

'''
TURN PPG INTO HEART RATE 
'''


ppg1signals, ppg1info = nk.ppg_process(data1['PPG, X, PPGED-R'], sampling_rate = 2000)
fig = nk.ppg_plot(ppg1signals)
#need to use fixpeaks function


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
PROCESS TEMPERATURE 
'''

'''
PROCESS SLIDER 
'''

'''
FIND START AND EVENTS - events are how we make epochs, epochs are what we analyse 
check change in channels - on is 5v, off is 0v, channels are 5,6,7
first channel to change within the first 30 seconds indicates start of epochs 

iterate through the 3 columns 
perform events_find on each column (1 array) 
append into events dictionary 
'''

#gets the events and adds name- need to change into capitals
BaselineEvents1 = nk.events_find(data1["Baseline"],threshold=0, threshold_keep='above')
BaselineEvents1["name"] = "Baseline"
ControlEvents1 = nk.events_find(data1.iloc[:,4],threshold=0, threshold_keep='above')
ControlEvents1["name"] = "Control"
ASMRevents1 = nk.events_find(data1["ASMR"], threshold=0, threshold_keep="above")
ASMRevents1["name"] = "ASMR"

#events into one dictionary
events = {}
EventsArrayList = [BaseLineEvents1,ControlEvents1, ASMRevents1]
for i in eventsarraylist:
     eventonset = i["onset"]
     name = i["name"]
     events[name] = eventonset

#order list by onset to get order of conditions and rename ASMRcondition, BaselineCondition etc.

'''

to  be readable by events_plot needs to be a dictionary like this: 
{'onset': array([ 1024,  4957,  9224, 12984]),
 'duration': array([300, 300, 300, 300]),
 'label': array(['1', '2', '3', '4'], dtype='<U11'),
 'condition': ['Negative', 'Neutral', 'Neutral', 'Negative']}
 
 probably make lists and get it to update 'condition' with  'name'
'''



'''
EPOCHS - split into 3 second chunks - epochs is a dictionary of df's 
'''
filelength =
epochevents = [a = [i for i in range (filelength) if i%3 == 0]]
epochs = nk.epochs_create(allsignals, events = epochevents, sampling_rate=2000, epochs_start=0, epochs_end=150)

'''
RATING - assign epochs a rating and a stimuli type (control, baseline, asmr)   
'''
#we have a df for every 3 second epoch - need to organise these into 3 groups
#update df with a rating column and stimuli type column
#epochs with times - do if statements for before conditions [1], conditions [2], assign with label for that condition
#label based on those

#Rating - epoch will have TSA slider info - update df with an if statement
'''
MATCH
1. epoch of same time value from start of the control period for participant2 (NOT same rating) 
2. 

iteration of the analysis will input data from experimental participant and
just baseline / control data from the yoked participant 

start time of experimental epoch 
in each epoch:
( epoch(value) - baseline(value) ) - 

'''