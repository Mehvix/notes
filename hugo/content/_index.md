---
title: Home
type: docs
---

{{< katex />}}

# home


## what

These are my personal notes for courses I've taken at Berkeley. It varies from course-to-course, but I try to take notes from lecture content as well as supplemental notes (i.e. CSM, discussion, labs).

These notes should serve as a supplement to course material, but no more than that. I believe you have to interact with the ideas yourself to truly understand them. That is, not rely solely on reading my notes.

I enjoy linking to other related pages, often Wikipedia, and try to remember to denote extra information that's not in scope of the course.


## how

This site is compiled with the latest version on [hugo](https://gohugo.io/) along with the [book](https://github.com/alex-shpak/hugo-book/) theme alongside some [css tweaks](https://github.com/Mehvix/notes/blob/master/hugo/static/css/custom_styling.css) to emulate [onedark](https://toolbox.mehvix.com/onedark/). $\LaTeX$ is done through [KaTeX](https://katex.org/) now, but [MathJax](https://mathjax.org/) is used on old pages.

I wrote this [python script](https://github.com/Mehvix/notes/blob/master/cleanr.py) to clean up and format slides/PDFs as `.md` files to speed up the process too.

## contributing

Feel free to point out (or even correct) mistakes by creating an [issue](https://github.com/Mehvix/notes/issues/new) / [pull request](https://github.com/Mehvix/notes/compare) or by reaching out me; my contacts are on my [www](https://www.mehvix.com).

If you would like to contribute, make a pull request on the [GitHub repository](https://github.com/Mehvix/notes). You only have to edit the `master` branch, GH actions generate the site after each push in the `gh-pages` branch (so ignore it).

When cloning this repository, you will (probably) have to run the following command to pull the book theme submodule:
```cmd
git submodule update --init --recursive
```

## todos

- [ ] Anki links
- [ ] HLJS -- will implement if I ever end up taking notes in a CS class
- [ ] Hugo function to generate preview of each class's notes on the their respective 'home' pages
    - E.x notes.mehvix.com/e-29/ would show a compilation of every week's table of contents


## todones

- [x] [OneDark](https://toolbox.mehvix.com/onedark/) theme :o
- [x] Import old [AP notes](https://github.com/Mehvix/ap-notes)
    - Made in Notion, will need to be cleaned up
<!-- - [ ] Create folders for each department with subfolders for each class
    - e.g. Math > 53 > \[chapters] -->
<!-- ^Decided against  -->