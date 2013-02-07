---
layout: article
title: Upgrading to the Yum-based SPMA
category: review
---

## Introduction

Quattor 13.02 ships with an entirely rewritten package manager, based
on Yum.  We explain here the steps needed to upgrade, both on an
already-installed worker node and on a freshly installed one.

## Getting the RPMs

You should [mirror the Yum repository](documentation/2013/01/11/mirroring-yum.html) for Quattor 13.02 or later.

### Getting the new Yum builds for SL5

The new SPMA requires at least the versions of Yum and Yum utils that
are part of SL6.  Fortunately, we can install them on SL5, too.  The
RPMs are available [here]()

## Creating the repository template

If you downloaded the RPMs into an existing repository, you just need
to run

```
ant update.rep.templates
```

Otherwise, you probably have to adjust the URL of an existing
repository template, or create a new one.  The instructions are
[at the old website](https://trac.lal.in2p3.fr/Quattor/wiki/Doc/SCDB/SWRepositories)

## Upgrading the component's templates

You can get them from the QWG repository, extract the templates from
the RPM and copy them:

    rpm2cpio ncm-spma-13.02.0-1.noarch.rpm|cpio -i --make-directories
    find usr/ -name '*.pan' -exec cp '{}' <your/working/copy/>/components/spma

or build the component your self from Git.

## Dependencies

This is your last experience with SPMA's dependency hell!

The new SPMA requires:

* `perl-Set-Scalar`, available from the Dag repository
* In SL5, `python-kitchen`, and `python-elementtree`.  The former is
  available in the EPEL repository.
* `yum-plugin-versionlock` (called `yum-versionlock` on SL5)
* Recent enough Yum and Yum utils.  The stock versions for SL6
  work.  For SL5, we recommend [the RPMs provided by UGent]().

The following lines work for SL5:

    "/software/packages" = {
        pkg_repl("perl-Set-Scalar", "1.25-1.el5.rf", "noarch");
        pkg_repl("yum", "3.2.29-20.el5, "noarch");
        pkg_repl("yum-versionlock", "1.1.16-21.el5", "noarch");
        pkg_repl("yum-utils", "1.1.31-4", "noarch");
    };

And for SL6:

    "/software/packages" = {
        pkg_repl("perl-Set-Scalar", "1.25-2.el6", "noarch");
        pkg_repl("yum", "3.2.29-22.el6_2.2", "noarch");
        pkg_repl("yum-plugin-versionlock", "1.1.30-10.el6", "noarch");
    };

## Deploying

With all this done, just deploy.  Use `ant deploy` or your in-home
equivalent.

The old SPMA will be able to install the new one.

## What's next

With this we cover the basics on how to upgrade to the new SPMA.

However, this is the least important step.  Probably, you have to
re-think your [upgrade]() and [mirroring]() strategies.
