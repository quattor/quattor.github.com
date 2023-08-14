---
layout: article
title: Quattor 23.6.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/23.6.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed. This release has been a long time coming and is suitably huge — we've merged 125 pull requests and resolved 17 issues.

Take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on next.


Backwards Incompatible Changes
------------------------------

### configuration-modules-core
* [**ncm-ceph:** Add support for orchestrator/cephadm under octopus](https://github.com/quattor/configuration-modules-core/pull/1490)
* [**ncm-ipmi:** Enhancements to IPMI module](https://github.com/quattor/configuration-modules-core/pull/1546)

### template-library-grid
* [Puppet cleanup](https://github.com/quattor/template-library-grid/pull/236)

### aii
* [**aii-ks:** generate kickstart repo entries based on SPMA configuration](https://github.com/quattor/aii/pull/316)

### cdp-listend
* [Use a standard location for scripts](https://github.com/quattor/cdp-listend/pull/26)

Changelog
---------

### ncm-query
* [add github action for tests](https://github.com/quattor/ncm-query/pull/14)

### LC
* [Make project name consistent with other repos and add RPM description](https://github.com/quattor/LC/pull/18)

### ncm-cdispd
* [Add RPM dependency on crontabs and logrotate](https://github.com/quattor/ncm-cdispd/pull/58)
* [Add github action for tests](https://github.com/quattor/ncm-cdispd/pull/57)

### template-library-core
* [**AII KS:** use the base OS repository template to configure the AII urls](https://github.com/quattor/template-library-core/pull/211)
* [Add a transitional type for strings being migrated to lists of strings](https://github.com/quattor/template-library-core/pull/212)
* [Cleanup blockdevices template](https://github.com/quattor/template-library-core/pull/215)
* [Cleanup filesystems template](https://github.com/quattor/template-library-core/pull/216)
* [Don't specific minor Python 3 version for checks](https://github.com/quattor/template-library-core/pull/217)
* [Fix type of ntpd_tinker_options/step #219](https://github.com/quattor/template-library-core/pull/220)
* [New function lvo_add to add lv options](https://github.com/quattor/template-library-core/pull/214)
* [New type for strings which represent lists of email addresses](https://github.com/quattor/template-library-core/pull/213)
* [add support for proc filesystem (and dummy proc blockdevice)](https://github.com/quattor/template-library-core/pull/207)
* [update actions to latest version](https://github.com/quattor/template-library-core/pull/218)

### configuration-modules-core
* [**CI:** fix hash key for m2 cache](https://github.com/quattor/configuration-modules-core/pull/1549)
* [Don't specify Python 3 minor version](https://github.com/quattor/configuration-modules-core/pull/1563)
* [Only search for the parent POM in Maven repositories](https://github.com/quattor/configuration-modules-core/pull/1612)
* [Update build-tools to 1.62 release (latest)](https://github.com/quattor/configuration-modules-core/pull/1602)
* [avoid warnings in github action run](https://github.com/quattor/configuration-modules-core/pull/1562)
* [**kafka & hnormalise:** Add and fix tests](https://github.com/quattor/configuration-modules-core/pull/1605)
* [**metaconfig:** add minor local leftovers changes](https://github.com/quattor/configuration-modules-core/pull/1581)
* [**metaconfig:** haproxy: tunnel timeout settings](https://github.com/quattor/configuration-modules-core/pull/1555)
* [**metaconfig:** named: support per zone forwarding](https://github.com/quattor/configuration-modules-core/pull/1516)
* [**ncm-authconfig:** sssd: add some more ipa configurables](https://github.com/quattor/configuration-modules-core/pull/1536)
* [**ncm-autofs:** Schema updates](https://github.com/quattor/configuration-modules-core/pull/1410)
* [**ncm-ceph:** Add support for orchestrator/cephadm under octopus](https://github.com/quattor/configuration-modules-core/pull/1490)
* [**ncm-chkconfig:** ensure that the services property doesn't remain undefined](https://github.com/quattor/configuration-modules-core/pull/1550)
* [**ncm-cron:** Use numeric comparison operator](https://github.com/quattor/configuration-modules-core/pull/1590)
* [**ncm-dirperm:** fix the wrong variable which causes confusion on error display ](https://github.com/quattor/configuration-modules-core/pull/1607)
* [**ncm-freeipa:** support freeipa 4.7](https://github.com/quattor/configuration-modules-core/pull/1403)
* [**ncm-grub:** provide alternative way to set kernel args](https://github.com/quattor/configuration-modules-core/pull/1540)
* [**ncm-hostsfile:** Test IPv6 and dual stack localhosts](https://github.com/quattor/configuration-modules-core/pull/1571)
* [**ncm-ipmi:** Enhancements to IPMI module](https://github.com/quattor/configuration-modules-core/pull/1546)
* [**ncm-metaconfig/httpd:** Don't render negate if set](https://github.com/quattor/configuration-modules-core/pull/1541)
* [**ncm-metaconfig:**  Support all combinations of udev rule creation](https://github.com/quattor/configuration-modules-core/pull/1518)
* [**ncm-metaconfig:** Add service action condrestart](https://github.com/quattor/configuration-modules-core/pull/1551)
* [**ncm-metaconfig:** add basic pakiti3 server config](https://github.com/quattor/configuration-modules-core/pull/1548)
* [**ncm-metaconfig:** add lvm_conf config support](https://github.com/quattor/configuration-modules-core/pull/1573)
* [**ncm-metaconfig:** add missing kafka options](https://github.com/quattor/configuration-modules-core/pull/1556)
* [**ncm-metaconfig:** add missing zookeeper 4lw options](https://github.com/quattor/configuration-modules-core/pull/1557)
* [**ncm-metaconfig:** beat schema for 7.0+ with kafka output support](https://github.com/quattor/configuration-modules-core/pull/1483)
* [**ncm-metaconfig:** beats: Remove trailing comma in choice](https://github.com/quattor/configuration-modules-core/pull/1610)
* [**ncm-metaconfig:** fix GresTypes in slurm config](https://github.com/quattor/configuration-modules-core/pull/1510)
* [**ncm-metaconfig:** generic: add multiline_exact module (avoids spurious newline)](https://github.com/quattor/configuration-modules-core/pull/1542)
* [**ncm-metaconfig:** haproxy: support frontend errorfile and use_backend](https://github.com/quattor/configuration-modules-core/pull/1539)
* [**ncm-metaconfig:** httpd: Add carevocationcheck configuration option](https://github.com/quattor/configuration-modules-core/pull/1537)
* [**ncm-metaconfig:** httpd: oidc: add OIDCStateMaxNumberOfCookies support](https://github.com/quattor/configuration-modules-core/pull/1561)
* [**ncm-metaconfig:** httpd: support expires](https://github.com/quattor/configuration-modules-core/pull/1543)
* [**ncm-metaconfig:** jaas configuration file support](https://github.com/quattor/configuration-modules-core/pull/1547)
* [**ncm-metaconfig:** kafka broker settings schema for 2.4](https://github.com/quattor/configuration-modules-core/pull/1438)
* [**ncm-metaconfig:** schema changes for kibana 8.1](https://github.com/quattor/configuration-modules-core/pull/1545)
* [**ncm-metaconfig:** schema updates and tests for elasticsearch 8.1](https://github.com/quattor/configuration-modules-core/pull/1544)
* [**ncm-metaconfig:** udev: Restore missing bind and prefix](https://github.com/quattor/configuration-modules-core/pull/1613)
* [**ncm-metaconfig:** version the slurm schema and add support for 21.08 and 23.02](https://github.com/quattor/configuration-modules-core/pull/1528)
* [**ncm-metaconfig:** xinetd: add log_on_success and log_on_failure](https://github.com/quattor/configuration-modules-core/pull/1413)
* [**ncm-metaconfig:** zookeeper: fix 4lw options to a list of choice](https://github.com/quattor/configuration-modules-core/pull/1608)
* [**ncm-modprobe:** Change mkinitrd references to dracut](https://github.com/quattor/configuration-modules-core/pull/1578)
* [**ncm-network:** fix gso hash mapping](https://github.com/quattor/configuration-modules-core/pull/1589)
* [**ncm-network:** fix typos and updated comments](https://github.com/quattor/configuration-modules-core/pull/1611)
* [**ncm-network:** nmstate support for configuring  dummy interfaces](https://github.com/quattor/configuration-modules-core/pull/1614)
* [**ncm-network:** support for managing network using nmstate](https://github.com/quattor/configuration-modules-core/pull/1601)
* [**ncm-nfs:** add lustre support](https://github.com/quattor/configuration-modules-core/pull/1530)
* [**ncm-ntpd:** Validate interface match option](https://github.com/quattor/configuration-modules-core/pull/1570)
* [**ncm-ntpd:** fix type of ntpd_tinker_options/step #1600](https://github.com/quattor/configuration-modules-core/pull/1599)
* [**ncm-shorewall:** add docker support](https://github.com/quattor/configuration-modules-core/pull/1616)
* [**ncm-shorewall:** support audit in shorewall/iptables](https://github.com/quattor/configuration-modules-core/pull/1597)
* [**ncm-spma:** apt: Finish implementation](https://github.com/quattor/configuration-modules-core/pull/1258)
* [**ncm-spma:** dnf support for enabling module streams](https://github.com/quattor/configuration-modules-core/pull/1558)
* [**ncm-spma:** enhance dnf provider to allow update to newer streams.](https://github.com/quattor/configuration-modules-core/pull/1576)
* [**ncm-spma:** fix dnf provider not to remove running kernel](https://github.com/quattor/configuration-modules-core/pull/1572)
* [**ncm-ssh:** add option prohibit-password to PermitRootLogin parameter](https://github.com/quattor/configuration-modules-core/pull/1604)
* [**ncm-sudo:** fix documentation typo](https://github.com/quattor/configuration-modules-core/pull/1574)
* [**ncm-syslogng:** Add deprecation warning to schema](https://github.com/quattor/configuration-modules-core/pull/1568)
* [**ncm-systemd:** Add path support](https://github.com/quattor/configuration-modules-core/pull/1583)
* [**ncm-systemd:** All Exec* options can be lists of strings](https://github.com/quattor/configuration-modules-core/pull/1567)
* [**ncm-systemd:** add support for slice and more resource control](https://github.com/quattor/configuration-modules-core/pull/1582)
* [**ncm-systemd:** all pre and post exec commands now take a list instead of a string](https://github.com/quattor/configuration-modules-core/pull/1464)
* [**tests:** run go-offline in gh pipeline](https://github.com/quattor/configuration-modules-core/pull/1598)
* [**workflows:** Fully move travis-build into panlint](https://github.com/quattor/configuration-modules-core/pull/1591)
* [**workflows:** Run unit tests on EL8](https://github.com/quattor/configuration-modules-core/pull/1593)

### ncm-lib-blockdevices
* [Add github action for tests](https://github.com/quattor/ncm-lib-blockdevices/pull/98)
* [Fix regex tests to reflect changes in line format](https://github.com/quattor/ncm-lib-blockdevices/pull/99)
* [**MD:** Don't specify chunk size when RAID level is 1](https://github.com/quattor/ncm-lib-blockdevices/pull/97)
* [**MD:** raid_level is a string](https://github.com/quattor/ncm-lib-blockdevices/pull/101)
* [add dummy blockdevice, and inherited Tmpfs and Proc](https://github.com/quattor/ncm-lib-blockdevices/pull/94)

### template-library-standard
* [Add support for configuring podman](https://github.com/quattor/template-library-standard/pull/148)
* [**CVMFS:** add HESS repository configuration](https://github.com/quattor/template-library-standard/pull/147)
* [Fix typo](https://github.com/quattor/template-library-standard/pull/145)
* [**Pakiti client:** manage the configuration](https://github.com/quattor/template-library-standard/pull/149)
* [Various filesystem-related updates I had lying around](https://github.com/quattor/template-library-standard/pull/130)
* [**features/docker:** add support for EL8 and for adding an extra YUM repository](https://github.com/quattor/template-library-standard/pull/144)
* [**features/fetch-crl:** add support for EL8](https://github.com/quattor/template-library-standard/pull/146)
* [machine-types/core refactoring to make it more flexible](https://github.com/quattor/template-library-standard/pull/140)
* [support for muti options settings for logical volumes](https://github.com/quattor/template-library-standard/pull/151)

### template-library-grid
* [Puppet cleanup](https://github.com/quattor/template-library-grid/pull/236)
* [machines-types update based on new standard/machine-types/core](https://github.com/quattor/template-library-grid/pull/241)

### ncm-ncd
* [Document wrapper commands and require logrotate](https://github.com/quattor/ncm-ncd/pull/134)
* [add github action for tests](https://github.com/quattor/ncm-ncd/pull/133)
* [**test/perl/cli:** Don't check failed component order](https://github.com/quattor/ncm-ncd/pull/136)

### CCM
* [Add RPM dependency on crontabs and logrotate](https://github.com/quattor/CCM/pull/208)
* [Add github action for tests](https://github.com/quattor/CCM/pull/207)
* [Document quattor-fetch alias](https://github.com/quattor/CCM/pull/209)
* [perltidy complain about operator present in possible arg for destination](https://github.com/quattor/CCM/pull/205)

### template-library-os
* [Add a template to configure Java on EL8, selecting the appropriate ve…](https://github.com/quattor/template-library-os/pull/104)
* [**EL8 firewalld:** force installation of iptables dependency](https://github.com/quattor/template-library-os/pull/101)
* [**EL8:** improved support for configuring AII install URL](https://github.com/quattor/template-library-os/pull/102)
* [Ensure that ncm-systemd process service entries](https://github.com/quattor/template-library-os/pull/103)

### aii
* [Add github action for tests](https://github.com/quattor/aii/pull/336)
* [**UEFI boot order definition:** set the device currently booted as the first entry](https://github.com/quattor/aii/pull/340)
* [**aii-core:** Binaries and Perl modules are not documentation](https://github.com/quattor/aii/pull/337)
* [**aii-ks:** fix regexp for UEFI PXE boot entry match](https://github.com/quattor/aii/pull/335)
* [**aii-ks:** generate kickstart repo entries based on SPMA configuration](https://github.com/quattor/aii/pull/316)

### release
* [Add script to build packages from a specific tag](https://github.com/quattor/release/pull/338)
* [Convert plenary_template_library to python3](https://github.com/quattor/release/pull/341)
* [Fix various issues with packager script](https://github.com/quattor/release/pull/346)
* [Support rpmlint 2.4](https://github.com/quattor/release/pull/342)
* [**quattor-repo:** Releases have repositories for major EL versions](https://github.com/quattor/release/pull/343)

### configuration-modules-grid
* [Add workflows for unit tests and panlint](https://github.com/quattor/configuration-modules-grid/pull/145)
* [Only search for the parent POM in Maven repositories](https://github.com/quattor/configuration-modules-grid/pull/148)
* [Override RPM URL to correct path](https://github.com/quattor/configuration-modules-grid/pull/146)
* [Update build-tools to 1.62 release (latest)](https://github.com/quattor/configuration-modules-grid/pull/147)

### cdp-listend
* [Add RPM dependency on crontabs and logrotate](https://github.com/quattor/cdp-listend/pull/25)
* [Use a standard location for scripts](https://github.com/quattor/cdp-listend/pull/26)
* [add github action for tests](https://github.com/quattor/cdp-listend/pull/24)

### CAF
* [Make project name consistent with other repos and add RPM description](https://github.com/quattor/CAF/pull/276)
