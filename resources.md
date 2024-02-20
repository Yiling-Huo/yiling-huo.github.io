---
layout: page-narrow
title: Resources
permalink: /resources/
---

Scripts and resources that I have created or modified. 

## Praat scripts:

- Make auditory serial presentation stimuli:

  <a href="/files/resources/praat/auditory-SP-stimuli-from-textgrid" download>Download</a>. [Tutorial](https://yiling-huo.github.io/tutorials/2023/03/10/make-auditory-sp-stimuli.html). A Praat script that, given the stimulus-onset asynchrony (SOA), makes auditory serial presentation stimuli from continuous speech recordings and their textgrids.
  
- Extract pitch contour:

  <a href="/files/resources/praat/extract_pitch_contour" download>Download</a>. [Tutorial](https://yiling-huo.github.io/tutorials/2023/03/10/extract-tone.html). A Praat script that extracts pitch contour information based on `.wav` sounds and `.Textgrid` files.

- Get duration:

  <a href="/files/resources/praat/get_duration" download>Download</a>. [Tutorial](https://yiling-huo.github.io/tutorials/2023/06/14/get-duration.html). A Praat script that gets audio file durations from a directory containing audio files. The script outputs a .csv file.

## Python scripts:

- Automated processing of Chinese cloze responses:

  <a href="/files/resources/python/chinese-cloze.zip" download>Download</a>. [Tutorial](https://yiling-huo.github.io/tutorials/2023/02/06/How-to-process-cloze.html). Two scripts that process data collected from cloze tasks in Chinese. In a cloze task, the participant sees incomplete sentences and is asked to complete the sentence by providing one or a few words.

- Compare images from two folders:

  <a href="/files/resources/python/compare_images.py" download>Download</a>. [Tutorial](https://yiling-huo.github.io/tutorials/2023/03/30/compare-images.html). A Python script that compares images from two folders to search for duplicates. 

- Convert audio:

  <a href="/files/resources/python/convert_audio.py" download>Download</a>. [Tutorial](https://yiling-huo.github.io/tutorials/2023/06/14/convert-audio.html). A Python script that converts audio file formats using pydub and ffmpeg. 

- Noise reduction:

  <a href="/files/resources/python/noise_reduction.py" download>Download</a>. [Tutorial](https://yiling-huo.github.io/tutorials/2023/07/23/noise-reduction.html). A Python script that reduces breathing and room noise from recordings. 

## R scripts:

- Remove outliers:

  <a href="/files/resources/r/remove_outlier_function.R" download>Download</a>. A simple function that removes outliers from a data frame based on the 3 s.d. rule. 

- Remove track loss trials:

  <a href="/files/resources/r/remove_trackloss.R" download>Download</a>. [Tutorial](https://yiling-huo.github.io/tutorials/2023/04/25/trackloss.html). A function that removes trials from visual world eye-tracking data where no eye gaze can be detected on any of the images in the visual display for an extensive proportion of the time. 

## Games:

*Troubleshoot:* If you're on Windows and you see an error saying *api-ms-win-core-path-l1-1-1.ddl is missing* when trying to open one of the games, this may be because your PC doesn't have the Visual C++ Redistributable for Visual Studio 2015 or 2017, which is required by Python. Try downloading it [for x86 (32bit) Windows](https://aka.ms/vs/16/release/vc_redist.x86.exe) or [for x64 (64 bit) Windows](https://aka.ms/vs/16/release/vc_redist.x64.exe). 

- Chengyu Maze 成语迷宫: <a id="chengyu"></a>

  <a href="/files/resources/games/chengyu-maze.zip" download>Download</a> (25 MB, *The build only works on Windows, please download the source code if using Mac.*) [Code](https://github.com/Yiling-Huo/chengyu-maze). A game that looks like the maze task used by psycholinguists, but with Chinese chengyu (four-character idioms). Made with pygame. 

  <p><img src="/images/resources/chengyu1.png"  width="40%"><img src="/images/resources/chengyu2.png"  width="40%"></p>

- TicTacToe Lite: <a id="tictactoe"></a>

  <a href="/files/resources/games/TicTacToe-Lite.zip" download>Download</a> (22.8 MB, *The build only works on Windows, please download the source code if using Mac.*) [Code](https://github.com/Yiling-Huo/tic-tac-toe). A mini-game tic-tac-toe game made with pygame. Based on a class practice in [PLIN0034](https://www.ucl.ac.uk/module-catalogue/modules/introduction-to-computational-linguistics-PLIN0034).

  <p><img src="/images/resources/tic-tac-toe.png"  width="40%"></p>

- Cyber fortune cookie: <a id="fortune"></a>

  <a href="/files/resources/games/cyber-fortune-cookie_exe.win-amd64-3.10.zip" download>Download</a> (23 MB, *The build only works on Windows, please download the source code if using Mac.*) [Code](https://github.com/Yiling-Huo/cyber-fortune-cookie). A mini-game made with python and pygame, in which you can open fortune cookies and get your fortune. 

  <p><img src="/images/resources/fortune-cookie-game.png"  width="40%"></p>