---
layout: article
title: Quattor 14.2.1 released
category: news
author: James Adams
---

After some delay caused by more than one failure of our release system, Quattor 14.2.1 has been released.

This release incorporates a large number of changes, notably:

  * `AII` - Support for `pXpY` and `emZ` [style network interfaces](https://github.com/quattor/aii/pull/39).
  * `ncm-ccm` - Fixed a bug which caused [tests to use incorrect parameter names](https://github.com/quattor/configuration-modules-core/pull/140).
  * `ncm-spma` - Support for [IPS packaging on Solaris](https://github.com/quattor/configuration-modules-core/pull/129).
  * `ncm-ncd` - Support for [choosing the Perl module behind a component](https://github.com/quattor/ncm-ncd/pull/11).
  * `ccm-purge` - Fixes to [add support for selectable database backends and configure a fixed number of profiles to keep](https://github.com/quattor/CCM/pull/16).
  * `ncm-pam` - [Various fixes](https://github.com/quattor/configuration-modules-core/pull/142).
  * `ncm-accounts` - Fixed [a bug](https://github.com/quattor/configuration-modules-core/issues/2) which prevented removal of unknown accounts in certain situations.
  * `ncm-iptables` - [Support for the 'log' target](https://github.com/quattor/configuration-modules-core/pull/144).

As always, thanks to everyone who contributed, next stop Quattor 14.4.

Complete Changelog
==================

aii
---

  * [Extend the validation regexp for bootif](https://github.com/quattor/aii/commit/7b23e7c)

CCM
---

  * [Replace ${file} with $file in an error message](https://github.com/quattor/CCM/commit/4c535b9)
  * [Use LC::Stat constants in ccm-purge](https://github.com/quattor/CCM/commit/9999987)
  * [Make purge time configurable via ccm.conf](https://github.com/quattor/CCM/commit/c3f811e)
  * [POD fixes for ccm-fetch](https://github.com/quattor/CCM/commit/909c5fa)
  * [ccm-purge: Keep minimum number of old profiles](https://github.com/quattor/CCM/commit/10cbb2f)
  * [ccm-purge: fix whitespace](https://github.com/quattor/CCM/commit/b1abf21)
  * [ccm-purge: add support for selectable database backends](https://github.com/quattor/CCM/commit/b4a6051)

cdp-listend
-----------

  * [Avoid cdp-listend start in early stage of Anaconda installation](https://github.com/quattor/cdp-listend/commit/e1f6552)

configuration-modules-core
--------------------------

  * [Enhanced package resolution to help the transition from SPMA to YUM. (allow to restrict package resolution to packages required by AII v2)](https://github.com/quattor/configuration-modules-core/commit/56da135)
  * [Uncomment done_testing()](https://github.com/quattor/configuration-modules-core/commit/52c2842)
  * [Fix bugs in ncm-grub](https://github.com/quattor/configuration-modules-core/commit/fcb5b7c)
  * [Remove boilerplate authors and acknowledge Jagath](https://github.com/quattor/configuration-modules-core/commit/9403450)
  * [ncm-grub: When $fullcontrol defined as "true", ncm-grub will chop the last charactor of the boot argument will result](https://github.com/quattor/configuration-modules-core/commit/a6ace6e)
  * [ncm-grub: if $fullcontrol defined as "false" in templates, ncm-grub reads it as "true" which will create wrong kernel args for default kernel](https://github.com/quattor/configuration-modules-core/commit/51734cc)
  * [Test the top-level SPMA component](https://github.com/quattor/configuration-modules-core/commit/fdee6ba)
  * [Add support for Solaris IPS.](https://github.com/quattor/configuration-modules-core/commit/108c400)
  * [Specify RPM dependencies manually to prevent dependency on perl(IPS)](https://github.com/quattor/configuration-modules-core/commit/de990ea)
  * [Add 'log' to the permissible targets of the nat table, otherwise rules that have log as a target will result in a broken iptables configuration.](https://github.com/quattor/configuration-modules-core/commit/d955f1f)
  * [Default packager should be 'yum'](https://github.com/quattor/configuration-modules-core/commit/e9138e7)
  * [The packager can only be 'yum' or 'ips'](https://github.com/quattor/configuration-modules-core/commit/27e00de)
  * [Drop dependencies on IPS from the RPM](https://github.com/quattor/configuration-modules-core/commit/e62729c)
  * [Whitespace and pom clean ups in ncm-pam](https://github.com/quattor/configuration-modules-core/commit/9f7d632)
  * [Adding missing functionality to ncm-pam](https://github.com/quattor/configuration-modules-core/commit/b004ab8)
  * [include Luis' suggestions](https://github.com/quattor/configuration-modules-core/commit/260978b)
  * [Change if @var > 0 to just @var](https://github.com/quattor/configuration-modules-core/commit/ae7545e)
  * [Report exact set publisher command if it fails](https://github.com/quattor/configuration-modules-core/commit/abc9bc0)
  * [use base instead of use vars with @ISA](https://github.com/quattor/configuration-modules-core/commit/9aa435e)
  * [Add a test for bug #138](https://github.com/quattor/configuration-modules-core/commit/8144c54)
  * [Remove boilerplate from the POM file.](https://github.com/quattor/configuration-modules-core/commit/8bb8022)
  * [Fix the defaults.pan template in sindes_getcert](https://github.com/quattor/configuration-modules-core/commit/820d02a)
  * [Run ccm-fetch with the correct parameters.](https://github.com/quattor/configuration-modules-core/commit/4f3c42c)
  * [Add end-to-end tests of Configure() entry point](https://github.com/quattor/configuration-modules-core/commit/420a57e)
  * [Continue if resource path does not exist](https://github.com/quattor/configuration-modules-core/commit/c5c8597)
  * [Use $$ for current PID in cmdfile and flagfile](https://github.com/quattor/configuration-modules-core/commit/dd8a5ae)
  * [Use current user ID on calls to CAF::FileWriter](https://github.com/quattor/configuration-modules-core/commit/62ee317)
  * [Add more Solaris SPMA unit tests](https://github.com/quattor/configuration-modules-core/commit/8f3253a)
  * [Add ips/imagedir to test PAN](https://github.com/quattor/configuration-modules-core/commit/104ef58)
  * [CAF::Process might return undef output](https://github.com/quattor/configuration-modules-core/commit/5e956c5)
  * [Add imagedir override to IPS schema](https://github.com/quattor/configuration-modules-core/commit/acf2e7a)
  * [Need build-profile 1.33 for $self->log fix](https://github.com/quattor/configuration-modules-core/commit/4867d2e)
  * [CAF::Process may return undef in run_pkg_command()](https://github.com/quattor/configuration-modules-core/commit/1b81b5b)
  * [First set of unit tests for Solaris SPMA](https://github.com/quattor/configuration-modules-core/commit/422744f)
  * [CAF::Process can return undef when testing](https://github.com/quattor/configuration-modules-core/commit/f44298c)
  * [image_create() should use current owner, not UID 0](https://github.com/quattor/configuration-modules-core/commit/7dd0dfa)
  * [get_fresh_pkgs() can take optional imagedir](https://github.com/quattor/configuration-modules-core/commit/24f8b21)
  * [Set spma.ips.author as distinct from author-info](https://github.com/quattor/configuration-modules-core/commit/103e968)
  * [merge_pkg_paths() should be a method](https://github.com/quattor/configuration-modules-core/commit/df66c04)
  * [Add spma-run to build directory](https://github.com/quattor/configuration-modules-core/commit/854dcfa)
  * [Add IPS library so that spma::ips can be tested](https://github.com/quattor/configuration-modules-core/commit/60730a8)
  * [Modify tests to use spma::yum](https://github.com/quattor/configuration-modules-core/commit/f53de46)
  * [Add Mark Bannister as contributor](https://github.com/quattor/configuration-modules-core/commit/f717d9f)
  * [Install all files in the right places.](https://github.com/quattor/configuration-modules-core/commit/87fe0fe)
  * [Module is now called NCM::Component::spma::yum](https://github.com/quattor/configuration-modules-core/commit/88099fb)
  * [Module is now called NCM::Component::spma::yum](https://github.com/quattor/configuration-modules-core/commit/1b5001c)
  * [Dump list of repos used if package not found](https://github.com/quattor/configuration-modules-core/commit/71f01a3)
  * [Minor update for spma::yum submodule](https://github.com/quattor/configuration-modules-core/commit/660e1ee)
  * [Add AUTHOR](https://github.com/quattor/configuration-modules-core/commit/e783adf)
  * [Add top-level spma.pod file](https://github.com/quattor/configuration-modules-core/commit/a5040ba)
  * [Don't use newlines with $self->error() as these also go to syslog](https://github.com/quattor/configuration-modules-core/commit/35df93c)
  * [Use project.version and let maven fill it in](https://github.com/quattor/configuration-modules-core/commit/44bfdea)
  * [Use pushargs() and rename imagedir_new to newdir](https://github.com/quattor/configuration-modules-core/commit/4419c71)
  * [image_create() now takes parameter (for image dir)](https://github.com/quattor/configuration-modules-core/commit/8c3ed5c)
  * [Verify format of packager before attempting to use it](https://github.com/quattor/configuration-modules-core/commit/8606dd7)
  * [CAF::Process splits on your behalf](https://github.com/quattor/configuration-modules-core/commit/8d6cc73)
  * [Put less code in main package, more in spmarun](https://github.com/quattor/configuration-modules-core/commit/24fd9cb)
  * [Use constants for well-known exit statuses](https://github.com/quattor/configuration-modules-core/commit/67acf88)
  * [Add missing semi-colon](https://github.com/quattor/configuration-modules-core/commit/d996a72)
  * [Use standard header](https://github.com/quattor/configuration-modules-core/commit/88b78cf)
  * [Initial commit of SPMA for Solaris 11 (with IPS)](https://github.com/quattor/configuration-modules-core/commit/e1f7908)

configuration-modules-grid
--------------------------

  * [support configuration of CHECKPOINTDIR](https://github.com/quattor/configuration-modules-grid/commit/6fdb639)

ncm-ncd
-------

  * [Fix bug when instantiating component proxies](https://github.com/quattor/ncm-ncd/commit/cdfbc46)
  * [Use the module when executing component methods](https://github.com/quattor/ncm-ncd/commit/c1acbbe)
  * [Fix the module's path when reporting EC errors](https://github.com/quattor/ncm-ncd/commit/e3fb4b0)
  * [Sanitise correctly the NCM module](https://github.com/quattor/ncm-ncd/commit/79d01c8)
  * [Remove some clutter](https://github.com/quattor/ncm-ncd/commit/1901c1f)
  * [Test the hasFile() method](https://github.com/quattor/ncm-ncd/commit/d4d6c1c)
  * [Fix bug in hasFile()](https://github.com/quattor/ncm-ncd/commit/b247f3c)
  * [Test prefix() with ncm-module and namespaces](https://github.com/quattor/ncm-ncd/commit/4041058)
  * [Remove some unwanted clutter](https://github.com/quattor/ncm-ncd/commit/a3b7198)
  * [Sanitize the name of the module to be loaded](https://github.com/quattor/ncm-ncd/commit/a15b2d0)
  * [Fix warning](https://github.com/quattor/ncm-ncd/commit/9ea4b33)
  * [Test and fix bug in component skipping.](https://github.com/quattor/ncm-ncd/commit/1b9bff5)
  * [Test the run_all_components method](https://github.com/quattor/ncm-ncd/commit/9174e0e)
  * [Improve gitignore](https://github.com/quattor/ncm-ncd/commit/581f03c)
  * [Remove unneeded cluck](https://github.com/quattor/ncm-ncd/commit/11901ca)
  * [Cosmetic change](https://github.com/quattor/ncm-ncd/commit/2e61256)
  * [Refactor _getComponents and executeConfigComponents](https://github.com/quattor/ncm-ncd/commit/4bca515)
  * [Test dependency resolution among components.](https://github.com/quattor/ncm-ncd/commit/2807a7c)
  * [Turn autodeps and allowbrokencomponents into boolean options](https://github.com/quattor/ncm-ncd/commit/0c9a5ac)
  * [Add simple tests for the _getComponents method.](https://github.com/quattor/ncm-ncd/commit/f87d11e)
  * [Validate the module name](https://github.com/quattor/ncm-ncd/commit/0aec63d)
  * [Use the declared module as the file associated to the component.](https://github.com/quattor/ncm-ncd/commit/8f7f674)
  * [Use the NAME field for the prefix](https://github.com/quattor/ncm-ncd/commit/e5c9f85)
  * [Load the Perl module specified in the profile](https://github.com/quattor/ncm-ncd/commit/44b9f00)
  * [Add an accessor for the MODULE field.](https://github.com/quattor/ncm-ncd/commit/4fb3776)
  * [Load the module and not the component name](https://github.com/quattor/ncm-ncd/commit/660a70b)
  * [Store the module to run with the component proxy](https://github.com/quattor/ncm-ncd/commit/c66af26)
  * [Test the _initialize method of ComponentProxy](https://github.com/quattor/ncm-ncd/commit/e065f20)
  * [Minor code cleanups.](https://github.com/quattor/ncm-ncd/commit/9bf5acf)
  * [Indent properly](https://github.com/quattor/ncm-ncd/commit/9b64ad4)
  * [Use the module to load from the ncm-module field](https://github.com/quattor/ncm-ncd/commit/8f8ceac)

