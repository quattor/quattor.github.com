---
layout: article
title: Quattor 26.2.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/26.2.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 151 pull requests and resolved 25 issues.

The next release should be later this year, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### configuration-modules-core
* [**ncm-metaconfig:** updated filebeat 7.x schema to fix #1728](https://github.com/quattor/configuration-modules-core/pull/1810)
* [**ncm-network:** dropin file support for main configuration of NetworkManager](https://github.com/quattor/configuration-modules-core/pull/1739)
* [**ncm-opennebula:** Add cpu pinning support](https://github.com/quattor/configuration-modules-core/pull/1776)
* [**ncm-postgresql:** Make pg_version mandatory in schema](https://github.com/quattor/configuration-modules-core/pull/1857)

### template-library-grid
* [Remove references to PBS knownhosts](https://github.com/quattor/template-library-grid/pull/251)

### CCM
* [Remove description field](https://github.com/quattor/CCM/pull/215)
* [Strip out all references to derivation](https://github.com/quattor/CCM/pull/214)

### configuration-modules-grid
* [**ncm-lbconfig:** Remove obsolete component](https://github.com/quattor/configuration-modules-grid/pull/155)
* [**ncm-pbsknownhosts:** Remove obsolete component](https://github.com/quattor/configuration-modules-grid/pull/154)

Changelog
---------

### ncm-query
* [Reuse shared workflows to run tests](https://github.com/quattor/ncm-query/pull/17)

### LC
* [Reuse shared workflows to run tests](https://github.com/quattor/LC/pull/21)

### ncm-cdispd
* [Reuse shared workflows to run tests](https://github.com/quattor/ncm-cdispd/pull/66)

### template-library-core
* [Add Rocky and Alma as supported distribution names](https://github.com/quattor/template-library-core/pull/244)
* [New option to allow override of how fstab entries get created.](https://github.com/quattor/template-library-core/pull/245)
* [Reuse shared workflows to run tests](https://github.com/quattor/template-library-core/pull/247)
* [**aii/server/config:** configure grub2_efi_kernel_root](https://github.com/quattor/template-library-core/pull/238)
* [**ncm-systemd schema:** port fix from configuration-module-core/main](https://github.com/quattor/template-library-core/pull/240)
* [**physdevices:** RAID controllers can have PCI details](https://github.com/quattor/template-library-core/pull/243)
* [**quattor/functions/network get_subnet_params:** allow to return subnet](https://github.com/quattor/template-library-core/pull/237)
* [**quattor/server/rpms:** fix DHCP client RPM for EL9](https://github.com/quattor/template-library-core/pull/236)

### configuration-modules-core
* [**CI:** panlint: Allow maven templates as first line](https://github.com/quattor/configuration-modules-core/pull/1743)
* [Reuse shared workflow to run all standard tests](https://github.com/quattor/configuration-modules-core/pull/1849)
* [Update maven build tools to 1.63](https://github.com/quattor/configuration-modules-core/pull/1848)
* [**authconfig:** sssd: add extra options](https://github.com/quattor/configuration-modules-core/pull/1812)
* [**metaconfig/named:** fix validation of logging channels in categories](https://github.com/quattor/configuration-modules-core/pull/1783)
* [**nc-fstab:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1755)
* [**ncm-accounts:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1747)
* [**ncm-altlogrotate:** global logrotate config fails to be modified in some cases](https://github.com/quattor/configuration-modules-core/pull/1813)
* [**ncm-authconfig:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1748)
* [**ncm-authconfig:** Use choice type where possible](https://github.com/quattor/configuration-modules-core/pull/1763)
* [**ncm-ccm:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1749)
* [**ncm-ceph:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1750)
* [**ncm-cron:** Cleanup lint warnings from pan templates](https://github.com/quattor/configuration-modules-core/pull/1799)
* [**ncm-cron:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1751)
* [**ncm-download:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1752)
* [**ncm-filesystems:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1753)
* [**ncm-freeipa:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1754)
* [**ncm-gmetad:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1756)
* [**ncm-grub:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1757)
* [**ncm-grub:** add for_next boolean to set default kernel outside ncm-grub](https://github.com/quattor/configuration-modules-core/pull/1819)
* [**ncm-icinga:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1758)
* [**ncm-metaconfig/ganesha:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1806)
* [**ncm-metaconfig:** Add chrony options for dealing with leap-second adjustments on time servers](https://github.com/quattor/configuration-modules-core/pull/1829)
* [**ncm-metaconfig:** Allow httpd wide headers to be set](https://github.com/quattor/configuration-modules-core/pull/1825)
* [**ncm-metaconfig:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1779)
* [**ncm-metaconfig:** Make `paths` optional in beats schema](https://github.com/quattor/configuration-modules-core/pull/1820)
* [**ncm-metaconfig:** Update defaults for SSL protocol and ciphersuite](https://github.com/quattor/configuration-modules-core/pull/1827)
* [**ncm-metaconfig:** add grafana](https://github.com/quattor/configuration-modules-core/pull/1818)
* [**ncm-metaconfig:** add prometheus](https://github.com/quattor/configuration-modules-core/pull/1817)
* [**ncm-metaconfig:** carbon-relay-ng: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1792)
* [**ncm-metaconfig:** chrony: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1793)
* [**ncm-metaconfig:** conntrackd: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1794)
* [**ncm-metaconfig:** cumulus: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1795)
* [**ncm-metaconfig:** dellnetworking: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1796)
* [**ncm-metaconfig:** devicemapper: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1791)
* [**ncm-metaconfig:** generic: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1797)
* [**ncm-metaconfig:** graphite: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1835)
* [**ncm-metaconfig:** graylog2: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1836)
* [**ncm-metaconfig:** haproxy - add cookie config option](https://github.com/quattor/configuration-modules-core/pull/1724)
* [**ncm-metaconfig:** httpd: Fix wrapping, indentation and lint issues in pan code](https://github.com/quattor/configuration-modules-core/pull/1837)
* [**ncm-metaconfig:** httpd: add more CAS options](https://github.com/quattor/configuration-modules-core/pull/1860)
* [**ncm-metaconfig:** httpd: support casscope](https://github.com/quattor/configuration-modules-core/pull/1830)
* [**ncm-metaconfig:** httpd: support requestheader in vhost](https://github.com/quattor/configuration-modules-core/pull/1816)
* [**ncm-metaconfig:** icinga-web: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1845)
* [**ncm-metaconfig:** irods: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1843)
* [**ncm-metaconfig:** kafka: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1798)
* [**ncm-metaconfig:** kerberos: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1844)
* [**ncm-metaconfig:** logstash: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1841)
* [**ncm-metaconfig:** named: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1785)
* [**ncm-metaconfig:** nginx: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1842)
* [**ncm-metaconfig:** openvpn: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1805)
* [**ncm-metaconfig:** prometheus: add metric_relabel_configs](https://github.com/quattor/configuration-modules-core/pull/1856)
* [**ncm-metaconfig:** rsyslog: Add condition support to all action types](https://github.com/quattor/configuration-modules-core/pull/1847)
* [**ncm-metaconfig:** rsyslog: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1804)
* [**ncm-metaconfig:** slurm: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1803)
* [**ncm-metaconfig:** ssh: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1802)
* [**ncm-metaconfig:** support Include for sshd_config](https://github.com/quattor/configuration-modules-core/pull/1851)
* [**ncm-metaconfig:** udev: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1839)
* [**ncm-metaconfig:** updated filebeat 7.x schema to fix #1728](https://github.com/quattor/configuration-modules-core/pull/1810)
* [**ncm-metaconfig:** xinetd: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1801)
* [**ncm-metaconfig:** zookeeper: Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1800)
* [**ncm-mysql:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1759)
* [**ncm-nagios:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1760)
* [**ncm-network:** Add support for IPv6 static routes to nmstate backend](https://github.com/quattor/configuration-modules-core/pull/1846)
* [**ncm-network:** dropin file support for main configuration of NetworkManager](https://github.com/quattor/configuration-modules-core/pull/1739)
* [**ncm-network:** nmstate support for adusting congestion window](https://github.com/quattor/configuration-modules-core/pull/1828)
* [**ncm-network:** support nmstate allowed route types](https://github.com/quattor/configuration-modules-core/pull/1786)
* [**ncm-openldap:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1761)
* [**ncm-openldap:** minimal support of mdb database](https://github.com/quattor/configuration-modules-core/pull/1824)
* [**ncm-opennebula:** Add FireEdge support](https://github.com/quattor/configuration-modules-core/pull/1855)
* [**ncm-opennebula:** Add cpu pinning support](https://github.com/quattor/configuration-modules-core/pull/1776)
* [**ncm-opennebula:** Add forecast conf for OpenNebula 7.x](https://github.com/quattor/configuration-modules-core/pull/1832)
* [**ncm-opennebula:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1762)
* [**ncm-opennebula:** add cpu overcommit ratio option](https://github.com/quattor/configuration-modules-core/pull/1737)
* [**ncm-opennebula:** add libvirt hw machine type option](https://github.com/quattor/configuration-modules-core/pull/1822)
* [**ncm-openstack:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1773)
* [**ncm-pam:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1772)
* [**ncm-pnp4nagios:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1771)
* [**ncm-postfix:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1770)
* [**ncm-postgresql:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1774)
* [**ncm-postgresql:** Make pg_version mandatory in schema](https://github.com/quattor/configuration-modules-core/pull/1857)
* [**ncm-profile:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1780)
* [**ncm-puppet:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1768)
* [**ncm-shorewall:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1769)
* [**ncm-spma:**  fix to retain rpms listed in whitelist path](https://github.com/quattor/configuration-modules-core/pull/1807)
* [**ncm-spma:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1790)
* [**ncm-spma:** support for ssl client settings for yumng and dnf backend.](https://github.com/quattor/configuration-modules-core/pull/1852)
* [**ncm-ssh:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1767)
* [**ncm-sudo:** Add support for use_pty with sudoers](https://github.com/quattor/configuration-modules-core/pull/1742)
* [**ncm-sudo:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1766)
* [**ncm-syslog:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1765)
* [**ncm-syslogng:** Fix wrapping and indentation in pan](https://github.com/quattor/configuration-modules-core/pull/1781)
* [**ncm-systemd:** Cleanup pan templates](https://github.com/quattor/configuration-modules-core/pull/1789)
* [**ncm-systemd:** More schema cleanup](https://github.com/quattor/configuration-modules-core/pull/1840)
* [**ncm-systemd:** ensure unit property is defined](https://github.com/quattor/configuration-modules-core/pull/1788)
* [**ncm-systemd:** template slice units will not have their state forced](https://github.com/quattor/configuration-modules-core/pull/1815)

### ncm-lib-blockdevices
* [**github/workflows:** Build packages and upload as artifacts](https://github.com/quattor/ncm-lib-blockdevices/pull/112)
* [option to always use device path for mounts instead of uuid](https://github.com/quattor/ncm-lib-blockdevices/pull/111)

### template-library-standard
* [Reuse shared workflows to run tests](https://github.com/quattor/template-library-standard/pull/177)
* [Update AMD EPYC CPUs](https://github.com/quattor/template-library-standard/pull/168)
* [**hardware/cpu:** Add Ampere Altra Max CPUs](https://github.com/quattor/template-library-standard/pull/169)
* [**hardware/cpu:** Add Intel Xeon CPUs from 2018](https://github.com/quattor/template-library-standard/pull/170)
* [**hardware/cpu:** Add Intel Xeon CPUs from 2021](https://github.com/quattor/template-library-standard/pull/173)
* [**hardware/cpu:** Add Intel Xeon CPUs from 2022](https://github.com/quattor/template-library-standard/pull/174)
* [**hardware/cpu:** Add Intel Xeon CPUs from 2023](https://github.com/quattor/template-library-standard/pull/175)
* [**hardware/cpu:** Add Intel Xeon CPUs from 2024](https://github.com/quattor/template-library-standard/pull/176)
* [**hardware/cpu:** Add/update Intel Xeon CPUs from 2019](https://github.com/quattor/template-library-standard/pull/171)
* [**hardware/cpu:** Add/update Intel Xeon CPUs from 2020](https://github.com/quattor/template-library-standard/pull/172)

### template-library-grid
* [Remove references to PBS knownhosts](https://github.com/quattor/template-library-grid/pull/251)
* [Reuse shared workflows to run tests](https://github.com/quattor/template-library-grid/pull/253)
* [**workflows:** Add missing colorama dependency for indent checker](https://github.com/quattor/template-library-grid/pull/250)

### ncm-ncd
* [Reuse shared workflow to run all standard tests](https://github.com/quattor/ncm-ncd/pull/141)

### CCM
* [**ProfileCache:** Include type in checksum calculation](https://github.com/quattor/CCM/pull/216)
* [Remove description field](https://github.com/quattor/CCM/pull/215)
* [Reuse shared workflows to run tests](https://github.com/quattor/CCM/pull/218)
* [Strip out all references to derivation](https://github.com/quattor/CCM/pull/214)

### template-library-os
* [Reuse shared workflows to run tests](https://github.com/quattor/template-library-os/pull/113)
* [**el8/9:** Make architecture independent](https://github.com/quattor/template-library-os/pull/111)

### template-library-openstack
* [Reuse shared workflows to run tests](https://github.com/quattor/template-library-openstack/pull/64)
* [Templates for OpenStack Antelope version](https://github.com/quattor/template-library-openstack/pull/63)

### aii
* [Remove legacy aii-dhcp script](https://github.com/quattor/aii/pull/359)
* [Reuse shared workflows to run tests](https://github.com/quattor/aii/pull/358)
* [**aii-dhcp:** support optional hostname ip verification](https://github.com/quattor/aii/pull/299)
* [**aii-ks:** Only wait for 120 seconds in wait_for_network](https://github.com/quattor/aii/pull/360)
* [**aii-pxelinux:** make ramdisk_size configurable](https://github.com/quattor/aii/pull/356)

### release
* [**Dockerfile:** "master" branches are now called "main"](https://github.com/quattor/release/pull/371)
* [Fix CI test in get-template-library](https://github.com/quattor/release/pull/377)
* [Update template library scripts for new repository structure](https://github.com/quattor/release/pull/370)
* [Update tooling to reflect changes to repository branching](https://github.com/quattor/release/pull/379)
* [**github/workflows:** Build packages and upload as artifacts](https://github.com/quattor/release/pull/376)
* [**releaser:** Fix various code smells](https://github.com/quattor/release/pull/355)
* [**workflows:** Allow use of maven templates in pan files](https://github.com/quattor/release/pull/378)

### configuration-modules-grid
* [Reuse shared workflow to run all standard tests](https://github.com/quattor/configuration-modules-grid/pull/157)
* [**ncm-lbconfig:** Remove obsolete component](https://github.com/quattor/configuration-modules-grid/pull/155)
* [**ncm-pbsknownhosts:** Remove obsolete component](https://github.com/quattor/configuration-modules-grid/pull/154)

### cdp-listend
* [Reuse shared workflows to run tests](https://github.com/quattor/cdp-listend/pull/37)

### CAF
* [Reuse shared workflows to run tests](https://github.com/quattor/CAF/pull/283)

### template-library-examples
* [Remove legacy repositories](https://github.com/quattor/template-library-examples/pull/44)
* [Reuse shared workflows to run tests](https://github.com/quattor/template-library-examples/pull/45)
* [Update the OS version definition for each server](https://github.com/quattor/template-library-examples/pull/42)
