---
layout: post
title: Extract normalised pitch contour
date: 2023-03-10 13:00
modified_date: 2023-06-14 15:00
author: Yiling Huo
comment_issue_id: 3
category: 'Tutorials' 
tags: ['Psycholinguistics', 'Praat']
reading-time: 5
---

On this page I present a Praat script that extracts pitch contour information based on `.wav` sounds and `.Textgrid` files. 

<!--excerpt-->

This script is useful for analysing lexical tone, but can be also useful for other analyses where pitch contour is important, e.g. intonation. 

## Step 1: Preparation

Download the <a href="/files/resources/praat/extract_pitch_contour" download>Praat script</a> (or see full script at the end of this page).

Gather your `.wav` files and your `.Textgrid` files in the same folder. The `.Textgrid` files should have the same name as the `.wav` files. The `.Textgrid` files should contain at least one interval tier, based on which pitch contour information should be extracted. 

For example, I am extracting the pitch contour of each syllable in a Chinese phrase, for further lexical tone analyses. My `.Textgrid` should contain one interval tier, where each syllable should be a named interval. 

![praat1](/images/tutorials/pitch/praat1.png)

*Note: Inside your `.Textgrid`, you may want to choose to set the interval boundaries around the vowel (where pitch contour information is mostly carried), to better capture the pitch contour. Or you may want to set the interval boundaries around the entire syllable, like what I did with ka and fei in the example, to better represent the length of the syllable, although this will result in some 'undefined'/NA values during some consonants.*

## Step 2: Run the script

Download and open [Praat](https://www.fon.hum.uva.nl/praat/).

Select Praat - Open Praat script..., and select `extract_pitch_contour`.

*If on Mac OS, replace the "\" in line 55 with "/".*

Select Run - Run. You will be presented with a user interface, where you can specify a number of variables. 

- General variables:
    - **Tier number**: index of the tier of interest (where the intervals are defined). 
    - **Sound file extensions**: The extension of should files in your folder (e.g.: .wav)
    - **Result file name**: name of the result file. Recommended extension `.csv`
    - **Normalise by**: precision of sampling. For example, 10 means that Praat will extract pitch information at time 0%, 10%, 20%, ..., 100% (10+1 data points in total); and 50 means that Praat will extract pitch information at times 0%, 2%, 4%, 6%, ..., 100% (50+1 data points in total). 
- Pitch parameters:
    - **Time steps**: (Praat default: 0.0) the measurement interval (frame duration), in seconds. If you supply 0, Praat will use a time step of 0.75 / (pitch floor), e.g. 0.01 seconds if the pitch floor is 75 Hz; in this example, Praat computes 100 pitch values per second.
    - **Pitch floor**: (Praat default: 75 Hz) candidates below this frequency will not be recruited. This parameter determines the length of the analysis window: it will be 3 longest periods long, i.e., if the pitch floor is 75 Hz, the window will be 3/75 = 0.04 seconds long.
    - **Pitch ceiling**: (Praat default: 600 Hz) candidates above this frequency will be ignored.

Define the variables based on what you need, then select OK. Praat will start processing your files, and an output file summarising all pitch information extracted will be created in the same folder:

![csv](/images/tutorials/pitch/csv.png)

The file selection procedure used in this script is from [Scott Seyfarth annotation.Praat](https://gist.github.com/scjs/ffbbba71cc8b3ff9d0476c82b2df9d0f). 

## Full script

```
# Created by Yiling Huo 30/09/2022
# File selection procedure from Scott Seyfarth annotation.Praat (https://gist.github.com/scjs/ffbbba71cc8b3ff9d0476c82b2df9d0f)
# What this script does:
# 1. Takes sound files and textgrid files with the same name, 
# 2. extract all intervals with a name in the selected tier,
# 3. divide each interval into a pre-determined amount of equal-length mini-intervals, 
# 4. extract pitch at each boundary of the mini-intervals, 
# 5. and save all the pitch information in a csv file.

# What this script is good for:
# Extract pitch contour information (e.g. lexical tone) for further analysis. 

# General variables:
    # Tier number: index of the tier of interest (where the intervals are defined).
    # Sound file extensions: The extension of should files in your folder (e.g.: .wav)
    # Result file name: name of the result file. Recommended extension .csv
    # Normalise by: precision of sampling. For example, 10 means that Praat will extract pitch information at time 0%, 10%, 20%, …, 100% (10+1 data points in total); and 50 means that Praat will extract pitch information at times 0%, 2%, 4%, 6%, …, 100% (50+1 data points in total).

# Pitch parameters:
    # Time steps: (Praat default: 0.0) the measurement interval (frame duration), in seconds. If you supply 0, Praat will use a time step of 0.75 / (pitch floor), e.g. 0.01 seconds if the pitch floor is 75 Hz; in this example, Praat computes 100 pitch values per second.
    # Pitch floor: (Praat default: 75 Hz) candidates below this frequency will not be recruited. This parameter determines the length of the analysis window: it will be 3 longest periods long, i.e., if the pitch floor is 75 Hz, the window will be 3/75 = 0.04 seconds long.
    # Pitch ceiling: (Praat default: 600 Hz) candidates above this frequency will be ignored.

form Extract normalised pitch contour
    comment General variables:
    word Sound_file_extension .wav
    sentence Result_file_name pitch.csv
    integer Normalise_by 10
    comment Pitch parameters:
    real Time_steps 0.0
    integer Pitch_floor 75
    integer Pitch_ceiling 600
    comment Press OK to choose a directory of sound files and textgrid files.
endform

procedure getTextGrid: .soundfile$
    .path$ = replace$: .soundfile$, sound_file_extension$, ".TextGrid", 0
    .textgrid = Read from file: .path$
endproc

procedure getFiles: .dir$, .ext$
    .obj = Create Strings as file list: "files", .dir$ + "/*" + .ext$
    .length = Get number of strings

    for .i to .length
        .fname$ = Get string: .i
        .files$ [.i] = .dir$ + "/" + .fname$
    endfor

    removeObject: .obj
endproc

directory$ = chooseDirectory$: "Choose your directory:"
outfile$ = directory$ + "\" + result_file_name$
writeFileLine: outfile$, "file,interval_number,interval_name,n,time,pitch"
@getFiles: directory$, sound_file_extension$

for i to getFiles.length
    soundfile = Read from file: getFiles.files$ [i]
    filename$ = selected$("Sound")

    @getTextGrid: getFiles.files$ [i]

    interval_count = Get number of intervals: tier_number
    intervals# = from_to#(1, interval_count)
    
    for j from 1 to size(intervals#)
        selectObject: getTextGrid.textgrid
        intervaln$ = string$(intervals#[j])
        intervalname$ = Get label of interval: tier_number, intervals#[j]
        if intervalname$ <> ""
            t0 = Get starting point: tier_number, intervals#[j]
            tn = Get end point: tier_number, intervals#[j]
            tj = (tn-t0)/normalise_by

            selectObject: soundfile
            To Pitch: time_steps, pitch_floor, pitch_ceiling
            for k from 0 to normalise_by
                t = t0 + k*tj
                pitch = Get value at time: t, "Hertz", "linear"
                appendFileLine: outfile$, "'filename$', 'intervaln$', 'intervalname$', 'k', 't', 'pitch'"
            endfor
        endif
    endfor

    select all
    Remove
endfor
```