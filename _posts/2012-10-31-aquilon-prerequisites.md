---
layout: article
title: Aquilon Prerequisites
category: documentation
modified: 2013-10-25
---

Most pre-requisites for Aquilon are either provided in the standard
Scientific Linux repositories (including Repoforge and EPEL).  The few
RPMs that SL doesn't provide are in the
[Aquilon Yum repository](http://yum.quattor.org/aquilon), and are:

* [KNC, the Kerberised NetCat](http://oskt.secure-endpoints.com/knc.html).
It is part of [Repoforge](http://repoforge.org), but as of this
writing they haven't built it yet. In the mean time it can be found in
[our externals repository](http://yum.quattor.org/externals/).
* `pyserial`, as a dependency for twisted
* `python-twisted-core`
* `python-twisted-web`
* `python-twisted-runner`
* `python-sqlalchemy`

The Python modules have been built from the Fedora 20 source RPMs.
