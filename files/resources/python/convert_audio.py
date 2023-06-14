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
