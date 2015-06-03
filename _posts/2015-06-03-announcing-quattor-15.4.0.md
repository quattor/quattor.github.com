---
layout: article
title: Quattor 15.4.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/15.4.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 118 pull requests and resolved 77 issues.

The next release should be 15.6 (theoretcially only three weeks away), take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Main New Features and Fixes
---------------------------
We are now building [client](http://yum.quattor.org/15.4.0/quattor-client-15.4.0-1.noarch.rpm) and [repository](http://yum.quattor.org/15.4.0/quattor-yum-repo-15.4.0-1.noarch.rpm) RPMs to allow existing hosts, VM images etc. to be payloaded more easily.

* `ncm-systemd` has been added to provide support for controlling systemd units.
* `ncm-opennebula` has been added to deploy and manage [OpenNebula](http://opennebula.org/) clouds.
* `ncm-metaconfig` has deprecated the `daemon` list in favour of the more useful `daemons` structure - users are encouraged to update their configuration.

Backwards Incompatible Changes
------------------------------
### ncm-metaconfig
* [**ncm-metaconfig**: service ganesha service change stat_exporter Access type](https://github.com/quattor/configuration-modules-core/pull/504)

Type changed from string to list of strings.

### ncm-opennebula
* [**ncm-opennebula**: Open vSwitch support and VNET pools](https://github.com/quattor/configuration-modules-core/pull/466)

Removed `type` from `opennebula_vnet` type definition as it was already deprecated and it not in later versions of OpenNebula.

This should not be a problem for most users as this is the first release featuring this component.

Full Changelog
--------------

### template-library-core
* [Add new schema attributes and other minor fixes](https://github.com/quattor/template-library-core/pull/67)
* [Restore addition python-elementtree on SL5](https://github.com/quattor/template-library-core/pull/68)
* [Support the ncm-module attribute for the structure_component type](https://github.com/quattor/template-library-core/pull/63)
* [included new type_uuid](https://github.com/quattor/template-library-core/pull/64)

### template-library-examples
* [Add repository snapshot templates for EL7 (and Condor)](https://github.com/quattor/template-library-examples/pull/24)
* [First release of OpenStack examples](https://github.com/quattor/template-library-examples/pull/20)
* [OpenNebula examples](https://github.com/quattor/template-library-examples/pull/23)
* [Update CPU templates to new namespace](https://github.com/quattor/template-library-examples/pull/25)
* [Use the new namespace for CPU](https://github.com/quattor/template-library-examples/pull/22)
* [**wmslb profile**: fix variable name defining the local config](https://github.com/quattor/template-library-examples/pull/26)

### configuration-modules-core
* [Add metaconfig usage tutorial](https://github.com/quattor/configuration-modules-core/pull/458)
* [Update all components to latest maven tools](https://github.com/quattor/configuration-modules-core/pull/489)
* [**ncm-authconfig**: Correct ldap object class for automount entries](https://github.com/quattor/configuration-modules-core/pull/471)
* [**ncm-authconfig**: switch to CCM::TextRender and TT unittests](https://github.com/quattor/configuration-modules-core/pull/498)
* [**ncm-autofs**: Add direct mount support](https://github.com/quattor/configuration-modules-core/pull/477)
* [**ncm-ccm**: support json_typed attribute](https://github.com/quattor/configuration-modules-core/pull/450)
* [**ncm-ceph**: Add `straw2` as possible bucket algorithm](https://github.com/quattor/configuration-modules-core/pull/478)
* [**ncm-ceph**: add some options needed for keyvalue and erasurecode](https://github.com/quattor/configuration-modules-core/pull/487)
* [**ncm-ceph**: add support for multiple gateways](https://github.com/quattor/configuration-modules-core/pull/443)
* [**ncm-ceph**: fix test_host_connection tries to access homeDir from wrong place](https://github.com/quattor/configuration-modules-core/pull/485)
* [**ncm-metaconfig**: CAF::TextRender only allows hashrefs as valid contents](https://github.com/quattor/configuration-modules-core/pull/488)
* [**ncm-metaconfig**: add service carbon-relay-ng](https://github.com/quattor/configuration-modules-core/pull/464)
* [**ncm-metaconfig**: add service ssh](https://github.com/quattor/configuration-modules-core/pull/470)
* [**ncm-metaconfig**: daemon user validation/deprecation should return true](https://github.com/quattor/configuration-modules-core/pull/511)
* [**ncm-metaconfig**: deprecate daemon property](https://github.com/quattor/configuration-modules-core/pull/479)
* [**ncm-metaconfig**: pass element instance to CCM::TextRender](https://github.com/quattor/configuration-modules-core/pull/475)
* [**ncm-metaconfig**: pass the contents as Element instance CAF::TextRender](https://github.com/quattor/configuration-modules-core/pull/467)
* [**ncm-metaconfig**: service ganesha service change stat_exporter Access type](https://github.com/quattor/configuration-modules-core/pull/504)
* [**ncm-modprobe**: fix for install, remove and options, added blacklist](https://github.com/quattor/configuration-modules-core/pull/449)
* [**ncm-mysql**: Flush privileges after user and database operations](https://github.com/quattor/configuration-modules-core/pull/486)
* [**ncm-mysql**: Schema fixes for `component_mysql_db_user` type](https://github.com/quattor/configuration-modules-core/pull/484)
* [**ncm-mysql**: allow an empty password for a DB user](https://github.com/quattor/configuration-modules-core/pull/507)
* [**ncm-network**: Add OpenVSwitch support for network interface](https://github.com/quattor/configuration-modules-core/pull/423)
* [**ncm-network**: add IPv6 support](https://github.com/quattor/configuration-modules-core/pull/461)
* [**ncm-network**: support EL7 generic eno devices](https://github.com/quattor/configuration-modules-core/pull/472)
* [**ncm-nfs**: Support PanFS mounts](https://github.com/quattor/configuration-modules-core/pull/453)
* [**ncm-nrpe**: Fix documentation issue](https://github.com/quattor/configuration-modules-core/pull/497)
* [**ncm-ofed**: support for more attributes](https://github.com/quattor/configuration-modules-core/pull/469)
* [**ncm-openldap**: Allow the checkpoint option to be set](https://github.com/quattor/configuration-modules-core/pull/410)
* [**ncm-openldap**: add checkpoint attribute](https://github.com/quattor/configuration-modules-core/pull/476)
* [**ncm-opennebula**: Open vSwitch support and VNET pools](https://github.com/quattor/configuration-modules-core/pull/466)
* [**ncm-opennebula**: Set oned.conf and more bug fixes](https://github.com/quattor/configuration-modules-core/pull/399)
* [**ncm-spma**: Restrict repository name](https://github.com/quattor/configuration-modules-core/pull/451)
* [**ncm-spma**: allow '.' in repository names](https://github.com/quattor/configuration-modules-core/pull/496)
* [**ncm-spma**: register for changes to /software/groups](https://github.com/quattor/configuration-modules-core/pull/490)
* [**ncm-spma**: remove call to resolve_pkg_rep](https://github.com/quattor/configuration-modules-core/pull/519)
* [**ncm-ssh**: Add support for AuthorizedKeysCommand* options](https://github.com/quattor/configuration-modules-core/pull/474)
* [**ncm-sudo**: Fix generation of parameter lists](https://github.com/quattor/configuration-modules-core/pull/465)
* [**ncm-symlinks**: documentation reformatting and clarification](https://github.com/quattor/configuration-modules-core/pull/500)
* [**ncm-sysctl**: NoAction and sysctl.d support](https://github.com/quattor/configuration-modules-core/pull/405)
* [**ncm-systemd**: initial support for systemd unit control](https://github.com/quattor/configuration-modules-core/pull/424)

### ncm-lib-blockdevices
* [Add methods to test for correct device, and add check for disk size](https://github.com/quattor/ncm-lib-blockdevices/pull/40)
* [Allow devpath variable interpolation in kickstart size check error message](https://github.com/quattor/ncm-lib-blockdevices/pull/46)
* [Blockdevices.pm: log message about undefined is_correct_device() method ...](https://github.com/quattor/ncm-lib-blockdevices/pull/48)
* [LV and LVM support force in kickstart](https://github.com/quattor/ncm-lib-blockdevices/pull/42)

### template-library-standard
* [Add gpt label support](https://github.com/quattor/template-library-standard/pull/53)
* [Fix horrible validation error for profile/env in cvmfs/client](https://github.com/quattor/template-library-standard/pull/52)
* [Move all CPUs into a manufacturer namespace and clean up the template contents](https://github.com/quattor/template-library-standard/pull/49)
* [**Quattor externals**: use official repos on yum.quattor.org](https://github.com/quattor/template-library-standard/pull/48)
* [Remove outdated frontier feature](https://github.com/quattor/template-library-standard/pull/51)
* [adding pakiti3 client support](https://github.com/quattor/template-library-standard/pull/50)

### template-library-grid
* [**Argus**: allow workarounds for performance issues](https://github.com/quattor/template-library-grid/pull/134)
* [Change the method how the WLCG repo name is defined](https://github.com/quattor/template-library-grid/pull/140)
* [**NFS client**: fix definition of NFS version to use (autofs)](https://github.com/quattor/template-library-grid/pull/142)
* [**WMS and LB**: use new (simpler) include syntax](https://github.com/quattor/template-library-grid/pull/143)
* [fix pbs static ldif paths when GIP_CE_USE_CACHE is true](https://github.com/quattor/template-library-grid/pull/137)
* [umd-3.htcondor](https://github.com/quattor/template-library-grid/pull/136)

### ncm-ncd
* [Cleanup the ComponentProxy _load method and unittests](https://github.com/quattor/ncm-ncd/pull/42)

### CCM
* [**CCM Fetch**: warn when dealing with "profiles from future" due to timesync issues](https://github.com/quattor/CCM/pull/52)
* [Fetch fix bug with templates from future](https://github.com/quattor/CCM/pull/56)
* [Support Element getTree convert functions for each TYPE](https://github.com/quattor/CCM/pull/51)
* [Support json_typed via config file](https://github.com/quattor/CCM/pull/48)

### maven-tools
* [Add Test::Quattor::Doc for documentation testing](https://github.com/quattor/maven-tools/pull/47)
* [Add improved methods for using TextRender TT tests in components](https://github.com/quattor/maven-tools/pull/48)
* [EL5/6 unittest fixes](https://github.com/quattor/maven-tools/pull/54)
* [Improve quattor logging during tests](https://github.com/quattor/maven-tools/pull/39)
* [Remove duplicate line causing 'variable masks earlier declaration' warnings](https://github.com/quattor/maven-tools/pull/51)
* [Test::Quattor::Object log history](https://github.com/quattor/maven-tools/pull/52)
* [Tidy up release steps](https://github.com/quattor/maven-tools/pull/50)
* [Use CCM::TextRender instead of CAF::TextRender in RegexpTest](https://github.com/quattor/maven-tools/pull/53)

### aii
* [**AII ks**: add lvmforce to schema and set the value for the rhel7rc variant](https://github.com/quattor/aii/pull/105)
* [**AII opennebula**: use cleaned up test methods](https://github.com/quattor/aii/pull/113)
* [Add support for locking down the bootloader](https://github.com/quattor/aii/pull/106)
* [Fix developer-info maven template in header](https://github.com/quattor/aii/pull/121)
* [**aii-ks**: Add disk size check](https://github.com/quattor/aii/pull/99)
* [**aii-ks**: Correct el7 variant from rhel7rc to el7](https://github.com/quattor/aii/pull/117)
* [**aii-ks**: ks-post-reboot should have proper unit on systemd ](https://github.com/quattor/aii/pull/103)
* [**aii-opennebula**: Include new install hook](https://github.com/quattor/aii/pull/112)
* [**aii-opennebula**: handle warnings and minor fixes](https://github.com/quattor/aii/pull/98)
* [**aii-pxelinux**: Include  configure hook](https://github.com/quattor/aii/pull/114)
* [**aii-pxelinux**: Include hook doc](https://github.com/quattor/aii/pull/123)
* [**aii-pxelinux**: add support for CentOS and Fedora variants](https://github.com/quattor/aii/pull/118)
* [**aii-web**: FIX errors and add JSON profiles suport](https://github.com/quattor/aii/pull/108)

### template-library-os
* [Fix EL7 support in OS templates](https://github.com/quattor/template-library-os/pull/69)
* [**OS_VERSION_PARAMS**: define 'family' key as 'el' (common to all RH derivatives](https://github.com/quattor/template-library-os/pull/68)
* [**OS_VERSION_PARAMS**: define 'family' key as 'el' (common to all RH derivatives)](https://github.com/quattor/template-library-os/pull/67)
* [**OS_VERSION_PARAMS**: define 'family' key as 'el' (common to all RH derivatives)](https://github.com/quattor/template-library-os/pull/66)

### release
* [Add pan annotation html documentation generator](https://github.com/quattor/release/pull/78)
* [Build packages for client and yum repositories](https://github.com/quattor/release/pull/64)
* [Improve build_all_repos script for EL5 and EL6](https://github.com/quattor/release/pull/88)
* [Package filtered copy of quattor-release](https://github.com/quattor/release/pull/100)
* [Replace original pom and release this repository](https://github.com/quattor/release/pull/98)
* [Run tests to produce metaconfig pan templates during release](https://github.com/quattor/release/pull/97)
* [Switch packaging from rpm to pom](https://github.com/quattor/release/pull/99)
* [Tag template-library-openstack during the release](https://github.com/quattor/release/pull/87)
* [more bugfixes for el5/el6 build all repos and the contextualisation script](https://github.com/quattor/release/pull/91)
* [releaser.sh: add template-library-openstack to the release](https://github.com/quattor/release/pull/89)

### configuration-modules-grid
* [**ncm-lcgbdii**: Only chown things that exist](https://github.com/quattor/configuration-modules-grid/pull/73)
* [Remove ncm-frontiersquid](https://github.com/quattor/configuration-modules-grid/pull/74)
* [Remove ncm-vomrs](https://github.com/quattor/configuration-modules-grid/pull/72)
* [**ncm-gip2**: fix typo in info message](https://github.com/quattor/configuration-modules-grid/pull/75)
* [**ncm-moab**: get moab includes working](https://github.com/quattor/configuration-modules-grid/pull/66)
* [**ncm-pbsserver**: power_state is also a unmodifiable attribute](https://github.com/quattor/configuration-modules-grid/pull/63)

### CAF
* [Add TextRender usage documentation](https://github.com/quattor/CAF/pull/84)
* [CAF::Process add missing execute() in "Piping in and out" pod section](https://github.com/quattor/CAF/pull/86)
* [Extend TextRender with make_contents postprocessing (and minor cleanup)](https://github.com/quattor/CAF/pull/87)
* [Remove stray quote in pom](https://github.com/quattor/CAF/pull/90)
* [**TextRender**: contents from Element instance and getTree convert options](https://github.com/quattor/CAF/pull/85)
