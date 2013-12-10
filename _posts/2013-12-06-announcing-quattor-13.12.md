---
layout: article
title: Quattor 13.12 is out!!
category: news
---

We have just tagged and uploaded to the
[Yum repositories](http://yum.quattor.org) Quattor 13.12.  Special
changes include:

## New features

### ncm-ncd

* Pre-deployment hooks receive now the list of components
  [scheduled for execution](https://github.com/quattor/ncm-ncd/pull/10).

### Configuration modules

* `ncm-metaconfig` now can
  [generate Java properties files](https://github.com/quattor/configuration-modules-core/pull/130).
  Use the `properties` module for that.

## Improvements to the automatic installer

* The kickstart generator now
  [supports the enable_service option](https://github.com/quattor/aii/pull/35).

## Miscellaneous bug fixes

### Packaging fixes

All packages ship now their man pages under `/usr/share/man`, which is
part of the standard MANPATH.

This fixes issues with users not finding the correct man pages.

### No more spurious lock errors on EL5

Under some circumstances, the CAF framework would display lots of
[lock-related errors in EL5 systems](https://github.com/quattor/CAF/issues/6).
This [is  fixed now](https://github.com/quattor/CAF/pull/7).

### Hooks in ncm-ncd

Pre and post-deployment hooks in ncm-ncd
[work now](https://github.com/quattor/ncm-ncd/pull/9).

### Fixes in configuration modules

* The package manager now
  [runs when the repository definitions change](https://github.com/quattor/configuration-modules-core/pull/128).
* Minor fixes in
  [ncm-openldap](https://github.com/quattor/configuration-modules-core/pull/134) and
  [ncm-ofed](https://github.com/quattor/configuration-modules-core/pull/111)
* We have fixed some
  [perl warnings in ncm-named](https://github.com/quattor/configuration-modules-core/pull/133).

## Upgrading

You can get the RPMs from the
[Yum repositories](http://yum.quattor.org).  Templates are provided,
as usual, in the
[core template library repository](https://github.com/quattor/template-library-core/tags)
in Github.

## Out of this release

Solaris support is improving!  We have received a `pkgtree` utility
for handling packages with Solaris IPS.  We are also merging an `ips`
submodule for SPMA.
