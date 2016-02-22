---
layout: article
title: Quattor 16.2.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/16.2.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 101 pull requests and resolved 40 issues.

The next release should be 16.4.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.

Backwards Incompatible Changes
------------------------------

### ncm-query
* [Drop broken useprofile option](https://github.com/quattor/ncm-query/pull/10)

### configuration-modules-core
* [**metaconfig:** service logstash: support escaped add_field keys](https://github.com/quattor/configuration-modules-core/pull/697)
* [**ncm-afsclt:** remove out of place code for managing PAM and iptables.](https://github.com/quattor/configuration-modules-core/pull/649)
* [**ncm-metaconfig:** service logstash: filter grok: the match pattern support a list of patterns](https://github.com/quattor/configuration-modules-core/pull/672)
* [**ncm-metaconfig:** service logstash: use a sensible type for mutate convert](https://github.com/quattor/configuration-modules-core/pull/691)

### CCM
* [Support group_readable profiles (and minor cleanup)](https://github.com/quattor/CCM/pull/83)

Changelog
---------

### quattor.github.com
* [Add known issue for cdispd](https://github.com/quattor/quattor.github.com/pull/162)

### ncm-query
* [Drop broken useprofile option](https://github.com/quattor/ncm-query/pull/10)

### template-library-examples
* [Add an el7 example and document YUM_OS_DISTRIBUTION variable](https://github.com/quattor/template-library-examples/pull/28)

### ncm-cdispd
* [Bump build tools to 1.48](https://github.com/quattor/ncm-cdispd/pull/27)
* [Bump build-tools to 1.48](https://github.com/quattor/ncm-cdispd/pull/28)
* [Handle the case of undefined ICLIST](https://github.com/quattor/ncm-cdispd/pull/26)

### template-library-core
* [Fix test_templates script](https://github.com/quattor/template-library-core/pull/106)
* [**LV:** add support for lvmcache in schema](https://github.com/quattor/template-library-core/pull/98)
* [Miscellaneous cleanups](https://github.com/quattor/template-library-core/pull/100)

### configuration-modules-core
* [Bump build tools to 1.47](https://github.com/quattor/configuration-modules-core/pull/654)
* [Bump buildtools to 1.48](https://github.com/quattor/configuration-modules-core/pull/712)
* [Change 'aii' links to render as code instead of links](https://github.com/quattor/configuration-modules-core/pull/640)
* [**Revert "ncm-spma:** add support for more yum.conf options"](https://github.com/quattor/configuration-modules-core/pull/718)
* [**Revert "ncm-spma:** makecache and use it via yum/repoquery -C"](https://github.com/quattor/configuration-modules-core/pull/719)
* [**metaconfig:** service logstash: support escaped add_field keys](https://github.com/quattor/configuration-modules-core/pull/697)
* [**ncm-accounts:** add the possility to define group required members](https://github.com/quattor/configuration-modules-core/pull/659)
* [**ncm-accounts:** fix some useful accounts on CentOS 7.2](https://github.com/quattor/configuration-modules-core/pull/682)
* [**ncm-afsclt:** remove out of place code for managing PAM and iptables.](https://github.com/quattor/configuration-modules-core/pull/649)
* [**ncm-ceph:** ceph uid for infernalis](https://github.com/quattor/configuration-modules-core/pull/674)
* [**ncm-download:** CAF::Process execute is a method, not a function](https://github.com/quattor/configuration-modules-core/pull/676)
* [**ncm-metaconfig:** add service beats and logstash plugin](https://github.com/quattor/configuration-modules-core/pull/660)
* [**ncm-metaconfig:** add service lmod](https://github.com/quattor/configuration-modules-core/pull/698)
* [**ncm-metaconfig:** add support for icinga-web](https://github.com/quattor/configuration-modules-core/pull/696)
* [**ncm-metaconfig:** add timestream basic config](https://github.com/quattor/configuration-modules-core/pull/694)
* [**ncm-metaconfig:** httpd auth require add shibboleth](https://github.com/quattor/configuration-modules-core/pull/705)
* [**ncm-metaconfig:** icinga-web - Use FILTER to convert to uppercase, not string method](https://github.com/quattor/configuration-modules-core/pull/713)
* [**ncm-metaconfig:** publish component version](https://github.com/quattor/configuration-modules-core/pull/663)
* [**ncm-metaconfig:** service elasticsearch support discovery.zen](https://github.com/quattor/configuration-modules-core/pull/671)
* [**ncm-metaconfig:** service httpd: support mod_auth_gssapi](https://github.com/quattor/configuration-modules-core/pull/673)
* [**ncm-metaconfig:** service logstash: filter grok: the match pattern support a list of patterns](https://github.com/quattor/configuration-modules-core/pull/672)
* [**ncm-metaconfig:** service logstash: use a sensible type for mutate convert](https://github.com/quattor/configuration-modules-core/pull/691)
* [**ncm-metaconfig:** service ncm-ncd - do not try to restart daemons](https://github.com/quattor/configuration-modules-core/pull/708)
* [**ncm-metaconfig:** service snoopy](https://github.com/quattor/configuration-modules-core/pull/661)
* [**ncm-metaconfig:** support convert option for predefined conversions](https://github.com/quattor/configuration-modules-core/pull/669)
* [**ncm-network:** Don't warn if hwaddr is missing from bridge interfaces](https://github.com/quattor/configuration-modules-core/pull/675)
* [**ncm-network:** Fix ovs_extra network script output](https://github.com/quattor/configuration-modules-core/pull/652)
* [**ncm-nfs:** fix incorrect exports hosts example in documentation ](https://github.com/quattor/configuration-modules-core/pull/667)
* [**ncm-ntpd:** support restricting file ownership/permissions via group ](https://github.com/quattor/configuration-modules-core/pull/706)
* [**ncm-opennebula:** Include more oned inherit values](https://github.com/quattor/configuration-modules-core/pull/656)
* [**ncm-openvpn:** add client max-routes setting](https://github.com/quattor/configuration-modules-core/pull/704)
* [**ncm-pam:** support expressions in the control parameter of the pam rules.](https://github.com/quattor/configuration-modules-core/pull/662)
* [**ncm-postgresql:** rewrite (and support el7)](https://github.com/quattor/configuration-modules-core/pull/620)
* [**ncm-spma:** add support for more yum.conf options](https://github.com/quattor/configuration-modules-core/pull/710)
* [**ncm-symlink:** fix message for duplicated links](https://github.com/quattor/configuration-modules-core/pull/684)
* [**ncm-symlink:** merge config-{common,rpm} into config](https://github.com/quattor/configuration-modules-core/pull/653)
* [**ncm-systemd:** allow non-listed unit(file)s that have valid show data](https://github.com/quattor/configuration-modules-core/pull/680)
* [**ncm-systemd:** always use systemctl show data for non-listed unit](https://github.com/quattor/configuration-modules-core/pull/687)
* [**ncm-systemd:** unitfile configuration support](https://github.com/quattor/configuration-modules-core/pull/615)

### ncm-lib-blockdevices
* [**BlockdevFactory:** issue #58 - error on unknown.](https://github.com/quattor/ncm-lib-blockdevices/pull/60)
* [Bump buildtools to 1.48](https://github.com/quattor/ncm-lib-blockdevices/pull/62)
* [**LV:** add support for Lvmcache](https://github.com/quattor/ncm-lib-blockdevices/pull/61)

### template-library-grid
* [**ARGUS:** fix service to restart after a sysconfig file change](https://github.com/quattor/template-library-grid/pull/166)
* [**CREAM:** remove useless inclusion of glitestartup configuration module](https://github.com/quattor/template-library-grid/pull/163)
* [**DPM:** new DAV configuration + various improvements/cleanups](https://github.com/quattor/template-library-grid/pull/161)
* [**GIP CE:** fix for problem introduced by workaround for a buggy lcg-info-dynamic-scheduler](https://github.com/quattor/template-library-grid/pull/141)
* [**HEP OSLibs:** fix package list cleared when HEP_OSLIBS=false](https://github.com/quattor/template-library-grid/pull/160)
* [**HTCondor support:** fixes and improvements](https://github.com/quattor/template-library-grid/pull/162)
* [**VO auger:** update VOMS server](https://github.com/quattor/template-library-grid/pull/157)
* [**VO descriptions:** various updates](https://github.com/quattor/template-library-grid/pull/158)
* [**WMS + LB:** use pkg_repl() to add packages](https://github.com/quattor/template-library-grid/pull/165)
* [**YUM repo:** fix definition of YUM_EMI_SNAPSHOT_DATE](https://github.com/quattor/template-library-grid/pull/167)
* [**gridftp:** ensure that ncm-symlink is included](https://github.com/quattor/template-library-grid/pull/164)

### ncm-ncd
* [Bump build tools to 1.48](https://github.com/quattor/ncm-ncd/pull/58)
* [Bump buildtools to 1.48](https://github.com/quattor/ncm-ncd/pull/57)

### CCM
* [Bump buildtools to 1.48](https://github.com/quattor/CCM/pull/84)
* [**CLI:** new query formats, default action and non-options args as paths ](https://github.com/quattor/CCM/pull/79)
* [**CacheManager:** clarify the meaning of the passed cid in an unlocked configuration](https://github.com/quattor/CCM/pull/81)
* [**Configuration:** getTree clears any error causing the failure](https://github.com/quattor/CCM/pull/82)
* [**Configuration:** getTree ignore existing errors](https://github.com/quattor/CCM/pull/85)
* [Fix purge_time config parameter in ccm-purge.](https://github.com/quattor/CCM/pull/87)
* [Localize $@ when using eval](https://github.com/quattor/CCM/pull/80)
* [Support group_readable profiles (and minor cleanup)](https://github.com/quattor/CCM/pull/83)
* [**ccm-initialise:** fix bug after code cleanup](https://github.com/quattor/CCM/pull/86)

### maven-tools
* [Mock reporter](https://github.com/quattor/maven-tools/pull/76)
* [PMpre and PMpost properties for uniform and versioned perl module headers](https://github.com/quattor/maven-tools/pull/62)
* [Support unittesting metaconfig services with element option(s) set](https://github.com/quattor/maven-tools/pull/70)
* [**Test::Quattor:** set_file_contents store a copy of the contents ](https://github.com/quattor/maven-tools/pull/72)
* [adapt metaconfig unittest suite to renamed convert option](https://github.com/quattor/maven-tools/pull/75)

### aii
* [Bump buildtools to 1.48](https://github.com/quattor/aii/pull/162)
* [Modernise include syntax](https://github.com/quattor/aii/pull/159)
* [**aii-ks:** support yum.conf options](https://github.com/quattor/aii/pull/160)
* [**aii:** add opennebula and freeipa rpm](https://github.com/quattor/aii/pull/156)
* [**ks:** double escaped variables in yum.conf heredoc-in-heredoc](https://github.com/quattor/aii/pull/154)

### template-library-os
* [Remove useless RPM-related template](https://github.com/quattor/template-library-os/pull/75)
* [**Sl6.x:** various misc. RPM list adjustments](https://github.com/quattor/template-library-os/pull/72)
* [**el7.x:** allow a flexible configuration of OS distrib/version to use for each node](https://github.com/quattor/template-library-os/pull/73)
* [**el7.x:** ensure that new required users for CentOS 7.2 are preserved](https://github.com/quattor/template-library-os/pull/74)

### configuration-modules-grid
* [Bump buildtools to 1.48](https://github.com/quattor/configuration-modules-grid/pull/91)
* [**ncm-dpmlfc:** fix rules to generate /etc/shift.conf](https://github.com/quattor/configuration-modules-grid/pull/87)
* [**ncm-pbsserver:** support serverdb initialisation](https://github.com/quattor/configuration-modules-grid/pull/84)
* [**ncm-xrootd:** Drop support for logKeep as a long](https://github.com/quattor/configuration-modules-grid/pull/90)

### CAF
* [**Application:** Support non-option arguments retrieval via arrayref ](https://github.com/quattor/CAF/pull/126)
* [Bump build-tools to 1.47](https://github.com/quattor/CAF/pull/122)
* [Bump buildtools to 1.48](https://github.com/quattor/CAF/pull/138)
* [**CAF test:** make copy of constant before set_contents](https://github.com/quattor/CAF/pull/130)
* [**CAF:** cleanup remove prototypes](https://github.com/quattor/CAF/pull/137)
* [**CAF::Reporter::log():** ensure that there is no undefined argument](https://github.com/quattor/CAF/pull/135)
* [Kerberos support via GSSAPI](https://github.com/quattor/CAF/pull/121)
* [Localize $@ when using eval](https://github.com/quattor/CAF/pull/128)
* [**ObjectText:** factored-out text related methods from TextRender ](https://github.com/quattor/CAF/pull/120)
* [Support PID logging](https://github.com/quattor/CAF/pull/136)
