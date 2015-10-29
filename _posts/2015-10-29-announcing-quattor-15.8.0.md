---
layout: article
title: Quattor 15.8.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/15.8.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 119 pull requests and resolved 43 issues.

Take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Main New Features and Fixes
---------------------------

Known issues
------------

Changelog
---------

### template-library-core
* [Add missing types required to support aquilon](https://github.com/quattor/template-library-core/pull/70)
* [Add script as primitive template test](https://github.com/quattor/template-library-core/pull/86)
* [Deprecate shipping of component code in profiles](https://github.com/quattor/template-library-core/pull/74)
* [Distinguish between IPv4 and IPv6 networks](https://github.com/quattor/template-library-core/pull/83)
* [Fix problems with is_network_name and related functions](https://github.com/quattor/template-library-core/pull/82)
* [Fix typo in function name](https://github.com/quattor/template-library-core/pull/81)
* [is_fqdn: only match FULLY QUALIFIED domain names](https://github.com/quattor/template-library-core/pull/76)
* [quattor/types/aii: add missing pxelinux hooks](https://github.com/quattor/template-library-core/pull/77)

### template-library-examples
* [OpenNebula: centos6 package list fix and new shared DS example](https://github.com/quattor/template-library-examples/pull/27)

### ncm-cdispd
* [Remove the execute bit from some docs and config](https://github.com/quattor/ncm-cdispd/pull/21)

### configuration-modules-core
* [Remove config-xml from components](https://github.com/quattor/configuration-modules-core/pull/553)
* [ncm-authconfig: add sssd nss memcache_timeout option](https://github.com/quattor/configuration-modules-core/pull/516)
* [ncm-authconfig: correct module regexp for pamadditions entry attribute](https://github.com/quattor/configuration-modules-core/pull/557)
* [ncm-autofs: cleanup code, add unittests and support autofs.conf via TT](https://github.com/quattor/configuration-modules-core/pull/530)
* [ncm-ccm: add tabcompletion option](https://github.com/quattor/configuration-modules-core/pull/561)
* [ncm-ccm: change profile_failover from hostURI to hostURI[].](https://github.com/quattor/configuration-modules-core/pull/554)
* [ncm-ccm: do not use stdin for testing with ccm-fetch](https://github.com/quattor/configuration-modules-core/pull/598)
* [ncm-ccm: use --cfgfile instead of -cfgfile to test new config file](https://github.com/quattor/configuration-modules-core/pull/594)
* [ncm-ceph: Extend schema with rgw options, and spread over multiple files](https://github.com/quattor/configuration-modules-core/pull/550)
* [ncm-ceph: Only check ceph-deploy version on deployhost](https://github.com/quattor/configuration-modules-core/pull/537)
* [ncm-ceph: various additions](https://github.com/quattor/configuration-modules-core/pull/520)
* [ncm-download timeouts](https://github.com/quattor/configuration-modules-core/pull/532)
* [ncm-fsprobe: Remove ncm-fsprobe](https://github.com/quattor/configuration-modules-core/pull/556)
* [ncm-iptables: use secure temporary file from File::Temp](https://github.com/quattor/configuration-modules-core/pull/566)
* [ncm-metaconfig: Fix fqdn issues](https://github.com/quattor/configuration-modules-core/pull/582)
* [ncm-metaconfig: add ganesha 2.2 support](https://github.com/quattor/configuration-modules-core/pull/518)
* [ncm-metaconfig: add kibana service](https://github.com/quattor/configuration-modules-core/pull/514)
* [ncm-metaconfig: add service ncm-ncd](https://github.com/quattor/configuration-modules-core/pull/543)
* [ncm-metaconfig: ganesha: fix Access_Type type](https://github.com/quattor/configuration-modules-core/pull/578)
* [ncm-metaconfig: hotfix: use arrayref for internal includepath](https://github.com/quattor/configuration-modules-core/pull/549)
* [ncm-metaconfig: named: add newline after each include](https://github.com/quattor/configuration-modules-core/pull/542)
* [ncm-metaconfig: perfsonar: replace module general with TT](https://github.com/quattor/configuration-modules-core/pull/541)
* [ncm-metaconfig: service elasticsearch](https://github.com/quattor/configuration-modules-core/pull/513)
* [ncm-metaconfig: service logstash add support for filter kv](https://github.com/quattor/configuration-modules-core/pull/515)
* [ncm-metaconfig: service logstash: change forwarder configfile location ](https://github.com/quattor/configuration-modules-core/pull/522)
* [ncm-metaconfig: service rpcidmap: control service name via RPCIDMAPD_SERVICE_PREFIX](https://github.com/quattor/configuration-modules-core/pull/521)
* [ncm-modprobe: close the mocked filehandles in the test ](https://github.com/quattor/configuration-modules-core/pull/577)
* [ncm-nagios & ncm-icinga: Seperate type definitions](https://github.com/quattor/configuration-modules-core/pull/563)
* [ncm-named: Add missing newline when inserting "search" options](https://github.com/quattor/configuration-modules-core/pull/527)
* [ncm-named: fix double-comma typo](https://github.com/quattor/configuration-modules-core/pull/540)
* [ncm-named: missing named.conf data in profile should not wipe existing file](https://github.com/quattor/configuration-modules-core/pull/523)
* [ncm-network: Actually use realhostname if it has been provided](https://github.com/quattor/configuration-modules-core/pull/546)
* [ncm-network: Add fqdn to interface_alias type](https://github.com/quattor/configuration-modules-core/pull/524)
* [ncm-network: Support all five systemd device naming schemes](https://github.com/quattor/configuration-modules-core/pull/528)
* [ncm-network: change type of nisdomain to something closer to reality](https://github.com/quattor/configuration-modules-core/pull/605)
* [ncm-network: handle uninitialised warning for aliases](https://github.com/quattor/configuration-modules-core/pull/591)
* [ncm-opennebula: Fix database schema](https://github.com/quattor/configuration-modules-core/pull/547)
* [ncm-opennebula: Sunstone configuration and shared datastores support](https://github.com/quattor/configuration-modules-core/pull/512)
* [ncm-puppet: close the filehandle instead of relying on the destroy ](https://github.com/quattor/configuration-modules-core/pull/552)
* [ncm-spma: hotfix: bump build tools to 1.46](https://github.com/quattor/configuration-modules-core/pull/548)
* [ncm-spma: purge_rep_list - Do nothing if SELF is not defined](https://github.com/quattor/configuration-modules-core/pull/564)
* [ncm-spma: support yum plugin configuration (including default versionlock and fastestmirror)](https://github.com/quattor/configuration-modules-core/pull/535)
* [ncm-ssh: Add ssh client PreferredAuthentications option](https://github.com/quattor/configuration-modules-core/pull/539)
* [ncm-ssh: Fix small bugs](https://github.com/quattor/configuration-modules-core/pull/526)
* [ncm-sudo fixes](https://github.com/quattor/configuration-modules-core/pull/533)
* [rename conflicting nagios and icinga function names](https://github.com/quattor/configuration-modules-core/pull/588)

### ncm-lib-blockdevices
* [Filesystem: add uuid support, and strict protected mountpoints or filesystems](https://github.com/quattor/ncm-lib-blockdevices/pull/52)
* [Partiton: Improved ks_pre partition removal](https://github.com/quattor/ncm-lib-blockdevices/pull/51)

### template-library-standard
* [Do not install cvmfs-keys with cvmfs](https://github.com/quattor/template-library-standard/pull/57)

### template-library-grid
* [Fix CRLF](https://github.com/quattor/template-library-grid/pull/145)
* [Set the version of HEP_OSlibs correspondingly to the OS version](https://github.com/quattor/template-library-grid/pull/147)
* [The /etc/lrms/lcg-info-dynamic-maui.defaults file should be readable by any](https://github.com/quattor/template-library-grid/pull/149)
* [fix nlist WN_CPU_SLOTS](https://github.com/quattor/template-library-grid/pull/146)

### ncm-ncd
* [Add option to check if CCM is disabled, and not run if it is the case](https://github.com/quattor/ncm-ncd/pull/45)
* [Support ignoring failing dependencies (or dependencies altogether)](https://github.com/quattor/ncm-ncd/pull/44)
* [ncm-ncd: ComponentProxy _load requires Configure method](https://github.com/quattor/ncm-ncd/pull/47)

### CCM
* [Add CCM specific tabcompletion support](https://github.com/quattor/CCM/pull/62)
* [Add CCM::TextRender predefined formats](https://github.com/quattor/CCM/pull/60)
* [Add support for CCM-based cli applications](https://github.com/quattor/CCM/pull/58)
* [CCM::Format class to convert CCM instances in formatted text](https://github.com/quattor/CCM/pull/55)
* [CLI: module for new CCM CLI (and ccm script) (Preview)](https://github.com/quattor/CCM/pull/65)
* [Fetch using json_typed requires untainted decode_json ](https://github.com/quattor/CCM/pull/57)
* [Mark /etc/ccm.conf as noreplace](https://github.com/quattor/CCM/pull/69)
* [TextRender: correctly handle CCM::Property instances](https://github.com/quattor/CCM/pull/64)
* [Use valid defaults for host and domain in default config file](https://github.com/quattor/CCM/pull/70)
* [bump build tools to 1.46](https://github.com/quattor/CCM/pull/67)
* [improve CCM  API with more convience methods and a CCM::Options class](https://github.com/quattor/CCM/pull/61)
* [support for multiple profile failover urls](https://github.com/quattor/CCM/pull/63)

### maven-tools
* [RegexpTest block separator should include newline](https://github.com/quattor/maven-tools/pull/56)
* [Rename Test::Quattor::TextRender::Base mock method to mock_textrender](https://github.com/quattor/maven-tools/pull/57)
* [Test::Quattor::Object Add report logging method](https://github.com/quattor/maven-tools/pull/58)
* [Test::Quattor::TextRender::Base: internal includepath is arrayref](https://github.com/quattor/maven-tools/pull/59)
* [pod2man: support .pm as source of pod, existing pod file will take precedence](https://github.com/quattor/maven-tools/pull/61)

### aii
* [AII dhcp pan code refactor to allow disabling of dhcp config](https://github.com/quattor/aii/pull/132)
* [AII kickstart: add support for ignore-errors-from-dependencies during initial spma](https://github.com/quattor/aii/pull/129)
* [Allow reinstallation of node and check final status in oneliners](https://github.com/quattor/aii/pull/124)
* [Bump builds tools and fix aii-opennebula test failure](https://github.com/quattor/aii/pull/140)
* [Consistent use of foreign CCM conf in aii-shellfe](https://github.com/quattor/aii/pull/125)
* [Support all five systemd device naming schemes](https://github.com/quattor/aii/pull/131)
* [aii-ks: improved disk/partiton removal in pre](https://github.com/quattor/aii/pull/133)
* [aii-ks: spma uses boolean_yes_no for proxy enabling](https://github.com/quattor/aii/pull/138)
* [aii-opennebula: set VNET single address range mac addresses as optional](https://github.com/quattor/aii/pull/127)
* [aii-shellfe: add --reinstall option](https://github.com/quattor/aii/pull/135)
* [ks: fix unittest regexps due to new output from ncm-lib-blockdevices](https://github.com/quattor/aii/pull/141)
* [opennebula-aii: Support for SPICE and SDL graphics](https://github.com/quattor/aii/pull/137)
* [pxelinux: add hooks unittests](https://github.com/quattor/aii/pull/139)

### template-library-os
* [Completion of sl5.x-x86_64 for UI installation](https://github.com/quattor/template-library-os/pull/70)

### release
* [Build TOC using new syntax](https://github.com/quattor/release/pull/103)
* [Correct RPM collection path](https://github.com/quattor/release/pull/116)
* [Deal with release dependencies better](https://github.com/quattor/release/pull/108)
* [Move email removal block into correct part of the loop](https://github.com/quattor/release/pull/102)
* [Remove release:perform from maven invocation](https://github.com/quattor/release/pull/101)
* [build_all_repos: Test for noreplace bits](https://github.com/quattor/release/pull/113)
* [build_all_repos: another fix for EL7 and EL5](https://github.com/quattor/release/pull/106)
* [build_all_repos: exclude maven 3.3.3 until rpm requirements are fixed](https://github.com/quattor/release/pull/120)

### configuration-modules-grid
* [Remove all config-xml templates](https://github.com/quattor/configuration-modules-grid/pull/82)
* [ncm-xrootd: Support all possible logKeep options](https://github.com/quattor/configuration-modules-grid/pull/78)
* [ncm-yaim_usersconf: Include correct component base structure](https://github.com/quattor/configuration-modules-grid/pull/80)

### CAF
* [Application export cfgfile option name](https://github.com/quattor/CAF/pull/91)
* [Application: support -cfgfile besides --cfgfile (like Appconfig would)](https://github.com/quattor/CAF/pull/112)
* [CAF::Application: fix 'Warning: cannot read config file: 0' message](https://github.com/quattor/CAF/pull/92)
* [FileEditor: support add_after_newline in add_or_replace_lines method](https://github.com/quattor/CAF/pull/95)
* [FileEditor:do not insert the missing newline if the to-be-inserted text starts with a newline](https://github.com/quattor/CAF/pull/99)
* [Fix failing unittests on EL5 due to missing mktemp --tmpdir option](https://github.com/quattor/CAF/pull/106)
* [TextRender: can't set ForceArray for predefined format general on EL5](https://github.com/quattor/CAF/pull/107)
* [TextRender: general/Config::General disable SaveSorted and enable ForceArray](https://github.com/quattor/CAF/pull/97)
* [TextRender: properly handle scalar contents and JSON rendering](https://github.com/quattor/CAF/pull/94)
* [TextRender: support empty relpath and multiple includepaths](https://github.com/quattor/CAF/pull/96)

### template-library-stratuslab
* [ncm-oned: Do not include NCM::Check](https://github.com/quattor/template-library-stratuslab/pull/8)
