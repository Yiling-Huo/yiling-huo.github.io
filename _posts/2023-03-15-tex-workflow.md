---
layout: post-narrow
title: My workflow of creating PDF and docx files using Rmd and Markdown
date: 2023-03-15 10:00
author: Yiling Huo
category: 'Tutorials'
tags: ['Markdown', 'Markdowns and TeX']
related: ['Markdowns and TeX']
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
    - [One (silly) trick](#silly-trick)

Useful link: <a href="https://yiling-huo.github.io/tutorials/2023/02/16/Rmarkdown-LaTex.html" target="_blank">A more detailed tutorial on creating `.Rmd` for rendering to `.pdf`</a>

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

![outline](/images/tutorial_mdtex/outline.png)

In VS Code, press `Ctrl`+`,`  to open settings. Search for `files` in settings, and at `Files: Associations`, associate `*.Rmd` with `rmd`. 

![file-associate](/images/tutorial_mdtex/file-associate.png)

#### **Setup themes language-specific editor fonts**

You can change the default dark theme to a theme that gets you into the mood of writing by selecting clicking on the Manage icon at the sidebar, then select Themes - Color Theme. Or press `Ctrl`+`K` then `Ctrl`+`T`. 

![theme](/images/tutorial_mdtex/theme.png)

In VS Code, press `Ctrl`+`Shift`+`P` to open the Command Palette. Search for `Preferences: Open User Settings (JSON)` to open `settings.json`. 

![font](/images/tutorial_mdtex/font.png)

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

#### **Use the Zen Mode**

I use the Zen Mode of VS Code when I'm writing. Zen Mode allows you to focus on the writing by hiding most of the UI. Enter Zen Mode by pressing `Ctrl`+`K` then `Z`. Exit Zen Mode by double pressing `Esc`. 

### **2.2 MiKTeX configurations** <a name="config-miktex"></a>

#### **Automatically install missing packages**

This step lets MiKTeX to automatically install missing LaTeX packages, so you don't need to approve each time. 

In MiKTeX Console, select Settings, then select Always for You can choose whether missing packages are to be installed automatically (on-the-fly). 

![miktex](/images/tutorial_mdtex/miktex.png)

### **2.3 R configurations** <a name="config-r"></a>

#### **Install tinytex and TinyTeX**

(I'm not sure whether this step is needed, but I was having trouble asking R to find MiKTeX when rendering PDFs, so I just installed TinyTeX instead.) In a R console (either in RStudio or VS Code), run `install.packages("tinytex")` and then `tinytex::install_tinytex()`. 

## **3. Example** <a name="example"></a>

### **3.1 Writing in `.md` then rendering `.pdf` and/or `.docx`** <a name="md"></a>

#### **How to render files using Pandoc**

This is an example of writing in `.md` and rendering `.pdf`, `.tex`, or `.docx` files using Pandoc. 

First, prepare your `.md` file. Write your main text in [Markdown syntax](https://www.markdownguide.org/basic-syntax/). Inside the YAML header which is enclosed in dashed at the beginning of the document, you can specify some variables for Pandoc. 

![md](/images/tutorial_mdtex/md.png)

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

![cd](/images/tutorial_website/cd.png)

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

![md-output](/images/tutorial_mdtex/md-output.png)

Change the output format to convert to other formats. To create `.docx`, if there are LaTeX code chunks in the `.md`, you can first convert to `.tex`, then to `.docx`

```
pandoc -C input.md -o output.tex

pandoc -C input.tex -o output.docx
```

![md-output1](/images/tutorial_mdtex/md-output1.png)

*Note that `.docx` requires more detailed options to work perfectly. I only use the `.docx` files so that my supervisor can directly comment and edit the texts on MS Teams. So missing a few unimportant elements or images not being the best size is trivial to me.*

#### **More elements to your `.md` file**

I have a more detailed [tutorial](https://yiling-huo.github.io/tutorials/coding/programming/2023/02/16/Rmarkdown-LaTex.html) on creating `.Rmd` for rendering to `.pdf`. The tutorial shows how to include figures, tables, citations, linguistic examples, etc. Anything that does not require R code chunks to realise can also be used in `.md` files. 

### **3.1 Writing in `.Rmd` then rendering `.pdf` and/or `.docx`** <a name="rmd"></a>

Once we have the R Extension for VS Code, we can write `.Rmd` files and convert to other formats inside VS Code. For example: 

![rmd](/images/tutorial_mdtex/rmd.png)

After preparing your `.Rmd` file, knit your file to `.pdf` other formats by clicking the Knit Rmd button, or pressing `Ctrl`+`Shift`+`K`. 

![rmd-knit](/images/tutorial_mdtex/rmd-knit.png)

Sample `.pdf` output:

![rmd-output](/images/tutorial_mdtex/rmd-output.png)

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

![rmd-output1](/images/tutorial_mdtex/rmd-output1.png)

#### **More elements to your `.Rmd` file**

I have a more detailed [tutorial](https://yiling-huo.github.io/tutorials/2023/02/16/Rmarkdown-LaTex.html) on creating `.Rmd` for rendering to `.pdf`. The tutorial shows how to include figures, tables, citations, linguistic examples, etc.

### **3.3 One (silly) trick** <a name="silly-trick"></a>

Since the only difference between a `.md` file and a `.Rmd` file (when no code chunks are involved) is a few lines in the YAML header, it's possible to switch back and form between `.md` and `.Rmd` simply by copy pasting the body text. This is silly but I like the flexibility of having a solution when I suddenly want to include something in the document that only the other format can handle. 