---
layout: article
title: Quattor 14.10.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/14.10.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 119 pull requests and resolved 68 issues.

The next release should be 14.12.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.

Changelog
---------

### template-library-core
* [Remove support for AII v2 (`AII_V2_INSTALL` variable)](https://github.com/quattor/template-library-core/pull/57)

### LC
* [Add a LICENCE file and clarify perl-LC status in Quattor](https://github.com/quattor/LC/pull/8)

### ncm-cdispd
* [Fix location check-ncm-cdispd](https://github.com/quattor/ncm-cdispd/pull/17)

### configuration-modules-core
* [Add example on __ncm-filecopy__](https://github.com/quattor/configuration-modules-core/pull/315)
* [Add new example on __autofs__](https://github.com/quattor/configuration-modules-core/pull/362)
* [Add `use_ssl`](https://github.com/quattor/configuration-modules-core/pull/337)
* [Authconfig schema fix](https://github.com/quattor/configuration-modules-core/pull/305)
* [Bump build tools to 1.38 and add POD unit test](https://github.com/quattor/configuration-modules-core/pull/338)
* [More documentation fixes](https://github.com/quattor/configuration-modules-core/pull/367)
* [__ncm-autofs__: Add examples section to documentation](https://github.com/quattor/configuration-modules-core/pull/318)
* [__ncm-autofs__: Add example to documentation](https://github.com/quattor/configuration-modules-core/pull/316)
* [__ncm-cdp__: Hotfix for failing cdp unittest using new buildtools](https://github.com/quattor/configuration-modules-core/pull/330)
* [__ncm-cdp__: hotfix for unittests ](https://github.com/quattor/configuration-modules-core/pull/319)
* [__ncm-ceph__: add finer configuration, osd-based objectstore features , support for some unreachable hosts and various fixes](https://github.com/quattor/configuration-modules-core/pull/289)
* [__ncm-ceph__: add support for radosgw config](https://github.com/quattor/configuration-modules-core/pull/320)
* [__ncm-ceph__: Doc updated](https://github.com/quattor/configuration-modules-core/pull/291)
* [__ncm-ceph__: fix for SSH multiplexing when using old SSH version](https://github.com/quattor/configuration-modules-core/pull/332)
* [__ncm-ceph__: fix incorrect paths for 'ls' and 'cat' commands on el6](https://github.com/quattor/configuration-modules-core/pull/324)
* [__ncm-ceph__:  remarks processed of pr #289](https://github.com/quattor/configuration-modules-core/pull/299)
* [__ncm-ceph__: use ods map for crushmap instead of making ssh connections](https://github.com/quattor/configuration-modules-core/pull/336)
* [__ncm-icinga__: updated schema](https://github.com/quattor/configuration-modules-core/pull/371)
* [__ncm-metaconfig__: remove perl dependencies, now via CAF::TextRender](https://github.com/quattor/configuration-modules-core/pull/360)
* [__ncm-metaconfig__: support daemons with actions](https://github.com/quattor/configuration-modules-core/pull/328)
* [__ncm-metaconfig__: Use `CAF::TextRender for rendering](https://github.com/quattor/configuration-modules-core/pull/327)
* [__ncm-mysql__: add missing dependency on ncm-spma](https://github.com/quattor/configuration-modules-core/pull/363)
* [__ncm mysql__: fix processing of `tableOptions` + misc. cleanups](https://github.com/quattor/configuration-modules-core/pull/329)
* [__ncm-mysql__: option for support of other mysql servicenames](https://github.com/quattor/configuration-modules-core/pull/322)
* [__ncm-network__: handle `NOQUATTOR` properly (and fall back to ping network test)](https://github.com/quattor/configuration-modules-core/pull/273)
* [__ncm-ntpd__: fix misplaced parenthesis](https://github.com/quattor/configuration-modules-core/pull/301)
* [__ncm-spma__: check the locked packages with wildcard in version](https://github.com/quattor/configuration-modules-core/pull/308)
* [__ncm-spma__: fix test warning (yum-versionlock.t use quoted string in range)](https://github.com/quattor/configuration-modules-core/pull/356)
* [__ncm-spma__ functions: fix test for an explicitly defined package version](https://github.com/quattor/configuration-modules-core/pull/302)
* [__ncm-spma__: pass fullsearch option from `update_pkgs_retry` to `update_pkgs`](https://github.com/quattor/configuration-modules-core/pull/375)
* [__ncm-spma__: regenerate the rpm dependencies](https://github.com/quattor/configuration-modules-core/pull/359)
* [__ncm-spma__: switch the default to `userpkgs_retry=true`](https://github.com/quattor/configuration-modules-core/pull/334)
* [__ncm-sudo__: add support for `secure_path`](https://github.com/quattor/configuration-modules-core/pull/314)
* [__ncm-symlink__: Capture the exception in mkpath](https://github.com/quattor/configuration-modules-core/pull/313)
* [__ncm-symlink__: log an error when processing duplicate links](https://github.com/quattor/configuration-modules-core/pull/326)
* [__ncm-useraccess__: fix test warning acknowledge the chown used once warning ](https://github.com/quattor/configuration-modules-core/pull/357)


### template-library-standard
* [Add CVMFS client configuration for non-LHC VOs (hosted at RAL)](https://github.com/quattor/template-library-standard/pull/37)
* [Add missing template to configure security trust](https://github.com/quattor/template-library-standard/pull/40)
* [CVMFS: remove support for SPMA](https://github.com/quattor/template-library-standard/pull/41)
* [Pakiti: configuration cleanup](https://github.com/quattor/template-library-standard/pull/36)
* [Perfsonar: various fixes](https://github.com/quattor/template-library-standard/pull/34)
* [Security trust config update and fixes](https://github.com/quattor/template-library-standard/pull/35)
* [perfSonar: add missing packages](https://github.com/quattor/template-library-standard/pull/38)
* [perfSonar: fix generation of script used to configure perfSonar ports](https://github.com/quattor/template-library-standard/pull/39)

### template-library-grid
* [Add EMI-3 APEL into EMI-2 (required for a smooth accounting transition)](https://github.com/quattor/template-library-grid/pull/16)
* [Add GIP configuration on Argus configuration](https://github.com/quattor/template-library-grid/pull/102)
* [Add a script to remove Running "zombie" job on CREAM-CE](https://github.com/quattor/template-library-grid/pull/98)
* [Add abilities to retrieve banning information from Argus](https://github.com/quattor/template-library-grid/pull/104)
* [Add glue1 provider for argus](https://github.com/quattor/template-library-grid/pull/103)
* [BDII: fix RPM list for resource BDII](https://github.com/quattor/template-library-grid/pull/114)
* [DPM: Improve DPM RPMs configuration to support EPEL-testing](https://github.com/quattor/template-library-grid/pull/99)
* [DPM: add possibility to configure with Puppet modules ](https://github.com/quattor/template-library-grid/pull/105)
* [Fix configuration of MyProxy server](https://github.com/quattor/template-library-grid/pull/94)
* [Fix privacy issue with default xrootd monitoring/reporting config](https://github.com/quattor/template-library-grid/pull/100)
* [Fix some gip issue with MPI and VOMS services](https://github.com/quattor/template-library-grid/pull/97)
* [GIP CE: fix publication of shares in cluster mode](https://github.com/quattor/template-library-grid/pull/112)
* [GIP CE: preliminary support for GLUE2 (static information)](https://github.com/quattor/template-library-grid/pull/109)
* [README: update list of supported EMI services](https://github.com/quattor/template-library-grid/pull/95)
* [VO configuration: update grid12 certificate, remove obsolete VOs](https://github.com/quattor/template-library-grid/pull/106)
* [WMS: misc. fixes/cleanups](https://github.com/quattor/template-library-grid/pull/107)
* [blparser: do not set log file group to tomcat if not on a CE](https://github.com/quattor/template-library-grid/pull/111)
* [gridftp: ensure that lcas-lcmaps-gt4-interface is installed](https://github.com/quattor/template-library-grid/pull/115)

### ncm-ncd
* [fix the inheritance order due to CAF::Object fake logging](https://github.com/quattor/ncm-ncd/pull/28)

### CCM
* [Add `escape()` function to `Element`.](https://github.com/quattor/CCM/pull/23)
* [Defined noquattor constants in `CCM::Fetch` module](https://github.com/quattor/CCM/pull/21)
* [`NOQUATTOR_FORCE` as exported constant](https://github.com/quattor/CCM/pull/25)
* [Various test cleanups](https://github.com/quattor/CCM/pull/26)

### maven-tools
* [Allow perl unittest selection ](https://github.com/quattor/maven-tools/pull/21)
* [Mock alternative names to log methods and (un)escape](https://github.com/quattor/maven-tools/pull/23)
* [Pass extra options to prove on the command line.](https://github.com/quattor/maven-tools/pull/17)
* [fix typo in escape legacy warn message](https://github.com/quattor/maven-tools/pull/26)

### aii
* [Fix wrong regex check on `installtype` when using a proxy](https://github.com/quattor/aii/pull/86)
* [Get the certificate from freeIPA](https://github.com/quattor/aii/pull/81)
* [IP info from bridge support](https://github.com/quattor/aii/pull/76)
* [Opennebula aii](https://github.com/quattor/aii/pull/79)
* [Opennebula aii ONE 4.8 network AR support](https://github.com/quattor/aii/pull/83)

### template-library-os
* [Add LICENSE information (Apache 2.0)](https://github.com/quattor/template-library-os/pull/55)
* [Add LICENSE information (Apache 2.0)](https://github.com/quattor/template-library-os/pull/54)
* [Add LICENSE information (Apache 2.0)](https://github.com/quattor/template-library-os/pull/53)
* [el7.x: add required dependencies for Quattor development](https://github.com/quattor/template-library-os/pull/58)
* [sl6.x: add required dependencies for Quattor development](https://github.com/quattor/template-library-os/pull/57)
* [sl6.x: various package group added/adjusted](https://github.com/quattor/template-library-os/pull/60)
* [sl6.x: various package group added/adjusted](https://github.com/quattor/template-library-os/pull/59)

### scdb
* [Add LICENSE information (Apache 2.0)](https://github.com/quattor/scdb/pull/27)
* [Add panc-version target to ant: displays pan compiler version](https://github.com/quattor/scdb/pull/25)
* [Add support for last svnkit version (1.8.6)](https://github.com/quattor/scdb/pull/29)
* [create-vanilla-SCDB.sh: upgrade panc to 10.1](https://github.com/quattor/scdb/pull/26)

### configuration-modules-grid
* [Add support for GLUE v2](https://github.com/quattor/configuration-modules-grid/pull/61)
* [Build tools upgraded to 1.38 + add POD unit test](https://github.com/quattor/configuration-modules-grid/pull/48)
* [add `authorized_users` field](https://github.com/quattor/configuration-modules-grid/pull/44)
* [__ncm-gip2__: fix missing retrieval of parameters in `write_encoded()`](https://github.com/quattor/configuration-modules-grid/pull/51)
* [__ncm-gip2__: use `CAF::FileWriter` instead of `LC::Check::file`](https://github.com/quattor/configuration-modules-grid/pull/33)
* [__ncm-glitestartup__: replace `CAF::FileEditor` by `CAF::FileReader`](https://github.com/quattor/configuration-modules-grid/pull/60)
* [__ncm-glitestartup__: replace use of `LC::Check::file/status` by `CAF`](https://github.com/quattor/configuration-modules-grid/pull/56)
* [__ncm-glitestartup__: replace use of `qx` by `CAF::Process`](https://github.com/quattor/configuration-modules-grid/pull/55)
* [__ncm-mkgridmap__: fix incorrect argument passed to `CAF::Process`](https://github.com/quattor/configuration-modules-grid/pull/54)
* [__ncm-mkgridmap__: use `CAF::Process` instead of backticks + misc. cleanups](https://github.com/quattor/configuration-modules-grid/pull/49)
* [__ncm-pbsclient__: add submitonly boolean to configure submission-only nodes](https://github.com/quattor/configuration-modules-grid/pull/45)
* [__ncm-pbsserver__: add 2 more attributes to schema](https://github.com/quattor/configuration-modules-grid/pull/59)
* [__ncm-xrootd__: render ordered config files](https://github.com/quattor/configuration-modules-grid/pull/46)

### cdp-listend
* [Create a target/lib/perl directory during builds](https://github.com/quattor/cdp-listend/pull/7)
* [Fix pod file processing in pom.xml](https://github.com/quattor/cdp-listend/pull/8)

### CAF
* [Add `CAF::FileReader` for read-only file accesses](https://github.com/quattor/CAF/pull/55)
* [Add pod verification unittest](https://github.com/quattor/CAF/pull/58)
* [Add reload functionality to CAF::Service](https://github.com/quattor/CAF/pull/50)
* [`CAF::Render` to render structured text](https://github.com/quattor/CAF/pull/51)
* [`CAF::Service`: implement `stop_sleep_start`method](https://github.com/quattor/CAF/pull/65)
* [`CAF::TextRender` support TT options](https://github.com/quattor/CAF/pull/68)
* [Process: add `get_executable` and `execute_if_exists`](https://github.com/quattor/CAF/pull/54)
* [Service: use .service name with systemctl by default ](https://github.com/quattor/CAF/pull/57)
* [TextRender: cache the rendered text and implement `does_render` test](https://github.com/quattor/CAF/pull/56)
* [add TextRender perl dependencies](https://github.com/quattor/CAF/pull/67)
* [fix inconsistencies between the POD initialization and the code](https://github.com/quattor/CAF/pull/66)
* [support __ncm-metaconfig__ based on TextRender ](https://github.com/quattor/CAF/pull/59)
* [use correct multiple inheritance order](https://github.com/quattor/CAF/pull/60)

### template-library-examples
* [Add LICENSE information (Apache 2.0)](https://github.com/quattor/template-library-examples/pull/17)
