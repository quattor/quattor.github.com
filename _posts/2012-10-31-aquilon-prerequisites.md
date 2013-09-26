---
layout: article
title: Aquilon Prerequisites
category: documentation
---

Dependencies for Aquilon on SL.  If using the Yum-based SPMA, Yum will
pull them in when installing the Aquilon RPM.

We will try to provide a Yum repository with these external
dependencies.  In the mean time, these are the steps to build the
missing bits yourself:

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

* Grab the SPEC file.
* Download the source tarball:

```sh
spectool -g knc.spec
```
* Build the RPM:

```sh
mock --spec knc.spec --sources <path-to-knc-sources> --buildsrpm
mock --rebuild knc*src.rpm
```

## Twisted

The versions shipped with Scientific Linux or Red Hat are too old.  At
least version 12.2 is needed.

Good news is that it's trivial to build:

* Get the Fedora 20 SRC RPMs for `python-twisted-web`,
   `python-twisted-core` and `python-twisted-runner` and `pyserial`.
* Install `mock` in your SL6 build system:

```sh
yum -y install mock
```

* Add yourself to the `mock` group.
* Build each package and install it into the mock environment

```sh
mock --no-clean --rebuild pyserial*src.rpm --resultdir twisted/
mock --no-clean --install twisted/pyserial*noarch.rpm
mock --no-clean --rebuild python-twisted-core*src.rpm --resultdir twisted/
mock --no-clean --install twisted/python-twisted-core*x86_64.rpm
mock --no-clean --rebuild python-twisted-web*src.rpm --resultdir twisted/
mock --no-clean --install twisted/python-twisted-web*noarch.rpm
mock --no-clean --rebuild python-twisted-runner*src.rpm --resultdir twisted/
```

* Your EL6 RPMs are now in the `twisted/` directory.  Copy them to
   your Yum repositories.

## SQLAlchemy

Again, we need version 0.8, not available yet on Scientific Linux.
Building it is also easy:

* Download the Fedora 20 SRC RPM.
* Install it locally

```sh
rpm -i python-sqlalchemy-0.8*src.rpm
```

* Edit the SPEC file and remove the `check` section.
* Rebuild with `rpmbuild -ba python-sqlalchemy.spec`.
