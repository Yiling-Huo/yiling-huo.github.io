---
layout: post
title: Convert audio file formats using Python
date: 2023-06-14 10:00
modified_date: 2024-08-06-14:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Python']
reading-time: 1
comment_issue_id: 8
---

I work closely with auditory stimuli. Sometimes I need to convert a large number of audio files from one format to another, usually because different experiment software works better with different audio formats. Here I share my Python script that converts all audio files in a folder from one format to another.

<!--excerpt-->

## Step 1: Preparation

Install [ffmpeg](https://ffmpeg.org/download.html). Remember to put ffmpeg in your PATH.

Install [Python](https://www.python.org/downloads/) (obviously) and pydub: `pip install pydub`. 

Download the <a href="https://gist.github.com/Yiling-Huo/08381aad8af9c227d8d1d4eab7fdeba2">Python script</a>.  Gather all your files in a folder. 

## Step 2: Run the script

Open `convert_audio.py` in an IDLE. Modify these variables: 

- AudioSegment.converter: string. Path to your `ffmpeg.exe`.
- AudioSegment.ffmpeg: string. Path to your `ffmpeg.exe`.
- AudioSegment.ffprobe: string. Path to your `ffprobe.exe`.

- dataDir: string. Input folder. Where your original audio files are located.
- outDir: string. Output folder. Where you want your converted files.
- input_format: string. Format of your original audio files. **Please include '.'**.
- output_format: string. Format of your output audio files. **Please include '.'**.

Run the script. Pydub is going to call ffmpeg to convert all files in your chosen folder with the original extension to the output format. 