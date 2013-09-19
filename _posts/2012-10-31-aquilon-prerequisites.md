---
layout: article
title: Aquilon Prerequisites
category: documentation
---

Dependencies for Aquilon on SL.  If using the Yum-based SPMA, Yum will
pull them in when installing the Aquilon RPM.

## Before we start: setting up mock

We'll need to install `mock` in our systems.  Just `yum -y install
mock`.

## KNC

This is the
[Kerberised NetCat](http://oskt.secure-endpoints.com/knc.html).  As of
Aquilon 1.10, version 1.7.1 is needed.  It is part of
[Repoforge](http://repoforge.org), but as of this writing they haven't
built it yet.

To build it yourself:

## Twisted

The versions shipped with Scientific Linux or Red Hat are too old.  At
least version 12.2 is needed.

Good news is that it's trivial to build:

1. Get the Fedora 20 SRC RPMs for `python-twisted-web`,
   `python-twisted-core` and `python-twisted-runner` and `pyserial`.
1. Install `mock` in your SL6 build system:
```bash
yum -y install mock
```
1. Add yourself to the `mock` group.
1. Build each package and install it into the mock environment
```bash
mock --no-clean --rebuild pyserial*src.rpm --resultdir twisted/
mock --no-clean --install twisted/pyserial*noarch.rpm
mock --no-clean --rebuild python-twisted-core*src.rpm --resultdir twisted/
mock --no-clean --install twisted/python-twisted-core*x86_64.rpm
mock --no-clean --rebuild python-twisted-web*src.rpm --resultdir twisted/
mock --no-clean --install twisted/python-twisted-web*noarch.rpm
mock --no-clean --rebuild python-twisted-runner*src.rpm --resultdir twisted/
```
1. Your EL6 RPMs are now in the `twisted/` directory.  Copy them to
   your Yum repositories.
