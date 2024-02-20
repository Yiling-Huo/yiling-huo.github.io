---
layout: post-narrow
title: Reducing breathing and room noise from speech samples
date: 2023-07-23 10:00
modified_date:
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Python']
comment_issue_id: 10
reading-time: 4
---

On this page I share my Python script that removes breathing and room noise from recordings of my participants' responses in a speech production experiment. 

<!--excerpt-->

I recently started a timed/speeded cloze experiment where participants complete sentences orally within a time limit. Reaction time is important in this paradigm: it reflects how much processing the participant needs before a lexical item wins the "inner competition" and gets produced. However during data processing I discovered a problem: although my recording equipment was good and the environment was quiet, some participants produced loud breathing sounds (they sounded very bored &#128517;) that my onset detection script will mistake as speech onset. Here is what I did to remove these sounds as much as possible in order to get more accurate speech onset data. 

What this script does:
- Based on by-participant noise samples, reduce noise from multiple recordings.
- Optionally normalize the sound volume after noise reduction. 

This script uses the stationary noise reduction method in the [noisereduce](https://timsainburg.com/noise-reduction-python.html) package. 

## Step 1: Preparation

Install Python and these packages: [pydub](https://github.com/jiaaro/pydub), [numpy](https://numpy.org/install/), and [noisereduce](https://github.com/timsainb/noisereduce). 

Download the <a href="/files/resources/python/noise_reduction.py" download>Python script</a> , or see the full script at the end of this page. 

Gather your recordings in one folder. The recordings must contain participant information in the exact same places in the file name. For example: `S01_trial_1.wav` , `S21_trial_1.wav`. 

Get one noise sample for each participant in another folder. The file names should only contain the participant information, such as `S01.wav`, `S21.wav`. the way I did this was to first use my onset detection script on the raw recordings, find out which recordings were affected by noise the most, and then extract a representative noise sample for each person. 

## Step 2: Run the script

Open `noise_reduction.py`  in an IDE and notice these variables:

- audioFormat: string. The format of your recordings (both speech and noise)

- inDir: string. The directory of your recordings.
- noiseDir: string. The directory of your noise samples. 
- outDir: string. Where to save the noise reduced sounds. 

- idFirst: integer. The index of the beginning of your participant info in the recordings' file name. For example, if my recordings have names such as `S01_trial_1.wav`, idFirst should be 0.
- idLast: integer. The index of the end of your participant info (not including the last letter). For something like `S01_trial_1.wav`, this should be 3. 

- normalise: boolean. Whether to normalize sound volume after noise reduction. 
- headroom: float. How close to the maximum volume to boost the signal up to (in dB).

Once you've set all these variables correctly, run the script. The script should first take all sound files in the noiseDir and create a dictionary that has participant ID as keys and noise samples as values. Then the script should take all sound files in inDir and find the corresponding noise sample using info in the file name, then reduce noise. Then, the script can optionally normalize the sound volume, and finally save the output to outDir. 

## Full script

```python
import os
from pydub import AudioSegment, effects
import numpy as np
import noisereduce as nr

##########

# set working directory to the python file's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# set audio format (both input and output)
audioFormat = 'wav'

# input and output directories
inDir = (os.getcwd()+'/recordings/')
noiseDir = (os.getcwd()+'/noise_samples/')
outDir = (os.getcwd()+'/noise_reduced/') 
if not os.path.exists(outDir):
    os.makedirs(outDir)

# set participant identification
'''
For example, if idFirst = 0 and idLast = 3
The script will take each file's first three letters (filename[0:3]) as your participant id
'''
idFirst = 0
idLast = 3

# set whether to normalise volume after noise reduction
'''
normalise = Ture to normalise volume
headroom is how close to the maximum volume to boost the signal up to (in dB)
'''
normalise = True
headroom = 2

##########

print('Input files are taken from ' + inDir)
print('Noise samples are taken from ' + noiseDir)
print('Output files are created in ' + outDir)

# define read and write functions
def read(file):
    a = AudioSegment.from_file(file)
    y = np.array(a.get_array_of_samples())
    return a.frame_rate, y

def write(file, data, rate, format, normalise_volume=True, headr=0.1):
    y = np.int16(data)
    channels = 2 if (data.ndim == 2 and data.shape[1] == 2) else 1
    song = AudioSegment(y.tobytes(), frame_rate=rate, sample_width=2, channels=channels)
    if normalise_volume:
        song = effects.normalize(song, headroom=headr)
    song.export(file, format=format)

print('Reducing noise...')

# get a dictionary of noise samples
noises = {}
noiseList = os.listdir(noiseDir)
for noise in noiseList:
    if noise[-(len(audioFormat)):]==audioFormat:
        r, noises[noise[:-(len(audioFormat))]] = read(noiseDir + noise)

# reduce noise (and optionally normalise volume) for recordings
# https://timsainburg.com/noise-reduction-python.html
# https://github.com/timsainb/noisereduce
fileList = os.listdir(inDir)
for file in fileList:
    if file[-(len(audioFormat)):]==audioFormat:
            print('Sound file: ' + file)
            rate, sound = read(inDir + file)
            noise = noises[file[idFirst:idLast]]
            print('Noise sample: ' + file[idFirst:idLast])
            reduced = nr.reduce_noise(y = sound, y_noise = noise, sr=rate, stationary=True)
            write(outDir+file, reduced, rate, audioFormat, normalise_volume=normalise, headr=headroom)

print ('Done.')
```