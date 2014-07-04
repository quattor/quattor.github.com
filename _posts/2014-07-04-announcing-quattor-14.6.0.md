---
layout: article
title: Quattor 14.6.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/14.6.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed!

The next release should be 14.8.0, the [backlog](https://gist.github.com/jrha/4f42a3757aea4d2054e8) for which is already huge.


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
