---
layout: post-narrow
title: Make auditory serial presentation stimuli
date: 2023-03-10 14:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Praat']
---

Psycholinguistic research sometimes requires the stimuli to have specific timing. On this page, I share a Praat script that given the stimulus-onset asynchrony (SOA), makes auditory serial presentation stimuli from continuous speech recordings and their textgrids. 

<!--excerpt-->

### Step 1: Preparation

Download the <a href="/files/resources/praat/auditory-SP-stimuli-from-textgrid" download>Praat script</a>.

Gather your stimuli `.wav` files, and make your `.Textgrid` files. The `.Textgrid` files should have the same name as your `.wav` files. Your textgrid files should contain at least one interval tier that Praat will use to make the serial presentation stimuli. For example, if I want to present a sentence word-by-word, with a between-word SOA = 800ms, my textgrid should look like this, where:

- Each word should be a named interval.
- Each interval name should be used **only once**. (Thus I numbered all my intervals.)

![praat1](/images/tutorials/auditory_sp/praat1.png)

Additionally, since this script is originally designed to make sentence stimuli, it allows the user to define punctuations. Punctuations will be added as additional silences in the final product. All punctuations should have *the same* interval name, here I used 'p'. 

*Note that while recording this example, the speaker was instructed to speak one word at a time, to avoid co-articulation. This script will of course be able to handle completely natural recordings, provided the correct textgrid annotations.*

### Step 2: Run the script

Download and run [Praat](https://www.fon.hum.uva.nl/praat/).

Select Praat - Open Praat script..., and select `auditory-SP-stimuli-from-textgrid`. 

Select Run - Run. You will be presented with a user interface, where you can specify a number of variables. 

- The generals:
    - **file directory**: Where your `.wav` and `.Textgrid` files are located. *Do not put `\` at the end*.
    - **save directory**: Where you want your output files to be saved. *Do not put `\` at the end*.
    - **txt file name**: Aside from manipulating the `.wav` files, the script will also generate a `.txt` file in the end which indicates the onset and offset of each interval in the final product. Define the `.txt` file's name here. 
    - **new sound file name ending**: You can optionally rename your output `.wav` files. For example, if you say `_sp` here, your `01.wav` will output `01_sp.wav`. Leave blank if you do not want to rename the output files. 
- The specifics:
    - **critical tier number**: The index of the interval tier that Praat will use to process the recordings. 
    - **soa in seconds**: Your stimulus-onset asynchrony (SOA). In seconds. 
    - **stretch fragments**: If checked, Praat will stretch fragments that are shorter than your SOA to the length of your SOA, so that stimuli can be perceived as continuous. 
    - **allow overtime**: If unchecked, Praat will compress fragments that are longer than your SOA. If checked, Praat will not compress long fragments (*note that this will not preserve the SOA*).
    - **minimum silence duration seconds**: You can optionally define a minimum duration of silence, if you wish to make sure each fragment is separated by at least some silence. 
    
        If `allow overtime` is unchecked, Praat will compress long fragments such that SOA is preserved after minimum silence is added to the end of the fragment. If `allow overtime` is unchecked, Praat will simply attach the minimum silence to the end of the fragment (*note that this will not preserve the SOA*).

        If `stretch fragments` is checked, Praat will stretch short fragments such that the duration of stretched fragments + minimum silence = SOA. 
    - **punctuation name**: The name of your punctuation interval. ***Note that this entry cannot be left blank. If you do not have punctuation in your stimuli, put at least one character here that is not the full name of any of your intervals.***
    - **punctuation duration**: The duration of punctuation. In seconds.


![praatui](/images/tutorials/auditory_sp/praatui.png)

Define the variables based on what you need, then select OK. Praat will start processing your `.wav` files. 

An example output `.wav` will look like this in Praat: 

![praat2](/images/tutorials/auditory_sp/praat2.png)

In addition, Praat will also write a `.txt` file to summarise the onset and offset of each fragment (including the silence): 

![txt](/images/tutorials/auditory_sp/txt.png)

You can see that Praat isn't perfect at manipulating the durations, but on the millisecond level, it does a good enough job. 
