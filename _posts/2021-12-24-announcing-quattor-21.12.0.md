---
layout: article
title: Quattor 21.12.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/21.12.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 36 pull requests and resolved 4 issues.

Take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.

Known Issues
------------
* **ncd-ncd:** Output from the new `--report` option may not always function correctly on EL6/7.

Backwards Incompatible Changes
------------------------------

### configuration-modules-core
* [**ncm-hostsfile:** Cleanup and tests](https://github.com/quattor/configuration-modules-core/pull/1502)
* [**ncm-metaconfig:** cumulus: support mgmt vrf and traditional bridges](https://github.com/quattor/configuration-modules-core/pull/1474)
* [**ncm-metaconfig:** extend slurm schema](https://github.com/quattor/configuration-modules-core/pull/1509)
* [**ncm-postfix:** remove misplaced unused global variables](https://github.com/quattor/configuration-modules-core/pull/1521)

### template-library-grid
* [**users:** Fix collisions with system managed groups](https://github.com/quattor/template-library-grid/pull/237)

Changelog
---------

### template-library-core
* [El8 support](https://github.com/quattor/template-library-core/pull/209)

### configuration-modules-core
* [Fix types for refactored components](https://github.com/quattor/configuration-modules-core/pull/1533)
* [**ncm-hostsfile:** Cleanup and tests](https://github.com/quattor/configuration-modules-core/pull/1502)
* [**ncm-metaconfig:** add active boolean (to allow skipping a service)](https://github.com/quattor/configuration-modules-core/pull/1522)
* [**ncm-metaconfig:** cumulus: support mgmt vrf and traditional bridges](https://github.com/quattor/configuration-modules-core/pull/1474)
* [**ncm-metaconfig:** extend slurm schema](https://github.com/quattor/configuration-modules-core/pull/1509)
* [**ncm-metaconfig:** ganesha: Access_Type should be enum, not string](https://github.com/quattor/configuration-modules-core/pull/1439)
* [**ncm-metaconfig:** generic: add php_variable for simple php-syntax configuration](https://github.com/quattor/configuration-modules-core/pull/1482)
* [**ncm-metaconfig:** httpd: support files in directory config](https://github.com/quattor/configuration-modules-core/pull/1514)
* [**ncm-metaconfig:** postfix - add missing smtp_tls_protocols option](https://github.com/quattor/configuration-modules-core/pull/1519)
* [**ncm-metaconfig:** resolve perltidy repeated , error](https://github.com/quattor/configuration-modules-core/pull/1527)
* [**ncm-network:** check if ovs-vswitchd has been initialized to prevent failure](https://github.com/quattor/configuration-modules-core/pull/1513)
* [**ncm-pam:** Use component config header macro](https://github.com/quattor/configuration-modules-core/pull/1511)
* [**ncm-postfix:** remove misplaced unused global variables](https://github.com/quattor/configuration-modules-core/pull/1521)
* [**ncm-resolver:** Use component config header macro](https://github.com/quattor/configuration-modules-core/pull/1512)
* [**ncm-resolver:** add support for options in resolv.conf](https://github.com/quattor/configuration-modules-core/pull/1508)
* [**ncm-spma:** yumdnf: initial dnf/yum4 based on yum](https://github.com/quattor/configuration-modules-core/pull/1401)

### ncm-lib-blockdevices
* [**Partiton:** fix some utf8 characters in comments](https://github.com/quattor/ncm-lib-blockdevices/pull/95)

### template-library-standard
* [Add new CPUs from RAL](https://github.com/quattor/template-library-standard/pull/139)
* [Add new nVidia GPU cards from RAL](https://github.com/quattor/template-library-standard/pull/138)
* [Add new network cards from RAL](https://github.com/quattor/template-library-standard/pull/137)
* [Add various RAID cards](https://github.com/quattor/template-library-standard/pull/135)
* [Add various SAS HBAs](https://github.com/quattor/template-library-standard/pull/136)
* [New hardware definition added (mainly CPUs)](https://github.com/quattor/template-library-standard/pull/142)
* [**Quattor repository config:** updated to support new layouti starting with v20.4.0](https://github.com/quattor/template-library-standard/pull/141)
* [Replace travis tests with GitHub actions](https://github.com/quattor/template-library-standard/pull/133)

### template-library-grid
* [**CI:** replace Travis by GitHub actions](https://github.com/quattor/template-library-grid/pull/242)
* [**users:** Fix collisions with system managed groups](https://github.com/quattor/template-library-grid/pull/237)

### maven-tools
* [Run maven integration tests as a GitHub action](https://github.com/quattor/maven-tools/pull/187)

### aii
* [Support active configuration attribute for plugins](https://github.com/quattor/aii/pull/280)
* [Use wipefs for RHEL6+](https://github.com/quattor/aii/pull/325)
* [bump pom.xml version to 21.4.1-SNAPSHOT](https://github.com/quattor/aii/pull/330)

### template-library-os
* [Initial templates for EL8 support](https://github.com/quattor/template-library-os/pull/100)

### ncm-ncd
* [Add --report option to report state](https://github.com/quattor/ncm-ncd/pull/126)
* [Add graph based report of component dependencies](https://github.com/quattor/ncm-ncd/pull/130)
* [**ncm-ncd:** must have HOME defined in ENV](https://github.com/quattor/ncm-ncd/pull/129)
