---
layout: article
title: Contributing to the Quattor Web Site
category: documentation
author: Michel Jouvin
modified: 2016-03-16
---

This page gives advices and best practices for contributing to the [Quattor web site](http://quattor.org).

## Introduction

The [Quattor web site](http://quattor.org) is hosted on GitHub, using the GitHub Pages service, and is the main source of information about Quattor.

GitHub Pages uses [Jekyll](http://jekyllrb.com), a framework to build blog-aware web sites.
Pages are written in [GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown) and stored in the [quattor.github.com repository](https://github.com/quattor/quattor.github.com) on GitHub.

Contents are added/modified to the web site by adding/modifying pages in the `_posts` directory of the repository master branch, using the standard pull request workflow.

A page should start with [Jekyll frontmatter](http://jekyllrb.com/docs/frontmatter/) as shown in the following example:

```
---
layout: article
title: Contributing to Quattor Web Site
category: documentation
author: Michel Jouvin
---
```

Valid categories are `news` or `documentation`.

To contribute to the web site, the standard GitHub work-flow (clone, branch, pull request) is followed.
Before opening a pull request, it is **important to test** your pages and ensure that they display as expected.
Testing your pages is something that must be done on your development machine and this requires to have a local Jekyll installation:
this cannot be tested on GitHub and just checking the rendering in the pull request is not enough as Jekyll has subtle differences with markdown used in other parts of GitHub.

This documentation gives a very brief installation on how to install and use Jekyll locally on your development system and contains a few remarks
on Jekyll markdown to avoid common pitfalls.


## Installing Ruby

Install [Ruby](https://www.ruby-lang.org/) 2.x and [Bundler](http://bundler.io/) if you don't have them installed already.

There are a few things to consider if you want to run Jekyll on Windows, which are well documented [on the Jekyll website](http://jekyllrb.com/docs/windows/#installation).
Apart these specific installation steps, it runs perfectly on Windows.

### Installing Jekyll and dependencies

Everything needed to build the website is described in the `Gemfile`, to install everything simply run:

    bundle install

You can keep your local bundle up to date by running:

    bundle update

## Using Jekyll

To start a local Jekyll server, go to the directory where you have cloned `quattor.github.com` and run:

    bundle exec jekyll serve -w

The server will start on port 4000 by default and watch for changes to the source files.

Jekyll does not use the pages you wrote directly but generates the site (under `_site`) from these pages.
As a consequence, you will need to wait a few seconds for Jekyll to rebuild the pages after each modification.

For more information on using Jekyll at GitHub and troubleshooting problems, you may want to visit [GitHub's Jekyll](https://help.github.com/articles/using-jekyll-with-pages) pages.

## Running tests

When you open a pull-request, [TravisCI](https://travis-ci.org/quattor/quattor.github.com) will run HTML-Proofer against Jekyll's output.
You can run the same tests locally by calling:

    ./travis-build

## Jekyll Markdown tricks

This documentation doesn't intend to be yet another Markdown documentation or tutorial.
There are plenty of existing guides: good starting points are:

* [Github Flavoured Markdown](https://help.github.com/articles/github-flavored-markdown).
* [Kramdown syntax guide](http://kramdown.gettalong.org/syntax.html#code-blocks) (much more detailed).

The sections below highlight a few commonly encountered difficulties when starting with Jekyll Markdown.

### Paragraph delimiter

In GFM, every line break is interpreted as a paragraph delimiter. Jekyll as a standard `markdown` requires a blank line.

This is true also to get special characters like `*` (bulleted list), <code>```</code> (fenced code block) to be interpreted, as they are taken into
account only a the start of a paragraph. If there is no blank line before them, they are considered part of the paragraph.

### Fenced code blocks in item lists

A fenced code block (between <code>```</code> lines) is terminating the list if it is starting on the first character of the line (without any identation). This
is not very pretty for bulleted list but this is even worst with numbered list: this breaks the numbering (every item starts a new list).

To include fenced code blocks without breaking the item list, the fenced blocks (including delimiters) must be indented to be in-line with the first character of the list item they belong to (two spaces for unordered lists, three for ordered).
A single line of whitespace must be present before and after each code block. Below is an example:

```
1. This is a numbered list.
1. I'm going to include a fenced code block as part of this item:

   ```
   Code
   More Code
   ```

1. We can put fenced code blocks inside nested bullets, too.
   * Like this:

     ```c
     printf("Hello, World!");
     ```

   1. The key is to indent your fenced block by **2** spaces.
   1. Also need to put a separating newline above and below the fenced block.
```

will display as:

1. This is a numbered list.
1. I'm going to include a fenced code block as part of this item:

   ```
   Code
   More Code
   ```

1. We can put fenced code blocks inside nested bullets, too.
   * Like this:

     ```c
     printf("Hello, World!");
     ```

   1. The key is to indent your fenced block by **2** spaces.
   1. Also need to put a separating newline above and below the fenced block.
