---
layout: article
title: Quattor 24.10.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/24.10.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 162 pull requests and resolved 49 issues.

The next release will be early 2025, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### ncm-cdispd
* [add unitfile for ncm-cdispd, remove initscripts/chkconfig support](https://github.com/quattor/ncm-cdispd/pull/61)

### template-library-core
* [**quattor/functions/network copy_network_params:** bootproto=none for unconfigured interfaces](https://github.com/quattor/template-library-core/pull/235)

### configuration-modules-core
* [**ncm-metaconfig:** add schema for slurm 24.05](https://github.com/quattor/configuration-modules-core/pull/1695)
* [**ncm-network:** Move nmstate options to new schema](https://github.com/quattor/configuration-modules-core/pull/1720)
* [**ncm-nfs:** Allow daemon to reload to be specified](https://github.com/quattor/configuration-modules-core/pull/1621)

### aii
* [Fixes for EL9 support](https://github.com/quattor/aii/pull/350)

### cdp-listend
* [Remove support for EL6 (init scripts)](https://github.com/quattor/cdp-listend/pull/33)

Changelog
---------

### quattor.github.com
* [Remove Ruby version requirement](https://github.com/quattor/quattor.github.com/pull/279)
* [Rework old TravisCI test config to GitHub actions](https://github.com/quattor/quattor.github.com/pull/277)
* [Update Perl coding style](https://github.com/quattor/quattor.github.com/pull/278)
* [**coding_style:** Document each's evilness](https://github.com/quattor/quattor.github.com/pull/280)

### ncm-query
* [Update build-tools to 1.62](https://github.com/quattor/ncm-query/pull/16)
* [**workflows:** Switch CI action over to our own container image](https://github.com/quattor/ncm-query/pull/15)

### LC
* [Update build-tools to 1.62](https://github.com/quattor/LC/pull/20)
* [**workflows:** Add CI action based on our own container image](https://github.com/quattor/LC/pull/19)

### ncm-cdispd
* [Add chkconfig as a rpm dependency](https://github.com/quattor/ncm-cdispd/pull/60)
* [Update build-tools to 1.62](https://github.com/quattor/ncm-cdispd/pull/64)
* [add unitfile for ncm-cdispd, remove initscripts/chkconfig support](https://github.com/quattor/ncm-cdispd/pull/61)
* [**workflows:** Switch CI action over to our own container image](https://github.com/quattor/ncm-cdispd/pull/62)

### template-library-core
* [**AII KS variant for EL9:** fix required packages and Anaconda version](https://github.com/quattor/template-library-core/pull/230)
* [**CI scripts (panlint/indent):** exclude deleted files](https://github.com/quattor/template-library-core/pull/233)
* [Revert "AII templates for tag 24.10.0-rc2"](https://github.com/quattor/template-library-core/pull/234)
* [Update list of multiversion schema](https://github.com/quattor/template-library-core/pull/222)
* [add bootmode option to provide support for uefi](https://github.com/quattor/template-library-core/pull/221)
* [**ci-scripts:** Indent checker only accepts a single file](https://github.com/quattor/template-library-core/pull/228)
* [**hardware:** Fix bugs in max threads calculation and validate schema property](https://github.com/quattor/template-library-core/pull/225)
* [**pan/types:** Add type for crypt format password hashes](https://github.com/quattor/template-library-core/pull/227)
* [**quattor/functions/network copy_network_params:** bootproto=none for unconfigured interfaces](https://github.com/quattor/template-library-core/pull/235)
* [**test-templates:** Don't include network backend specific schema](https://github.com/quattor/template-library-core/pull/232)
* [**types/hardware:** Add HEPScore23 and deprecate HS06](https://github.com/quattor/template-library-core/pull/229)
* [**workflows:** Add missing colorama dependency](https://github.com/quattor/template-library-core/pull/226)
* [**workflows:** Consolidate, update and remove travis references](https://github.com/quattor/template-library-core/pull/224)
* [**workflows:** Run template testing action on our own container image](https://github.com/quattor/template-library-core/pull/223)

### configuration-modules-core
* [/var/tmp is supposed to be reboot persistent ](https://github.com/quattor/configuration-modules-core/pull/1715)
* [**CI configuration:** use same structure/scripts as in other repositories](https://github.com/quattor/configuration-modules-core/pull/1738)
* [**Dockerfile:** Switch to using our own base image](https://github.com/quattor/configuration-modules-core/pull/1709)
* [**Fixes #1704:** ncm-grub::pxeboot return SUCCESS on non-UEFI systems](https://github.com/quattor/configuration-modules-core/pull/1705)
* [**fixes #1684:** NCM::Component::spma::dnf: Update dnf.pm](https://github.com/quattor/configuration-modules-core/pull/1685)
* [**metaconfig:** cumulus: basic initialisation script and bgp frr support](https://github.com/quattor/configuration-modules-core/pull/1580)
* [**ncm-altlogrotate:** Support 'su' directive](https://github.com/quattor/configuration-modules-core/pull/1619)
* [**ncm-authconfig:** sssd: Schema improvements](https://github.com/quattor/configuration-modules-core/pull/1622)
* [**ncm-metaconfig beats:** add seccomp to file beat schema to allow seccomp config for filebeat.yml](https://github.com/quattor/configuration-modules-core/pull/1700)
* [**ncm-metaconfig:** Allow basic httpd remoteip config to be expressed](https://github.com/quattor/configuration-modules-core/pull/1701)
* [**ncm-metaconfig:** Remove spurious semicolon at end of line](https://github.com/quattor/configuration-modules-core/pull/1726)
* [**ncm-metaconfig:** SSH add SyslogFacility option](https://github.com/quattor/configuration-modules-core/pull/1654)
* [**ncm-metaconfig:** add schema for slurm 24.05](https://github.com/quattor/configuration-modules-core/pull/1695)
* [**ncm-metaconfig:** fix a typo in 'actions' resource description](https://github.com/quattor/configuration-modules-core/pull/1663)
* [**ncm-metaconfig:** fix errors in slurm 23.02 schema](https://github.com/quattor/configuration-modules-core/pull/1633)
* [**ncm-metaconfig:** haproxy - add ciphersuites config options](https://github.com/quattor/configuration-modules-core/pull/1652)
* [**ncm-metaconfig:** httpd - add missing cipher and sslopensslconfcmd](https://github.com/quattor/configuration-modules-core/pull/1650)
* [**ncm-metaconfig:** nginx add DHE-RSA-CHACHA20-POLY1305 cipher suite](https://github.com/quattor/configuration-modules-core/pull/1716)
* [**ncm-metaconfig:** ssh daemon configuration support](https://github.com/quattor/configuration-modules-core/pull/1452)
* [**ncm-metaconfig:** telegraf: Add support](https://github.com/quattor/configuration-modules-core/pull/1609)
* [**ncm-metaconfig:** upstream minor schema changes](https://github.com/quattor/configuration-modules-core/pull/1727)
* [**ncm-mysql:** add an option to use encrypted user password](https://github.com/quattor/configuration-modules-core/pull/1661)
* [**ncm-network core schema:** allow realhostname to be a short hostname](https://github.com/quattor/configuration-modules-core/pull/1595)
* [**ncm-network:** Move nmstate options to new schema](https://github.com/quattor/configuration-modules-core/pull/1720)
* [**ncm-network:** Remove legacy schema](https://github.com/quattor/configuration-modules-core/pull/1725)
* [**ncm-network:** Throw error if commands used with nmstate](https://github.com/quattor/configuration-modules-core/pull/1631)
* [**ncm-network:** add additional bonding options](https://github.com/quattor/configuration-modules-core/pull/1735)
* [**ncm-network:** add ipv6 support to the nmstate backend](https://github.com/quattor/configuration-modules-core/pull/1687)
* [**ncm-network:** add nmstate infiniband support](https://github.com/quattor/configuration-modules-core/pull/1676)
* [**ncm-network:** add support for device configuration dropin file](https://github.com/quattor/configuration-modules-core/pull/1712)
* [**ncm-network:** add two  missing schema types](https://github.com/quattor/configuration-modules-core/pull/1623)
* [**ncm-network:** fix multi bonding configuration and arp_ip_target bonding options](https://github.com/quattor/configuration-modules-core/pull/1640)
* [**ncm-network:** fix nmstate package definition in Kickstart config](https://github.com/quattor/configuration-modules-core/pull/1630)
* [**ncm-network:** improvements made to perl code to construct dummy interface hash](https://github.com/quattor/configuration-modules-core/pull/1624)
* [**ncm-network:** nmstate - add additional route rule parameters](https://github.com/quattor/configuration-modules-core/pull/1659)
* [**ncm-network:** nmstate - fix default gateway and policy routing table](https://github.com/quattor/configuration-modules-core/pull/1642)
* [**ncm-network:** nmstate change the way dummy interfaces are created.](https://github.com/quattor/configuration-modules-core/pull/1683)
* [**ncm-network:** nmstate dgw fix](https://github.com/quattor/configuration-modules-core/pull/1656)
* [**ncm-network:** nmstate enhancements](https://github.com/quattor/configuration-modules-core/pull/1647)
* [**ncm-network:** nmstate support for alias ip addresses](https://github.com/quattor/configuration-modules-core/pull/1688)
* [**ncm-network:** nmstate: Fix indentation errors](https://github.com/quattor/configuration-modules-core/pull/1741)
* [**ncm-network:** nmstate: add mac-address to nmstate config](https://github.com/quattor/configuration-modules-core/pull/1632)
* [**ncm-network:** nmstate: simple interfaces reorder on apply/delete](https://github.com/quattor/configuration-modules-core/pull/1693)
* [**ncm-network:** provide a better way to cleanup inactive connections](https://github.com/quattor/configuration-modules-core/pull/1635)
* [**ncm-network:** provide backward compatibility for vlan interface config for nmstate.](https://github.com/quattor/configuration-modules-core/pull/1667)
* [**ncm-network:** refactor network core schema](https://github.com/quattor/configuration-modules-core/pull/1673)
* [**ncm-network:** set profile-name and set dhcp to disable for static config](https://github.com/quattor/configuration-modules-core/pull/1637)
* [**ncm-nfs:** Allow daemon to reload to be specified](https://github.com/quattor/configuration-modules-core/pull/1621)
* [**ncm-nmstate:** relax syntax of VLAN interface names](https://github.com/quattor/configuration-modules-core/pull/1679)
* [**ncm-nmstate:** remove confusing warning in IPv6 configuration](https://github.com/quattor/configuration-modules-core/pull/1733)
* [**ncm-opennebula:** Add Ceph system datastore support](https://github.com/quattor/configuration-modules-core/pull/1651)
* [**ncm-opennebula:** add opennebula 6.0.x support](https://github.com/quattor/configuration-modules-core/pull/1526)
* [**ncm-opennebula:** do not use qxl video driver](https://github.com/quattor/configuration-modules-core/pull/1723)
* [**ncm-opennebula:** sec fix for opennebula 6.8](https://github.com/quattor/configuration-modules-core/pull/1670)
* [**ncm-postfix:** add support for smtpd_relay_restrictions](https://github.com/quattor/configuration-modules-core/pull/1697)
* [**ncm-spma:** Include APT backend in RPM for now](https://github.com/quattor/configuration-modules-core/pull/1617)
* [**ncm-spma:** support for dnf backend schema to support main_options](https://github.com/quattor/configuration-modules-core/pull/1703)
* [**ncm-spma:** update to dnf backend to exclude additional kernel packages.](https://github.com/quattor/configuration-modules-core/pull/1730)
* [**ncm-spma:** yumdnf: Don't attempt to expand groups with repoquery](https://github.com/quattor/configuration-modules-core/pull/1620)
* [**ncm-ssh:** add MaxSessions ssh option](https://github.com/quattor/configuration-modules-core/pull/1634)
* [**ncm-ssh:** add ssh/sshd option GSSAPIKexAlgorithms to schema](https://github.com/quattor/configuration-modules-core/pull/1714)
* [**ncm-ssh:** extend AllowTcpForwarding to support valid values](https://github.com/quattor/configuration-modules-core/pull/1707)
* [**ncm-sysctl:** Cleanup & fixes](https://github.com/quattor/configuration-modules-core/pull/1710)
* [**ncm-systemd:** Add PrivateNetwork schema entry](https://github.com/quattor/configuration-modules-core/pull/1668)
* [**ncm-systemd:** systemctl show can doublequoted backslash values](https://github.com/quattor/configuration-modules-core/pull/1694)
* [**network:** nmstate add support for ovsintport and ovsbridge](https://github.com/quattor/configuration-modules-core/pull/1719)
* [**tests:** update dockerfile to rockylinux:8](https://github.com/quattor/configuration-modules-core/pull/1625)

### ncm-lib-blockdevices
* [Add RHEL9 Anaconda version](https://github.com/quattor/ncm-lib-blockdevices/pull/104)
* [Allow to create label on vfat type](https://github.com/quattor/ncm-lib-blockdevices/pull/103)
* [Update build-tools to 1.62](https://github.com/quattor/ncm-lib-blockdevices/pull/109)

### template-library-standard
* [**CI scripts (panlint/indent):** exclude deleted files](https://github.com/quattor/template-library-standard/pull/165)
* [Cleanup filesystem config](https://github.com/quattor/template-library-standard/pull/155)
* [Ensure max_threads is set for all CPUs defined under /hardware/cpu/](https://github.com/quattor/template-library-standard/pull/161)
* [Update CI scripts](https://github.com/quattor/template-library-standard/pull/167)
* [**card/gpu:** Fix name of nvidia/tesla_a100_80gb-sxm](https://github.com/quattor/template-library-standard/pull/162)
* [**ci-scripts:** Indent checker only accepts a single file](https://github.com/quattor/template-library-standard/pull/164)
* [**hardware/card/gpu:** Add various NVIDIA cards used at RAL](https://github.com/quattor/template-library-standard/pull/157)
* [**hardware/card/raid:** Add two DELL controllers](https://github.com/quattor/template-library-standard/pull/158)
* [**hardware/cpu/amd:** adding epyc_9654](https://github.com/quattor/template-library-standard/pull/159)
* [**hardware/cpu:** Minor corrections from RAL](https://github.com/quattor/template-library-standard/pull/156)
* [**machine-types/core:** refactoring to avoid loading Quattor schema too early](https://github.com/quattor/template-library-standard/pull/166)
* [**workflows:** Update and make consistent with template-library-core](https://github.com/quattor/template-library-standard/pull/163)

### template-library-grid
* [Modernize CI scripts](https://github.com/quattor/template-library-grid/pull/246)
* [**features/mysqld:** fix syntax error](https://github.com/quattor/template-library-grid/pull/247)
* [**umd-3:** Fix max_threads reference](https://github.com/quattor/template-library-grid/pull/245)

### ncm-ncd
* [Add an explicit dependency on the Perl metapackage](https://github.com/quattor/ncm-ncd/pull/138)
* [Update build-tools to 1.62](https://github.com/quattor/ncm-ncd/pull/139)

### CCM
* [**Fetch:** Remove suffix from downloaded profile](https://github.com/quattor/CCM/pull/210)
* [Update build-tools to 1.62](https://github.com/quattor/CCM/pull/217)
* [**workflows:** Switch CI action over to our own container image](https://github.com/quattor/CCM/pull/212)

### template-library-os
* [Add CI scripts from template-library-examples](https://github.com/quattor/template-library-os/pull/107)
* [EL9 initial templates](https://github.com/quattor/template-library-os/pull/106)

### template-library-openstack
* [Add CI scripts to check modified templates](https://github.com/quattor/template-library-openstack/pull/56)
* [**CI scripts (panlint/indent):** exclude deleted files](https://github.com/quattor/template-library-openstack/pull/60)
* [Major refactoring of templates for Ussuri version](https://github.com/quattor/template-library-openstack/pull/53)
* [OpenStack Victoria support](https://github.com/quattor/template-library-openstack/pull/54)
* [Templates for OpenStack Wallaby version](https://github.com/quattor/template-library-openstack/pull/55)
* [Templates for OpenStack Xena version](https://github.com/quattor/template-library-openstack/pull/59)
* [Templates for OpenStack Yoga version](https://github.com/quattor/template-library-openstack/pull/61)

### aii
* [/var/tmp is supposed to be reboot persistent](https://github.com/quattor/aii/pull/347)
* [Add panlint and indent to CI scripts](https://github.com/quattor/aii/pull/351)
* [Define default installation boot protocol as static](https://github.com/quattor/aii/pull/352)
* [Fixes for EL9 support](https://github.com/quattor/aii/pull/350)
* [Update build tools to 1.62](https://github.com/quattor/aii/pull/353)
* [**aii/ks:** Add variants for EL8 and EL9](https://github.com/quattor/aii/pull/341)
* [**aii/ks:** support for sending mail in el9 using correct s-nail format](https://github.com/quattor/aii/pull/345)
* [**workflows:** Switch CI action over to our own container image](https://github.com/quattor/aii/pull/346)

### release
* [Add configuration for rpmlint 1.x ](https://github.com/quattor/release/pull/351)
* [**Dockerfile:** Add rpm-build and don't set USER or CMD](https://github.com/quattor/release/pull/354)
* [**Dockerfile:** add procps-ng for sysctl tests](https://github.com/quattor/release/pull/352)
* [Releaser fixes](https://github.com/quattor/release/pull/361)
* [Update Dockerfile to RockyLinux 8 + add workflow to build it](https://github.com/quattor/release/pull/349)
* [**get-template-library:** Add debugging information when --continuous integration is present](https://github.com/quattor/release/pull/363)
* [**get-template-library:** Add debugging information when --continuous integration is present](https://github.com/quattor/release/pull/362)
* [**get-template-library:** Quattor version update in cluster build properties](https://github.com/quattor/release/pull/366)
* [**get-template-library:** add support for GitHub Actions](https://github.com/quattor/release/pull/364)
* [**get-template-library:** exclude all versions before 23.x](https://github.com/quattor/release/pull/359)
* [**get-template-library:** remove obsolete monitoring repository](https://github.com/quattor/release/pull/358)
* [**rpmlint:** Allow metaconfig templates to be non-executable scripts](https://github.com/quattor/release/pull/350)

### configuration-modules-grid
* [small error with the creation of the lsc voms file from quat…](https://github.com/quattor/configuration-modules-grid/pull/149)
* [**workflows:** Switch CI action over to our own container image](https://github.com/quattor/configuration-modules-grid/pull/150)

### cdp-listend
* [Add chkconfig as an rpm dependency](https://github.com/quattor/cdp-listend/pull/28)
* [Remove support for EL6 (init scripts)](https://github.com/quattor/cdp-listend/pull/33)
* [Update build-tools to 1.62](https://github.com/quattor/cdp-listend/pull/36)
* [**cdp-listend:** Factor out calls to notification handlers](https://github.com/quattor/cdp-listend/pull/23)
* [**fix typo:** cdp-listend should not mess with sshd](https://github.com/quattor/cdp-listend/pull/29)
* [switch unitfile to EL9 recommended PIDfile path](https://github.com/quattor/cdp-listend/pull/32)
* [**workflows:** Switch CI action over to our own container image](https://github.com/quattor/cdp-listend/pull/35)

### CAF
* [Replace four instances of while-each with foreach](https://github.com/quattor/CAF/pull/277)
* [**ServiceActions:** Unescape daemon names](https://github.com/quattor/CAF/pull/279)
* [Update build-tools to 1.62](https://github.com/quattor/CAF/pull/280)
* [add github action for tests](https://github.com/quattor/CAF/pull/275)
* [**workflows:** Switch CI action over to our own container image](https://github.com/quattor/CAF/pull/278)

### template-library-examples
* [Add CI scripts](https://github.com/quattor/template-library-examples/pull/39)
* [Update grid-related examples](https://github.com/quattor/template-library-examples/pull/40)
* [**workflows:** Add missing colorama dependency for the indent checker](https://github.com/quattor/template-library-examples/pull/41)
