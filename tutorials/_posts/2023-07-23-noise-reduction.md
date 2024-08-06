---
layout: post
title: Reducing breathing and room noise from speech samples
date: 2023-07-23 10:00
modified_date: 2024-08-06 14:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Python']
comment_issue_id: 10
reading-time: 3
---

On this page I share my Python script that removes breathing and room noise from recordings of my participants' responses in a speech production experiment. 

<!--excerpt-->

I recently started a timed/speeded cloze experiment where participants complete sentences orally within a time limit. Reaction time is important in this paradigm: it reflects how much processing the participant needs before a lexical item wins the "inner competition" and gets produced. However during data processing I discovered a problem: although my recording equipment was good and the environment was quiet, some participants produced loud breathing sounds (they sounded very bored &#128517;) that my onset detection script will mistake as speech onset. Here is what I did to remove these sounds as much as possible in order to get more accurate speech onset data. 

What this script does:
- Based on by-participant noise samples, reduce noise from multiple recordings.
- Optionally normalize the sound volume after noise reduction. 

This script uses the stationary noise reduction method in the [noisereduce](https://timsainburg.com/noise-reduction-python.html) package. 

## Step 1: Preparation

Install Python and these packages: [pydub](https://github.com/jiaaro/pydub), [numpy](https://numpy.org/install/), and [noisereduce](https://github.com/timsainb/noisereduce). 

Download the <a href="https://gist.github.com/Yiling-Huo/6fc080cba8f3f4260252c20bbf8eb320">Python script</a>.

Gather your recordings in one folder. The recordings must contain participant information in the exact same places in the file name. For example: `S01_trial_1.wav` , `S21_trial_1.wav`. 

Get one noise sample for each participant in another folder. The file names should only contain the participant information, such as `S01.wav`, `S21.wav`. the way I did this was to first use my onset detection script on the raw recordings, find out which recordings were affected by noise the most, and then extract a representative noise sample for each person. 

## Step 2: Run the script

Open `noise_reduction.py`  in an IDE and notice these variables:

- audioFormat: string. The format of your recordings (both speech and noise)

- inDir: string. The directory of your recordings.
- noiseDir: string. The directory of your noise samples. 
- outDir: string. Where to save the noise reduced sounds. 

- idFirst: integer. The index of the beginning of your participant info in the recordings' file name. For example, if my recordings have names such as `S01_trial_1.wav`, idFirst should be 0.
- idLast: integer. The index of the end of your participant info (not including the last letter). For something like `S01_trial_1.wav`, this should be 3. 

- normalise: boolean. Whether to normalize sound volume after noise reduction. 
- headroom: float. How close to the maximum volume to boost the signal up to (in dB).

Once you've set all these variables correctly, run the script. The script should first take all sound files in the noiseDir and create a dictionary that has participant ID as keys and noise samples as values. Then the script should take all sound files in inDir and find the corresponding noise sample using info in the file name, then reduce noise. Then, the script can optionally normalize the sound volume, and finally save the output to outDir. 