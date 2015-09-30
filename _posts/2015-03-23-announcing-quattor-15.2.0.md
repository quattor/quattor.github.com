---
layout: article
title: Quattor 15.2.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/15.2.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 131 pull requests and resolved 47 issues.

The next release should be 15.4.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Main New Features and Fixes
---------------------------

Known issues
------------

Changelog
---------

### ncm-query
* [Add tabcompletion support](https://github.com/quattor/ncm-query/pull/5)
* [Support non-root query](https://github.com/quattor/ncm-query/pull/7)
* [Upgrade maven tools to 1.42](https://github.com/quattor/ncm-query/pull/9)

### LC
* [Upgrade maven tools to 1.42](https://github.com/quattor/LC/pull/13)

### ncm-cdispd
* [Upgrade maven tools to 1.42](https://github.com/quattor/ncm-cdispd/pull/20)
* [bump build-tools version](https://github.com/quattor/ncm-cdispd/pull/19)

### spma
* [Add EU DataGrid LICENSE](https://github.com/quattor/spma/pull/3)

### configuration-modules-core
* [Activate NoAction support on multiple components](https://github.com/quattor/configuration-modules-core/pull/393)
* [Fix pod-check unittest to include the pod files](https://github.com/quattor/configuration-modules-core/pull/433)
* [Fixes for EL5 and EL6](https://github.com/quattor/configuration-modules-core/pull/439)
* [Fixes for EL7 unittest on base EL7 install](https://github.com/quattor/configuration-modules-core/pull/429)
* [__New component__: ncm-nss](https://github.com/quattor/configuration-modules-core/pull/385)
* [Remove panc-maven-plugin configuration from configuration module pom files](https://github.com/quattor/configuration-modules-core/pull/395)
* [Remove panc-maven-plugin configuration from configuration module pom files](https://github.com/quattor/configuration-modules-core/pull/388)
* [Required unit-test fixes for EL7 (and root)](https://github.com/quattor/configuration-modules-core/pull/411)
* [Upgrade maven tools to 1.42](https://github.com/quattor/configuration-modules-core/pull/445)
* [__components unittests should not modify CAF__::FileWriter and use NoAction early on](https://github.com/quattor/configuration-modules-core/pull/390)
* [more unittest cleanup](https://github.com/quattor/configuration-modules-core/pull/418)
* [__ncm-accounts__: check for duplicate uids or gids in schema](https://github.com/quattor/configuration-modules-core/pull/422)
* [__ncm-authconfig__: fix pam_update_file problem](https://github.com/quattor/configuration-modules-core/pull/383)
* [__ncm-ccm__: handle ccm-fetch with noquattor present](https://github.com/quattor/configuration-modules-core/pull/275)
* [__ncm-ceph__: Add documentation for sub-modules](https://github.com/quattor/configuration-modules-core/pull/394)
* [__ncm-ceph__: add error message on empty osd](https://github.com/quattor/configuration-modules-core/pull/366)
* [__ncm-ceph__: fix git no ident error](https://github.com/quattor/configuration-modules-core/pull/438)
* [__ncm-ceph__: update versions info](https://github.com/quattor/configuration-modules-core/pull/400)
* [__ncm-ceph__: use textrender for crushmap](https://github.com/quattor/configuration-modules-core/pull/397)
* [__ncm-cron__: Correct example smear from string to long](https://github.com/quattor/configuration-modules-core/pull/415)
* [__ncm-cron__: Fix race condition bug](https://github.com/quattor/configuration-modules-core/pull/447)
* [__ncm-gpfs__: add 4.1 support](https://github.com/quattor/configuration-modules-core/pull/414)
* [__ncm-icinga__: contact group definition is not mandatory for contacts. ](https://github.com/quattor/configuration-modules-core/pull/448)
* [__ncm-metaconfig__: bulk migration metaconfig config-templates](https://github.com/quattor/configuration-modules-core/pull/398)
* [__ncm-metaconfig__: service perfsonar: Config::General does not respect order](https://github.com/quattor/configuration-modules-core/pull/417)
* [__ncm-metaconifg__: initial metaconfig service mtrg](https://github.com/quattor/configuration-modules-core/pull/391)
* [__ncm-network__: add xmit_hash_policy as an allowed bonding option](https://github.com/quattor/configuration-modules-core/pull/444)
* [__ncm-network__: allow for bonding with lacp while keeping validation](https://github.com/quattor/configuration-modules-core/pull/420)
* [__ncm-network__: fix documentation bonding example](https://github.com/quattor/configuration-modules-core/pull/416)
* [__ncm-nss__: Add a changelog](https://github.com/quattor/configuration-modules-core/pull/402)
* [__ncm-nss__: Add to top-level POM file](https://github.com/quattor/configuration-modules-core/pull/396)
* [__ncm-nss__: Log output of buildDB script as debug](https://github.com/quattor/configuration-modules-core/pull/407)
* [__ncm-opennebula__: add support for OpenNebula](https://github.com/quattor/configuration-modules-core/pull/350)
* [__ncm-postgresql__: cleaned up documentation](https://github.com/quattor/configuration-modules-core/pull/384)
* [__ncm-spma__: improve yum locked_all_packges message logging](https://github.com/quattor/configuration-modules-core/pull/386)
* [__ncm-sudo__: the privilege_lines option should be optional.](https://github.com/quattor/configuration-modules-core/pull/442)
* [__ncm-useraccess__: make sure the test dir for the close.t unittest exists.](https://github.com/quattor/configuration-modules-core/pull/377)

### ncm-lib-blockdevices
* [Make unittest pass with 1.40 buildtools](https://github.com/quattor/ncm-lib-blockdevices/pull/41)
* [Upgrade maven tools to 1.42](https://github.com/quattor/ncm-lib-blockdevices/pull/44)

### template-library-standard
* [Add configuration for the EGI CVMFS repository](https://github.com/quattor/template-library-standard/pull/44)
* [Fix white-space issues](https://github.com/quattor/template-library-standard/pull/42)
* [New Intel CPU](https://github.com/quattor/template-library-standard/pull/43)

### template-library-grid
* [Add LogLevel to dmlite.conf, needed by DPM 1.8.9](https://github.com/quattor/template-library-grid/pull/123)
* [Add machine features to wn.](https://github.com/quattor/template-library-grid/pull/132)
* [Add multicore support for APEL](https://github.com/quattor/template-library-grid/pull/117)
* [Allow dmlite loglevel to be customized](https://github.com/quattor/template-library-grid/pull/128)
* [__DPM config__: ensure that the DPM-readable version of host certificate is created](https://github.com/quattor/template-library-grid/pull/125)
* [Disable directory creation for the CVMFS mountpoint](https://github.com/quattor/template-library-grid/pull/122)
* [Enhancement for tuning dmlite (DPM Head Node)](https://github.com/quattor/template-library-grid/pull/121)
* [Fix LBSERVER status and rpm version checks](https://github.com/quattor/template-library-grid/pull/131)
* [Fix WMProxy status and rpm version checks](https://github.com/quattor/template-library-grid/pull/130)
* [__GIP CE__: finalize GLUE2 publication + fixes for GLUE1](https://github.com/quattor/template-library-grid/pull/113)
* [Htcondor](https://github.com/quattor/template-library-grid/pull/126)
* [__README__: fix typo](https://github.com/quattor/template-library-grid/pull/133)
* [Remove CERN's old (decommissioned) VOMS servers](https://github.com/quattor/template-library-grid/pull/129)
* [Umd 3 htcondor](https://github.com/quattor/template-library-grid/pull/119)
* [Use the TORQUE_CONFIG_DIR variable to place the myinit.sh script](https://github.com/quattor/template-library-grid/pull/127)

### ncm-ncd
* [Detect wrong component](https://github.com/quattor/ncm-ncd/pull/35)
* [Do not allow components to be installed from code in the profile](https://github.com/quattor/ncm-ncd/pull/36)
* [Do not allow components to be installed from code in the profile](https://github.com/quattor/ncm-ncd/pull/33)
* [Remove CERN specific wrappers and notd configs](https://github.com/quattor/ncm-ncd/pull/32)
* [Remove HLConfig](https://github.com/quattor/ncm-ncd/pull/31)
* [Upgrade maven tools to 1.42](https://github.com/quattor/ncm-ncd/pull/37)
* [keys() on EL5/6 needs a hash, not only a hashref ](https://github.com/quattor/ncm-ncd/pull/40)

### CCM
* [CCfg _readConfigFile should not retest if configuration file exists](https://github.com/quattor/CCM/pull/47)
* [Prepare for scalar type metadata refinement for JSON profiles](https://github.com/quattor/CCM/pull/34)
* [Refactor and re-enable unittest to prepare for some speed optimisations](https://github.com/quattor/CCM/pull/32)
* [Remove all support for XMLDB format profile](https://github.com/quattor/CCM/pull/30)
* [Support anonymous config](https://github.com/quattor/CCM/pull/35)
* [__Switch to CAF__::FileReader in CCM](https://github.com/quattor/CCM/pull/33)
* [Upgrade maven tools to 1.42](https://github.com/quattor/CCM/pull/44)
* [implement Element getTree with depth](https://github.com/quattor/CCM/pull/37)
* [use mkpath instead of make_path to allow EL5 unittests](https://github.com/quattor/CCM/pull/41)

### maven-tools
* [__Add Test__::Quattor::Textrender::Component](https://github.com/quattor/maven-tools/pull/37)
* [Add support for running unit tests in build-scripts](https://github.com/quattor/maven-tools/pull/31)
* [BUILD_INFO: clarifications after doing 1.42 release](https://github.com/quattor/maven-tools/pull/46)
* [BUILD_INFO: document the release process (Maven release plugin)](https://github.com/quattor/maven-tools/pull/43)
* [__Extend the Test__::Quattor modules with TextRender and RegexpTest to allow easy metaconfig testing](https://github.com/quattor/maven-tools/pull/34)
* [Fixes the unittest failing ](https://github.com/quattor/maven-tools/pull/36)
* [Improve build tools documentation](https://github.com/quattor/maven-tools/pull/38)
* [Minor fixes to build scripts](https://github.com/quattor/maven-tools/pull/41)
* [__Refactor Test__::Quattor and add unittests](https://github.com/quattor/maven-tools/pull/27)
* [Support template unittesting through controlled failure of compilations](https://github.com/quattor/maven-tools/pull/42)
* [build-profile (parent pom): define panc-maven-plugin version to use (10.2)](https://github.com/quattor/maven-tools/pull/32)
* [build-profile (parent pom): define panc-maven-plugin version to use (10.2)](https://github.com/quattor/maven-tools/pull/30)

### aii
* [__Ks pxelinux special devices__: add improved logging and checking](https://github.com/quattor/aii/pull/96)
* [Properly handle pxelinux special ksdevice=MAC ](https://github.com/quattor/aii/pull/95)
* [Upgrade maven tools to 1.42](https://github.com/quattor/aii/pull/109)
* [__aii-opennebula__: fix failing unittests](https://github.com/quattor/aii/pull/93)

### template-library-os
* [Add new groups based on yum groupinfo](https://github.com/quattor/template-library-os/pull/56)
* [__EL7__: Fix white-space issues](https://github.com/quattor/template-library-os/pull/62)
* [__SL5__: Fix white-space issues](https://github.com/quattor/template-library-os/pull/63)
* [__SL6__: Fix white-space issues](https://github.com/quattor/template-library-os/pull/61)
* [__rpms/quattor-development__: add perl-File-Copy-Recursive](https://github.com/quattor/template-library-os/pull/65)
* [__rpms/quattor-development__: add perl-File-Copy-Recursive](https://github.com/quattor/template-library-os/pull/64)

### release
* [Add build_all_repos script](https://github.com/quattor/release/pull/72)
* [Copy metaconfig templates to template-library-core at release](https://github.com/quattor/release/pull/71)
* [Only tag template libraries with release version](https://github.com/quattor/release/pull/67)
* [build_all_repos: Support panc download and bugfixes](https://github.com/quattor/release/pull/74)
* [build_all_repos: add QUATTOR_TEST_TEMPLATE_LIBRARY_CORE in env.sh](https://github.com/quattor/release/pull/77)
* [__get-template-library__: ensure that bash is used](https://github.com/quattor/release/pull/75)
* [__get-template-library__: support for new tag format as introduced by #67](https://github.com/quattor/release/pull/79)
* [move to readthedocs](https://github.com/quattor/release/pull/69)

### configuration-modules-grid
* [Fix missing template files](https://github.com/quattor/configuration-modules-grid/pull/69)
* [Update build tools and remove explicit definition of panc-maven-plugin version](https://github.com/quattor/configuration-modules-grid/pull/65)
* [Upgrade maven tools to 1.42](https://github.com/quattor/configuration-modules-grid/pull/67)
* [__ncm-xrootd__: bump build tools to 1.40 for EL7](https://github.com/quattor/configuration-modules-grid/pull/62)

### template-library-core
* [__README__: update the URL about template library update](https://github.com/quattor/template-library-core/pull/62)
* [Refactor quattor/schema](https://github.com/quattor/template-library-core/pull/58)
* [Update panc compiler version to use for Quattor development](https://github.com/quattor/template-library-core/pull/60)

### cdp-listend
* [Add a unittest](https://github.com/quattor/cdp-listend/pull/9)
* [Upgrade maven tools to 1.42](https://github.com/quattor/cdp-listend/pull/10)

### CAF
* [Always define noaction in File*](https://github.com/quattor/CAF/pull/75)
* [__CAF__::Object add report method to conditional logger](https://github.com/quattor/CAF/pull/80)
* [__Call LC__::Check::file in noaction mode](https://github.com/quattor/CAF/pull/74)
* [__FileEditor__: clarify the list context implied by BEGINING_OF_FILE and ENDING_OF_FILE](https://github.com/quattor/CAF/pull/73)
* [FileReader can read from a pipe](https://github.com/quattor/CAF/pull/83)
* [__Service__: set explicit service timeout instead of passing undef with sysv](https://github.com/quattor/CAF/pull/71)
* [__TextRender__: improve fail message when dealing with non-existing tplname](https://github.com/quattor/CAF/pull/70)
* [Upgrade maven tools to 1.42](https://github.com/quattor/CAF/pull/82)
* [Verifying new 1.39 build-tools](https://github.com/quattor/CAF/pull/76)

### template-library-examples
* [Quattor repository configuration updated to match documentation](https://github.com/quattor/template-library-examples/pull/18)
* [Use group of clusters to be able to select what to compile in create-vanilla-SCDB.sh](https://github.com/quattor/template-library-examples/pull/21)

### rpmt-py
* [Add EU DataGrid LICENSE](https://github.com/quattor/rpmt-py/pull/2)
