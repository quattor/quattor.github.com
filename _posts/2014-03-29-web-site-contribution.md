---
layout: article
title: Contributing to Quattor Web Site
category: documentation
author: Michel Jouvin
---


This page gives advices and best practices for contributing to Quattor web site.

## Introduction

Quattor [web site](http://quattor.org) is hosted on GitHub, using the GitHub Pages service, and is the main source of information about Quattor.

GitHub Pages uses [Jekyll](http://jekyllrb.com), a framework to build blog-aware web sites. Pages are written using the GitHub Flavored Markdown 
([GFC](https://help.github.com/articles/github-flavored-markdown)) syntax. They are stored in Quattor `quattor.github.com` repository on GitHub.
Contents is added/modified to the web site by adding/modifying pages in the `_posts` directory of the repository master branch, using standard
pull request workflow.

A page must start with special header lines like:

```
---
layout: article
title: Contributing to Quattor Web Site
category: documentation
author: Michel Jouvin
---
```

Valid categories are `news`, `blog` and `documentation`.

To contribute to the web site, it is important to the standard GitHub workflow (clone, branch, pull request). But before making a pull request, it is also 
**important to test** your pages and ensure that they display as expected. Testing your pages is something that must be done on your development machine
and this requires to have a local Jekyll installation: this cannot be tested on GitHub and just checking the rendering in the pull request is not enough
as Jekyll has subtle differences with markdown used in other parts of GitHub.

This documentation gives a very brief installation on how to install and use Jekyll locally on your development system. And it contains a few remarks
on Jekyll markdown to avoid common pitfalls.


## Installing Jekyll

Jekyll installation is well documented on Jekyll [web site](http://jekyllrb.com/docs/installation). This involves installing Ruby if you don't have it
already. There are a few specificities if you want to run Jekyll on Windows, also well documented in a [dedicated page](http://jekyllrb.com/docs/windows/#installation).
Apart these specific installation steps, it runs perfectly on Windows.

### Windows pitfalls

A few common problems when installing Jekyll on Windows (7/8) are:

* Be sure to use the Ruby and Ruby Development Kit for your architecture. You should not try to use 32-bit version on Windows x64.
* Jekyll uses internally `Pygments`, a Python module for doing syntax highlighting. Ruby-Python mix on Windows is a nightmare and you should avoid it! The
workaround is to use an alternate, pure-Ruby, compatible highlighting system called `rouge`. It is easily installed with:

     ```
     gem install rouge
     ```
    
To use `rouge` instead of `Pygments`, you need to specify an alternate configuration file when starting Jekyll with option `--config=`. The configuration file
depends on the version of Jekyll you are using:

* Jekyll v1.9 (current version at the time of this writing): `_config_rouge.yml` (`--config=_config_rouge.yml`)
* Jekyll v2: `_config_rouge_v2.yml`  (`--config=_config_rouge_v2.yml`)


## Using Jekyll

To start your local Jekyll server, the easiest is to go to the directory where your Git clone of `quattor.github.com` is and issue the following command:

```
jekyll server --baseurl='' [--config=file]  (see above)
```

The server is starting on port 4000 by default.

Jekyll is not using the pages you wrote directly but is generating the site from these pages. As a consquence, you need to **restart the server** after
every page modification you want to see.


## Jekyll Markdown tricks

This documentation doesn't intend to be yet another Markdown documentation or tutorial. There are plenty of them: a good entry point is 
[GFC web site](https://help.github.com/articles/github-flavored-markdown). The sections below describes a few frequent difficulties when starting
with Jekyll Markdown.


### Paragraph delimiter

In GFC, every line break is interpreted as a paragraph delimiter. Jekyll as a standard `markdown` requires a blank line.

This is true also to get the special characters like `*` (bulleted list), ````` (fenced code block) be interpreted, as they are taken into
account only a the start of a paragraph. If there is no blank line before them, they are considered as text part of the paragraph.

### Fenced code blocks in item lists

A fenced code block (between ````` lines) is terminating the list if it is starting on the first character of the line (without any identation). This
is not very pretty for bulleted list but this is even worst with numbered list: this breaks the numbering (every item starts a new list).

To include fenced code blocks without breaking the item list, the fenced blocks (including delimiters) must be idented with a number of space equals to
`4 * list level`. Below is an example:

```markdown
1. This is a numbered list.
1. I'm going to include a fenced code block as part of this bullet:

    ```
    Code
    More Code
    ```
1. We can put fenced code blocks inside nested bullets, too.
   1. Like this:

        ```c
        printf("Hello, World!");
        ```
   1. The key is to indent your fenced block by **(4 * bullet_indent_level)** spaces.
   1. Also need to put a separating newline above and below the fenced block.
```

will display as:

1. This is a numbered list.
1. I'm going to include a fenced code block as part of this bullet:

    ```
    Code
    More Code
    ```
1. We can put fenced code blocks inside nested bullets, too.
   1. Like this:

        ```c
        printf("Hello, World!");
        ```
   1. The key is to indent your fenced block by **(4 * bullet_indent_level)** spaces.
   1. Also need to put a separating newline above and below the fenced block.