# Import necessary libraries 
from pydub import AudioSegment 
import os
import numpy as np
import pylab as plt

path = r"..\ICAP"
files = os.listdir(path)
files = [path + "\\" + f for f in files if f.endswith('.wav')]

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

for i in range(len(files)):
    FileName = files[i]
    print("CutFile File Name is ",FileName)
    audio = AudioSegment.from_file(FileName,format="wav")
    (filepath,tempfilename) = os.path.split(FileName)
    (name,extension) = os.path.splitext(tempfilename)
    print(name)
    n = len(audio) 
    counter = 1
    interval = 30 * 1000
    overlap = 0
      
    start = 0
    end = 0
      
    # Flag to keep track of end of file. 
    # When audio reaches its end, flag is set to 1 and we break 
    flag = 0
      
    # Iterate from 0 to end of the file, 
    # with increment = interval 
    for i in range(0,  n, interval): 
        if i == 0: 
            start = 0
            end = interval 
        else: 
            start = end - overlap 
            end = start + interval  
      
        # When end becomes greater than the file length, 
        # end is set to the file length 
        # flag is set to 1 to indicate break. 
        if end >= n: 
            end = n 
            flag = 1
      
        # Storing audio file from the defined start to end 
        chunk = audio[start:end] 
      
        # Filename / Path to store the sliced audio 
        filename = name + '-' +str(counter)+'.wav'
      
        createFolder('./'+name+'/')
        # Store the sliced audio file to the defined path 
        chunk.export('./'+name+'/' + filename, format ="wav") 
        # Print information about the current chunk 
        print("Processing chunk "+str(counter)+". Start = "
                            +str(start)+" end = "+str(end)) 
      
        # Increment counter for the next chunk 
        counter = counter + 1
          
        # Slicing of the audio file is done. 
        # Skip the below steps if there is some other usage 
        # for the sliced audio files. 