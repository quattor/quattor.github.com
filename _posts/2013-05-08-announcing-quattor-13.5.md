---
layout: article
title: Quattor 13.5 is out!!
category: news
---

We have just tagged and uploaded to the
[Yum repositories](http://yum.quattor.org) Quattor 13.5.  Special
changes include:

## New configuration modules

### Moved from the Stratuslab repositories

Modules configuring [Ganglia](http://ganglia.sourceforge.net/) and
[libvirtd](http://libvirt.org/) have been moved to the core
repository, and are part now of our releases.  Many thanks to the
Stratuslab members for this contribution.

### Imported from old SVN

We have recovered `ncm-cups` from the old Subversion repositories.
There weren't any reports about the usage of this component during
many years, so we don't know if it will handle correctly modern
versions of CUPS.

## Improvements to configuration modules

* `ssh`: The component now
  [validates the configuration file for SSHD](https://github.com/quattor/configuration-modules-core/pull/46)
  before writing it to disk.
* `download`: had many fixes
* `metaconfig`:
  [do not rewrite a file if it cannot be rendered properly](https://github.com/quattor/configuration-modules-core/issues/40).
  Also, it is now possible to add preambles to the generated files.
* `spma`:
  * [Handle wildcards in package declarations](https://github.com/quattor/configuration-modules-core/pull/60).
    Please see the full documentation of
    [how to manage packages](http://quattor.org/documentation/2013/04/05/package-management.html)
  * [Detect when packages in the profile fail to install](https://github.com/quattor/configuration-modules-core/issues/58).
  * The way packages are selected for removal has been
    [greately improved](https://github.com/quattor/configuration-modules-core/pull/33).
    The new version should be more robust and produce way less
    conflicting transactions.
* `modprobe` generates correct initrds again.

## Improvements to the automatic installer

* The Kickstart generator now supports the `logging` directive.  This
  will enable syslog during the Anaconda phase.
* The installer will try harder to bootstrap the machine even if some
  Yum repositories are temporarily unavailable.
* LVM on SL5 is correctly handled again.

## Next release

Next release will be Quattor 13.6 and will happen end of June.
