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