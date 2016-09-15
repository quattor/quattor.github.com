---
layout: article
title: Quattor 16.8.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/16.8.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 134 pull requests and resolved 29 issues.
Extra thanks go to @wdpypere for cleaning up much of the component documentation during this release cycle.

The next release should be 16.10.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### template-library-core
* [Throw error if short hostname is used as a network_name](https://github.com/quattor/template-library-core/pull/120)

### configuration-modules-core
* [**ncm-metaconfig:** cgroups: change default cgconfig location](https://github.com/quattor/configuration-modules-core/pull/771)

### template-library-standard
* [Add Intel CPUs from ARK](https://github.com/quattor/template-library-standard/pull/66)
* [Provide network driver templates](https://github.com/quattor/template-library-standard/pull/79)

### CCM
* [**DB:** refactor and cleanup](https://github.com/quattor/CCM/pull/106)
* [**Element:** remove (unused) getUnescapedName method](https://github.com/quattor/CCM/pull/119)
* [**Path:** support escape path and safe_unescape](https://github.com/quattor/CCM/pull/102)

Changelog
---------

### template-library-core
* [Add a transitional type to allow components to migrate to real booleans](https://github.com/quattor/template-library-core/pull/119)
* [Introduce an absolute_file_path type](https://github.com/quattor/template-library-core/pull/121)
* [Throw error if short hostname is used as a network_name](https://github.com/quattor/template-library-core/pull/120)
* [**aii schema:** add protected option](https://github.com/quattor/template-library-core/pull/110)
* [**aii-opennebula:** Fix default values of global variables](https://github.com/quattor/template-library-core/pull/122)

### template-library-examples
* [**HW templates:** Fix name of some CPU templates](https://github.com/quattor/template-library-examples/pull/31)
* [**HW templates:** update namespaces for NIC templates](https://github.com/quattor/template-library-examples/pull/32)

### ncm-cdispd
* [bump build-scripts to 1.50](https://github.com/quattor/ncm-cdispd/pull/31)

### configuration-modules-core
* [**ncm-*:** Update build tools to 1.50](https://github.com/quattor/configuration-modules-core/pull/858)
* [**ncm-accounts:** make documentation a bit more consistent](https://github.com/quattor/configuration-modules-core/pull/836)
* [**ncm-afsclt:** documentation cleanup](https://github.com/quattor/configuration-modules-core/pull/837)
* [**ncm-afsclt:** use FileEditor not FileReader (for old CAF).](https://github.com/quattor/configuration-modules-core/pull/823)
* [**ncm-aiiserver:** cleanup documentation](https://github.com/quattor/configuration-modules-core/pull/838)
* [**ncm-altlogrotate:** minor fixes for documentation](https://github.com/quattor/configuration-modules-core/pull/839)
* [**ncm-amandaserver:** documentation cleanup](https://github.com/quattor/configuration-modules-core/pull/840)
* [**ncm-authconfig:** minor documentation fixes](https://github.com/quattor/configuration-modules-core/pull/841)
* [**ncm-autofs:** documentation fixes](https://github.com/quattor/configuration-modules-core/pull/842)
* [**ncm-ccm:** add missing "use CAF::FileReader"](https://github.com/quattor/configuration-modules-core/pull/885)
* [**ncm-chkconfig:** alllow query state with noaction](https://github.com/quattor/configuration-modules-core/pull/830)
* [**ncm-chkconfig:** documentation cleanup](https://github.com/quattor/configuration-modules-core/pull/843)
* [**ncm-cron:** documentation fixes](https://github.com/quattor/configuration-modules-core/pull/845)
* [**ncm-cups:** cleanup documentation](https://github.com/quattor/configuration-modules-core/pull/846)
* [**ncm-directoryservices:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/847)
* [**ncm-download:** cleanup documentation](https://github.com/quattor/configuration-modules-core/pull/848)
* [**ncm-download:** code cleanup](https://github.com/quattor/configuration-modules-core/pull/833)
* [**ncm-download:** config-rpm is not part of the templates anymore](https://github.com/quattor/configuration-modules-core/pull/844)
* [**ncm-etcservices:** documentation cleanup](https://github.com/quattor/configuration-modules-core/pull/849)
* [**ncm-filesystems:** documentation cleanup](https://github.com/quattor/configuration-modules-core/pull/851)
* [**ncm-fmonagent:** documentation cleanup](https://github.com/quattor/configuration-modules-core/pull/855)
* [**ncm-fstab:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/856)
* [**ncm-ganglia:** cleanup documentation](https://github.com/quattor/configuration-modules-core/pull/857)
* [**ncm-gmetad:** cleanup documentation](https://github.com/quattor/configuration-modules-core/pull/860)
* [**ncm-gmond:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/861)
* [**ncm-gpfs:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/863)
* [**ncm-grub:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/864)
* [**ncm-grub:** support setting password in grub.conf.](https://github.com/quattor/configuration-modules-core/pull/783)
* [**ncm-hostsaccess:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/862)
* [**ncm-hostsfile:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/865)
* [**ncm-icinga:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/866)
* [**ncm-interactivelimits:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/867)
* [**ncm-ipmi:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/874)
* [**ncm-iptables:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/875)
* [**ncm-ldconf:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/877)
* [**ncm-libvirtd:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/878)
* [**ncm-mcx:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/879)
* [**ncm-metaconfig:** Include libvirtd conf file for the QEMU driver](https://github.com/quattor/configuration-modules-core/pull/809)
* [**ncm-metaconfig:** add joincomma and joinspace convert options](https://github.com/quattor/configuration-modules-core/pull/760)
* [**ncm-metaconfig:** add rsync template for xinetd](https://github.com/quattor/configuration-modules-core/pull/790)
* [**ncm-metaconfig:** beats: allow more than one output](https://github.com/quattor/configuration-modules-core/pull/826)
* [**ncm-metaconfig:** cgroups: change default cgconfig location](https://github.com/quattor/configuration-modules-core/pull/771)
* [**ncm-metaconfig:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/881)
* [**ncm-metaconfig:** moab: use stricter schema](https://github.com/quattor/configuration-modules-core/pull/791)
* [**ncm-metaconfig:** ptpd: add extra attributes to deal with large clock skew](https://github.com/quattor/configuration-modules-core/pull/792)
* [**ncm-metaconfig:** zkrsync: add timeout option](https://github.com/quattor/configuration-modules-core/pull/795)
* [**ncm-modprobe:** minor clean up documentation](https://github.com/quattor/configuration-modules-core/pull/882)
* [**ncm-modprobe:** overwrite initramfs if it exists, instead of initrd.](https://github.com/quattor/configuration-modules-core/pull/799)
* [**ncm-mysql:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/883)
* [**ncm-nagios:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/886)
* [**ncm-named:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/887)
* [**ncm-network:** documentation cleanup](https://github.com/quattor/configuration-modules-core/pull/889)
* [**ncm-network:** use CAF::FileWriter to compare and report the differences](https://github.com/quattor/configuration-modules-core/pull/778)
* [**ncm-nfs:** add cephfs share type to NFS component schema](https://github.com/quattor/configuration-modules-core/pull/822)
* [**ncm-nfs:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/891)
* [**ncm-nrpe:** documenatation clean up](https://github.com/quattor/configuration-modules-core/pull/892)
* [**ncm-nsca:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/893)
* [**ncm-nscd:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/894)
* [**ncm-nss:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/896)
* [**ncm-nss:** replace LC::Check with FileWriter](https://github.com/quattor/configuration-modules-core/pull/810)
* [**ncm-ntpd:** documentation clean up](https://github.com/quattor/configuration-modules-core/pull/897)
* [**ncm-ofed:** documentation cleanup](https://github.com/quattor/configuration-modules-core/pull/898)
* [**ncm-opennebula:** Include support for new OpenNebula v5 oned.conf](https://github.com/quattor/configuration-modules-core/pull/784)
* [**ncm-opennebula:** Support v5.0.0 vnets and hyps allocation](https://github.com/quattor/configuration-modules-core/pull/824)
* [**ncm-opennebula:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/899)
* [**ncm-opennebula:** opennebula schema minor fix](https://github.com/quattor/configuration-modules-core/pull/873)
* [**ncm-openvpn:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/900)
* [**ncm-pam:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/901)
* [**ncm-pnp4nagios:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/902)
* [**ncm-postfix:** clean up documentation](https://github.com/quattor/configuration-modules-core/pull/903)
* [**ncm-postfix:** use CCM::TextRender](https://github.com/quattor/configuration-modules-core/pull/808)
* [**ncm-spma:** yum: pass error_is_warn from update_pkgs_retry also to spare_dependencies](https://github.com/quattor/configuration-modules-core/pull/869)
* [**ncm-systemd:** Add systemd_make_mountunit function to convert path in mount unitname](https://github.com/quattor/configuration-modules-core/pull/759)

### ncm-lib-blockdevices
* [bump build-scripts to 1.50](https://github.com/quattor/ncm-lib-blockdevices/pull/66)

### template-library-standard
* [Add Intel CPUs from ARK](https://github.com/quattor/template-library-standard/pull/66)
* [Add directories under hardware/nic/ for each nic manufacturer.](https://github.com/quattor/template-library-standard/pull/69)
* [Fix hardware template namespaces](https://github.com/quattor/template-library-standard/pull/81)
* [Provide network driver templates](https://github.com/quattor/template-library-standard/pull/79)
* [document cvmfs helper functions](https://github.com/quattor/template-library-standard/pull/74)

### template-library-grid
* [**Worker Node:** update 'machine/job features' to current specification](https://github.com/quattor/template-library-grid/pull/180)

### ncm-ncd
* [**ComponentProxy:** report differences between profile and package version](https://github.com/quattor/ncm-ncd/pull/71)
* [Further Component cleanup](https://github.com/quattor/ncm-ncd/pull/70)
* [**NCM::Component:** remove template method](https://github.com/quattor/ncm-ncd/pull/68)
* [bump build-scripts to 1.50](https://github.com/quattor/ncm-ncd/pull/73)
* [**ncm-ncd:** set default lock wait to 15 minutes](https://github.com/quattor/ncm-ncd/pull/72)

### CCM
* [**DB:** refactor and cleanup](https://github.com/quattor/CCM/pull/106)
* [**Download:** don't create empty cache file when none existed before](https://github.com/quattor/CCM/pull/125)
* [**Element:** remove (unused) getUnescapedName method](https://github.com/quattor/CCM/pull/119)
* [**Fetch::Config:** existing attributes and parameters should precede resp parameters and configvalues](https://github.com/quattor/CCM/pull/117)
* [**Path:** support escape path and safe_unescape](https://github.com/quattor/CCM/pull/102)
* [**TextRender:** add support for converting list/nlist, incl TextRender element options](https://github.com/quattor/CCM/pull/96)
* [bump build-scripts to 1.50](https://github.com/quattor/CCM/pull/127)
* [**ccm:** cli should run in tainted mode](https://github.com/quattor/CCM/pull/118)

### maven-tools
* [**ProfileCache:** default ccm.cfg should have tabcompletion disabled](https://github.com/quattor/maven-tools/pull/105)
* [**Test::Quattor:** mocked FileWriter close handles backup](https://github.com/quattor/maven-tools/pull/103)
* [**Test::Quattor:** support mocked CAF::Path::move](https://github.com/quattor/maven-tools/pull/101)
* [**Test::Quattor::NoAction:** set NoAction independent of the CAF::Object::NoAction](https://github.com/quattor/maven-tools/pull/100)
* [**Test::Quattor::TextRender::Suite:** run tests in sorted order](https://github.com/quattor/maven-tools/pull/97)
* [**Test::Quattor::command_history_ok:** add 2nd nocommand argument](https://github.com/quattor/maven-tools/pull/102)
* [**mvnprove:** add -t option to generate the trace commandline](https://github.com/quattor/maven-tools/pull/98)

### aii
* [**Shellfe:** profileinfo from dir using dir:// cdburl](https://github.com/quattor/aii/pull/195)
* [**Shellfe:** profileinfo from dir using dir:// cdburl](https://github.com/quattor/aii/pull/191)
* [**Shellfe:** profileinfo from dir using dir:// cdburl](https://github.com/quattor/aii/pull/185)
* [**aii-ks:** fix yum install packages debug report message](https://github.com/quattor/aii/pull/177)
* [**aii-opennebula:** Include OpenNebula v5.0 support](https://github.com/quattor/aii/pull/192)
* [**aii-opennebula:** Include PCI Passthrough support](https://github.com/quattor/aii/pull/183)
* [**aii-opennebula:** Include regex support within aii config file](https://github.com/quattor/aii/pull/181)
* [**aii-opennebula:** Template cleanup](https://github.com/quattor/aii/pull/197)
* [**aii-shellfe :** add protected feature and move to module](https://github.com/quattor/aii/pull/190)
* [bump build-scripts to 1.50](https://github.com/quattor/aii/pull/198)
* [refactor aii-dhcp](https://github.com/quattor/aii/pull/186)

### release
* [**releaser:** Include opennebula when publishing aii templates](https://github.com/quattor/release/pull/251)
* [support CAF and CCM and pan annotations](https://github.com/quattor/release/pull/105)

### configuration-modules-grid
* [bump build-scripts to 1.50](https://github.com/quattor/configuration-modules-grid/pull/119)
* [**ncm-pbsclient:** add support for job_oom_score_adjust](https://github.com/quattor/configuration-modules-grid/pull/108)
* [**ncm-pbsserver:** cleanup handling of special/readonly node attributes](https://github.com/quattor/configuration-modules-grid/pull/107)
* [**ncm-xrootd:** manage sec.protocol config lines](https://github.com/quattor/configuration-modules-grid/pull/105)

### cdp-listend
* [bump build-scripts to 1.50](https://github.com/quattor/cdp-listend/pull/14)

### CAF
* [**FileWriter:** add support for keeps_state to override the global NoAction on per-file basis](https://github.com/quattor/CAF/pull/181)
* [**FileWriter:** support for setting file modification time via mtime option](https://github.com/quattor/CAF/pull/180)
* [**Kerberos:** support credential request and check](https://github.com/quattor/CAF/pull/179)
* [**Object:** add conditional log method](https://github.com/quattor/CAF/pull/176)
* [**Path:** support move method](https://github.com/quattor/CAF/pull/166)
* [**Process:** factor out LC::Process calls for consistent behaviour](https://github.com/quattor/CAF/pull/168)
* [**Reporter:** handle non-printable characters](https://github.com/quattor/CAF/pull/178)
* [bump build-scripts to 1.50](https://github.com/quattor/CAF/pull/184)
