---
layout: post-narrow
title: Convert audio file formats using Python
date: 2023-06-14 10:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Python']
reading-time: 2
comment_issue_id: 8
---

I work closely with auditory stimuli. Sometimes I need to convert a large number of audio files from one format to another, usually because different experiment software works better with different audio formats. Here I share my Python script that converts all audio files in a folder from one format to another.

<!--excerpt-->

## Step 1: Preparation

Install [ffmpeg](https://ffmpeg.org/download.html). Remember to put ffmpeg in your PATH.

Install [Python](https://www.python.org/downloads/) (obviously) and pydub: `pip install pydub`. 

Download the <a href="/files/resources/python/convert_audio.py" download>Python script</a> (or see full script at the end of this page). Gather all your files in a folder. 

## Step 2: Run the script

Open `convert_audio.py` in an IDLE. Modify these variables: 

- AudioSegment.converter: string. Path to your `ffmpeg.exe`.
- AudioSegment.ffmpeg: string. Path to your `ffmpeg.exe`.
- AudioSegment.ffprobe: string. Path to your `ffprobe.exe`.

- dataDir: string. Input folder. Where your original audio files are located.
- outDir: string. Output folder. Where you want your converted files.
- input_format: string. Format of your original audio files. **Please include '.'**.
- output_format: string. Format of your output audio files. **Please include '.'**.

Run the script. Pydub is going to call ffmpeg to convert all files in your chosen folder with the original extension to the output format. 

## Full script

```python
import os
from pydub import AudioSegment

# set working directory to the python file's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# force pydub to find ffmpeg
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\bin\\ffprobe.exe"

# chose input and output folders (where the original files are and where you want to save new files)
dataDir = (os.getcwd() + '/') # input folder
outDir = (os.getcwd()+'/output/') # output folder
if not os.path.exists(outDir):
    os.makedirs(outDir)
print ('Input files are taken from ' + dataDir)
print ('Output files are created in ' + outDir)

# set up input and output formats
input_format = '.mp3'
output_format = '.wav'

dataFileList = os.listdir(dataDir)
for dataFile in dataFileList:
    if dataFile[-(len(input_format)):]==input_format:
        print ('Loading ' + dataFile + '...')
        try:
            sound = AudioSegment.from_file(dataFile)
            outname = outDir + dataFile[:-(len(input_format))] + output_format
            print("Output file: " + outname)
            sound.export(outname, format=output_format[-1:])
        except IOError:
            print('cannot open file ')

print ('Done.')
```