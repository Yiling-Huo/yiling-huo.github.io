---
layout: post-narrow
title: Python program to present an array of pictures and their labels
date: 2024-02-20 21:00
modified_date:
author: Yiling Huo
category: 'Tutorials'
tags: ['Psycholinguistics', 'Python', 'Visual world eye-tracking']
comment_issue_id: 11
reading-time: 6
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
- Download the <a href="/files/resources/python/fam-task.py" download>Python script</a> , or see the full script at the end of this page. 
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

## Full script

```python
import pygame, csv, os, sys, random
from datetime import datetime

##########
# Appearances
##########

white = '#FFFFFF'
black = '#000000'
blue = '#0000FF'

input_file = 'pic-names.csv'
pic_dir = 'assets/'
results_dir = 'results/'

instructions = ['您将看到图片，以及图片所指代的名词', '请熟悉每张图片所指代的词', '按空格键进入下一张图片']

instruction_font = 'simsun'
instruction_font_size = 50
trial_font = 'simsun'
trial_font_size = 75

##########
# Materials
##########

# get a dict of pics and names with pics as keys and names as values
with open(input_file, 'r', encoding='utf-8') as input:
    cr = csv.reader(input)
    content = [line for line in cr]
    pics = {}
    first = True
    for row in content:
        if first:
            first = False
        else:
            pics[row[1]] = row[0]

##########
# Functions
##########

# wipe screen
def wipe():
    pygame.draw.rect(screen, white, pygame.Rect(0, 0, screen_width, screen_height))
    pygame.display.flip()

# next trial
def next_trial():
    global pic, text, last_time, pic, text
    global subj, data, data_pic, data_label, trial_number
    wipe()
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    now_time = now.strftime("%H-%M-%S")
    current_time = pygame.time.get_ticks()
    if len(pics) > 0:
        # record data for last trial
        rt = current_time - last_time
        if trial_number != 0:
            data.append([now_date, now_time, subj, trial_number, data_pic, data_label, rt])
        # get a new random trial
        rand_key = random.choice(list(pics.keys()))
        # use fixed pic size (400x400 for same size as eye tracking exp) or use screen proportion
        #pic = pygame.transform.scale(pygame.image.load('assets/'+rand_key),(400,400))
        pic = pygame.transform.scale(pygame.image.load(pic_dir+rand_key),((screen_width*0.27),(screen_width*0.27)))
        text = text_font_trial.render(pics[rand_key], True, black)
        screen.blit(pic, ((screen_width*0.365),(screen_height*0.15)))
        screen.blit(text, text.get_rect(center = (screen_width*0.5, screen_height*0.75)))
        # change relevant variables
        data_pic = rand_key
        data_label = pics[rand_key]
        trial_number += 1
        pics.pop(rand_key)
        pygame.display.flip()
        last_time = pygame.time.get_ticks()
    else:
        # record data for last trial
        rt = current_time - last_time
        data.append([now_date, now_time, subj, trial_number, data_pic, data_label, rt])
        with open(results_dir+subj+'.csv', 'w', encoding='utf-8') as output:
            wr = csv.writer(output, lineterminator='\n')
            for row in data:
                wr.writerow(row)
        pygame.quit()
        sys.exit()

##########
# Main task
##########
def main():
    global screen, screen_width, screen_height, text_font_ins, text_font_trial
    global pic, text, data, last_time, trial_number, subj
    # Set working directory to the location of this .py file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))\
    # create results folder if nonexistent
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    # pygame initialisation
    pygame.init()
    # full screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((700, 500))
    # get screen size
    screen_width, screen_height = screen.get_size()
    clock = pygame.time.Clock()
    screen.fill(white)
    text_font_subj = pygame.font.SysFont('arial', 50)
    text_font_ins = pygame.font.SysFont(instruction_font, instruction_font_size)
    text_font_trial = pygame.font.SysFont(trial_font, trial_font_size)

    # manage double esc quit
    esc_pressed = False
    last_esc_time = 0
    double_esc_time = 500  # milliseconds

    # task variables
    subj = 's'
    data = [['date', 'time', 'subject', 'trial', 'pic', 'label', 'rt']]
    started = False
    entering_subject = True
    trial_number = 0
    pic = None
    text = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # quit if esc key is pressed twice within double_esc_time (500ms)
            elif event.type == pygame.KEYDOWN:
                # handle first half of quit if esc key pressed twice
                if event.key == pygame.K_ESCAPE:
                    esc_pressed = True
                    current_time = pygame.time.get_ticks()
                    if esc_pressed and (current_time - last_esc_time) < double_esc_time:
                        # write data file anyways even in case of force quit
                        with open(results_dir+subj+'.csv', 'w', encoding='utf-8') as output:
                            wr = csv.writer(output, lineterminator='\n')
                            for row in data:
                                wr.writerow(row)
                        pygame.quit()
                        sys.exit()
                    esc_pressed = True
                    last_esc_time = current_time
                ### handle subject number entering
                elif entering_subject:
                    if event.key == pygame.K_RETURN:
                        entering_subject = False
                        wipe()
                    elif event.key == pygame.K_BACKSPACE:
                        subj = subj[:-1]
                        wipe()
                    else:
                        subj += event.unicode
                        wipe()
                elif not started:
                    if event.key == pygame.K_RETURN:
                        started = True
                        last_time = pygame.time.get_ticks()
                        next_trial()
                else:
                    if event.key == pygame.K_SPACE:
                        next_trial()
            # second half of handling quit, when esc is up (unpressed), esc_pressed is set to false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    esc_pressed = False
    
        if entering_subject:
            message1 = text_font_subj.render('Please enter subject number', True, black)
            screen.blit(message1, message1.get_rect(center = (screen_width*0.5, screen_height*0.3)))
            message2 = text_font_subj.render(subj, True, blue)
            screen.blit(message2, message2.get_rect(center = (screen_width*0.5, screen_height*0.5)))
            message3 = text_font_subj.render('Press Enter to continue', True, black)
            screen.blit(message3, message3.get_rect(center = (screen_width*0.5, screen_height*0.7)))
        elif not started:
            for i in range(len(instructions)):
                message = text_font_ins.render(instructions[i], True, black)
                screen.blit(message, message.get_rect(center = (screen_width*0.5, (i+1)*(screen_height*(1/(len(instructions)+1))))))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```