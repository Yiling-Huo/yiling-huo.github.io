---
layout: post
title: Python program to present an array of pictures and their labels
date: 2024-02-20 21:00
modified_date: 2024-08-06 14:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Python', 'Visual world eye-tracking']
comment_issue_id: 11
reading-time: 3
---

In a visual world eye-tracking experiment, sometimes the researcher needs to familiarise participants with the pictures they will see before the eye-tracking procedure to allow the participants to associate each picture with a specific label. On this page I share a Python program for this familiarisation task, based on pygame. 

<!--excerpt-->

What this program does:
- Present the participant with a series of pictures + labels.
- Participants advance to the next picture + label by pressing the space key.
- Record the duration each picture + label was presented. 

*The experiment (instructions and trial) can be in any language supported by UTF-8. Just make sure you specify a font that supports that language.*

## Step 1: Preparation

- Make sure Python and [pygame](https://www.pygame.org/docs/) are installed.
- Download the <a href="https://gist.github.com/Yiling-Huo/b9468742a3dec01e762f87f35de7729a">Python script</a>.
- Gather the pictures you want to present in a single folder.
- Get a .csv file for your list of pictures to be presented:
    - The first column is the labels
    - The second column is the picture file names
    - The first row is the header
    - <img src="/images/tutorials/fam-task/pic-list.png"  width="40%">

## Step 2: Run the script

Open the Python script in an IDE and pay attention to these variables:

- input_file: string. The path to your .csv file containing the list of pictures and their labels.
- pic_dir: string. The path to the folder containing all of your pictures. Make sure it ends with the '/'. 
- results_dir: string. The path to the folder where you want the duration data to be stored. Make sure it ends with the '/'. 
- instructions: list of strings. A list of instructions to show the participants. Each element is shown in one line. 
- instruction_font: string. Name of the font that you'd like to use for the instructions. Must exist in the system. 
- instruction_font_size: integer. Font size of the instructions. 
- trial_font: string. Name of the font that you'd like to use in trials (to show the labels). Must exist in the system. 
- trial_font_size: integer. Font size of the labels. 

Change the values of those variables to suit your needs. Then, run the Python script.

You should first see a screen that asks you to provide a subject number. This will be the name of your results file as well as the subject number recorded in the data. Start typing and press Enter to confirm and advance. 

<img src="/images/tutorials/fam-task/subject.png"  width="70%">

Then, you should see the instructions. Press Enter to start the task. 

<img src="/images/tutorials/fam-task/ins.png"  width="70%">

In each trial, a random picture along with its label is presented on the screen, with the picture on top, the label below. Press **space** once the participant is done with looking at it and advance to the next trial. 

<img src="/images/tutorials/fam-task/trial.png"  width="70%">

Once all trials in the list have finished, the program will quit after creating a data file named subject.csv in the designated folder. The data file will record the date and time of trial, the subject number, the trial number, the picture file, the label, and how much time is spent on presenting that picture (rt, in milliseconds).

<img src="/images/tutorials/fam-task/data.png"  width="70%">

At any time when the program is running, **quit the program by pressing Escape twice in a row**. A data file with all presented trials will be created before quitting so don't worry about losing records. 