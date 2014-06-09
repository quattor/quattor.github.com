---
layout: article
title: Quattor 14.5.0 released
category: news
author: James Adams
modified: 2014-06-09
---

Another troublesome release cycle, but Quattor 14.5.0 has finally been released!

Once again this release incorporates a large number of changes, notably the introduction of configuration modules for Ceph and Puppet.

For the first time we have incorporated the template libraries in the release process, this should hopefully make upgrades much smoother for many sites.

Packages are available from our [yum repository](http://yum.quattor.org/14.5.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed!

The next release should be 14.6.0, exciting changes already lined up include EL7 support and Solaris support for ncm-cron.


Obsolete Components
-------------------
At the last workshop the following components were identified as being unmaintained and unused and so have been removed from configuration-modules-core.

In most cases their functionality has been superseeded by `ncm-metaconfig`

If you find that you are have a desperate need for one or more of them, speak up!

* `ncm-alternatives`
* `ncm-diskless_server`
* `ncm-drbd`
* `ncm-iscsitarget`
* `ncm-krb5clt`
* `ncm-linuxha`
* `ncm-mailaliases`
* `ncm-networkupstools`
* `ncm-oramonserver`
* `ncm-pacemaker`
* `ncm-pakiti`
* `ncm-php`
* `ncm-pine`
* `ncm-portmap`
* `ncm-pvss`
* `ncm-raidman`
* `ncm-rproxy`
* `ncm-runlevel`
* `ncm-selinux`
* `ncm-serialclient`
* `ncm-sindes_getcert`
* `ncm-slocate`
* `ncm-squid`
* `ncm-srvtab`
* `ncm-sshkeys`
* `ncm-state`
* `ncm-tftpd`
* `ncm-tomcat`
* `ncm-xen`
* `ncm-zephyrclt`


Changelog
---------

#### CAF
* [Revert whence exposure in CAF::FileWriter](https://github.com/quattor/CAF/pull/17).
* [Expose seek offset to add_or_replace_lines](https://github.com/quattor/CAF/pull/12).
* [Expose seek offset to add_or_replace_lines](https://github.com/quattor/CAF/pull/12).

#### CCM
* [LWP https fixes for EL7 support](https://github.com/quattor/CCM/pull/18).

#### LC
* [Revert "proper untainting of path"](https://github.com/quattor/LC/pull/5).
* [proper untainting of path variable in path_for_open](https://github.com/quattor/LC/pull/3).

#### aii
* [Add a --template-path option.](https://github.com/quattor/aii/pull/62).
* [Make Python 2.6 the default Python version to build for.](https://github.com/quattor/aii/pull/64).
* [Add a hook registering hosts into FreeIPA](https://github.com/quattor/aii/pull/63).
* [Allow AII to use netcat to send logfiles to kickstart syslog server](https://github.com/quattor/aii/pull/51).
* [Add more unittests to AII and start code refresh](https://github.com/quattor/aii/pull/58).
* [AII yum install post support glob](https://github.com/quattor/aii/pull/50).
* [AII removal of extra_packages and clarification of base_packages](https://github.com/quattor/aii/pull/57).
* [aii-ks: clean up usage of extra_packages vs. base_packages vs. packages](https://github.com/quattor/aii/pull/55).
* [Fix URL substitution on reverse proxies](https://github.com/quattor/aii/pull/48).
* [Remove notify and filter options, and all CDB dependencies](https://github.com/quattor/aii/pull/45).
* [Changes to aii-ks configuration for better integration with sl6.x and](https://github.com/quattor/aii/pull/40).

#### configuration-modules-core
* [ncm-spma: fix buggy config-rpm.pan (wrong prefix)](https://github.com/quattor/configuration-modules-core/pull/207).
* [unit tests: update ccm.cfg to use default DB format](https://github.com/quattor/configuration-modules-core/pull/204).
* [ncm-ntpd enhancements to make /etc/ntp.conf more configureable](https://github.com/quattor/configuration-modules-core/pull/197).
* [Ceph component fixes](https://github.com/quattor/configuration-modules-core/pull/206).
* [Remove component bloat](https://github.com/quattor/configuration-modules-core/pull/205).
* [Add test for correct handling of empty group set](https://github.com/quattor/configuration-modules-core/pull/203).
* [ncm-spma: deal with undef and empty groups](https://github.com/quattor/configuration-modules-core/pull/202).
* [devices fix and fixes after reinstall with journals on partitions](https://github.com/quattor/configuration-modules-core/pull/200).
* [Fix tests in ncm-authconfig.](https://github.com/quattor/configuration-modules-core/pull/199).
* [ncm-grub: Add support for configuring a console argument](https://github.com/quattor/configuration-modules-core/pull/163).
* [Fix bug in smear calculations and added test](https://github.com/quattor/configuration-modules-core/pull/196).
* [ncm-network requires net-tools (for ifconfig and route usage)](https://github.com/quattor/configuration-modules-core/pull/191).
* [Untaint the target variable to avoid unsecure dependency warnings while running ncm-symlink](https://github.com/quattor/configuration-modules-core/pull/192).
* [Skip malformed package names.](https://github.com/quattor/configuration-modules-core/pull/178).
* [ncm-puppet: fix tests](https://github.com/quattor/configuration-modules-core/pull/190).
* [ncm-aiiserver: use ncm-ccm configuration for https-related parameters](https://github.com/quattor/configuration-modules-core/pull/186).
* [Ncm puppet](https://github.com/quattor/configuration-modules-core/pull/167).
* [Fix ncm-aiiserver (missing osinstalldir and nbpdir, retrieval of some in...](https://github.com/quattor/configuration-modules-core/pull/183).
* [Retry the restart of nscd up to 3 times](https://github.com/quattor/configuration-modules-core/pull/179).
* [ncm-spma: partial package version resolution + include of config-common](https://github.com/quattor/configuration-modules-core/pull/174).
* [metaconfig: Restart daemons in Solaris, too](https://github.com/quattor/configuration-modules-core/pull/171).
* [filecopy: cast perms string to oct](https://github.com/quattor/configuration-modules-core/pull/166).
* [Fix typo in metaconfig documentation](https://github.com/quattor/configuration-modules-core/pull/162).
* [config.pan should include the common config](https://github.com/quattor/configuration-modules-core/pull/156).
* [Improve the error message when failing to lock a package](https://github.com/quattor/configuration-modules-core/pull/149).
* [ncm-accounts: add is_user_or_group function and 2 types defined_user and defined_group](https://github.com/quattor/configuration-modules-core/pull/155).
* [ncm-pam: only add the option key if the boolean is true](https://github.com/quattor/configuration-modules-core/pull/154).

#### configuration-modules-grid
* [ncm-xrootd: add support for managing rucioprefix directive](https://github.com/quattor/configuration-modules-grid/pull/13).
* [ncm-dpmlfc: add missing GLOBUS_THREAD_MODEL and 'export' modifier to sysconfig files](https://github.com/quattor/configuration-modules-grid/pull/15).
* [ncm-wmslb: reestablish ApacheLogLevel option used by the template library](https://github.com/quattor/configuration-modules-grid/pull/16).
* [ncm-dpmlfc: fix hash length comparison](https://github.com/quattor/configuration-modules-grid/pull/14).
* [unit tests: update ccm.cfg to use default DB format](https://github.com/quattor/configuration-modules-grid/pull/12).

#### ncm-lib-blockdevices
* [Fix volgroup_required handling.](https://github.com/quattor/ncm-lib-blockdevices/pull/29).
* [Fix bug due to missing newline on fstab entries](https://github.com/quattor/ncm-lib-blockdevices/pull/27).
* [Force filesystemtype](https://github.com/quattor/ncm-lib-blockdevices/pull/19).
* [Remove SL4 support by fixing the parted units to use MB](https://github.com/quattor/ncm-lib-blockdevices/pull/21).
* [Use the newest&greatest build tools.](https://github.com/quattor/ncm-lib-blockdevices/pull/22).
* [More unittest fixes](https://github.com/quattor/ncm-lib-blockdevices/pull/18).
* [Fix unittests](https://github.com/quattor/ncm-lib-blockdevices/pull/16).

#### ncm-ncd
* [Run ncm-ncd in a chrooted environment.](https://github.com/quattor/ncm-ncd/pull/21).
* [/var/lock and /var/run are volatile on EL7](https://github.com/quattor/ncm-ncd/pull/17).

#### template-library-core
* [Update README to match recent evolutions.](https://github.com/quattor/template-library-core/pull/47).
* [correct prefix for packages](https://github.com/quattor/template-library-core/pull/45).
* [Add function copy_network_params used by standard network configuration](https://github.com/quattor/template-library-core/pull/39).
* [Fix AII server configuration](https://github.com/quattor/template-library-core/pull/37).
* [Quattor client rpms: remove usage of extra_packages](https://github.com/quattor/template-library-core/pull/41).
* [Fix repository_config() to avoid overriding already defined repository parameters](https://github.com/quattor/template-library-core/pull/35).
* [Add JSON profile support (variable QUATTOR_PROFILE_FORMAT)](https://github.com/quattor/template-library-core/pull/32).

#### template-library-grid
* [EMI2 VOMS server certificate update](https://github.com/quattor/template-library-grid/pull/41).
* [Changes for EMI-3 accounting support](https://github.com/quattor/template-library-grid/pull/25).
* [EMI-2 Update 23](https://github.com/quattor/template-library-grid/pull/21).
* [Merge request from Pansanel:master](https://github.com/quattor/template-library-grid/pull/17).
* [Add EMI-3 APEL into EMI-2 (required for a smooth accounting transition)](https://github.com/quattor/template-library-grid/pull/16).
* [Misc. changes to improve compatibility with YUM-based deployment and](https://github.com/quattor/template-library-grid/pull/13).
* [EMI-2 updates from Pansanel trunk](https://github.com/quattor/template-library-grid/pull/12).
* [EMI-3: fixes for standard BDII_site + updates](https://github.com/quattor/template-library-grid/pull/2).
* [Fixes for CE gip](https://github.com/quattor/template-library-grid/pull/9).
* [Fixes for CE gip](https://github.com/quattor/template-library-grid/pull/10).
* [EMI-3 updates from Pansanel trunk](https://github.com/quattor/template-library-grid/pull/8).
* [EMI-2: several fixes and updates](https://github.com/quattor/template-library-grid/pull/1).
* [EMI-3 WN, DPM_disk and BDII with Yum based SPMA](https://github.com/quattor/template-library-grid/pull/7).
* [New EMI-2 update version: 22](https://github.com/quattor/template-library-grid/pull/6).
* [EMI-2 updates from Pansanel trunk](https://github.com/quattor/template-library-grid/pull/5).
* [Add the ability to switch off the creation of symlink](https://github.com/quattor/template-library-grid/pull/4).
* [Emi 3](https://github.com/quattor/template-library-grid/pull/3).
* [EMI-3: fixes for standard BDII_site + updates](https://github.com/quattor/template-library-grid/pull/2).
* [EMI-2: several fixes and updates](https://github.com/quattor/template-library-grid/pull/1).

#### template-library-os
* [Add ability to do base network configuration as part of the OS configuration](https://github.com/quattor/template-library-os/pull/40).
* [Add a few feature RPM list](https://github.com/quattor/template-library-os/pull/37).
* [Sl5.x x86 64](https://github.com/quattor/template-library-os/pull/35).
* [Fix openafs-client RPM list](https://github.com/quattor/template-library-os/pull/34).
* [Do not define /system/kernel/version, let standard templates do it.](https://github.com/quattor/template-library-os/pull/32).
* [Sl640 x86 64 spma](https://github.com/quattor/template-library-os/pull/19).
* [Sl630 x86 64 spma](https://github.com/quattor/template-library-os/pull/18).
* [Draft templates for sl6.x-x86_64](https://github.com/quattor/template-library-os/pull/16).
* [Draft templates for sl5.x-x86_64](https://github.com/quattor/template-library-os/pull/15).
* [Revert, wrong branch](https://github.com/quattor/template-library-os/pull/14).
* [Sl640 x86 64 spma](https://github.com/quattor/template-library-os/pull/13).
* [Update RPM version of Nagios; remove lal specific plugin](https://github.com/quattor/template-library-os/pull/12).
* [Add EMI-3.0 os config](https://github.com/quattor/template-library-os/pull/11).
* [Draft templates for sl5.x-x86_64](https://github.com/quattor/template-library-os/pull/9).
* [Misc. changes to SL4.7 32-bit templates](https://github.com/quattor/template-library-os/pull/1).
* [Sl630 x86 64 spma](https://github.com/quattor/template-library-os/pull/8).
* [Misc. changes to SL6.2 OS templates (+ LAL specific templates removed)](https://github.com/quattor/template-library-os/pull/7).
* [Misc. changes to SL 5.8 templates](https://github.com/quattor/template-library-os/pull/6).
* [Misc. changes to SL5.7 32-bit templates](https://github.com/quattor/template-library-os/pull/5).
* [Misc. changes to SL5.6 templates](https://github.com/quattor/template-library-os/pull/4).
* [Misc. changes to SL5.5 templates](https://github.com/quattor/template-library-os/pull/3).
* [Misc. changes to SL4.7 64-bit templates](https://github.com/quattor/template-library-os/pull/2).
