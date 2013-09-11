---
layout: article
title: Quattor 13.9 is out!!
category: news
---

We have just tagged and uploaded to the
[Yum repositories](http://yum.quattor.org) Quattor 13.9.  Special
changes include:

## New features

* `ncm-ncd` can now execute
  [hooks before and after running any components](https://trac.lal.in2p3.fr/Quattor/wiki/Development/PrePostActionsNCMNCD).
  The API is not yet set in stone, and might change in future
  releases.

### Useability improvements

* Quattor commands have been renamed, to be more meaningful:
  * `quattor-configure` executes configuration modules, aliasing old
    `ncm-ncd`.
  * `quattor-query` queries the profile in a node, aliasing old
    `ncm-query`.
  * `quattor-installer` aliases many `aii-shellfe` options.
* `quattor-configure` and `quattor-query` (and their old names) have
  now basic Bash autocompletion support.  The names of the the
  installed components and the most common options will be expanded.

## Improvements to configuration modules

* `network` used to conflict with NetworkManager.  It is now allowed
  to
  [disable it up front](https://github.com/quattor/configuration-modules-core/pull/88).
* The `add` flag for `ncm-chkconfig` implies
  [restoring the service runlevel to its default values](https://github.com/quattor/configuration-modules-core/pull/99)


### Backwards-incompatible changes

* `sudo` supports now
  [the EXEC, SETENV, LOG_INPUT, LOG_OUTPUT and their NO_* counterparts](https://github.com/quattor/configuration-modules-core/pull/98)
  in the privilege lines.  The validation for this field has changed,
  and you'll have to add the ':' characters yourself.
* `openvpn` supports multiple server configurations.  Your existing
  server configurations must be enclosed in an nlist now.

## Bugs fixed

* `ncm-spma` improved its detection of packages that couldn't be
  versionlocked.
* Components complying with the
  [coding style](https://trac.lal.in2p3.fr/Quattor/wiki/Development/Code/CodingStyle)
  document will now show the changes that would happen to a file, even
  under `--noaction`.
* `metaconfig`
  [supports now noaction](https://github.com/quattor/configuration-modules-core/pull/102).
* The installer works reliably again on SL 6.4.

## Upgrading

We have created a
[GitHub repository](https://github.com/quattor/config-modules-core-templates)
for simplifying the upgrades of the core configuration modules.  Just
clone this repository or download the appropriate tag.

If this approach is useful, future releases will provide
easy-to-download templates for the Grid modules and the client
packages.

## Next release

Next release will be Quattor 13.10 and will happen by the end of October.
