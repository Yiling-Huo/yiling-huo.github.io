---
layout: post-narrow
title: Get audio file durations using praat
date: 2023-06-14 14:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Praat']
---

On this page I share a Praat script that gets audio file durations from a directory containing audio files. The script outputs a .csv file.

<!--excerpt-->

## Step 1: Preparation

Download the <a href="/files/resources/praat/get_duration" download>Praat script</a>. Gather all your files in a folder. 

## Step 2: Run the script

Open [Praat](https://www.fon.hum.uva.nl/praat/) and Select Praat - Open Praat script..., and select the `get duration` script.

Select Run - Run. You will be taken to a window where you can choose where your audio files are located. 

![ui](/images/tutorials/get_duration/ui.png)

After choosing the directory, Praat is going to look at all files with the provided extension, get the files' durations, and create a output .csv file in the same folder. The output should look like this:

![output](/images/tutorials/get_duration/output.png)

The file selection procedure used in this script is from [Scott Seyfarth annotation.Praat](https://gist.github.com/scjs/ffbbba71cc8b3ff9d0476c82b2df9d0f). 