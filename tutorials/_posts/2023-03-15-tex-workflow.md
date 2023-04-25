---
layout: post-narrow
title: My workflow of creating PDF and docx files using Rmd and Markdown
date: 2023-03-15 10:00
modified_date: 2023-04-17 13:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Markdown', 'TeX']
---

On this page, I record my workflow of working with Markdown, RMarkdown, and Pandoc, to achieve a good writing and rendering experience, while allowing some room for collaboration.

<!--excerpt-->

Here are the things I do in this workflow:

- Write in `.md`.
- Convert to `.pdf` using Pandoc to make pretty documents.
- Convert to `.docx` using Pandoc to collaborate with colleagues (often using MS Teams). 
- (Convert from `.docx` to `.pdf`, or to `.md` for further editing.)

Or

- Write in `.Rmd`. 
- Convert to `.pdf` using `knitr` to make pretty documents.
- Convert to `.docx` using `knitr` to collaborate. 

For now, I'm keeping both options because 
1. The text editor I'm using, [VS Code](https://code.visualstudio.com/), does not support document outline for `.Rmd`. So it's easier to organise the text if I write in `.md`. 
2. I prefer using VS Code to write rather than RStudio (which does support document outline for `.Rmd`), as I'm used to writing stuff while looking at the MS Word default font Calibri, which is easily achievable in VS Code. 
3. However, `knitr` and `rticles` makes it easier to convert documents and use publisher templates, instead of writing a long command line, it's just a few simple clicks. 
4. Also, sometimes my documents need to include codes, which I find is easier to do with `.Rmd`. 
5. Nevertheless it's easy enough to switch back and forth between `.md` and `.Rmd`, so I can have the best of both worlds. 

### On this page
1. [My setup](#setup)
2. [My configurations](#config)
    - [VS Code configurations](#config-vs)
    - [MiKTeX configurations](#config-miktex)
    - [R configurations](#config-r)
3. [Example](#example)
    - [Writing in `.md` then rendering `.pdf` and/or `.docx`](#md)
    - [Writing in `.Rmd` then rendering `.pdf` and/or `.docx`](#rmd)
4. [Putting together a large document: `.rmd` parent and `.md`/`.rmd` children](#parent)
5. [Tips](#tips)
    - [Using VS Code's snippets](#snippet)
    - [One (silly) trick](#silly-trick)

Might be helpful: <a href="https://yiling-huo.github.io/tutorials/2023/02/16/rmarkdown-latex.html" target="_blank">A more detailed tutorial on creating `.Rmd` for rendering to `.pdf`</a>

## **1. My setup** <a name="setup"></a>

On my **Windows 10** operating system, I installed these:

- [VS Code](https://code.visualstudio.com/)
- [MiKTeX](https://miktex.org/download)
- [Pandoc](https://pandoc.org/installing.html)
- [R](https://cran.r-project.org/mirrors.html)
- (not necessarily but)[RStudio](https://posit.co/products/open-source/rstudio/)

## **2. My configurations** <a name="config"></a>

### **2.1 VS Code configurations** <a name="config-vs"></a>

#### **Install R support**

This is to use R from VS Code. Install the [R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r) for VS Code. 

#### **Link Rmd files with rmd language**

This step ensures any language specific settings you use in VS Code get correctly assigned to `.Rmd` files. I chose to link `.Rmd` with the `rmd` language, to use `knitr` from within VS Code. However, this link will make VS Code fail to generate document outline. If you don't feel like you need to knit directly from VS Code, you can instead link `.Rmd` with `markdown`, which will allow VS Code to generate document outline, which is super helpful for organising your texts:

![outline](/images/tutorials/mdtex/outline.png)

In VS Code, press `Ctrl`+`,`  to open settings. Search for `files` in settings, and at `Files: Associations`, associate `*.Rmd` with `rmd`. 

![file-associate](/images/tutorials/mdtex/file-associate.png)

#### **Setup themes and language-specific editor fonts**

You can change the default dark theme to a theme that gets you into the mood of writing by selecting clicking on the Manage icon at the sidebar, then select Themes - Color Theme. Or press `Ctrl`+`K` then `Ctrl`+`T`. 

![theme](/images/tutorials/mdtex/theme.png)

In VS Code, press `Ctrl`+`Shift`+`P` to open the Command Palette. Search for `Preferences: Open User Settings (JSON)` to open `settings.json`. 

![font](/images/tutorials/mdtex/font.png)

Inside `settings.json`, add

```
    "[markdown]": {
        "editor.fontFamily": "Calibri",
        "editor.fontSize": 18
    },
    "[rmd]": {
        "editor.fontFamily": "Calibri",
        "editor.fontSize": 18
    },
```

These lines specify that I want VS Code to show `markdown` as well as `rmd` files with Calibri size 18, which is what I feel the most comfortable looking at while I'm writing large chunks of texts. 

#### **Install spellcheck**

Spellcheck is perhaps the most important thing I need to be able to write directly in VS Code. Install [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker). 

For me, it's also very helpful to include `"editor.renderWhitespace": "all"` in my `settings.json`, so that I could monitor whether I accidentally put more whitespace than needed in my texts. 

#### **Install word count**

Word count is important for writing, needless to say. Unfortunately I haven't found a VS Code word count extension that's designed specifically for text writing (only counting words while ignoring markdown symbols and code chunks). The word count extension I'm currently using is [WordCounter](https://marketplace.visualstudio.com/items?itemName=kirozen.wordcounter).

#### **Use the Zen Mode**

I use the Zen Mode of VS Code when I'm writing. Zen Mode allows you to focus on the writing by hiding most of the UI. Enter Zen Mode by pressing `Ctrl`+`K` then `Z`. Exit Zen Mode by double pressing `Esc`. 

### **2.2 MiKTeX configurations** <a name="config-miktex"></a>

#### **Automatically install missing packages**

This step lets MiKTeX to automatically install missing LaTeX packages, so you don't need to approve each time. 

In MiKTeX Console, select Settings, then select Always for You can choose whether missing packages are to be installed automatically (on-the-fly). 

![miktex](/images/tutorials/mdtex/miktex.png)

### **2.3 R configurations** <a name="config-r"></a>

#### **Install tinytex and TinyTeX**

(I'm not sure whether this step is needed, but I was having trouble asking R to find MiKTeX when rendering PDFs, so I just installed TinyTeX instead.) In a R console (either in RStudio or VS Code), run `install.packages("tinytex")` and then `tinytex::install_tinytex()`. 

## **3. Example** <a name="example"></a>

### **3.1 Writing in `.md` then rendering `.pdf` and/or `.docx`** <a name="md"></a>

#### **How to render files using Pandoc**

This is an example of writing in `.md` and rendering `.pdf`, `.tex`, or `.docx` files using Pandoc. 

First, prepare your `.md` file. Write your main text in [Markdown syntax](https://www.markdownguide.org/basic-syntax/). Inside the YAML header which is enclosed in dashed at the beginning of the document, you can specify some variables for Pandoc. 

![md](/images/tutorials/mdtex/md.png)

Note that some arguments are written differently in the `.md` YAML header and the `.Rmd` header. For example, where `.Rmd` can use `extra_dependencies: [""]` to use LaTeX packages, `.md` has to use `header-includes: usepackage{}`:

```
---
header-includes:
    - \usepackage{xeCJK}
    - \usepackage{booktabs}
---
```

*The default Pandoc PDF layout is somewhat odd with extremely large margins, which is why I like to specify page margins manually using `geometry: "left=cm,right=cm,top=cm,bottom=cm"`.*

After preparing your `.md` file, search for `cmd` in your Start menu to open a command prompt. In the command prompt, go to your directory by running `cd`:

![cd](/images/tutorials/website/cd.png)

use Pandoc to convert your documents by running

```
pandoc input.md -o output.pdf
```

If you are using `xeCJK`, switch to xelatex engine by adding `--pdf-engine=xelatex`. If you have any citations, add `-C` to include the citation procedure: 

```
pandoc -C --pdf-engine=xelatex input.md -o output.pdf
```

Pandoc options are very powerful. Detailed formatting such as using templates are all realised using options. More details at [Pandoc User's Guide](https://pandoc.org/MANUAL.html#options). 

Your output file should be created:

![md-output](/images/tutorials/mdtex/md-output.png)

Change the output format to convert to other formats. To create `.docx`, if there are LaTeX code chunks in the `.md`, you can first convert to `.tex`, then to `.docx`

```
pandoc -C input.md -o output.tex

pandoc -C input.tex -o output.docx
```

![md-output1](/images/tutorials/mdtex/md-output1.png)

*Note that `.docx` requires more detailed options to work perfectly. I only use the `.docx` files so that my supervisor can directly comment and edit the texts on MS Teams. So missing a few unimportant elements or images not being the best size is trivial to me.*

#### **More elements to your `.md` file**

I have a more detailed [tutorial](https://yiling-huo.github.io/tutorials/coding/programming/2023/02/16/rmarkdown-latex.html) on creating `.Rmd` for rendering to `.pdf`. The tutorial shows how to include figures, tables, citations, linguistic examples, etc. Anything that does not require R code chunks to realise can also be used in `.md` files. 

### **3.2 Writing in `.Rmd` then rendering `.pdf` and/or `.docx`** <a name="rmd"></a>

Once we have the R Extension for VS Code, we can write `.Rmd` files and convert to other formats inside VS Code. For example: 

![rmd](/images/tutorials/mdtex/rmd.png)

After preparing your `.Rmd` file, knit your file to `.pdf` other formats by clicking the Knit Rmd button, or pressing `Ctrl`+`Shift`+`K`. 

![rmd-knit](/images/tutorials/mdtex/rmd-knit.png)

Sample `.pdf` output:

![rmd-output](/images/tutorials/mdtex/rmd-output.png)

Sample `.docx` output. Use `output: word_document` to knit to `.docx`. Note that knitting directly to `.docx` will ignore LaTeX code. If you have LaTeX code in your document, you can first convert to `.tex` by letting R keep the `.tex` file when rendering to `.pdf`, then let Pandoc handle the `.tex` to `.docx` conversion:

```
---
output:
    pdf_document:
        keep_tex: true
---
```

```
pandoc -C input.tex -o output.docx
```

![rmd-output1](/images/tutorials/mdtex/rmd-output1.png)

#### **More elements to your `.Rmd` file**

I have a more detailed [tutorial](https://yiling-huo.github.io/tutorials/2023/02/16/rmarkdown-latex.html) on creating `.Rmd` for rendering to `.pdf`. The tutorial shows how to include figures, tables, citations, linguistic examples, etc.

## **4. Putting together a large document: `.rmd` parent and `.md`/`.rmd` children**<a name="parent"></a>

When a document gets long, you may prefer to write different sections separately in separate files. It's easy to use RMarkdown to put many child files together and organise them into a neat large document. As far as I know, RMarkdown can handle both Markdown children and RMarkdown children. To include child files in a RMarkdown file, use:

````
```{r, child=c('one.Rmd', 'two.Rmd')}
```
````

For example, I have written the intro, methods, and discussion sections for a paper separately. Here's what the main RMarkdown file looks like:

````
---
title: "Sample"
author: "Yiling Huo"
date: \today
bibliography: ref.bib
csl: apa.csl
reference-section-title: "References"
output:
    pdf_document:
        latex_engine: xelatex
        keep_tex: true
        number_sections: true
---

# Introduction

```{r, child='intro.md'}
```

# Experiment 1

```{r, child=c('exp1_intro.md', 'exp1_methods.md', 'exp1_dis.md')}
```

# General Discussion

```{r, child='general_dis.md'}
```
````

A sample child document `exp1_methods.md`:

````
## Methods

### Participants

Sample text Sample text Sample text Sample text 

### Stmuli

Sample text Sample text Sample text Sample text Sample text Sample text Sample text 

### Procedure

Sample text Sample text Sample text 

## Restults

Sample text Sample text Sample text Sample text 

## Discussion

Sample text Sample text Sample text 
````

When I knit the parent RMarkdown, the output looks like this:

![parent-output](/images/tutorials/mdtex/parent-output.png)

## **5. Tips** <a name="tips"></a>

### **5.1 Using VS Code's snippet** <a name="snippet"></a>

Snippets allow users to easily insert templated codes or texts. I put some frequently used LaTeX codes as snippets for markdown and RMarkdown, such as codes to wrap text around figures, which saves me loads of time and brain cells when I'm writing. 

To create your own snippets, select File - Preferences - Configure User Snippets, and then select the markdown or the rmd language. 

A `language.json` file will be opened, where you can create customised snippets for a specific language. The snippet contains a name, a prefix which is what you need to type to call the snippet, a body which is the code context, and a description. For example, this is my snippet for inserting a figure that allows text to wrap around it: 

```{json}
"Latex Wrap figure": {
    "prefix": ["wfig"],
    "body":[
        "```{=latex}",
        "\\begin{wrapfigure}{$1}{0.${2}2\\textwidth}",
        "\\centering",
        "\\includegraphics[width=0.$2\\textwidth]{$3}",
        "\\caption{$4}",
        "\\label{$5}",
        "\\end{wrapfigure}",
        "```"
    ],
    "description": "Wrap figure with latex wrapfigure."
}
```

Placeholders such as `$1` and `$2` allow you to quickly jump to the next placeholder with the `Tab` key. In my example snippet, `$1` is where to put the position of the wrap box (`l` left, `r` right, etc.), `$2` is the percentage width of the figure, with `0.${2}2` in the second body line to automatically set the width of the wrap box to 2% larger than the figure width. `$3` is the name of the figure, `$4` is the caption, and `$5` is the label. 

Note that you will need to escape JSON symbols such as backslashes and double quotes by putting a backslash `\` in front of them. In order to include the LaTeX line break symbol `\\`, you'll need six backslashes in `language.json`: `\\\\\\`. 

VS Code will not automatically activate snippets for markdown. To force it, press `Ctrl`+`space` before typing the prefix. 

### **5.2 One (silly) trick** <a name="silly-trick"></a>

Since the only difference between a `.md` file and a `.Rmd` file (when no code chunks are involved) is a few lines in the YAML header, it's possible to switch back and form between `.md` and `.Rmd` simply by copy pasting the body text. This is silly but I like the flexibility of having a solution when I suddenly want to include something in the document that only the other format can handle. 