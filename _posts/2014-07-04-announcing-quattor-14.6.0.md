---
layout: article
title: Quattor 14.6.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/14.6.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed!

The next release should be 14.8.0, the [backlog](https://gist.github.com/jrha/4f42a3757aea4d2054e8) for which is already huge.

Main New Features and Fixes
---------------------------

* AII can install both 13.1.x (SPMA-managed) and 14.x (YUM-managed) machines: this is now the **recommended** and **only supported** version of AII.
A site updating to 14.6.0 is recommended to upgrade its AII server first: this is the only version of AII capable of installing 14.6.0 machines.

* `ncm-cdispd` now properly reexecutes failed components every time a new profile is received, even though their configuration was not changed.
Previous versions were not doing this and this could result in a machine staying in a partially configured state.

* Grid template library also received a significant number of fixes for UMD-3 services. One of them is related to ncm-xrootd being blocked during 
restart of xrootd services with the effect of stalling ncm-ncd and thus preventing further deployment (until the ncm-ncd time out) and 
letting xrootd stopped. 

Known issues
------------

* `ncm-xrootd`: the fix describes above unfortunately contains a mistake that let xrootd disk instances unmanaged by xrootd startup script after 
executing the component (see https://github.com/quattor/configuration-modules-grid/pull/29). If you run into this problem, you may want to get the 
fixed version (that will be part of 14.8) from http://quattorsrv.lal.in2p3.fr/packages/site/ncm-xrootd-14.6.1-SNAPSHOT20140716143750.noarch.rpm: 
this will require you to edit cfg/quattor/14.6.0/components/xrootd/config.pan to update the RPM version.


Changelog
---------

### CAF
* [Restore the whence feature](https://github.com/quattor/CAF/pull/19).
* [Start CAF::Service](https://github.com/quattor/CAF/pull/15).

### aii
* [aii-server RPM: fix missing requirement for perl-XML-Simple](https://github.com/quattor/aii/pull/73).
* [aii-ks: fixes to support installation of 13.1.x systems with AII 14.x](https://github.com/quattor/aii/pull/68).
* [aii should not enforce the logging host ](https://github.com/quattor/aii/pull/71).
* [EL7 support](https://github.com/quattor/aii/pull/60).

### cdp-listend
* [Add fetch_offset option](https://github.com/quattor/cdp-listend/pull/3).

### configuration-modules-core
* [ncm-grub: fix handling of an undefined kernel version](https://github.com/quattor/configuration-modules-core/pull/231).
* [ncm-mysql: fix mysqlAddUser not being called as a $self method](https://github.com/quattor/configuration-modules-core/pull/235).
* [Simpler version of pkg_repl()](https://github.com/quattor/configuration-modules-core/pull/185).
* [Add Solaris support to ncm-cron.](https://github.com/quattor/configuration-modules-core/pull/201).
* [ncm-dirperm: make path attribute an absolute path](https://github.com/quattor/configuration-modules-core/pull/218).
* [cdp-listend fetch_offset support](https://github.com/quattor/configuration-modules-core/pull/220).
* [Add support for ConnectTimeout and BatchMode](https://github.com/quattor/configuration-modules-core/pull/219).
* [Fix declaration of dependencies.](https://github.com/quattor/configuration-modules-core/pull/216).

### configuration-modules-grid
* [ncm-xrootd: ensure that local redirector is started first](https://github.com/quattor/configuration-modules-grid/pull/27).
* [ncm-xrootd: extend rule syntax to allow to request a line removal](https://github.com/quattor/configuration-modules-grid/pull/20).
* [ncm-lcgbdii: untaint file name before calling chown](https://github.com/quattor/configuration-modules-grid/pull/23).
* [ncm-gip2: untaint file/directory names before calling chown](https://github.com/quattor/configuration-modules-grid/pull/22).
* [ncm-dpmlfc: define DPM_HOST/DPNS_HOST exported + various fixes](https://github.com/quattor/configuration-modules-grid/pull/19).

### ncm-cdispd
* [Fix ncm-cdispd forgetting about failed configuration modules](https://github.com/quattor/ncm-cdispd/pull/6).

### ncm-lib-blockdevices
* [Add support for parted flags to partitions](https://github.com/quattor/ncm-lib-blockdevices/pull/31).

### ncm-ncd
* [Make --noautodeps ignore missing dependencies](https://github.com/quattor/ncm-ncd/pull/22).

### template-library-core
* [AII server: adjust default RPM configuration](https://github.com/quattor/template-library-core/pull/52).
* [Add "console" attribute to hardware structure](https://github.com/quattor/template-library-core/pull/42).
* [bring blockdevices template in sync with latest ncm-lib-blockdevices](https://github.com/quattor/template-library-core/pull/49).

### template-library-examples
* [DPM config: fix missing definition of DMLITE_TOKEN_PASSWORD](https://github.com/quattor/template-library-examples/pull/14).

### template-library-standard
* [perfSonar: make port range redefinition more flexible](https://github.com/quattor/template-library-standard/pull/24).
