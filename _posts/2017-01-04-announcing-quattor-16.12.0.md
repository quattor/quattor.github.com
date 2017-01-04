---
layout: article
title: Quattor 16.12.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/16.12.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 70 pull requests and resolved 29 issues.

The next release should be 17.2, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### template-library-core
* [Make CPU hyperthreading optional and remove default value](https://github.com/quattor/template-library-core/pull/134)

### configuration-modules-core
* [**ncm-shorewall:** rewrite and support tcpri](https://github.com/quattor/configuration-modules-core/pull/780)

### ncm-ncd
* [**NCM::Component:** remove escape and unescape methods](https://github.com/quattor/ncm-ncd/pull/102)
* [Set check-noquattor to true by default](https://github.com/quattor/ncm-ncd/pull/100)

### CCM
* [Remove Property class](https://github.com/quattor/CCM/pull/150)

Changelog
---------

### template-library-core
* [Add valid_interface type](https://github.com/quattor/template-library-core/pull/135)
* [Make CPU hyperthreading optional and remove default value](https://github.com/quattor/template-library-core/pull/134)
* [Support vxvm blockdevices](https://github.com/quattor/template-library-core/pull/138)
* [Test basic pan linting tests](https://github.com/quattor/template-library-core/pull/103)
* [Upgrade default panc version to 10.3-1](https://github.com/quattor/template-library-core/pull/129)
* [Use SELF in validation](https://github.com/quattor/template-library-core/pull/136)

### configuration-modules-core
* [Configure travis to run linting tests](https://github.com/quattor/configuration-modules-core/pull/987)
* [Round of cleanup to prepare for removal of CCM::Property module](https://github.com/quattor/configuration-modules-core/pull/972)
* [**ncm-*:** Change nlists to dicts in pan templates](https://github.com/quattor/configuration-modules-core/pull/994)
* [**ncm-*:** Reflow indentation in pan templates](https://github.com/quattor/configuration-modules-core/pull/995)
* [**ncm-*:** Remove curly braces from include statements](https://github.com/quattor/configuration-modules-core/pull/993)
* [**ncm-*:** Trim whitespace from Pan templates](https://github.com/quattor/configuration-modules-core/pull/988)
* [**ncm-accounts:** Minor documentation fixes](https://github.com/quattor/configuration-modules-core/pull/977)
* [**ncm-aiiserver:** fix documentation link issue](https://github.com/quattor/configuration-modules-core/pull/979)
* [**ncm-authconfig:** add sssd IPA support](https://github.com/quattor/configuration-modules-core/pull/963)
* [**ncm-ccm:** Clean up](https://github.com/quattor/configuration-modules-core/pull/982)
* [**ncm-cdp :** Update ncm-cdp schema to support hostname](https://github.com/quattor/configuration-modules-core/pull/945)
* [**ncm-download:** download to temporary file.](https://github.com/quattor/configuration-modules-core/pull/976)
* [**ncm-freeipa:** bump Net::FreeIPA for improved compatibility on el6](https://github.com/quattor/configuration-modules-core/pull/996)
* [**ncm-freeipa:** initial support](https://github.com/quattor/configuration-modules-core/pull/750)
* [**ncm-freeipa:** mock_rpc mocks JSON::XS which should be unmocked before Devel::Cover produces the digests](https://github.com/quattor/configuration-modules-core/pull/989)
* [**ncm-gpfs:** add ccr support](https://github.com/quattor/configuration-modules-core/pull/911)
* [**ncm-gpfs:** allow to run mmsdrfrestore after each configfetch](https://github.com/quattor/configuration-modules-core/pull/957)
* [**ncm-gpfs:** reinstall gpfs update packages after base](https://github.com/quattor/configuration-modules-core/pull/827)
* [**ncm-mcx, ncm-directoryservices:** Remove unescape method from NCM::Component](https://github.com/quattor/configuration-modules-core/pull/980)
* [**ncm-metaconfig:** Include Singularity service](https://github.com/quattor/configuration-modules-core/pull/954)
* [**ncm-metaconfig:** service httpd: tighten security related settings](https://github.com/quattor/configuration-modules-core/pull/974)
* [**ncm-network, ncm-authconfig, ncm-metaconfig:** Use new valid_interface type](https://github.com/quattor/configuration-modules-core/pull/981)
* [**ncm-network:** Remove useless log message](https://github.com/quattor/configuration-modules-core/pull/969)
* [**ncm-opennebula:** Include OpenNebula labels support](https://github.com/quattor/configuration-modules-core/pull/967)
* [**ncm-postgresql:** remove empty pods](https://github.com/quattor/configuration-modules-core/pull/1004)
* [**ncm-shorewall:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/909)
* [**ncm-shorewall:** rewrite and support tcpri](https://github.com/quattor/configuration-modules-core/pull/780)
* [**ncm-systemd:** remove empty pod files](https://github.com/quattor/configuration-modules-core/pull/1001)
* [**ncm-useraccess:** close dangling FileWriter instance before DESTROY](https://github.com/quattor/configuration-modules-core/pull/990)

### template-library-standard
* [New Intel network card](https://github.com/quattor/template-library-standard/pull/89)

### template-library-grid
* [Use CPU max_threads to calculate slot count](https://github.com/quattor/template-library-grid/pull/185)
* [**defaults/grid/config:** fix typo introducted in 7e39550](https://github.com/quattor/template-library-grid/pull/188)

### ncm-ncd
* [**CLI:** report the used CCM configuration CID and (optional) name](https://github.com/quattor/ncm-ncd/pull/101)
* [FIX load ccm bash_completion functions](https://github.com/quattor/ncm-ncd/pull/103)
* [**NCM::Component:** remove escape and unescape methods](https://github.com/quattor/ncm-ncd/pull/102)
* [Remove support for add_files / get_files and FILES attribute](https://github.com/quattor/ncm-ncd/pull/96)
* [Set check-noquattor to true by default](https://github.com/quattor/ncm-ncd/pull/100)

### CCM
* [**Fetch::Config:** support valid principal with -](https://github.com/quattor/CCM/pull/155)
* [**Fetch::Download:** handle content decoding failure](https://github.com/quattor/CCM/pull/159)
* [**Path:** add /software/components/download/files/ to safe unescape paths](https://github.com/quattor/CCM/pull/151)
* [Remove Property class](https://github.com/quattor/CCM/pull/150)
* [Remove tests for removed CCM modules](https://github.com/quattor/CCM/pull/157)
* [Remove unused syncfile](https://github.com/quattor/CCM/pull/152)
* [**TextRender:** cast_double and cast_long fail on non-numeric argument](https://github.com/quattor/CCM/pull/153)

### maven-tools
* [Perl warnings during tests are equivalent to failing test (and warn_is_ok function to disable this behaviour)](https://github.com/quattor/maven-tools/pull/112)
* [Prepare for CCM namespace cleanup](https://github.com/quattor/maven-tools/pull/121)
* [**Test::Quattor::Component:** remove mocked methods that have been removed in NCM::Component](https://github.com/quattor/maven-tools/pull/116)
* [**Test::Quattor::Critic:** add Perl::Critic whitelist testing](https://github.com/quattor/maven-tools/pull/115)
* [**Test::Quattor::Critic:** use tempfile instead of /dev/null for empty profile](https://github.com/quattor/maven-tools/pull/117)
* [**Test::Quattor::Unittest:** add baseline unittests](https://github.com/quattor/maven-tools/pull/114)
* [Tidy and Critic should not check pod files](https://github.com/quattor/maven-tools/pull/119)
* [**maven-tools:** add component config.pan and schema.pan header templates](https://github.com/quattor/maven-tools/pull/113)

### aii
* [Round of cleanup to prepare for removal of CCM::Property module](https://github.com/quattor/aii/pull/232)
* [**aii-ks:** remove Component escape method](https://github.com/quattor/aii/pull/233)
* [**aii-opennebula:** Include ONE labels support](https://github.com/quattor/aii/pull/226)
* [**aii-opennebula:** Include VM placement algorithm support](https://github.com/quattor/aii/pull/236)

### configuration-modules-grid
* [Configure travis to run linting tests](https://github.com/quattor/configuration-modules-grid/pull/127)
* [**ncm-*:** Change nlists to dicts in pan templates](https://github.com/quattor/configuration-modules-grid/pull/126)
* [**ncm-*:** Remove curly-braces from pan templates](https://github.com/quattor/configuration-modules-grid/pull/125)
* [**ncm-*:** Trim whitespace from pan templates](https://github.com/quattor/configuration-modules-grid/pull/124)

### cdp-listend
* [Add hostname configuration option to choose the hostname/IP to listen on](https://github.com/quattor/cdp-listend/pull/16)

### CAF
* [**FileWriter:** disable chatty LC::Check by default unless NoAction](https://github.com/quattor/CAF/pull/98)
* [**Kerberos:** handle exception thrown by CAF::Process (e.g. during kinit)](https://github.com/quattor/CAF/pull/201)
* [Remove add_files to track files](https://github.com/quattor/CAF/pull/199)
