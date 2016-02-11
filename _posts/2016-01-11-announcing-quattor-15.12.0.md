---
layout: article
title: Quattor 15.12.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/15.12.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 71 pull requests and resolved 24 issues.

The next release should be 16.2.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.

Known Issues
------------

ncm-cdispd has [an issue](https://github.com/quattor/ncm-cdispd/issues/25) which appears to be a race condition, under certain rare circumstances this could lead to subsequent profiles to not be processed and leaving client nodes to become unconfigurable. The exactly circumstances that allow a node to encounter this problem are currently unknown, so we would appreciate reports from anyone who does encounter it.

A fix is available in [this pull-request](https://github.com/quattor/ncm-cdispd/pull/26).

Changelog
---------

### template-library-core
* [Add a benchmark field to the hardware type definition](https://github.com/quattor/template-library-core/pull/87)
* [Add boolean hyperthreading for structure cpu.](https://github.com/quattor/template-library-core/pull/94)
* [Add function to validate that paths in dict keys are valid files](https://github.com/quattor/template-library-core/pull/96)
* [**Blockdevices:** add metadata option to md devs](https://github.com/quattor/template-library-core/pull/80)
* [Remove component code parameter](https://github.com/quattor/template-library-core/pull/75)
* [check filesystems array has no duplicate mountpoints or blockdevs](https://github.com/quattor/template-library-core/pull/93)

### ncm-cdispd
* [restore the old ICLIST on ncm-ncd failure](https://github.com/quattor/ncm-cdispd/pull/23)

### configuration-modules-core
* [**ncm-altlogrotate:** Remove timestamp at top of file](https://github.com/quattor/configuration-modules-core/pull/634)
* [**ncm-authconfig:** add extra TT unittest for sssd access_provider simple](https://github.com/quattor/configuration-modules-core/pull/571)
* [**ncm-autofs:** maps unittest refine test](https://github.com/quattor/configuration-modules-core/pull/647)
* [**ncm-ccm:** Add support for configuring keep_old and trust](https://github.com/quattor/configuration-modules-core/pull/573)
* [**ncm-ceph:** add -L to file](https://github.com/quattor/configuration-modules-core/pull/580)
* [**ncm-ceph:** add mds_cache_size param](https://github.com/quattor/configuration-modules-core/pull/642)
* [**ncm-ceph:** fix user for known_hosts and fix output for destroy and restart](https://github.com/quattor/configuration-modules-core/pull/595)
* [**ncm-download:** allow kinit to run in NoAction mode.](https://github.com/quattor/configuration-modules-core/pull/568)
* [**ncm-filecopy, ncm-metaconfig:** validate file paths](https://github.com/quattor/configuration-modules-core/pull/628)
* [**ncm-fstab:** add protected filesystems and strict option](https://github.com/quattor/configuration-modules-core/pull/562)
* [**ncm-gpfs:** add gpfs.hadoop-connector to gpfs packages](https://github.com/quattor/configuration-modules-core/pull/623)
* [**ncm-hostsfile:** fix removal of old entries which were managed by NCM.](https://github.com/quattor/configuration-modules-core/pull/644)
* [**ncm-hostsfile:** merge config-{common,rpm} into config.pan](https://github.com/quattor/configuration-modules-core/pull/611)
* [**ncm-icinga:** adapt schema for recent icinga 1.X versions](https://github.com/quattor/configuration-modules-core/pull/630)
* [**ncm-interactivelimits:** merge config-{rpm,common} into config.pan.](https://github.com/quattor/configuration-modules-core/pull/601)
* [**ncm-iptables:** move from config-{common,rpm}.pan into config.pan](https://github.com/quattor/configuration-modules-core/pull/569)
* [**ncm-metaconfig:** Add ptpd service](https://github.com/quattor/configuration-modules-core/pull/632)
* [**ncm-metaconfig:** add cachefilesd service](https://github.com/quattor/configuration-modules-core/pull/637)
* [**ncm-metaconfig:** add libvirtd service](https://github.com/quattor/configuration-modules-core/pull/624)
* [**ncm-metaconfig:** add moab service (legacy component schema)](https://github.com/quattor/configuration-modules-core/pull/633)
* [**ncm-metaconfig:** add new options for ganesha 2.2](https://github.com/quattor/configuration-modules-core/pull/613)
* [**ncm-metaconfig:** cgroups service](https://github.com/quattor/configuration-modules-core/pull/638)
* [**ncm-metaconfig:** cleanup component templates](https://github.com/quattor/configuration-modules-core/pull/621)
* [**ncm-metaconfig:** logstash and elasticsearch 2.0 support](https://github.com/quattor/configuration-modules-core/pull/626)
* [**ncm-metaconfig:** remove daemon property](https://github.com/quattor/configuration-modules-core/pull/456)
* [**ncm-metaconfig:** service httpd: initial apache 2.4 format support](https://github.com/quattor/configuration-modules-core/pull/599)
* [**ncm-modprobe:** merge config-{common,rpm} into config.pan](https://github.com/quattor/configuration-modules-core/pull/602)
* [**ncm-nscd:** merge config-{common,rpm} into config.pan](https://github.com/quattor/configuration-modules-core/pull/635)
* [**ncm-ntpd:** introduce useserverip boolean to force hostname to IP](https://github.com/quattor/configuration-modules-core/pull/558)
* [**ncm-opennebula:**  Include support to tune ONE VMM drivers](https://github.com/quattor/configuration-modules-core/pull/596)
* [**ncm-opennebula:** Configure Opennebula services on demand](https://github.com/quattor/configuration-modules-core/pull/572)
* [**ncm-resolver:** merge config-{rpm,common} into config.pan](https://github.com/quattor/configuration-modules-core/pull/603)
* [**ncm-spma:** support yum noaction](https://github.com/quattor/configuration-modules-core/pull/565)
* [**ncm-ssh:** fix some issues introduced during rewrite.](https://github.com/quattor/configuration-modules-core/pull/606)
* [**ncm-ssh:** make config checks configurable.](https://github.com/quattor/configuration-modules-core/pull/645)

### ncm-lib-blockdevices
* [**Md:** add support for named md devices, newer metadata, and parted in favour of fdisk](https://github.com/quattor/ncm-lib-blockdevices/pull/56)

### template-library-grid
* [Move WLCG related stuff in features/wlcg](https://github.com/quattor/template-library-grid/pull/151)
* [Slot reporting](https://github.com/quattor/template-library-grid/pull/153)
* [Worker node machine features + Torque client job features](https://github.com/quattor/template-library-grid/pull/152)
* [conf for new puppet modules](https://github.com/quattor/template-library-grid/pull/154)

### CCM
* [Don't update current.cid to a broken database.](https://github.com/quattor/CCM/pull/77)
* [**Fetch:** refactor in submodules](https://github.com/quattor/CCM/pull/66)
* [Remove exec-maven-plugin version definition (done in master pom file)](https://github.com/quattor/CCM/pull/72)
* [**TextRender:** support builtin module general as alias for CCM/general](https://github.com/quattor/CCM/pull/73)
* [bump build-tools to 1.47](https://github.com/quattor/CCM/pull/78)

### maven-tools
* [Minor fixes](https://github.com/quattor/maven-tools/pull/69)
* [Test::Quattor set_service_variant support reload and additional actions](https://github.com/quattor/maven-tools/pull/66)
* [TextRender support distinguished CCM cache_root for Suite runs](https://github.com/quattor/maven-tools/pull/65)
* [Update maven plugins used by build tools](https://github.com/quattor/maven-tools/pull/64)

### aii
* [**aii-ks:** fix swap noformat in ks not working under anaconda 7](https://github.com/quattor/aii/pull/155)
* [**aii-ks:** when selinux is disabled in ks, don't install selinux policy rpms](https://github.com/quattor/aii/pull/144)
* [**aii-opennebula:** Include VM disk CACHE option](https://github.com/quattor/aii/pull/149)
* [**aii-opennebula:** include support to set different RPC cloud domains](https://github.com/quattor/aii/pull/143)
* [**kickstart:** add excludepkgs/includepkgs support](https://github.com/quattor/aii/pull/152)
* [**pxelinux:** lpxelinux support](https://github.com/quattor/aii/pull/147)

### template-library-os
* [**El7 support:** ensure that kernel RPM is part of the configuration](https://github.com/quattor/template-library-os/pull/71)

### configuration-modules-grid
* [Add new queue attributes](https://github.com/quattor/configuration-modules-grid/pull/83)
* [**ncm-dpmlfc:** major rewrite to support DAV configuration](https://github.com/quattor/configuration-modules-grid/pull/86)

### CAF
* [Cleanup and unittest Object, Log, Reporter and ReporterMany](https://github.com/quattor/CAF/pull/103)
* [Reduce verbosity of noaction mode](https://github.com/quattor/CAF/pull/119)
* [Remove unused ReporterObject and RepLogger](https://github.com/quattor/CAF/pull/104)
* [**Service:** support subclassing](https://github.com/quattor/CAF/pull/118)
* [**TextRender:** remove builtin general (provided via CCM::TextRender)](https://github.com/quattor/CAF/pull/116)
* [remove TextRender markdown, replaced by blog post](https://github.com/quattor/CAF/pull/111)
