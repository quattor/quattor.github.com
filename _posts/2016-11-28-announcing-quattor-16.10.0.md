---
layout: article
title: Quattor 16.10.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/16.10.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 126 pull requests and resolved 68 issues.

The next release should be 16.12.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### configuration-modules-core
* [**ncm-opennebula:** Use resource dictionaries instead of lists](https://github.com/quattor/configuration-modules-core/pull/888)
* [**ncm-spma:** Refactor schema and only include relevant types](https://github.com/quattor/configuration-modules-core/pull/716)

### CCM
* [ccm-fetch report changed profile](https://github.com/quattor/CCM/pull/122)

### configuration-modules-grid
* [**ncm-maui:** cleanup](https://github.com/quattor/configuration-modules-grid/pull/117)

Changelog
---------

### template-library-core
* [Fix tests](https://github.com/quattor/template-library-core/pull/133)
* [Improved interface for partitions_add()](https://github.com/quattor/template-library-core/pull/126)
* [Make monitoring optional](https://github.com/quattor/template-library-core/pull/125)
* [Preferred console should not be mandatory](https://github.com/quattor/template-library-core/pull/128)
* [**functions/package:** add a comment/description to pkg_compare_version funciton](https://github.com/quattor/template-library-core/pull/131)
* [**types/metadata:** add optional id and timestamp to the branch_type](https://github.com/quattor/template-library-core/pull/127)

### template-library-openstack
* [Add memcache server for horizon](https://github.com/quattor/template-library-openstack/pull/16)
* [Add openvswitch + other fixes](https://github.com/quattor/template-library-openstack/pull/21)
* [Additional ha config](https://github.com/quattor/template-library-openstack/pull/15)
* [Fix OPENSTACK_MEMCACHE_HOSTS variable name](https://github.com/quattor/template-library-openstack/pull/29)
* [Fix OS_MEMCACHE_HOSTS variable name](https://github.com/quattor/template-library-openstack/pull/26)
* [Generalise HA Specific config.](https://github.com/quattor/template-library-openstack/pull/37)
* [Horizon tweaks](https://github.com/quattor/template-library-openstack/pull/40)
* [Keepalived virtual router ID](https://github.com/quattor/template-library-openstack/pull/19)
* [Logging changes](https://github.com/quattor/template-library-openstack/pull/41)
* [Mitaka](https://github.com/quattor/template-library-openstack/pull/17)
* [Mitaka nova api](https://github.com/quattor/template-library-openstack/pull/18)
* [More flexible keystone wsgi](https://github.com/quattor/template-library-openstack/pull/23)
* [Rename variables](https://github.com/quattor/template-library-openstack/pull/22)
* [Revert "Add mongodb user as kept_users"](https://github.com/quattor/template-library-openstack/pull/32)
* [Update keystone authentication to take into account changes in Mitaka](https://github.com/quattor/template-library-openstack/pull/20)

### configuration-modules-core
* [Add configuration options for new features in ceph jewel:](https://github.com/quattor/configuration-modules-core/pull/938)
* [**metaconfig:** service ncm-ncd: add new config options](https://github.com/quattor/configuration-modules-core/pull/948)
* [**ncm-accounts, ncm-amandaserver, ncm-cups, ncm-iptables, ncm-nscd:** Use legacy type for simple yes/no strings](https://github.com/quattor/configuration-modules-core/pull/956)
* [**ncm-accounts:** Add users and groups used by RabbitMQ, Memcached and MongoDB](https://github.com/quattor/configuration-modules-core/pull/935)
* [**ncm-aiiserver:** do not add (empty) attributes for unused CCM properties](https://github.com/quattor/configuration-modules-core/pull/971)
* [**ncm-aiiserver:** support changing cachedir and some cleanup](https://github.com/quattor/configuration-modules-core/pull/828)
* [**ncm-ccm:** support purge_time config setting.](https://github.com/quattor/configuration-modules-core/pull/922)
* [**ncm-download:** fix GSSAPI on GET requests.](https://github.com/quattor/configuration-modules-core/pull/921)
* [**ncm-download:** fix proxy handling.](https://github.com/quattor/configuration-modules-core/pull/923)
* [**ncm-fstab, ncm-filesystems:** pass logger to NCM::Blockdevices](https://github.com/quattor/configuration-modules-core/pull/946)
* [**ncm-fstab:** enable NoAction support.](https://github.com/quattor/configuration-modules-core/pull/916)
* [**ncm-gpfs:** add new hdfs-protocol package to GPFSRPMS](https://github.com/quattor/configuration-modules-core/pull/895)
* [**ncm-metaconfig:** Include opennebula aii conf](https://github.com/quattor/configuration-modules-core/pull/788)
* [**ncm-metaconfig:** device-mapper: fix for parse errors in multipath.conf](https://github.com/quattor/configuration-modules-core/pull/920)
* [**ncm-metaconfig:** hadoop config](https://github.com/quattor/configuration-modules-core/pull/880)
* [**ncm-metaconfig:** libvirtd include support to setup VM domains](https://github.com/quattor/configuration-modules-core/pull/919)
* [**ncm-metaconfig:** nginx fix ssl conf](https://github.com/quattor/configuration-modules-core/pull/884)
* [**ncm-opennebula:** Include OneFlow support](https://github.com/quattor/configuration-modules-core/pull/890)
* [**ncm-opennebula:** Use resource dictionaries instead of lists](https://github.com/quattor/configuration-modules-core/pull/888)
* [**ncm-opennebula:** config template cleanup](https://github.com/quattor/configuration-modules-core/pull/835)
* [**ncm-postgresql:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/904)
* [**ncm-profile:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/905)
* [**ncm-puppet:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/906)
* [**ncm-resolver:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/907)
* [**ncm-sendmail:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/908)
* [**ncm-spma:** Refactor schema and only include relevant types](https://github.com/quattor/configuration-modules-core/pull/716)
* [**ncm-spma:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/910)
* [**ncm-ssh:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/912)
* [**ncm-sudo:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/927)
* [**ncm-symlink:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/928)
* [**ncm-sysconfig:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/929)
* [**ncm-sysctl:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/930)
* [**ncm-syslog:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/931)
* [**ncm-syslogng:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/932)
* [**ncm-systemd:** Fix links where they should not be used](https://github.com/quattor/configuration-modules-core/pull/942)
* [**ncm-systemd:** unmask masked units before state change](https://github.com/quattor/configuration-modules-core/pull/965)
* [**ncm-useraccess:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/933)

### ncm-lib-blockdevices
* [**Filesystem.pm:** add support for vfat filesystems](https://github.com/quattor/ncm-lib-blockdevices/pull/72)
* [Make it possible to pass a logger to NCM::Blockdevices](https://github.com/quattor/ncm-lib-blockdevices/pull/70)
* [fix path for parted on EL6](https://github.com/quattor/ncm-lib-blockdevices/pull/68)

### template-library-standard
* [Add new CVMFS repository](https://github.com/quattor/template-library-standard/pull/71)
* [DML should not change a global variable directly](https://github.com/quattor/template-library-standard/pull/65)
* [**Security trust:** miscellaneous updates](https://github.com/quattor/template-library-standard/pull/87)
* [Update ca from 1.60 to 1.73 + Add debug info on ca repository](https://github.com/quattor/template-library-standard/pull/84)
* [cvmfs client improvements](https://github.com/quattor/template-library-standard/pull/78)
* [**cvmfs:** use PKG_VERSION_xxx to test pkg_compare_version() return values](https://github.com/quattor/template-library-standard/pull/90)
* [**fetch-crl:** use metaconfig instead of sysconfig](https://github.com/quattor/template-library-standard/pull/60)
* [**filesystem/config:** add support for configuring a biosboot partition (legacy BIOS or UEFI)](https://github.com/quattor/template-library-standard/pull/85)
* [get cvmfs-config-default for newer versions of cvmfs](https://github.com/quattor/template-library-standard/pull/83)
* [**perfsonar:** update (simplify) the RPM list](https://github.com/quattor/template-library-standard/pull/86)

### template-library-grid
* [**DPM:** use PKG_VERSION_xxx for testing pkg_compare_version() return value](https://github.com/quattor/template-library-grid/pull/184)

### ncm-ncd
* [**CLI:** get the NOQUATTOR constants from CCM::Fetch::Config](https://github.com/quattor/ncm-ncd/pull/95)
* [Collection of fixes for minor issues](https://github.com/quattor/ncm-ncd/pull/88)
* [**ComponentProxy:** untaint config version with version regex match](https://github.com/quattor/ncm-ncd/pull/79)
* [**ComponentProxyList:** set_state: improved reporting with empty message](https://github.com/quattor/ncm-ncd/pull/98)
* [Improved tabcompletion and CLI cleanup](https://github.com/quattor/ncm-ncd/pull/81)
* [**ncm-ncd:** fix typo in log message](https://github.com/quattor/ncm-ncd/pull/83)

### CCM
* [**Configuration:** add name](https://github.com/quattor/CCM/pull/137)
* [Correct cfgfile option in ccm-fetch and ccm-initialise pod](https://github.com/quattor/CCM/pull/141)
* [**Fetch:** fetchProfile pod: replace -1 with used $ERROR](https://github.com/quattor/CCM/pull/129)
* [**Fetch::Config:** export the NOQUATTOR constants](https://github.com/quattor/CCM/pull/136)
* [Remove directory of ancient documentation](https://github.com/quattor/CCM/pull/133)
* [Remove unused context and preprocessor options](https://github.com/quattor/CCM/pull/145)
* [**Syncfile:** cleanup unused code and remove any hint that something is (un)locked](https://github.com/quattor/CCM/pull/142)
* [**Textrender:** fix link which fails documentation build](https://github.com/quattor/CCM/pull/135)
* [**ccm-fetch and ccm-initialise:** log to file/syslog](https://github.com/quattor/CCM/pull/126)
* [ccm-fetch report changed profile](https://github.com/quattor/CCM/pull/122)
* [**ccm-fetch:** add missing CCM::Fetch](https://github.com/quattor/CCM/pull/140)
* [**ccm-fetch:** initCfg is required to get correct permissions](https://github.com/quattor/CCM/pull/139)
* [**ccm-fetch:** rephrase group_readable/world_readable config options](https://github.com/quattor/CCM/pull/147)
* [change default DB format to CDB_File](https://github.com/quattor/CCM/pull/144)
* [improve tabcompletion to support ncm-ncd](https://github.com/quattor/CCM/pull/130)

### template-library-os
* [Ensure that state of iptables and firewalld services are consistently defined](https://github.com/quattor/template-library-os/pull/84)
* [**el6.x:** Minor changes to some rpms templates](https://github.com/quattor/template-library-os/pull/80)
* [**rpms/quattor-development:** add perl-XML-Simple required by AII unit tests](https://github.com/quattor/template-library-os/pull/82)
* [**rpms/quattor-development:** add perl-XML-Simple required by AII unit tests](https://github.com/quattor/template-library-os/pull/81)

### aii
* [**.gitignore:** add IDE projet files](https://github.com/quattor/aii/pull/227)
* [Add pod syntax tests](https://github.com/quattor/aii/pull/215)
* [Allow components as userhooks](https://github.com/quattor/aii/pull/203)
* [**Shellfe:** Correct handling when fetchProfile returns an error](https://github.com/quattor/aii/pull/207)
* [**Shellfe:** report all perl warnings](https://github.com/quattor/aii/pull/221)
* [**aii-ks:** fix logging of pre and post script actions for EL7](https://github.com/quattor/aii/pull/218)
* [**aii-opennebula:** configure fix](https://github.com/quattor/aii/pull/205)
* [**ks:** schema: bonding is optional and best-effort when not defined](https://github.com/quattor/aii/pull/202)

### configuration-modules-grid
* [Remove ncm-gold component](https://github.com/quattor/configuration-modules-grid/pull/118)
* [Remove ncm-moab component, replaced by metaconfig service moab](https://github.com/quattor/configuration-modules-grid/pull/116)
* [**ncm-maui:** cleanup](https://github.com/quattor/configuration-modules-grid/pull/117)
* [**ncm-yaim:** clean up documentation](https://github.com/quattor/configuration-modules-grid/pull/120)
* [**ncm-yaim_userconf:** clean up documentation](https://github.com/quattor/configuration-modules-grid/pull/121)
* [remove ncm-yaim* components](https://github.com/quattor/configuration-modules-grid/pull/122)

### release
* [Fixes for build_all_repos](https://github.com/quattor/release/pull/265)
* [Use correct yum variables in repo definition](https://github.com/quattor/release/pull/261)

### ncm-cdispd
* [Improved handling of missing CPE](https://github.com/quattor/ncm-cdispd/pull/44)
* [Only touch statefiles for active, to be dispatched components](https://github.com/quattor/ncm-cdispd/pull/38)
* [Proper initialisation on ICLIST list of components](https://github.com/quattor/ncm-cdispd/pull/34)
* [Remove CDISPD::Utils custom escape](https://github.com/quattor/ncm-cdispd/pull/40)
* [**Utils:** use NCD::ComponentProxyList set_state function to set the statefile](https://github.com/quattor/ncm-cdispd/pull/43)
* [**ncm-cdispd:** add verbose_logfile](https://github.com/quattor/ncm-cdispd/pull/42)
* [**ncm-cdispd:** report sleep when no updated profile found with debug 1](https://github.com/quattor/ncm-cdispd/pull/46)

### CAF
* [**CAF:** Various fixes which fail documentation build](https://github.com/quattor/CAF/pull/192)
* [**Kerberos:** get a TGT using kinit as part of create_credential_cache](https://github.com/quattor/CAF/pull/196)
* [**Kerberos:** harden the logging of GSSAPI arguments](https://github.com/quattor/CAF/pull/193)
* [**Lock:** make sure the CAF::Reporter is usable when no log instance is passed](https://github.com/quattor/CAF/pull/195)
* [**Path:** untaint paths](https://github.com/quattor/CAF/pull/198)
* [**Reporter:** support VERBOSE_LOGFILE to always log verbose to logfile](https://github.com/quattor/CAF/pull/190)
