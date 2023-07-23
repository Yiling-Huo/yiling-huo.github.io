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