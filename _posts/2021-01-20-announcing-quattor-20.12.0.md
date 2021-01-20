
---
layout: article
title: Quattor 20.12.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/20.12.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 69 pull requests and resolved 5 issues.

The next release should be NEXT.0, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### configuration-modules-core
* [** ncm-metaconfig:** update httpd apache ssl settings ](https://github.com/quattor/configuration-modules-core/pull/1390)
* [**ncm-ceph:** remove unsupported code (Jewel)](https://github.com/quattor/configuration-modules-core/pull/1462)
* [**ncm-metaconfig:** haproxy - add mode option for frontend and backend and ACLs](https://github.com/quattor/configuration-modules-core/pull/1400)

Changelog
---------

### template-library-core
* [Add NVMe to block device interface types](https://github.com/quattor/template-library-core/pull/203)
* [add caf_serviceaction type](https://github.com/quattor/template-library-core/pull/201)
* [**hardware types:** add options structure](https://github.com/quattor/template-library-core/pull/198)
* [**pan/types:** Add string type for search paths](https://github.com/quattor/template-library-core/pull/196)
* [**pan/types:** Cleanup style - lint, indentation, wrapping](https://github.com/quattor/template-library-core/pull/197)
* [**quattor/functions/hardware:** Provide function to get max_threads for all CPUs](https://github.com/quattor/template-library-core/pull/199)
* [**structure_software:** add new modules subtree for e.g. DNF modules](https://github.com/quattor/template-library-core/pull/202)

### configuration-modules-core
* [** ncm-metaconfig:** update httpd apache ssl settings ](https://github.com/quattor/configuration-modules-core/pull/1390)
* [Run Unit Tests in Docker using a GitHub action](https://github.com/quattor/configuration-modules-core/pull/1442)
* [**altlogrotate:** fix _glob handling multiple arguments](https://github.com/quattor/configuration-modules-core/pull/1444)
* [**ncm-altlogrotate:** allow yearly rotation](https://github.com/quattor/configuration-modules-core/pull/1449)
* [**ncm-authconfig:** sssd: add override_shell option](https://github.com/quattor/configuration-modules-core/pull/1457)
* [**ncm-ceph:** remove unsupported code (Jewel)](https://github.com/quattor/configuration-modules-core/pull/1462)
* [**ncm-cron:** Provide schema validation to match the component code](https://github.com/quattor/configuration-modules-core/pull/1431)
* [**ncm-download:** Fix white-space lint in test resources](https://github.com/quattor/configuration-modules-core/pull/1469)
* [**ncm-download:** support daemon actions on change](https://github.com/quattor/configuration-modules-core/pull/1454)
* [**ncm-gpfs:** add ib_rdma_monitor_portstate to mmsysmon config](https://github.com/quattor/configuration-modules-core/pull/1459)
* [**ncm-icinga:** add missing notification options](https://github.com/quattor/configuration-modules-core/pull/1433)
* [ncm-metaconfig generic templates](https://github.com/quattor/configuration-modules-core/pull/1394)
* [**ncm-metaconfig:** add chrony service](https://github.com/quattor/configuration-modules-core/pull/1473)
* [**ncm-metaconfig:** add conntrackd service and keepalived vrrp_sync_groups](https://github.com/quattor/configuration-modules-core/pull/1468)
* [**ncm-metaconfig:** add dellnetworking configuration](https://github.com/quattor/configuration-modules-core/pull/1406)
* [**ncm-metaconfig:** add mysql conf](https://github.com/quattor/configuration-modules-core/pull/1348)
* [**ncm-metaconfig:** allow auth_type 'CAS' in httpd schema](https://github.com/quattor/configuration-modules-core/pull/1447)
* [**ncm-metaconfig:** beats: Support metaconfig schemas for beat versions pre6.0, 6.{0, 1, 2} and 6.3+](https://github.com/quattor/configuration-modules-core/pull/1389)
* [**ncm-metaconfig:** dellnetworking: support disabling ipv6](https://github.com/quattor/configuration-modules-core/pull/1432)
* [**ncm-metaconfig:** devicemapper: fix bug in schema](https://github.com/quattor/configuration-modules-core/pull/1425)
* [**ncm-metaconfig:** haproxy - add mode option for frontend and backend and ACLs](https://github.com/quattor/configuration-modules-core/pull/1400)
* [**ncm-metaconfig:** httpd: add davrods (webdav for irods) config](https://github.com/quattor/configuration-modules-core/pull/1370)
* [**ncm-metaconfig:** httpd: support vhost serveralias and redirect](https://github.com/quattor/configuration-modules-core/pull/1475)
* [**ncm-metaconfig:** logstash 7.0 json filter](https://github.com/quattor/configuration-modules-core/pull/1423)
* [**ncm-metaconfig:** rsyslog kafka output action](https://github.com/quattor/configuration-modules-core/pull/1424)
* [**ncm-metaconfig:** singularity - add limit_container_groups](https://github.com/quattor/configuration-modules-core/pull/1441)
* [**ncm-metaconfig:** slurm topology schema and tt file](https://github.com/quattor/configuration-modules-core/pull/1434)
* [**ncm-metaconfig:** switch to CAF::ServiceActions](https://github.com/quattor/configuration-modules-core/pull/1341)
* [**ncm-metaconfig:** the content should not only be a dict](https://github.com/quattor/configuration-modules-core/pull/1387)
* [**ncm-metaconfig:** udev: add more udev rules](https://github.com/quattor/configuration-modules-core/pull/1460)
* [**ncm-metaconfig:** udev: add nvme to blockdev](https://github.com/quattor/configuration-modules-core/pull/1430)
* [**ncm-network:** always enable the network service](https://github.com/quattor/configuration-modules-core/pull/1402)
* [**ncm-network:** cleanup network interfaces with partition info in the name](https://github.com/quattor/configuration-modules-core/pull/1465)
* [**ncm-network:** support ethtool channels](https://github.com/quattor/configuration-modules-core/pull/1372)
* [**ncm-network:** support rules and routes using routing tables](https://github.com/quattor/configuration-modules-core/pull/1322)
* [**ncm-ntpd:** Add support for the 'interface' directive](https://github.com/quattor/configuration-modules-core/pull/1470)
* [**ncm-openvpn:** Modified to use generic "service" command rather than init.d script](https://github.com/quattor/configuration-modules-core/pull/1466)
* [**ncm-postfix:** add missing option to schema](https://github.com/quattor/configuration-modules-core/pull/1399)
* [**ncm-puppet:** Document string quoting behaviour](https://github.com/quattor/configuration-modules-core/pull/1417)
* [**ncm-shorewall:** add support for providers and rtrules configuration](https://github.com/quattor/configuration-modules-core/pull/1428)
* [**ncm-shorewall:** add support for snat and deprecate masq](https://github.com/quattor/configuration-modules-core/pull/1467)
* [ncm-spma DNF backend](https://github.com/quattor/configuration-modules-core/pull/1404)
* [**ncm-spma:** yumng improvements](https://github.com/quattor/configuration-modules-core/pull/1420)
* [**ncm-ssh:** Add schema entry for RevokedKeys option](https://github.com/quattor/configuration-modules-core/pull/1446)
* [**ncm-ssh:** add HashKnownHosts schema entry](https://github.com/quattor/configuration-modules-core/pull/1445)
* [ncm-symlink minor PAN template fixes](https://github.com/quattor/configuration-modules-core/pull/1411)
* [**ncm-systemd:** Add support for Socket in units](https://github.com/quattor/configuration-modules-core/pull/1448)
* [**ncm-systemd:** Allow Exec* becoming lists](https://github.com/quattor/configuration-modules-core/pull/1414)
* [**ncm-systemd:** add extra unit options for sandboxing](https://github.com/quattor/configuration-modules-core/pull/1396)
* [**ncm-systemd:** respect startstop when unitfile is changed](https://github.com/quattor/configuration-modules-core/pull/1453)

### ncm-lib-blockdevices
* [Accumulated changes](https://github.com/quattor/ncm-lib-blockdevices/pull/93)

### template-library-standard
* [Add Xeon Gold 5222](https://github.com/quattor/template-library-standard/pull/132)
* [Add template for NVMe devices](https://github.com/quattor/template-library-standard/pull/131)

### template-library-grid
* [Fix Travis configuration](https://github.com/quattor/template-library-grid/pull/235)
* [**umd-4:** Backport cleanup from umd-3 branch](https://github.com/quattor/template-library-grid/pull/231)

### CCM
* [**TextRender:** joincomma/joinspace should also work on TT scalars](https://github.com/quattor/CCM/pull/198)

### maven-tools
* [Update defaults for critic and tidy tests to off](https://github.com/quattor/maven-tools/pull/184)
* [Update tests and documentation to reflect critic and tidy tests being disabled](https://github.com/quattor/maven-tools/pull/185)
* [**render_test:** tool to render metaconfigservices for compiled profiles](https://github.com/quattor/maven-tools/pull/163)

### aii
* [**aii-ks:** Avoid spurious changes in the output](https://github.com/quattor/aii/pull/324)
* [**aii-ks:** Update regex tests to handle wipefs changes in ncm-lib-blockdevices](https://github.com/quattor/aii/pull/327)

### CAF
* [Add support for try-restart/condrestart](https://github.com/quattor/CAF/pull/273)


