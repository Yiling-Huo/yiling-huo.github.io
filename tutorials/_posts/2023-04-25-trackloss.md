---
layout: post
title: Remove track loss trials from visual world eye-tracking data
date: 2023-04-25 10:00
modified_date: 2024-07-24 20:00
author: Yiling Huo
comment_issue_id: 6
category: 'Tutorials'
tags: ['Psycholinguistics', 'R']
reading-time: 2
---

One step of cleaning visual world eye-tracking data is to exclude track loss trials. These are trials where for an extensive amount of time, no eye gaze was detected on any objects in the visual display. There are multiple reasons for track loss. For example, the participant may not have paid attention to the visual display, or the eye-tracker may have been 'drifting'. On this page, I share an R function that removes track loss trials from visual world eye-tracking data. 

<!--excerpt-->

My method is inspired by the [eyetrackingR package](http://www.eyetracking-r.com/).

## Step 1: Preparation

Download the <a href="/files/resources/r/remove_trackloss.R" download>R script</a>.

Prepare your data. As an R data frame, your data should contain at least three columns: 
- Participant id
- Trial number
- Track loss: a binary numeric column indexing whether eye gaze was detected on any of the objects in the visual display. 0 = no eye gaze on any objects; 1 = eye gaze detected on an object. 

![sample_data](/images/tutorials/trackloss/data.png)

## Step 2: Source the function

Open your IDE for R. Here, I'm using RStudio. Open `remove_trackloss.R`, and source it by pressing `source`. The function should be loaded to your R environment. 

![source](/images/tutorials/trackloss/source.png)

## Step 3: Run the function

Next, load your data and remove track loss trials by running:

```r
cleaned_data <- remove_trackloss(data=data, subject_col = 'subject', trial_col = 'trial', trackloss_col = 'tracked', threshold = 0.5)
```

Where:

- `data` is the name of your data frame.
- `subject_col` (string) is the name of your column where your participant id info is.
- `trial_col` (string) is the name of your column where your trial number info is.
- `trackloss_col` (string) is the name of your column where to put your info about whether eye gaze is detected on any images. 
- `threshold` (numeric) is the threshold of track loss. For example, 0.5 means that if eye gaze is not detected for more than 50% of observations in a trial, that trial will be counted as a track loss trial. 

The function is going to return a data frame that has all the track loss trials removed. 

![cleaned](/images/tutorials/trackloss/data_cleaned.png)

In addition, the console output tells you the data frame it was working with, the number of trials excluded, the (original) total number of trials, and the percentage excluded. It should look like something like this:

![output](/images/tutorials/trackloss/output.png)