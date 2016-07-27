---
layout: article
title: Quattor 16.6.0 released
category: news
author: James Adams
---

It's been a long process, essentially building a double release (having skipped 16.4.0) but we've finally arrived at 16.6.0!

Packages are available from our [yum repository](http://yum.quattor.org/16.6.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 166 pull requests and resolved 56 issues.

The next release should be 16.8.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### configuration-modules-core
* [Resolver list lengths](https://github.com/quattor/configuration-modules-core/pull/786)
* [**ncm-nfs:** rewrite for NoActionSupported and unittests](https://github.com/quattor/configuration-modules-core/pull/724)

### CAF
* [Correct aliasing of new/open for CAF::FileWriter/Editor/Reader](https://github.com/quattor/CAF/pull/141)
* [fix race condition in locking](https://github.com/quattor/CAF/pull/132)

Changelog
---------

### quattor.github.com
* [Add a 'Development' category to docmenu](https://github.com/quattor/quattor.github.com/pull/177)
* [Add a new menu 'Meetings' for meeting/workshop summaries](https://github.com/quattor/quattor.github.com/pull/178)
* [Add some context to the meetings index page](https://github.com/quattor/quattor.github.com/pull/180)
* [Cleanup textrender posts and add metaconfig convert option](https://github.com/quattor/quattor.github.com/pull/165)
* [Fix whitespace around block-level elements and improve FAQ](https://github.com/quattor/quattor.github.com/pull/175)
* [Include info about meetings on Contacts page](https://github.com/quattor/quattor.github.com/pull/160)
* [Munge link into something renderable](https://github.com/quattor/quattor.github.com/pull/173)
* [Posts on quattor development](https://github.com/quattor/quattor.github.com/pull/166)
* [Remove 'Historical Wiki' from menu](https://github.com/quattor/quattor.github.com/pull/176)
* [**travis:** recent html-proofer command is called htmlproofer](https://github.com/quattor/quattor.github.com/pull/167)

### ncm-query
* [**pom.xml:** bump build-tools and fix rpmlint issues](https://github.com/quattor/ncm-query/pull/11)

### LC
* [**pom.xml:** bump build-tools and fix rpmlint error](https://github.com/quattor/LC/pull/14)

### ncm-cdispd
* [Make the RPMs more rpmlint compliant.](https://github.com/quattor/ncm-cdispd/pull/29)

### template-library-core
* [Add new template for legacy types](https://github.com/quattor/template-library-core/pull/111)
* [Allow thread count of CPU to be specified](https://github.com/quattor/template-library-core/pull/113)
* [**Blockdevices/LV :** add chunksize option](https://github.com/quattor/template-library-core/pull/107)
* [[pan/units] added more binary constants](https://github.com/quattor/template-library-core/pull/117)
* [**filesystems_uniq_paths:** tmpfs can be used multiple times as a blockdevice](https://github.com/quattor/template-library-core/pull/115)
* [quattor client ncm-ncd rpm do not overwrite lock](https://github.com/quattor/template-library-core/pull/85)
* [**quattor/client/rpms:** use pkg_repl() to configure RPMs](https://github.com/quattor/template-library-core/pull/114)

### configuration-modules-core
* [Adapt unittests to new buildtools](https://github.com/quattor/configuration-modules-core/pull/730)
* [Add Eclipse .project to .gitignore](https://github.com/quattor/configuration-modules-core/pull/803)
* [Add PyCharm project files to .gitignore](https://github.com/quattor/configuration-modules-core/pull/802)
* [Add templates for new issues and pull-requests](https://github.com/quattor/configuration-modules-core/pull/726)
* [Remove DTA typeglob](https://github.com/quattor/configuration-modules-core/pull/769)
* [Resolver list lengths](https://github.com/quattor/configuration-modules-core/pull/786)
* [Unittest hotfixes](https://github.com/quattor/configuration-modules-core/pull/762)
* [**config-rpm:** do not define groups/names/yumng by default](https://github.com/quattor/configuration-modules-core/pull/807)
* [**ncm-*:** Remove variants of yesno pseudo-boolean](https://github.com/quattor/configuration-modules-core/pull/749)
* [**ncm-acccounts:** fix failing unittests](https://github.com/quattor/configuration-modules-core/pull/757)
* [**ncm-afsclt:** Fix warning caused redeclaration of variable with my.](https://github.com/quattor/configuration-modules-core/pull/818)
* [**ncm-afsclt:** fix handling of size AUTOMATIC](https://github.com/quattor/configuration-modules-core/pull/816)
* [**ncm-ccm:** allow lowercase characters in trust realm.](https://github.com/quattor/configuration-modules-core/pull/731)
* [**ncm-ccm:** ccm group_readable option](https://github.com/quattor/configuration-modules-core/pull/709)
* [**ncm-ceph:** add TT test](https://github.com/quattor/configuration-modules-core/pull/728)
* [**ncm-ceph:** add options to schema](https://github.com/quattor/configuration-modules-core/pull/756)
* [**ncm-ceph:** remove outdated examples](https://github.com/quattor/configuration-modules-core/pull/725)
* [**ncm-dirperm:** checkmount feature.](https://github.com/quattor/configuration-modules-core/pull/616)
* [**ncm-filecopy:** Update filecopy.pod example to make it work](https://github.com/quattor/configuration-modules-core/pull/775)
* [**ncm-filesystems:** pom.xml fix rpmlint 'description too long' error](https://github.com/quattor/configuration-modules-core/pull/765)
* [**ncm-iptables:** Rewrite, add unit tests and add support for per-rule comments](https://github.com/quattor/configuration-modules-core/pull/688)
* [**ncm-metaconfig:** Add support for haproxy](https://github.com/quattor/configuration-modules-core/pull/727)
* [**ncm-metaconfig:** Add support for keepalived](https://github.com/quattor/configuration-modules-core/pull/729)
* [**ncm-metaconfig:** add service for limits.conf file](https://github.com/quattor/configuration-modules-core/pull/736)
* [**ncm-metaconfig:** add service nrpe to replace ncm-nrpe](https://github.com/quattor/configuration-modules-core/pull/723)
* [**ncm-metaconfig:** add zkrsync config file ](https://github.com/quattor/configuration-modules-core/pull/733)
* [**ncm-metaconfig:** basic sysconfig for ceph](https://github.com/quattor/configuration-modules-core/pull/722)
* [**ncm-metaconfig:** ganesha: add config_ces](https://github.com/quattor/configuration-modules-core/pull/772)
* [**ncm-metaconfig:** httpd support GSSAPI auth](https://github.com/quattor/configuration-modules-core/pull/751)
* [**ncm-metaconfig:** increase default verbosity to track changes/actions at info level](https://github.com/quattor/configuration-modules-core/pull/666)
* [**ncm-metaconfig:** lmod: scDescript needs quoted values](https://github.com/quattor/configuration-modules-core/pull/767)
* [**ncm-named:** resolv.conf: generate correct options](https://github.com/quattor/configuration-modules-core/pull/766)
* [**ncm-network:** support hardcoded ovirtmgmt bridge name](https://github.com/quattor/configuration-modules-core/pull/794)
* [**ncm-nfs:** rewrite for NoActionSupported and unittests](https://github.com/quattor/configuration-modules-core/pull/724)
* [**ncm-nss:** wait for nscd to restart before returning](https://github.com/quattor/configuration-modules-core/pull/781)
* [**ncm-opennebula:** Fix RPC history](https://github.com/quattor/configuration-modules-core/pull/782)
* [**ncm-opennebula:** Include VNET update_ar](https://github.com/quattor/configuration-modules-core/pull/734)
* [**ncm-opennebula:** Update oneadmin user template and user public ssh keys](https://github.com/quattor/configuration-modules-core/pull/747)
* [**ncm-spma:** Backport changes from reverting yumng schema](https://github.com/quattor/configuration-modules-core/pull/798)
* [**ncm-spma:** Support yum gpgkey/gpgcakey/repo_gpgcheck repository settings](https://github.com/quattor/configuration-modules-core/pull/721)
* [**ncm-spma:** introduce new yumng sub-module ](https://github.com/quattor/configuration-modules-core/pull/761)
* [**ncm-spma:** remove ips.pm and spma-run from (linux) rpmbuild ](https://github.com/quattor/configuration-modules-core/pull/768)
* [**ncm-spma:** software repository protocol url should be a software_repository_url](https://github.com/quattor/configuration-modules-core/pull/793)
* [**ncm-spma:** spma-run: Lock use reporter instance for reporting](https://github.com/quattor/configuration-modules-core/pull/804)
* [**ncm-spma:** yum create and use cache](https://github.com/quattor/configuration-modules-core/pull/711)
* [**ncm-ssh:** Fix for multiline option values with special chars.](https://github.com/quattor/configuration-modules-core/pull/745)
* [**ncm-sudo:** add boolean option 'visiblepw' to ncm-sudo.](https://github.com/quattor/configuration-modules-core/pull/817)
* [**ncm-sudo:** missing elements in list of STRING_OPTS in sudo.pm](https://github.com/quattor/configuration-modules-core/pull/796)
* [**ncm-symlink:** do not make changes if symlink is correct](https://github.com/quattor/configuration-modules-core/pull/738)
* [**ncm-syslogng:** fix flags support.](https://github.com/quattor/configuration-modules-core/pull/732)

### ncm-lib-blockdevices
* [**LV:** add chunksize and cachemode options](https://github.com/quattor/ncm-lib-blockdevices/pull/63)
* [**MD:** add ks anaconda useexisting flag when set in aii](https://github.com/quattor/ncm-lib-blockdevices/pull/64)
* [**pom.xml:** bump build-tools and fix rpmlint isses](https://github.com/quattor/ncm-lib-blockdevices/pull/65)

### template-library-standard
* [Cvmfs extra repos](https://github.com/quattor/template-library-standard/pull/72)
* [**MW version definition:** allow to disable MW client configuration](https://github.com/quattor/template-library-standard/pull/70)
* [New CPUs](https://github.com/quattor/template-library-standard/pull/63)
* [Set required RPMs accordingly to cvmfs version](https://github.com/quattor/template-library-standard/pull/62)
* [Use pkg_compare_version to compare CVMFS client versions](https://github.com/quattor/template-library-standard/pull/61)

### template-library-grid
* [GIP_CE_MAUI_PLUGIN_DEFAULTS_FILE should be world readable](https://github.com/quattor/template-library-grid/pull/175)
* [**Globus:** remove SASL_PATH env variable definition](https://github.com/quattor/template-library-grid/pull/178)
* [**UMD-3:** update DPM's HTTP configuration](https://github.com/quattor/template-library-grid/pull/169)
* [new offline/draining mechanism for condor nodes](https://github.com/quattor/template-library-grid/pull/173)
* [support for SUBMIT REQUESTS](https://github.com/quattor/template-library-grid/pull/171)
* [support for gpu and intel mic resources](https://github.com/quattor/template-library-grid/pull/170)
* [**xrootd:** define GSI security protocol params by default](https://github.com/quattor/template-library-grid/pull/176)

### ncm-ncd
* [Add history/event support](https://github.com/quattor/ncm-ncd/pull/51)
* [**ignore NCM::** namespace for all unittests](https://github.com/quattor/ncm-ncd/pull/59)
* [**ncm-ncd:** Lock use reporter instance for reporting](https://github.com/quattor/ncm-ncd/pull/64)

### CCM
* [**CCM:** fetchProfile should close all CAF::File* instances ](https://github.com/quattor/CCM/pull/101)
* [Enable tabcompletion generation and json_typed by default](https://github.com/quattor/CCM/pull/97)
* [Fix EL5 JSON::XS dependency](https://github.com/quattor/CCM/pull/115)
* [**ProfileCache:** Lock use reporter instance for reporting](https://github.com/quattor/CCM/pull/111)
* [Support download using Kerberos authentication](https://github.com/quattor/CCM/pull/93)
* [**TextRender:** support rendering non-hash root element via CCM.contents ](https://github.com/quattor/CCM/pull/90)
* [bump build-tools to 1.49](https://github.com/quattor/CCM/pull/99)
* [**ccm-initialise / ProfileCache:** factor out the creation and setup of cache_root](https://github.com/quattor/CCM/pull/88)
* [**perl dependency JSON-XS:** set an explicit requirement on RPM version](https://github.com/quattor/CCM/pull/116)
* [**pom.xml:** cleanup rpmlint errors](https://github.com/quattor/CCM/pull/98)

### maven-tools
* [**BUILD_INFO:** fix typos, clarifications](https://github.com/quattor/maven-tools/pull/86)
* [Make the RPMs more rpmlint compliant.](https://github.com/quattor/maven-tools/pull/81)
* [Make the RPMs more rpmlint compliant.](https://github.com/quattor/maven-tools/pull/78)
* [Mock CAF::Path](https://github.com/quattor/maven-tools/pull/82)
* [Package build-scripts as standalone Test::Quattor](https://github.com/quattor/maven-tools/pull/77)
* [Remove .project](https://github.com/quattor/maven-tools/pull/84)
* [**Test::Quattor:** rename caf_check to caf_path (after CAF::Path renaming)](https://github.com/quattor/maven-tools/pull/93)
* [**Test::Quattor::Object:** support is_quiet / is_verbose / get_debuglevel / event](https://github.com/quattor/maven-tools/pull/80)
* [**Test::Quattor::ProfileCache:** get_config_for_profile report error](https://github.com/quattor/maven-tools/pull/94)
* [**build-profile:** use existing RPM group instead to build rpms](https://github.com/quattor/maven-tools/pull/95)
* [**mvnprove:** also extract build plugins from pluginManagement](https://github.com/quattor/maven-tools/pull/90)
* [**mvnprove:** fix bugs in PMpost / PMpre](https://github.com/quattor/maven-tools/pull/96)
* [**namespace unittest:** handle relative paths in INC](https://github.com/quattor/maven-tools/pull/88)
* [**package-build-scripts:** no actual submodule ](https://github.com/quattor/maven-tools/pull/87)

### template-library-openstack
* [HA additions](https://github.com/quattor/template-library-openstack/pull/9)
* [Split init script](https://github.com/quattor/template-library-openstack/pull/14)
* [update mongodb to 3.2](https://github.com/quattor/template-library-openstack/pull/10)

### aii
* [**aii-core:** add an explicit requirement for perl-XML-Simple](https://github.com/quattor/aii/pull/189)
* [**aii-ks:** handle disabled/ignored packages when packagesinpost enabled](https://github.com/quattor/aii/pull/171)
* [**aii-ks:** sha512 instead of md5 for password hashes](https://github.com/quattor/aii/pull/169)
* [**aii-opennebula:** Add an option to change user/group resources](https://github.com/quattor/aii/pull/178)
* [**aii-opennebula:** var without default](https://github.com/quattor/aii/pull/164)
* [**ks:** add useexisting when using el7 with md](https://github.com/quattor/aii/pull/165)
* [**ks:** generate ccm.conf like ncm-ccm](https://github.com/quattor/aii/pull/161)
* [**ks:** yum_setup: support gpgkeys (and some cleanup)](https://github.com/quattor/aii/pull/176)
* [**pom.xml:** bump build-tools to 1.49 and fix rpmlint issues](https://github.com/quattor/aii/pull/174)

### template-library-os
* [iscsid daemon](https://github.com/quattor/template-library-os/pull/78)
* [let the daemon iscsid on if the variable OS_CORE_ISCSI_ENABLED is set to true](https://github.com/quattor/template-library-os/pull/79)
* [**quattor-development:** add perl-Config-General RPM](https://github.com/quattor/template-library-os/pull/77)
* [**quattor-development:** add perl-Config-General RPM](https://github.com/quattor/template-library-os/pull/76)

### release
* [**.gitignore:** add PyCharm work directory](https://github.com/quattor/release/pull/247)
* [Add rpmlint to build_all_repos](https://github.com/quattor/release/pull/244)
* [add a script to convert a tracwiki file into markdown](https://github.com/quattor/release/pull/246)
* [**releaser:** Check that a reference core template library has been set](https://github.com/quattor/release/pull/252)

### configuration-modules-grid
* [Adapt unittests to new buildtools](https://github.com/quattor/configuration-modules-grid/pull/93)
* [Mock sleep and bump build tools to 1.49](https://github.com/quattor/configuration-modules-grid/pull/100)
* [Remove 'local *DTA' from all configuration modules](https://github.com/quattor/configuration-modules-grid/pull/102)
* [**ncm-dpmlfc/xroot:** adapt to new CAF::RuleBasedEditor constants](https://github.com/quattor/configuration-modules-grid/pull/106)
* [**ncm-dpmlfc:** fix typo in shift.conf rules leading to missing DPNS_TRUST](https://github.com/quattor/configuration-modules-grid/pull/96)
* [**ncm-dpmlfc:** use CAF::RuleBasedEditor](https://github.com/quattor/configuration-modules-grid/pull/97)
* [**ncm-glitestartup:** flag template as documentation](https://github.com/quattor/configuration-modules-grid/pull/111)
* [**ncm-pbsserver:** add legacy_vmem server attribute](https://github.com/quattor/configuration-modules-grid/pull/99)
* [**ncm-xrootd:** add ability to manage sec.protocol options](https://github.com/quattor/configuration-modules-grid/pull/89)
* [**ncm-xrootd:** add securityProtocol resource to schema](https://github.com/quattor/configuration-modules-grid/pull/114)
* [**ncm-xrootd:** use CAF::RuleBasedEditor](https://github.com/quattor/configuration-modules-grid/pull/98)

### cdp-listend
* [Make the RPMs more rpmlint compliant.](https://github.com/quattor/cdp-listend/pull/11)

### CAF
* [Add PyCharm and Eclipse files to gitignore](https://github.com/quattor/CAF/pull/174)
* [Correct aliasing of new/open for CAF::FileWriter/Editor/Reader](https://github.com/quattor/CAF/pull/141)
* [**FileEditor:** add a 'source' option in constructor](https://github.com/quattor/CAF/pull/156)
* [**FileEditor:** fix tempfile() calling sequence in unit tests](https://github.com/quattor/CAF/pull/152)
* [**FileEditor:** fix unitialized warning in debug message ](https://github.com/quattor/CAF/pull/162)
* [**FileReader:** fix example](https://github.com/quattor/CAF/pull/140)
* [**FileWriter:** add conditional logger interfaces](https://github.com/quattor/CAF/pull/154)
* [**FileWriter:** add is_verbose method to determine log verbosity](https://github.com/quattor/CAF/pull/165)
* [**History:** support event tracking](https://github.com/quattor/CAF/pull/117)
* [**Kerberos:** make it work](https://github.com/quattor/CAF/pull/145)
* [**Lock:** handle existing old-style locks](https://github.com/quattor/CAF/pull/173)
* [**Lock:** set_lock correct number of retries (and test)](https://github.com/quattor/CAF/pull/175)
* [**Path tests:** use correct test messages](https://github.com/quattor/CAF/pull/171)
* [**Path:** common file and directory operations similar to LC::Check](https://github.com/quattor/CAF/pull/142)
* [**Path:** disable chatty LC::Check by default unless NoAction](https://github.com/quattor/CAF/pull/170)
* [**Reporter:** add methods to query state of reporter](https://github.com/quattor/CAF/pull/147)
* [Rule based editor](https://github.com/quattor/CAF/pull/151)
* [Rule based editor improvements](https://github.com/quattor/CAF/pull/163)
* [**Rule based editor:** more unit tests + fixes](https://github.com/quattor/CAF/pull/164)
* [fix race condition in locking](https://github.com/quattor/CAF/pull/132)
* [**pom:** Fix rpmlint errors](https://github.com/quattor/CAF/pull/155)

### template-library-examples
* [**Ceph:** Add examples and usable templates for ceph](https://github.com/quattor/template-library-examples/pull/29)
