---
layout: article
title: Quattor 17.2.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/17.2.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 92 pull requests and resolved 24 issues.

The next release should be 17.3.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### template-library-core
* [Add CPU architecture type definition](https://github.com/quattor/template-library-core/pull/143)
* [Add structures to model operating system information](https://github.com/quattor/template-library-core/pull/142)
* [Remove /system/oldnames from schema](https://github.com/quattor/template-library-core/pull/146)

### configuration-modules-core
* [**ncm-grub:** full overhaul](https://github.com/quattor/configuration-modules-core/pull/999)
* [**ncm-metaconfig:** devicemapper: fix multipath config](https://github.com/quattor/configuration-modules-core/pull/1025)

### ncm-lib-blockdevices
* [**Partition:** export partition_sort instead of partition_compare](https://github.com/quattor/ncm-lib-blockdevices/pull/80)

### aii
* [**AII:Shellfe:** Add option to run methods in parallel](https://github.com/quattor/aii/pull/239)

### template-library-os
* [**Firewalld:** fix previous commit (ae1911a7e83)](https://github.com/quattor/template-library-os/pull/85)

Changelog
---------

### quattor.github.com
* [components spring17 cleaning post](https://github.com/quattor/quattor.github.com/pull/199)

### ncm-query
* [Update build tools to version 1.51](https://github.com/quattor/ncm-query/pull/12)

### LC
* [Update build tools to version 1.51](https://github.com/quattor/LC/pull/15)

### ncm-cdispd
* [Update build tools to version 1.51](https://github.com/quattor/ncm-cdispd/pull/47)

### template-library-core
* [Add CPU architecture type definition](https://github.com/quattor/template-library-core/pull/143)
* [Add opennebula tree in system](https://github.com/quattor/template-library-core/pull/137)
* [Add structures to model operating system information](https://github.com/quattor/template-library-core/pull/142)
* [Add support for vxfs and zfs filesystem types](https://github.com/quattor/template-library-core/pull/144)
* [Metadata annotation](https://github.com/quattor/template-library-core/pull/147)
* [Remove /system/oldnames from schema](https://github.com/quattor/template-library-core/pull/146)
* [**Travis:** add a test to compile the library against examples](https://github.com/quattor/template-library-core/pull/140)
* [**blockdevices:** add validation check configuration to physical devices](https://github.com/quattor/template-library-core/pull/139)

### configuration-modules-core
* [** ncm-download:** allow_older boolean to allow downloading remote files that are older then current file](https://github.com/quattor/configuration-modules-core/pull/1005)
* [Deprecate group support in YUM backends](https://github.com/quattor/configuration-modules-core/pull/1041)
* [add .docbuilder.cfg for documentation.](https://github.com/quattor/configuration-modules-core/pull/1008)
* [**ncm-accounts:** switch to 00-tqu and code cleanup](https://github.com/quattor/configuration-modules-core/pull/1031)
* [**ncm-authconfig:** sssd: use sensible default debug_level](https://github.com/quattor/configuration-modules-core/pull/1006)
* [**ncm-download:** switch to CAF::Download::LWP](https://github.com/quattor/configuration-modules-core/pull/984)
* [**ncm-filesystems:** Use partition_sort instead of sorting partition_compare](https://github.com/quattor/configuration-modules-core/pull/1040)
* [**ncm-fstab:** pass tree instead of config](https://github.com/quattor/configuration-modules-core/pull/986)
* [**ncm-grub:** full overhaul](https://github.com/quattor/configuration-modules-core/pull/999)
* [**ncm-grub:** support settings passwords ](https://github.com/quattor/configuration-modules-core/pull/1022)
* [**ncm-icinga:** Remove function prototypes from test case](https://github.com/quattor/configuration-modules-core/pull/1020)
* [**ncm-metaconfig:** devicemapper: fix multipath config](https://github.com/quattor/configuration-modules-core/pull/1025)
* [**ncm-metaconfig:** opennebula Include CA option](https://github.com/quattor/configuration-modules-core/pull/1016)
* [**ncm-ofed:** new options and cleanup](https://github.com/quattor/configuration-modules-core/pull/1010)
* [**ncm-opennebula:** Add aii component rpm](https://github.com/quattor/configuration-modules-core/pull/1056)
* [**ncm-opennebula:** Documentation fixes](https://github.com/quattor/configuration-modules-core/pull/1060)
* [**ncm-opennebula:** Opennebula refactoring and AII code](https://github.com/quattor/configuration-modules-core/pull/1009)
* [**ncm-shorewall:** add stoppedrules support](https://github.com/quattor/configuration-modules-core/pull/1013)

### ncm-lib-blockdevices
* [**Blockdevices:** determine correct disksize using integers (not floats) in bash](https://github.com/quattor/ncm-lib-blockdevices/pull/73)
* [**LV:** force lvconvert by passing -y](https://github.com/quattor/ncm-lib-blockdevices/pull/76)
* [**Partition:** export partition_sort instead of partition_compare](https://github.com/quattor/ncm-lib-blockdevices/pull/80)
* [Switch to 00-tqu](https://github.com/quattor/ncm-lib-blockdevices/pull/77)
* [Update build tools to version 1.51](https://github.com/quattor/ncm-lib-blockdevices/pull/78)
* [rename device validation 'correct' to 'validate'](https://github.com/quattor/ncm-lib-blockdevices/pull/79)

### template-library-standard
* [Configure Travis to test the library against SCDB examples](https://github.com/quattor/template-library-standard/pull/92)
* [Configure travis to run linting tests](https://github.com/quattor/template-library-standard/pull/91)
* [Move panlint travis script into same location as SCDB script](https://github.com/quattor/template-library-standard/pull/93)

### template-library-grid
* [Configure Travis to test library against SCDB examples (umd-3)](https://github.com/quattor/template-library-grid/pull/190)
* [Configure Travis to test library against SCDB examples (umd-4)](https://github.com/quattor/template-library-grid/pull/189)
* [Configure travis to run linting tests](https://github.com/quattor/template-library-grid/pull/187)

### ncm-ncd
* [Bump build-tools and switch to 00-tqu](https://github.com/quattor/ncm-ncd/pull/104)
* [**ComponentProxy:** disable uninitialized warnings while restoring ENV and SIG](https://github.com/quattor/ncm-ncd/pull/106)
* [Update build tools to version 1.51](https://github.com/quattor/ncm-ncd/pull/105)

### CCM
* [**Fetch::Download:** switch to CAF::Download::LWP](https://github.com/quattor/CCM/pull/156)
* [Switch to 00-tqu](https://github.com/quattor/CCM/pull/160)
* [Update build tools to version 1.51](https://github.com/quattor/CCM/pull/166)
* [Use a branch type value allowed by the schema when testing](https://github.com/quattor/CCM/pull/165)
* [add documentation config file](https://github.com/quattor/CCM/pull/164)

### maven-tools
* [Add PMcomponent maven template for (regular) component Perl modules](https://github.com/quattor/maven-tools/pull/128)
* [**Critic:** no more backticks/qx/system, use CAF::Process](https://github.com/quattor/maven-tools/pull/125)
* [**ProfileCache:** prepare_profile_cache checks for valid object template](https://github.com/quattor/maven-tools/pull/127)
* [**Unittest:** support emptypoddirs](https://github.com/quattor/maven-tools/pull/129)
* [add documentation config file](https://github.com/quattor/maven-tools/pull/123)
* [**mvnprove:** support actual tracing while running prove](https://github.com/quattor/maven-tools/pull/133)

### aii
* [**AII:Shellfe:** Add option to run methods in parallel](https://github.com/quattor/aii/pull/239)
* [Remove opennebula from aii](https://github.com/quattor/aii/pull/253)
* [Remove stray 1 from info message](https://github.com/quattor/aii/pull/259)
* [**aii-core:** fix typos in Shellfe.pm](https://github.com/quattor/aii/pull/249)
* [**aii-core:** switch to CAF::Download::LWP](https://github.com/quattor/aii/pull/237)
* [**aii-ks:** relax test regexp due to fp rounding issues](https://github.com/quattor/aii/pull/242)
* [**aii-ks:** rename ncm-lib-blockdevices 'correct' to 'validate'](https://github.com/quattor/aii/pull/244)
* [**aii-opennebula:** Add VM image driver option](https://github.com/quattor/aii/pull/238)
* [**aii-shellfe:** add missing test resource file](https://github.com/quattor/aii/pull/251)

### template-library-os
* [Enable execution of create-vanilla-SCDB through Travis (el7.x-x86_64)](https://github.com/quattor/template-library-os/pull/87)
* [Enable execution of create-vanilla-SCDB through Travis (sl6.x-x86_64)](https://github.com/quattor/template-library-os/pull/86)
* [**Firewalld:** fix previous commit (ae1911a7e83)](https://github.com/quattor/template-library-os/pull/85)
* [**Sl6.x:** add new perl dependencies for Quattor development](https://github.com/quattor/template-library-os/pull/90)
* [**Travis config:** more flexible configuration layout (el7.x-x86_64)](https://github.com/quattor/template-library-os/pull/88)
* [**Travis config:** more flexible configuration layout (sl6.x-x86_64)](https://github.com/quattor/template-library-os/pull/89)
* [**el7.x Quattor development:** add perl-Text-Diff](https://github.com/quattor/template-library-os/pull/92)
* [**el7.x:** add new perl dependencies for Quattor development](https://github.com/quattor/template-library-os/pull/91)

### release
* [**build_all_repos:** add externals repo](https://github.com/quattor/release/pull/281)
* [**build_all_repos:** don't build ncm-freeipa on el5](https://github.com/quattor/release/pull/284)
* [**build_all_repos:** skip whole aii repo on el5, do not try to filter the pom.xml](https://github.com/quattor/release/pull/283)

### configuration-modules-grid
* [add documentation config file](https://github.com/quattor/configuration-modules-grid/pull/128)
* [**ncm-*:** Update build tools to version 1.51](https://github.com/quattor/configuration-modules-grid/pull/129)

### cdp-listend
* [Update build tools to version 1.51](https://github.com/quattor/cdp-listend/pull/17)

### CAF
* [**CAF::Download::LWP:** CAF interface for LWP to handle https settings](https://github.com/quattor/CAF/pull/203)
* [**CAF::Path:** fix typo in file_exists() documentation](https://github.com/quattor/CAF/pull/215)
* [**Download/LWP and Kerberos:** disable unitialized warnings while making local ENV copy](https://github.com/quattor/CAF/pull/221)
* [**FileEditor:** fix add_or_replace_sysconfig_lines ](https://github.com/quattor/CAF/pull/211)
* [**FileWriter:** resolve cyclic dependency](https://github.com/quattor/CAF/pull/214)
* [Handle Download::LWP on el5/el6](https://github.com/quattor/CAF/pull/209)
* [**Reporter:** add structured logging and message templating](https://github.com/quattor/CAF/pull/204)
* [**Reporter:** support struct logging and templating using old TT without STRICT support (eg el5)](https://github.com/quattor/CAF/pull/220)
* [**RuleBasedEditor:** use CCM::Path for unescape](https://github.com/quattor/CAF/pull/208)
* [Switch to 00-tqu](https://github.com/quattor/CAF/pull/206)
* [Update build tools to version 1.51](https://github.com/quattor/CAF/pull/212)
* [add documentation config file](https://github.com/quattor/CAF/pull/207)

### template-library-examples
* [**Travis config:** more flexible configuration layout](https://github.com/quattor/template-library-examples/pull/35)
