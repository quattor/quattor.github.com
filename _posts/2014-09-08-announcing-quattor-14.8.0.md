---
layout: article
title: Quattor 14.8.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/14.8.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 85 pull requests and resolved 78 issues.

The next release should be 14.10.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Changelog
---------

### template-library-core
* [__13.1.4 release__: 13.1.3 + some modified configuration modules](https://github.com/quattor/template-library-core/pull/34)
* [Fix too restrictive check for boot interface MTU configuration](https://github.com/quattor/template-library-core/pull/56)
* [__Quattor schema__: make /system/kernel mandatory and /system/kernel/version optional](https://github.com/quattor/template-library-core/pull/54)

### ncm-cdispd
* [Improve ncd status logging](https://github.com/quattor/ncm-cdispd/pull/13)
* [Log delayed signal handling as info](https://github.com/quattor/ncm-cdispd/pull/16)
* [ncm-cdispd code cleanup](https://github.com/quattor/ncm-cdispd/pull/11)
* [ncm-cdispd code cleanup](https://github.com/quattor/ncm-cdispd/pull/9)

### configuration-modules-core
* [Improve dirperm documentation](https://github.com/quattor/configuration-modules-core/pull/277)
* [Make `artifactId` consistent with other configuration module repos](https://github.com/quattor/configuration-modules-core/pull/279)
* [Modernise ncm pam](https://github.com/quattor/configuration-modules-core/pull/239)
* [Remove Yum metadata if the repository descriptions change](https://github.com/quattor/configuration-modules-core/pull/236)
* [add clear_warnings before running tests and then check for warnings](https://github.com/quattor/configuration-modules-core/pull/290)
* [__ncm-accounts__: Invalidate nscd caches when databases change](https://github.com/quattor/configuration-modules-core/pull/278)
* [__ncm-aiiserver__: fix unittests on fedora](https://github.com/quattor/configuration-modules-core/pull/286)
* [__ncm-authconfig__: small fix for inconsistency that breaks webpage](https://github.com/quattor/configuration-modules-core/pull/276)
* [__ncm-cdp__: Restart cdp-listend](https://github.com/quattor/configuration-modules-core/pull/283)
* [__ncm-ceph__: add erasure code support](https://github.com/quattor/configuration-modules-core/pull/270)
* [__ncm-ceph__: add option to gather ssh hosts keys automatically](https://github.com/quattor/configuration-modules-core/pull/269)
* [__ncm-ceph__: fixes for issues #224 and #226](https://github.com/quattor/configuration-modules-core/pull/248)
* [__ncm-cron:__ (Linux): do not remove cron entries that are still part of the configuration](https://github.com/quattor/configuration-modules-core/pull/230)
* [__ncm-download__: Fixed false failure bug, added noaction support](https://github.com/quattor/configuration-modules-core/pull/262)
* [__ncm-download__: Force Net::SSL with LWP](https://github.com/quattor/configuration-modules-core/pull/246)
* [__ncm-grub__: fix configuration module definition (suppress snapshot id)](https://github.com/quattor/configuration-modules-core/pull/292)
* [__ncm-grub__: remove support for magic kernel version](https://github.com/quattor/configuration-modules-core/pull/238)
* [__ncm-metaconfig__: Bump build tools to 1.36](https://github.com/quattor/configuration-modules-core/pull/284)
* [__ncm-metaconfig__: Use CAF::Service for restarting daemons](https://github.com/quattor/configuration-modules-core/pull/285)
* [__ncm-metaconfig__: Use CAF::Service for restarting daemons.](https://github.com/quattor/configuration-modules-core/pull/222)
* [__ncm-named__: clear warnings before unittesting](https://github.com/quattor/configuration-modules-core/pull/287)
* [__ncm-named__: fix retrieval of named root directory from sysconfig](https://github.com/quattor/configuration-modules-core/pull/243)
* [__ncm-resolver__: Check all servers listed in configuration](https://github.com/quattor/configuration-modules-core/pull/282)
* [__ncm-resolver__: Merge stderr and stdout when checking for timeouts](https://github.com/quattor/configuration-modules-core/pull/223)
* [__ncm-spma__: retry full update when userpkgs are not allowed](https://github.com/quattor/configuration-modules-core/pull/265)
* [__ncm-spma__: yum-complete-transaction requires -y option to run without interruption](https://github.com/quattor/configuration-modules-core/pull/295)
* [ncm-sudo noaction support](https://github.com/quattor/configuration-modules-core/pull/240)
* [__ncm-useraccess__: add an additional ownership check on .ssh dir](https://github.com/quattor/configuration-modules-core/pull/263)

### ncm-lib-blockdevices
* [Add EU-Datagrid license ](https://github.com/quattor/ncm-lib-blockdevices/pull/36)
* [Fix 2 minor issues](https://github.com/quattor/ncm-lib-blockdevices/pull/35)
* [__Partition.pm__: avoid adding useless code in KS config file](https://github.com/quattor/ncm-lib-blockdevices/pull/34)
* [Require parted binary](https://github.com/quattor/ncm-lib-blockdevices/pull/38)
* [Use all free space when a LV can grow](https://github.com/quattor/ncm-lib-blockdevices/pull/37)

### template-library-standard
* [Add generic templates to describe YUM repositories for Quattor repositories](https://github.com/quattor/template-library-standard/pull/30)
* [Allow GLITE_BASE_CONFIG_SITE to be optional](https://github.com/quattor/template-library-standard/pull/33)
* [Fix inclusion of pakiti config](https://github.com/quattor/template-library-standard/pull/32)
* [__kernel_version_arch__: do not define kernel version if not explicitly set](https://github.com/quattor/template-library-standard/pull/29)

### template-library-grid
* [Apel](https://github.com/quattor/template-library-grid/pull/67)
* [__DPM config__: fix typo leading to missing xrootd redir config](https://github.com/quattor/template-library-grid/pull/73)
* [__LB locallogger__: remove useless configuration of glitestartup configuration module](https://github.com/quattor/template-library-grid/pull/90)
* [__Repository configuration__: add support for using UMD-3 repos rather than EMI-3](https://github.com/quattor/template-library-grid/pull/74)
* [Templates for EMI3 WLCG VOBOX](https://github.com/quattor/template-library-grid/pull/81)
* [__VOBOX__: fix typo](https://github.com/quattor/template-library-grid/pull/89)
* [VOMS certificates and VO params update](https://github.com/quattor/template-library-grid/pull/82)
* [__VOMS config__: do not restart Tomcat after a config change by default](https://github.com/quattor/template-library-grid/pull/75)
* [VOMS server configuration fixes](https://github.com/quattor/template-library-grid/pull/84)
* [WMS configuration fixes](https://github.com/quattor/template-library-grid/pull/88)

### scdb
* [__create-vanilla-SCDB__: rewrite using get-template-library](https://github.com/quattor/scdb/pull/22)
* [__quattor.build.xml__: fix handling of cluster.pan.dep.ignore](https://github.com/quattor/scdb/pull/24)

### ncm-ncd
* [Add add_files and get_files methods](https://github.com/quattor/ncm-ncd/pull/15)

### template-library-os
* [Various package group modifications](https://github.com/quattor/template-library-os/pull/52)
* [sl6.x rpms category adjustments](https://github.com/quattor/template-library-os/pull/50)

### maven-tools
* [bin.xml assembly changes/improvements:](https://github.com/quattor/maven-tools/pull/20)

### aii
* [Make wipe_metadata more reliable](https://github.com/quattor/aii/pull/78)
* [increase log rate and allow for longer sleep. ](https://github.com/quattor/aii/pull/75)
* [kickstart bonding support](https://github.com/quattor/aii/pull/65)
* [make wipe_metadata faster](https://github.com/quattor/aii/pull/61)

### release
* [Check format of release number](https://github.com/quattor/release/pull/47)
* [Correct tag name for core components](https://github.com/quattor/release/pull/52)
* [Push HEAD along with tags](https://github.com/quattor/release/pull/48)

### configuration-modules-grid
* [Add LICENSE](https://github.com/quattor/configuration-modules-grid/pull/32)
* [__glitestartup__: fix EMI support](https://github.com/quattor/configuration-modules-grid/pull/37)
* [__glitestartup__: restore copyright for original version](https://github.com/quattor/configuration-modules-grid/pull/39)
* [__ncm-apel__: Remove outdated apel component](https://github.com/quattor/configuration-modules-grid/pull/30)
* [__ncm-gip2__: += create static LDIF files using the output of an external command](https://github.com/quattor/configuration-modules-grid/pull/31)
* [__ncm-gsissh__: make compatible with recent version of gsissh](https://github.com/quattor/configuration-modules-grid/pull/41)
* [__ncm-vomsclient__: end .lsc files with new-line character](https://github.com/quattor/configuration-modules-grid/pull/35)
* [__ncm-xrootd__: fix disk instance not added to the list of managed instances](https://github.com/quattor/configuration-modules-grid/pull/29)

### CAF
* [Empty command process](https://github.com/quattor/CAF/pull/41)
* [Implement start, stop and restart methods.](https://github.com/quattor/CAF/pull/21)
* [__Reporter__: improve syslogging of multiline messages](https://github.com/quattor/CAF/pull/34)
* [__Reporter__: verbose messages enabled when debug level >= 1](https://github.com/quattor/CAF/pull/30)
* [Service OS flavour for mocking/unittests](https://github.com/quattor/CAF/pull/44)
* [Store manipulated files in the log object](https://github.com/quattor/CAF/pull/11)
* [Stringify process](https://github.com/quattor/CAF/pull/31)
* [add a noAction() method to Object and FileWriter to return the noaction flag value](https://github.com/quattor/CAF/pull/28)
* [provide an interface to access generated output more as a stream](https://github.com/quattor/CAF/pull/35)
* [suppress redefine warning of change_hook redefinition](https://github.com/quattor/CAF/pull/48)
