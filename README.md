# Introduction to SAS for Incoming Predocs

<img src="censas.png" alt="drawing" width="500"/>

This is a simple website built to serve as a SAS guide for incoming predocs. It is built using [Jupyter Books](https://jupyterbook.org/intro.html) and hosted using [Netlify](https://www.netlify.com/). Jupyter Books turns [Jupyter Notebooks](https://jupyter.org/) (which rely on Python) and markdown files into websites that are structured as books. 

## Adding & Modifying Content

The Jupyter Book [guide](https://jupyterbook.org/start/overview.html) has a great tutorial about how Jupyter Books work. We will briefly go over how to add/modify content here. 

### Modifying Content

All of the content for our website is stored in the `content` folder. Markdown and Jupyter Notebooks are stored within folders (representing chapters or sections) within the `content` folder. To modify an already existing page, simply edit the corresponding markdown or Jupyter Notebook. 

### Adding Content

There are two steps to adding content

- Create the corresponding markdown file or Jupyter Notebook
- Add a line in the `_toc.yml` file so Jupyter Books knows where this content should go

The first step is to simply save your markdown file or Jupyter Notebook in the relevent location in the `content` folder. To add `my_new_file.md` to the website, you would add the following line to `_toc.yml`

```
- file: content/my_new_file.md
```

### Incorporating the Changes

Once you've added your markdown or Jupyter Notebook file to the `content` folder and updated the `_toc.yml` file you need to "re-build" the Jupyter Book to incorporate your changes into the website's html files. To do this simply run 

```
jupyter-book build cen-sas-intro
```

from the command line. This will rebuild the html files with your changes. Once you have re-built the Jupyter Book all you have to do is push your changes to the `master` branch and Netlify will detect this update and refresh the site. 
