---
layout: post
title: Extract normalised pitch contour
date: 2023-03-10 13:00
author: Yiling Huo
categories: [Tutorials, 'Psycholinguistics']
---

On this page I present a Praat script that extracts pitch contour information based on `.wav` sounds and `.Textgrid` files. 

<!--excerpt-->

This script is useful for analysing lexical tone, but can be also useful for other analyses where pitch contour is important, e.g. intonation. 

## Step 1: Preparation

Download the <a href="/files/resources/praat/extract_pitch_contour" download>Praat script</a>.

Gather your `.wav` files and your `.Textgrid` files in the same folder. The `.Textgrid` files should have the same name as the `.wav` files. The `.Textgrid` files should contain at least one interval tier, based on which pitch contour information should be extracted. 

For example, I am extracting the pitch contour of each syllable in a Chinese phrase, for further lexical tone analyses. My `.Textgrid` should contain one interval tier, where each syllable should be a named interval. 

![praat1](/images/tutorial_pitch/praat1.png)

## Step 2: Run the script

Download and open [Praat](https://www.fon.hum.uva.nl/praat/).

Select Praat - Open Praat script..., and select `extract_pitch_contour`.

Select Run - Run. You will be presented with a user interface, where you can specify a number of variables. 

- General variables:
    - Tier number: index of the tier of interest (where the intervals are defined). 
    - Sound file extensions: The extension of should files in your folder (e.g.: .wav)
    - Result file name: name of the result file. Recommended extension `.csv`
    - Normalise by: precision of sampling. For example, 10 means that Praat will extract pitch information at time 0%, 10%, 20%, ..., 100% (10+1 data points in total); and 50 means that Praat will extract pitch information at times 0%, 2%, 4%, 6%, ..., 100% (50+1 data points in total). 
- Pitch parameters:
    - Time steps: (Praat default: 0.0) the measurement interval (frame duration), in seconds. If you supply 0, Praat will use a time step of 0.75 / (pitch floor), e.g. 0.01 seconds if the pitch floor is 75 Hz; in this example, Praat computes 100 pitch values per second.
    - Pitch floor: (Praat default: 75 Hz) candidates below this frequency will not be recruited. This parameter determines the length of the analysis window: it will be 3 longest periods long, i.e., if the pitch floor is 75 Hz, the window will be 3/75 = 0.04 seconds long.
    - Pitch ceiling: (Praat default: 600 Hz) candidates above this frequency will be ignored.

Define the variables based on what you need, then select OK. Praat will start processing your files, and an output file summarising all pitch information extracted will be created in the same folder:

![csv](/images/tutorial_pitch/csv.png)

File selection procedure used in this script is from [Scott Seyfarth annotation.Praat](https://gist.github.com/scjs/ffbbba71cc8b3ff9d0476c82b2df9d0f). 
