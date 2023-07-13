---
layout: post-narrow
title: Comparing images from two folders
date: 2023-03-30 15:00
modified_date: 2023-06-14 15:00
author: Yiling Huo
comment_issue_id: 5
category: 'Tutorials'
tags: ['Psycholinguistics', 'Python']
---

Sometimes psychology researchers need to recycle stimuli from old experiments, usually because they have already got some standardized measures for the old stimuli. 

Say for my new experiment, I want to recycle visual stimuli from both Exp A and Exp B. But here's the problem: some of the stimuli from the two experiments are duplicates, and the duplicates all have different file names. How do I make sure I don't have duplicates in the recycled stimuli?

On this page, I share a Python script that compares images from two folders and removes duplicates. 

<!--excerpt-->

## Step 1: Preparation

Download the <a href="/files/resources/python/compare_images.py" download>Python script</a> (or see full script at the end of this page).

Gather your images to compare in two folders. 

This script will compare every image in `folder 1` with those in `folder 2`  and vice versa to search for duplicates, but *it will not try to find duplicates within each folder*. It's built this way with in mind the process of recycling visual stimuli from old experiments, thus `folder 1` may be a folder where visual stimuli from Exp A are saved, and `folder 2` is for Exp B. Within one experiment I assume the researcher has already checked for duplicates when they did the experiments previously. 

## Step 2: Run the script

Open `compare_images.py` in an IDLE.

This script will take every image in folder 1, compare it with every image in folder 2, and vice versa. A summary file `summary.csv` will be created, which is a list of unique images from the two folders. This script can optionally copy all unique images to another folder, with duplicates renamed. In case of a duplicate, the script will write down the image's file name in folder 1 and folder 2 respectively, and its new name if `copy == True`.

Note that this script uses the `imagehash` package to compare images. This package is good at detecting true duplicates, but cannot detect slightly edited images:

![good](/images/tutorials/compare_img/good.png) 

![bad](/images/tutorials/compare_img/bad.png)

At the beginning of the script, define your variables:

- `dir1` (string) is the first folder to compare.
- `dir2` (string) is the second folder to compare.
- `format` (list of strings) is a list of all image formats to compare. 
- `outdir` (string) is the directory to save the summary file.
- `copy` (boolean) controls whether the script copies unique images to a new folder. 
- `copydir` (string) the directory to copy unique images to, if `copy = True`. 

Run the script, and a `summary.csv` will be created, like this:

![summary-true](/images/tutorials/compare_img/summary-true.png)

Images will also be copied if `copy == True`. Note that as the images are duplicates, the script will copy the image from *folder 1* to the new folder. 

If `copy == False`, the summary file will look like this:

![summary-false](/images/tutorials/compare_img/summary-false.png)

## Full script

```python
# This script compares images from two folders, write down duplicate images, and optionally copy all unique images from the two folders into a new folder. 
# Created by Yiling Huo, 30 March 2023

import os, csv, shutil, ntpath
from PIL import Image
import imagehash

# Set working directory to the location of this .py file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

##########
# Set variables
# Set the two folders where the images are
dir1 = (os.getcwd() + '/folder1/') # image folder 1
dir2 = (os.getcwd() + '/folder2/') # image folder 2
format = ['.jpg', '.png'] # format of images to compare

outdir = (os.getcwd() + '/') # where to save the summary file


# Set whether the script should copy all unique images to another folder
copy = False
copydir = (os.getcwd() + '/unique/')
############

# create directories if not existing:
if not os.path.exists(outdir):
    os.makedirs(outdir)

if not os.path.exists(copydir):
    os.makedirs(copydir)

# define a compare image function that returns a row of filenames if the image is a duplicate, nothing if the image is not a duplicate
# on it's way, this function also saves the duplicate image (save image 1), rename it as image1-image2.ext, if copy = True
# this function uses imagehash to compare images

# by default, copy = False, copydir is the working directory
def compare_pic(pic1, pic2, copy=False, copydir=os.getcwd()):
    filename1 = ntpath.basename(pic1)
    filename2 = ntpath.basename(pic2)
    name1 = filename1.replace(os.path.splitext(filename1)[-1].lower(), '')
    name2 = filename2.replace(os.path.splitext(filename2)[-1].lower(), '')
    hash1 = imagehash.average_hash(Image.open(pic1))
    hash2 = imagehash.average_hash(Image.open(pic2))
    hash = hash1 - hash2
    if hash != 0:
        row=[]
        return(row)
    else:
        if copy == False:
            newname = name1+'-'+name2+os.path.splitext(filename1)[-1].lower()
            row = [filename1, filename2, 'NA']
            return(row)
        else:
            newname = name1+'-'+name2+os.path.splitext(filename1)[-1].lower()
            shutil.copyfile(pic1, copydir+newname)
            row = [filename1, filename2, newname]
            return(row)

# loop through images in the two folders
with open(outdir + 'summary.csv', 'w', encoding='utf-8-sig') as summary: # encoding='tif-8-sig' to accommodate other languages and the need to open in MS Excel or other apps
    write_summary = csv.writer(summary, lineterminator='\n')  # the lineterminator parameter is needed in Windows
    first_row=['name_in_folder_1', 'name_in_folder_2', 'name_in_new_folder']
    write_summary.writerow(first_row)

    picFileList1 = os.listdir(dir1)
    picFileList2 = os.listdir(dir2)

    # loop through images in dir1, to find if any images are duplicates from dir2
    for pic1 in picFileList1:
        row=[]
        dup = False
        ext1 = os.path.splitext(pic1)[-1].lower()
        if ext1 in format:
            print('Comparing image...' + pic1)
            for pic2 in picFileList2:
                ext2 = os.path.splitext(pic2)[-1].lower()
                if ext2 in format:
                    row = compare_pic(dir1+pic1, dir2+pic2, copy=copy, copydir=copydir)
                    if len(row) != 0:
                        write_summary.writerow(row)
                        dup = True
                        break
            if dup == False:
                if copy == True:
                    shutil.copyfile(dir1+pic1, copydir+pic1)
                    row = [pic1, 'NA', pic1]
                    write_summary.writerow(row)
                else: 
                    row = [pic1, 'NA', 'NA']
                    write_summary.writerow(row)

    # run the for loop again, this time to pick out unique images in dir2
    for pic2 in picFileList2:
        row=[]
        dup2 = False
        ext2 = os.path.splitext(pic2)[-1].lower()
        if ext2 in format:
            print('Comparing image...' + pic2)
            for pic1 in picFileList1:
                ext1 = os.path.splitext(pic1)[-1].lower()
                if ext1 in format:
                    row = compare_pic(dir1+pic1, dir2+pic2, copy=copy, copydir=copydir)
                    if len(row) != 0:
                        dup2 = True
                        break
            if dup2 == False:
                if copy == True:
                    shutil.copyfile(dir2+pic2, copydir+pic2)
                    row = ['NA', pic2, pic2]
                    write_summary.writerow(row)
                else: 
                    row = ['NA', pic2, 'NA']
                    write_summary.writerow(row)
```