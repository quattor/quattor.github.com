---
layout: article
title: Pan compiler v10.0 released
category: news
---

Version 10.0 of the Pan compiler is out. It contains the following changes:

* [Remove session directory functionality](https://github.com/quattor/pan/issues/27)
* [Remove deprecated options from panc ant task](https://github.com/quattor/pan/issues/5)
* [Remove panc-old script](https://github.com/quattor/pan/issues/4)
* [Remove deprecation level attribute in favor of warnings attribute in pan-syntax-check mojo](https://github.com/quattor/pan/issues/2)
* [Restore backward compatibility for gzip output flag](https://github.com/quattor/pan/issues/26)

**NOTE**: This is **NOT A DROP-IN REPLACEMENT** for pan v9.x!  The panc
script, ant task, and maven plugins use a consistent and streamlined
set of options that are not backward compatible.  The changes from the
old options to the new ones should be obvious, but there is
information in the pan book if more detail is needed.

**NOTE**: Some users have reported degraded performance with this
version of the compiler.  In my own tests v10.0 is about 13% slower in
real time than v9.2.  At the same time, v10.0 uses about 11% less CPU
than v9.3.  This probably means a higher level of I/O contention in
the newer version, but I've not had time to track down the cause.
This will hopefully be resolved in the incremental v10 series releases
to come.

As usual, this release is available in
[SourceForge](https://sourceforge.net/projects/quattor/files/panc/10.0/?).

The various artefacts of the build are also available through the
[central Maven repository](http://repo.maven.apache.org/maven2/org/quattor/pan/panc/10.0/).
