---
layout: article
title: Quattor 17.3.0 released
category: news
author: James Adams
---

<div class="alert alert-danger" role="alert">
    <p><b>Warning</b>: This release contains a [serious bug](https://github.com/quattor/configuration-modules-core/issues/1141) that can break logrotate configuration. We recommend that you do not deploy it unless you are certain you will not be affected.</p>
</div>

Packages are available from our [yum repository](http://yum.quattor.org/17.3.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 78 pull requests and resolved 36 issues.

The next release should be 17.4.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### template-library-core
* [**quattor/functions/network:** cleanup and removal of get_subnet_params function](https://github.com/quattor/template-library-core/pull/150)

### ncm-cdispd
* [Do not set a default value for state directory](https://github.com/quattor/ncm-cdispd/pull/48)

### configuration-modules-core
* [**ncm-aiiserver:** add support for AII Grub-2 related options](https://github.com/quattor/configuration-modules-core/pull/1061)
* [**ncm-authconfig:** switch to 00-tqu and buildtools 1.52](https://github.com/quattor/configuration-modules-core/pull/1046)

### ncm-ncd
* [**ncm-ncd:** modified event reporting under NoAction=1 with new FileWriter](https://github.com/quattor/ncm-ncd/pull/109)

### CCM
* [**Cleanup:** move internal modules in subdirectories and remove/integrate util scripts](https://github.com/quattor/CCM/pull/162)

### maven-tools
* [**Test::Quattor:** set $Test::Quattor::NoAction default to 1](https://github.com/quattor/maven-tools/pull/160)

Changelog
---------

### template-library-core
* [**blockdevices schema:** add support for esp partition flag](https://github.com/quattor/template-library-core/pull/153)
* [**functions/network.pan:** readd a modernized get_subnet_params()](https://github.com/quattor/template-library-core/pull/154)
* [**quattor/functions/network:** add ip_in_network function](https://github.com/quattor/template-library-core/pull/151)
* [**quattor/functions/network:** cleanup and removal of get_subnet_params function](https://github.com/quattor/template-library-core/pull/150)

### LC
* [**LC::Check:** fix link() for hardlink creation](https://github.com/quattor/LC/pull/16)

### ncm-cdispd
* [Do not set a default value for state directory](https://github.com/quattor/ncm-cdispd/pull/48)
* [bump build-tools to 1.54](https://github.com/quattor/ncm-cdispd/pull/49)

### configuration-modules-core
* [Bump builds-scripts to 1.54](https://github.com/quattor/configuration-modules-core/pull/1107)
* [CCM cleanup fallout](https://github.com/quattor/configuration-modules-core/pull/1077)
* [**aiiserver:** options unittest: support older perl versions that do not have generic newline](https://github.com/quattor/configuration-modules-core/pull/1123)
* [**ncm-accounts/ncm-authconfig:** handle sensitive data ](https://github.com/quattor/configuration-modules-core/pull/1089)
* [**ncm-aiiserver:** add support for AII Grub-2 related options](https://github.com/quattor/configuration-modules-core/pull/1061)
* [**ncm-aiiserver:** switch to 00-tqu and buildtools 1.52](https://github.com/quattor/configuration-modules-core/pull/1044)
* [**ncm-altlogrotate:** cleanup and refactor](https://github.com/quattor/configuration-modules-core/pull/1045)
* [**ncm-authconfig:** switch to 00-tqu and buildtools 1.52](https://github.com/quattor/configuration-modules-core/pull/1046)
* [**ncm-autofs:** switch to 00-tqu and buildtools 1.52](https://github.com/quattor/configuration-modules-core/pull/1047)
* [**ncm-ccm:** switch to 00-tqu and buildtools 1.52](https://github.com/quattor/configuration-modules-core/pull/1048)
* [**ncm-cdp:** switch to 00-tqu and buildtools 1.52](https://github.com/quattor/configuration-modules-core/pull/1049)
* [**ncm-directoryservices ncm-fmonagent ncm-mcx:** Deprecate with warnings](https://github.com/quattor/configuration-modules-core/pull/1051)
* [**ncm-filesystems:** rewrite to reuse ncm-fstab code](https://github.com/quattor/configuration-modules-core/pull/985)
* [**ncm-freeipa:** mock_rpc: handle JSON boolean string conversion with mixed JSON::PP and JSON::XS environment](https://github.com/quattor/configuration-modules-core/pull/1062)
* [**ncm-grub:** add get_info method and warn when default kernel has more than one entry](https://github.com/quattor/configuration-modules-core/pull/1019)
* [**ncm-icinga:** check service names for invalid characters](https://github.com/quattor/configuration-modules-core/pull/1065)
* [**ncm-icinga:** start warning about deprecated config options.](https://github.com/quattor/configuration-modules-core/pull/1068)
* [**ncm-network:** core-schema: add additional checks to make sure gateway and broadcast are in network range](https://github.com/quattor/configuration-modules-core/pull/1043)
* [**ncm-network:** device name regex: allow function and device in PCI name](https://github.com/quattor/configuration-modules-core/pull/1073)
* [**ncm-postgresql:** Add warning about deprecated configuration options.](https://github.com/quattor/configuration-modules-core/pull/1067)
* [**ncm-spma:** support Solaris pkg exact-install and whitelists](https://github.com/quattor/configuration-modules-core/pull/1036)

### ncm-lib-blockdevices
* [bump build-tools to 1.54](https://github.com/quattor/ncm-lib-blockdevices/pull/85)

### ncm-ncd
* [Fix version stringification issue in unittest](https://github.com/quattor/ncm-ncd/pull/115)
* [Try to reproduce error seen during build_all_repos](https://github.com/quattor/ncm-ncd/pull/113)
* [build build-tools to 1.54](https://github.com/quattor/ncm-ncd/pull/112)
* [**ncm-ncd:** modified event reporting under NoAction=1 with new FileWriter](https://github.com/quattor/ncm-ncd/pull/109)
* [tabcompletion unittest requires access to the CCM TT files](https://github.com/quattor/ncm-ncd/pull/107)

### CCM
* [**Cleanup:** move internal modules in subdirectories and remove/integrate util scripts](https://github.com/quattor/CCM/pull/162)
* [**Configuration:** CacheManager::Configuration has to be childclass of placeholder deprecated Configuration](https://github.com/quattor/CCM/pull/170)
* [bump build-tools to 1.54 ](https://github.com/quattor/CCM/pull/171)

### maven-tools
* [Add keeps_state as a valid option for mocked _make_link()](https://github.com/quattor/maven-tools/pull/154)
* [**Critic:** enforce ProhibitTrailingWhitespace](https://github.com/quattor/maven-tools/pull/155)
* [**Test/Quattor.pm:** fix mocked symlink-related methods](https://github.com/quattor/maven-tools/pull/149)
* [**Test/Quattor/Panc:** refine valid annotation](https://github.com/quattor/maven-tools/pull/136)
* [**Test::Quattor:** add initial support for mocked FileEditor source option](https://github.com/quattor/maven-tools/pull/158)
* [**Test::Quattor:** mock CAF::Path link-related functions](https://github.com/quattor/maven-tools/pull/142)
* [**Test::Quattor:** mock CAF::Path::_listdir](https://github.com/quattor/maven-tools/pull/152)
* [**Test::Quattor:** set $Test::Quattor::NoAction default to 1](https://github.com/quattor/maven-tools/pull/160)
* [**Test::Quattor::Filetools:** writefile: support writing 0 or empty string](https://github.com/quattor/maven-tools/pull/146)
* [**Test::Quattor::Panc:** panc_annotations return both exitcode and output](https://github.com/quattor/maven-tools/pull/144)
* [**Test::Quattor::ProfileCache:** use a ccm.cfg per compiled profile](https://github.com/quattor/maven-tools/pull/148)
* [**Test::Quattor::_make_link:** fix error message with missing target](https://github.com/quattor/maven-tools/pull/156)
* [**Test::Quattor::_make_link:** use file exists for link target test and set fail attribute on failure](https://github.com/quattor/maven-tools/pull/157)
* [**mvnprove:** PMcomponent: force newline before package](https://github.com/quattor/maven-tools/pull/147)
* [**mvnprove:** trace the tests, not prove (and include tracing compiletime)](https://github.com/quattor/maven-tools/pull/137)

### aii
* [Add UEFI support through Grub-based PXE loader](https://github.com/quattor/aii/pull/225)
* [Bump build-tools to 1.54](https://github.com/quattor/aii/pull/267)
* [Use aii-shellfe config options for CCM fetch as well](https://github.com/quattor/aii/pull/265)
* [**pxelinux:** allow network device names with pci function and/or device](https://github.com/quattor/aii/pull/263)

### release
* [Remove workaround for broken maven 3.3.3 packages](https://github.com/quattor/release/pull/292)
* [Script to build last N aquilon protocol releases and latest aquilon release with RAL customisations](https://github.com/quattor/release/pull/275)
* [**build_all_repos:** fix missing quote](https://github.com/quattor/release/pull/294)
* [**build_all_repos:** ignore mocked test modules from src/test/resources](https://github.com/quattor/release/pull/293)
* [trac2md improvements](https://github.com/quattor/release/pull/290)

### configuration-modules-grid
* [Cleanup usage of deprecated CCM modules](https://github.com/quattor/configuration-modules-grid/pull/130)
* [bump build-scripts to 1.54](https://github.com/quattor/configuration-modules-grid/pull/131)

### cdp-listend
* [bump build-tools to 1.54](https://github.com/quattor/cdp-listend/pull/18)

### CAF
* [**CAF:** fix pod issues for rebuild to rst.](https://github.com/quattor/CAF/pull/228)
* [**CAF::Application:** add methods option_exists() and set_options()](https://github.com/quattor/CAF/pull/224)
* [**CAF::Path:** add methods to manage links](https://github.com/quattor/CAF/pull/225)
* [**FileWriter/Editor:** fix bug in close with source](https://github.com/quattor/CAF/pull/238)
* [**FileWriter:** Handle default permissions](https://github.com/quattor/CAF/pull/243)
* [**FileWriter:** use atomic write](https://github.com/quattor/CAF/pull/202)
* [**Filewriter:** support sensitive option](https://github.com/quattor/CAF/pull/226)
* [**Path.pm:** add a debug message in _make_link](https://github.com/quattor/CAF/pull/227)
* [**Path:** _get_noaction should try instance noAction method first](https://github.com/quattor/CAF/pull/244)
* [**Path:** move: do not cleanup dest, but add backup of dest using hardlink](https://github.com/quattor/CAF/pull/229)
* [Update build tools to 1.53](https://github.com/quattor/CAF/pull/231)
* [bump build-tools to 1.54](https://github.com/quattor/CAF/pull/246)
* [**filewriter/fileeditor tests:** reset the string reference to avoid perl warnings](https://github.com/quattor/CAF/pull/235)
* [**filewriter_notmocked.t:** fix regexp to be EL6 compatible](https://github.com/quattor/CAF/pull/233)
