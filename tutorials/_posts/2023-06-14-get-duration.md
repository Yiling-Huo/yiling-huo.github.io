---
layout: post-narrow
title: Get audio file durations using Praat
date: 2023-06-14 14:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Praat']
---

On this page I share a Praat script that gets audio file durations from a directory containing audio files. The script outputs a .csv file.

<!--excerpt-->

## Step 1: Preparation

Download the <a href="/files/resources/praat/get_duration" download>Praat script</a> (or see full script at the end of this page). Gather all your files in a folder. 

## Step 2: Run the script

Open [Praat](https://www.fon.hum.uva.nl/praat/) and Select Praat - Open Praat script..., and select the `get duration` script.

Select Run - Run. You will be taken to a window where you can choose where your audio files are located. 

<img src="/images/tutorials/get_duration/ui.png"  width="49%">

After choosing the directory, Praat is going to look at all files with the provided extension, get the files' durations, and create a output .csv file in the same folder. The output should look like this:

![output](/images/tutorials/get_duration/output.png)

The file selection procedure used in this script is from [Scott Seyfarth annotation.Praat](https://gist.github.com/scjs/ffbbba71cc8b3ff9d0476c82b2df9d0f). 

## Full script

```
form Get audio file duration
    word Sound_file_extension .mp3
    sentence Output_file_name output.csv
    comment Press OK to choose a directory.
endform

procedure getFiles: .dir$, .ext$
    .obj = Create Strings as file list: "files", .dir$ + "/*" + .ext$
    .length = Get number of strings

    for .i to .length
        .fname$ = Get string: .i
        .files$ [.i] = .dir$ + "/" + .fname$

    endfor

    removeObject: .obj

endproc

directory$ = chooseDirectory$: "Choose a directory:"
outfile$ = directory$ + "\" +output_file_name$
writeFileLine: outfile$, "file,duration"
@getFiles: directory$, sound_file_extension$

for i to getFiles.length
    soundfile = Read from file: getFiles.files$ [i]
    filename$ = selected$("Sound")
    filename_full$ = filename$ + sound_file_extension$
    duration = Get total duration
    duration_mili = duration * 1000
    appendFileLine: outfile$, "'filename_full$', 'duration_mili'"

    select all
    Remove
endfor
```