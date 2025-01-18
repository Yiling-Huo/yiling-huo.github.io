---
layout: post
title: Extract by-interval average formants in Praat
date: 2024-06-27 15:00
modified_date: 2025-01-18 14:00
author: Yiling Huo
# comment_issue_id: 12
category: 'Tutorials' 
tags: ['Psycholinguistics', 'Praat']
reading-time: 2
---

On this page I present a Praat script that extracts by-interval average formants.

<!--excerpt-->

## Step 1: Preparation

Download the <a href="https://gist.github.com/Yiling-Huo/58919bc5b79fb8e4223538995dc07c65">Praat script</a> (or see full script at the end of this page).

Gather your sound files and your .Textgrid files in the same folder. The .Textgrid files should have the same name as the sound files. The .Textgrid files should contain at least one interval tier, based on which mean formants should be extracted. Each interval for which mean formants are needed should have a non-empty name. 

![praat1](/images/tutorials/formant/praat1.png)

## Step 2: Run the script

Download and open [Praat](https://www.fon.hum.uva.nl/praat/).

Select Praat - Open Praat script..., and select the file `get_formants`.

*If on Mac OS, replace the "\" in line 28 with "/".*

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