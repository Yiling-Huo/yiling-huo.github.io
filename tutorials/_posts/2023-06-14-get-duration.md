---
layout: post
title: Get audio file durations using Praat
date: 2023-06-14 14:00
modified_date: 2024-08-06-14:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Praat']
comment_issue_id: 9
reading-time: 1
---

On this page I share a Praat script that gets audio file durations from a directory containing audio files. The script outputs a .csv file.

<!--excerpt-->

## Step 1: Preparation

Download the <a href="https://gist.github.com/Yiling-Huo/2964a50ab5fcdf78a6544d5da29e83d2">Praat script</a>. 

## Step 2: Run the script

Open [Praat](https://www.fon.hum.uva.nl/praat/) and Select Praat - Open Praat script..., and select the `get duration` script.

*If on Mac OS, replace the "\" in line 22 with "/".*

Select Run - Run. You will be taken to a window where you can choose where your audio files are located. 

<img src="/images/tutorials/get_duration/ui.png"  width="49%">

After choosing the directory, Praat is going to look at all files with the provided extension, get the files' durations, and create a output .csv file in the same folder. The output should look like this:

![output](/images/tutorials/get_duration/output.png)

The file selection procedure used in this script is from [Scott Seyfarth annotation.Praat](https://gist.github.com/scjs/ffbbba71cc8b3ff9d0476c82b2df9d0f). 