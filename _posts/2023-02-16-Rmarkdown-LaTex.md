---
layout: post
title: How I set up my LaTeX writing environment inside R
date: 2023-02-16 21:00
author: Yiling Huo
categories: Tutorials
---

As an academic rooky I feel that I will eventually need to deal with LaTeX one way or another. However, I wonder whether I have to fully learn LaTeX if I'm already familiar with markdown, a way simpler formatting language. So I started searching the internet for solutions, and I think I found something useful for me. 

LaTeX comes in a thousand flavours and each person will have a different preference. This post is therefore mostly recording what I have done for myself. 

For context, I study psycholinguistics, where I put participants inside or in front of machines and do experiments with them (non-invasively, of course). So I already regularly deal with not-quire-small data sets in R, and share my workflow and results with supervisors and colleagues using R Markdown. I also teach an introduction to statistics with R workshop where it'd be nice to prepare handouts that can include R codes and R results. I am also interested in sharing stuff I created with the community so it'd be nice to create pretty documentations. So when I learned that I can integret LaTeX with R Markdown, I immediately felt that this is where I want to start. 

Some other things about my solusion that I like include:

- I can use RStudio's MS word style visual editor to edit the documents.
- I'm already working with R and RStudio, and I want to minimise new software that needed to be installed. 
- I like the simpler, visually less-confusing style of markdown. 

In this post, I will walk you step by step through how I set up everything to use R Markdown to generate LaTeX files, including simple handouts, journal articles, books, and theses. 

### On this page
1. [Prerequisites](#step1)
2. [Write a simple pdf handout with R Markdown](#step2)
    - [Writing your texts in R Markdown](#step2.1)
    - [Including R and/or other languages codes and results](#step2.2)
    - [Including figures and plots](#step2.3)
    - [Including tables](#step2.4)
    - [Including math equations](#step2.5)
    - [Including syntax trees](#step2.6)
    - [References and citations](#step2.7)
3. [Write a journal article with R Markdown](#step3)
4. [To be updated: Write a book with R Markdown](#step4)
5. [Tips](#step5)

Useful resources:

- [R Markdown Cookbook](https://bookdown.org/yihui/rmarkdown-cookbook/)
- [Tinytex documentation](https://yihui.org/tinytex/)
- [Mathematics in R Markdown](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html)
- [tablesgenerator](https://www.tablesgenerator.com/)


## **1. Prerequisites** <a name="step1"></a>

My solution requires [R](https://cloud.r-project.org/), [RStudio](https://posit.co/downloads/), and [Pandoc](https://pandoc.org/installing.html).

Inside RStudio, install tinytex and TinyTeX by running `install.packages("tinytex")` and then `tinytex::install_tinytex()` in the console. 

>How it works:
>1. In RStudio, I create R Markdown `.rmd` files and write my texts, codes, and generate my results and plots. 
>2. I knit my `.rmd` file. During this process, RStudio calls Pandoc, which will convert the document to `.tex` and generate a `.pdf` file accordingly. 


## **2. Write a simple pdf handout with R Markdown** <a name="step2"></a>

Create a new `.rmd` file: File - New File - R Markdown...

Select Default Output Format: PDF. 

![create_rmd](/images/rmdtex_tutorial/create_rmd.png)

A `.rmd` file will be created, including some default text showing you how to write in markdown syntax and how to include R codes and plots. 

![default_rmd](/images/rmdtex_tutorial/default_rmd.png)

The `.rmd` file contains two parts: a YAML header, which is enclosed in triple dashes on either side; and the text body. Inside the YAML header, we specify global variables for the document, and Pandoc will read the YAML header and adjust the LaTeX preamble accordingly during output. 

We can edit this `.rmd` file and knit it: 

![example_rmd](/images/rmdtex_tutorial/example_rmd.png) ![example_pdf](/images/rmdtex_tutorial/example_pdf.png)


### **Writing your texts in R Markdown:** <a name="step2.1"></a>

Use [markdown syntax](https://www.markdownguide.org/basic-syntax/) to write your texts. For example, for your section title (heading level 1), you can write `# 1. Introduction`. To bold your text, write `**text to bold**`. 

(If you have used markdown before, you may be inclined to include HTML codes for more detailed formatting. Unfortunately HTML will be ignored when Pandoc converts markdown to LaTeX. For anything that you instinctively want to use HTML, just google a LaTeX solution.)

### **Including R and/or other languages codes and results:** <a name="step2.2"></a>

In RStudio, you can include a R code chunk in your document by pressing Ctrl + Alt + I (Mac: Cmd + Option + I); or clicking the Add Chunk button in the toolbar; or simply typing ` ```{r} ` and ` ``` `. 

You can name your chunk by typing after {r, separeated by a space: ` ```{r chunk_name} `. Chunk options are separated by comma: ` ```{r chunk_name, echo = TRUE, message = FALSE, warning = FALSE} `. Chunk options control whether and how the code and the results are shown in your output document. You can find a list of all possible chunk ooptions at the [knitr documentation](https://yihui.org/knitr/options/). 

````{r}
```{r}
# First, let's create our data frame
value <- c(76, 67, 66, 72, 74, 64, 72, 70, 74, 78, 66, 63, 68, 68, 60, 67, 58, 70, 67, 66)
group <- rep(c('journal', 'blog'), each=10)
data_2 <- data.frame(group, value)

# independent samples t-test
### Task: complete the following line and run the t-test.
t.test(value ~ group, data=data_2, var.equal=TRUE)
```
````

![r_chunk](/images/rmdtex_tutorial/r_chunk.png)

R Markdown supports many languages other than R through the `knitr` package. A list of supported languages can be found [here](https://bookdown.org/yihui/rmarkdown-cookbook/other-languages.html). For example, if I want to include a chunk of python code: 

````{python}
```{python}
a = "Hello"
b = "world"

print(a + " " + b)
```
```` 

![python](/images/rmdtex_tutorial/python.png)

### **Including figures and plots:** <a name="step2.3"></a>

#### *method 1: include plots as images*

R Markdown allows including external images quite easily. If you have been working in other R project and generated R plots, you can save the plots as `.pdf` first, and include the `.pdf` image in your `.rmd` document. 

In your other R project, if you have base R plots:
```{r}
# dimensions are in inches. width = 7.25 satisfies most journal requirements.

# create pdf file
pdf("file_name.pdf", width = 7.25, height = 5)
# your code for the plot
boxplot(value ~ group, data = data_2) 
# close the pdf file
dev.off()
```

If you have ggplot2 plots:

```{r}
pdf("file_name.pdf", width = 7.25, height = 5)
print(ggplot_object)
dev.off()
```

In your `.rmd`, specify chunk options, then use `knitr` to include the plot:

````{r}
```{r, echo=FALSE, out.width="40%", out.height="40%", fig.align="center", fig.cap="\\label{fig:fig1}Plot of our data"}

knitr::include_graphics("./file_name.pdf")
```
```` 

![pdf_plot](/images/rmdtex_tutorial/pdf_plot.png)

Other images can also be included in this manner. 

#### *method 2: include R plots as R object*

Another method is to directly include your R plots as a R object. In your other R project, run:

```{r}
saveRDS(object_name, "./file_name.rds")
```

Note that your plot cannot refer to data frames other than the one originally mentioned in the main function. For example, the following plot CANNOT be successfully read:

```{r}
plot <- ggplot(data_frame_1, aes(x=a, y=b)) +
    	geom_bar(stat='stat') +
        goem_point(data=data_frame_2, aes(x=mean(V1), y=0.5)) # the point refers to data from another data frame
```

In your `.rmd`: 

````{r}
```{r, echo=FALSE, out.width="40%", out.height="40%", fig.align="center", fig.cap="\\label{fig:fig1}Plot of our data"}

plot <- readRDS("rile_name.rds")
plot
```
```` 

### **Including tables:** <a name="step2.4"></a>

#### *method 1: markdown tables*

Markdown allows you to create simple tables. Use pipes (|) to create cells and use multiple hyphens (---) to separate the header from other cells. More details [here](https://www.markdownguide.org/extended-syntax/). For example:

```
| p-value | decision |
| --- | --- |
| $p>0.05$ | do not reject $H_0$ |
| $p<0.05$ | reject $H_0$ |
```

![simple_table](/images/rmdtex_tutorial/simple_table.png)

#### *method 2: LaTeX tables*

If your table goes beyond the capacity of markdown, for example, if you want to merge cells, you can directly include a LaTeX table as a LaTeX chunk. Don't worry about not knowing LaTeX, there are many online tools such as [tablesgenerator](https://www.tablesgenerator.com/) that allow you to generate LaTeX code for tables. Simple copy and paste the codes in your document. You can also make it a code chunk. For example: 

````
```{=latex}
\begin{table}[]
\begin{tabular}{lllll}
\cline{1-2}
\multicolumn{2}{|l|}{table title}                                          \\ \cline{1-2}
\multicolumn{1}{|l|}{p-value}             & \multicolumn{1}{l|}{decision}  \\ \cline{1-2}
\multicolumn{1}{|l|}{p\textgreater{}0.05} & \multicolumn{1}{l|}{do not reject H0} \\ \cline{1-2}
\multicolumn{1}{|l|}{p\textless{}0.05}    & \multicolumn{1}{l|}{reject H0} \\ \cline{1-2} 
\end{tabular}
\end{table}
```
````

![latex_table](/images/rmdtex_tutorial/latex_table.png)

The table generator may tell you to add packages to your dobument preamble, you can do so in the YAML header at the beginning of your document. For example:

```
---
output:
  pdf_document: 
    extra_dependencies: ["multirow", "booktabs", "qtree"]
---
```

### **Including math equations:** <a name="step2.5"></a>

Inline mathematics are enclosed in dollar signs on both sides. For example, `$E=mc^2$` will render $E=mc^2$. 

Use double dollar signs for displayed equations. For example, `$$E=mc^2$$` will render:

$$E=mc^2$$

A list of how to write common mathmatical notations can be found [here](https://rpruim.github.io/s341/S19/from-class/MathinRmd.html). 


### **Including syntax trees:** <a name="step2.6"></a>

I work closely with linguistics, so one day I may need to include syntax trees in my documents.

Syntax trees can be easily included as LaTeX codes using the package [Qtree](https://www.ling.upenn.edu/advice/latex/qtree/qtreenotes.pdf). Include the `qtree` package in the YAML header:

```
---
output:
  pdf_document: 
    extra_dependencies: ["qtree"]
---
```

The `qtree` package allows users to write syntax trees in phrase marker style, and will generate trees during output:

````
```{=latex}
\Tree [.S This [.VP [.V is ] \qroof{a simple tree}.NP ] ]
```
````

![tree](/images/rmdtex_tutorial/tree.png)

### **References and citations:** <a name="step2.7"></a>

#### *Citing others' work:*

Citations can be managed simply. To begin, you can put all of your citations in `.bib` format in a `.bib` file. (To create a new `.bib` file, simply create a new `.txt` file then change the extension.) Put the `.bib` file in the same folder as your `.rmd` file. Inside the `.bib` file, write your citations like this: 

```
@article{kutas1984brain,
  title={Brain potentials during reading reflect word expectancy and semantic association},
  author={Kutas, Marta and Hillyard, Steven A},
  journal={Nature},
  volume={307},
  number={5947},
  pages={161--163},
  year={1984},
  publisher={Nature Publishing Group UK London}
}

@book{chomsky2014minimalist,
  title={The minimalist program},
  author={Chomsky, Noam},
  year={2014},
  publisher={MIT press}
}
```
From your source material, simply look for BibTeX format citation, copy and paste.

Specify your reference file in the YAML header:

```
---
bibliography: references.bib
---
```

Note that the first argument is your citation `key`, such as `kutas1984brain` and `chomsky2014minimalist`. To cite an item in-text, simply write `@key`. To enclose citation in parentehses, write `[@key]`. To cite multiple items in one parentehses, write `[@key1; @key2; @key3]`. More detailed explanation can be found [here](https://bookdown.org/yihui/rmarkdown-cookbook/bibliography.html). 

Citation style is managed by `.csl` files. Download the desired `.csl` file [here](https://www.zotero.org/styles?q=APA) and put it in the same folder. 

```
---
bibliography: references.bib
csl: apa-6th-edition.csl
---
```

```
The N400 ERP component's amplitude is associated with a word's predictability (cloze probability) [@kutas1984brain]. 

**References**
```

![citation](/images/rmdtex_tutorial/citation.png)

#### *Labelling and referencing tables and figures:*

Labelling and referencing tables and figures can be managed by some simple LaTeX syntax. 

To label and reference a markdown table:

```
| Header 1 | Header 2 |
| --- | --- |
| Cell content 1 | Cell content 2 |

Table: \label{tablekey} Your Caption.

In Table \ref{tablekey}, we can learn about how to reference tables. 
```

![table_ref](/images/rmdtex_tutorial/table_ref.png)

To label and reference a LaTeX table, include lines `\caption{}` and `\label{}` after line `\begin{table}[]`. Online table generators can take care of this. 

````
```{=latex}
\begin{table}[h]
\caption{Caption}
\label{tablekey2}
\centering
\begin{tabular}{@{}lllll@{}}
\cmidrule(r){1-2}
\multicolumn{2}{l}{Header} \\ \cmidrule(r){1-2}
Cell 1       & Cell 2      \\ \cmidrule(r){1-2}
\end{tabular}
\end{table}
```

In Table \ref{tablekey2}, we can learn about how to reference tables.
````

To label and reference a figure, use the `fig.cap=""` option:

````{r}
```{r, echo=FALSE, out.width="40%", out.height="40%", fig.align="center", fig.cap="\\label{figkey}Plot of our data"}

knitr::include_graphics("./file_name.pdf")
```

Figure \ref{figkey} shows how to reference figures. 
```` 

![fig_ref](/images/rmdtex_tutorial/fig_ref.png)

## **3. Write a journal article with R Markdown** <a name="step3"></a>

You can use the `rticles` [package](https://github.com/rstudio/rticles) to easily use templates from a large number of publishers. 

In R console, run `install.packages("rticles")`. 

In File - New File - R Markdown..., select using templates, and select your target publisher. Replace the template content with your content, and your document will be the format required by your target publisher. 

For example, I have created an example using the Taylor & Francis Journal Article template: 

![example_article](/images/rmdtex_tutorial/example_article.png) ![example_article_pdf](/images/rmdtex_tutorial/example_article_pdf.png)

## **4. To be updated: Write a book with R Markdown** <a name="step4"></a>

It's possible to write chapters of books with `.rmd` and combine them with `.rnw`. More detail to be updated!

## **5. Tips** <a name="step5"></a>

### Use RStudio's visual editor 

You may find it easier to edit texts using RStudio's MS Word style visual editor. In RStutio, turn on visual editor at the toolbar:

![visual_editor](/images/rmdtex_tutorial/visual_editor.png)