---
layout: post
title: Extract by-interval mean formants in Praat
date: 2024-06-27 15:00
# modified_date: 2023-06-14 15:00
author: Yiling Huo
comment_issue_id: 12
category: 'Tutorials' 
tags: ['Psycholinguistics', 'Praat']
reading-time: 2
---

On this page I present a Praat script that extracts by-interval mean formants.

<!--excerpt-->

## Step 1: Preparation

Download the <a href="/files/resources/praat/get_formants" download>Praat script</a> (or see full script at the end of this page).

Gather your sound files and your .Textgrid files in the same folder. The .Textgrid files should have the same name as the sound files. The .Textgrid files should contain at least one interval tier, based on which mean formants should be extracted. Each interval for which mean formants are needed should have a non-empty name. 

![praat1](/images/tutorials/formant/praat1.png)

## Step 2: Run the script

Download and open [Praat](https://www.fon.hum.uva.nl/praat/).

Select Praat - Open Praat script..., and select the file `get_formants`.

Select Run - Run. You will be presented with a user interface, where you can specify a number of variables. 

- **Sound file extensions**: The extension of should files in your folder (e.g.: .wav)
- **Result file name**: name of the result file. This file will be comma-separated, so I recommend using the `.csv` extension. 
- **Tier number**: index of the tier of interest (where the intervals are defined). 

![praat2](/images/tutorials/formant/praat2.png)

Edit if needed, then select OK. You will be given a chance to choose a folder. All files with your defined extension and .Textgrid files with the same names will be processed. A .csv file will be created, which contains the following:

- The name of the sound file
- The number of the interval
- The name of the interval
- The average formants

![csv](/images/tutorials/formant/csv.png)

The file selection procedure used in this script is from [Scott Seyfarth annotation.Praat](https://gist.github.com/scjs/ffbbba71cc8b3ff9d0476c82b2df9d0f). 

## Full script

```
form Get by-interval average formants
    word Sound_file_extension .wav
    sentence Output_file_name formants.csv
    integer Tier_number 1
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

procedure getTextGrid: .soundfile$
    .path$ = replace$: .soundfile$, sound_file_extension$, ".TextGrid", 0
    .textgrid = Read from file: .path$
endproc

directory$ = chooseDirectory$: "Choose a directory:"
outfile$ = directory$ + "\" +output_file_name$
writeFileLine: outfile$, "file,interval_number,interval_name,start_time,end_time,f1,f2,f3,f4"
@getFiles: directory$, sound_file_extension$

for i to getFiles.length
    soundfile = Read from file: getFiles.files$ [i]
    filename$ = selected$("Sound")
    filename_full$ = filename$ + sound_file_extension$

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
            selectObject: soundfile
            Edit
            editor: soundfile
                Select: t0, tn
                f1 = Get first formant
                f2 = Get second formant
                f3 = Get third formant
                f4 = Get fourth formant
            Close
            appendFileLine: outfile$, "'filename_full$', 'intervaln$', 'intervalname$', 't0', 'tn', 'f1', 'f2', 'f3', 'f4'"
        endif
    endfor

    select all
    Remove
endfor
```