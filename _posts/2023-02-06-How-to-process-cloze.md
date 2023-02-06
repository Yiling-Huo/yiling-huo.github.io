---
layout: post
title: Automated processing of Chinese cloze responses
date: 2023-02-06 16:00
author: Yiling Huo
categories: Tutorials
---

<p>The cloze task is widely used in psycholinguistics, mainly to determine the predictability of a word given certain context. In a cloze task, the participant sees incomplete sentences, and is asked to complete the sentences by writing down one or a few words. The predictability, or the cloze probability, of a given word is the proportion of people who fill a gap in a sentence with that specific word. Therefore, processing cloze responses includes counting the frequency of each word appeared in all responses. In many languages, such as English, this task is easy to automate: word boundaries are easy to determine. In languages such as Chinese, where no written word boundaries exist, we need a solution to automate the processing of cloze responses. </p>

One possible solution is to use a text segmentation tool. Many good text segmentation tools exist for Chinese for python, such as [Jieba](https://github.com/fxsjy/jieba), [SnowNLP](https://github.com/isnowfy/snownlp), [PkuSeg](https://github.com/lancopku/pkuseg-python). However, I find that text segmentation is not necessary for processing cloze responses. Instead, I present a solution based on a Chinese word database, [SUBTLEX-CH](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch).

SUBTLEX-CH is a database of word frequencies based on a corpus of film and television subtitles (33.5 million words). I chose to process my cloze data based on this database bacause it includes most Chinese words, and its format is fairly easy to process. 

I have created two scripts to extract the frequency of **every common noun** appeared in responses (common noun as opposted to propoer nouns such as names, institutes). The scripts only count nouns as nouns are the most common target words in psycholinguistics experiments using eye-tracking or ERP methods. You can modify the script to accommodate the parts of speech you would like to include in your results.

On this page, I will explain step-by-step how my scripts work.

### On this page
1. [Step 1: Preparation](#step1)
2. [Step 2: Create a word index using SUBTLEX-CH](#step2)
3. [Step 3: Process cloze responses](#step3)

### **Step 1: Preparation** <a name="step1"></a>

Go to [SUBTLEX-CH](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch) and download `SUBTLEX-CH-WF-PoS.zip`. Extract `SUBTLEX-CH-WF_PoS.xlsx`.

Go to [my resources page](https://github.com/Yiling-Huo/resources_huo/tree/main/Python_scripts/Automated_processing_of_Chinese_cloze_responses) and download `01_create_index_using_SUBTLEX_CH_PoS.py` and `02_process_cloze_data.py`. 

Pre-process your data. Your data should be in **long form** (one response per row), in `.csv` format, and contain at least these two columns:

- sentence: your sentence frames
- respons: your participant's response

`sample_data.csv` provides some [sample data](https://github.com/Yiling-Huo/resources_huo/blob/main/Python_scripts/Automated_processing_of_Chinese_cloze_responses/sample_data.csv).

![sample data](/images/cloze_tutorial/exdata.png)

Finally, put `your data.csv`, `SUBTLEX-CH-WF_PoS.xlsx`, `01_create_index_using_SUBTLEX_CH_PoS.py`, and `02_process_cloze_data.py` in the same folder. 

### **Step 2: Create a word index using SUBTLEX-CH** <a name="step2"></a>

Run `01_create_index_using_SUBTLEX_CH_PoS.py`. Required modules: os, [openpyxl](https://pypi.org/project/openpyxl/), csv

This should create `index.csv` in the index folder. 

![index](/images/cloze_tutorial/index.png)

*If you would like to process not only nouns, you can modify line 46 to include all parts of speech you would like to include. A list of part of speech coding used in the database can be found [here](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch/labels.doc).*

```python
46            if row[3] == 'n': # common noun is marked using 'n' in SUBTLEX-CH
```

*For example, if you want both nouns and adjectives:*

```python
46            if row[3] in ['n', 'a']:
```

### **Step 3: Process cloze responses** <a name="step3"></a>

Open `02_process_cloze_data.py`. 

This script will first sort the index from longest to shortest, and count each appearences of the longest possible word(s) in each response. For example, if the participant responded with "北京烤鸭", "北京" and "烤鸭" will be counted once respectively, while "北" or "鸭" will not be counted. This aviods multiple counting. 

Check lines 23 to 32 for the variables, customise if needed:

```python
23 # settings
24 inputFile = 'data.csv'
25 outputFile = 'cloze_results.csv'
26 responseColumn = 'response' # the column name of responses
27 sentenceColumn = 'sentence' # column name of sentence frame
28
29 inputFormat = 'utf-8' # input format. Default utf-8
30 outputFormat = 'utf-8-sig' # output format. Default outputs a utf-8 csv file with BOM to read easily in MS Excel
31 
32 header = ['sentence', 'response', 'count', 'cloze_probability', 'number_of_response'] # header of the output file
```

Run `02_process_cloze_data.py`. 

An output file should be created in the same folder. 

![output](/images/cloze_tutorial/output.png)

If the participant did not respond with a common noun, frequency of `no_match` will +1. As we can see, for the second sentence, one participant did not respond with any word in our common noun corpus. If you have too many `no_match`s, it's probable that SUBTLEX-CH did not have your target word. Simply add your target word to the index to solve this. You can either modify the scripts, or simply modify `index.csv`.

After the processing, you will need to **manually integret sub- and super-category responses**. For example, in the sample output, for sentence two, you may consider adding the frequency of 玫瑰, 鲜花, 花朵, 野花 to the frequency of 花. 

**References**

Cai, Q., & Brysbaert, M. (2010). SUBTLEX-CH: Chinese Word and Character Frequencies Based on Film Subtitles. Plos ONE, 5(6), e10729. https://doi.org/10.1371/journal.pone.0010729.
