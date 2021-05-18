---
layout: article
title: Quattor 21.4.0 released
category: news
author: James Adams
---

Packages are available from our [yum repository](http://yum.quattor.org/21.4.0/), both the RPMs and the repository metadata are signed with [my GPG key](http://yum.quattor.org/GPG/RPM-GPG-KEY-quattor-jrha).

As always, many thanks to everyone who contributed! We merged 36 pull requests and resolved 6 issues.

The next release should be 21.6, take a look at the [backlog](http://www.quattor.org/release/) to see what we're working on.


Backwards Incompatible Changes
------------------------------

### configuration-modules-core
* [**ncm-opennebula:** include 5.12.x support](https://github.com/quattor/configuration-modules-core/pull/1456)

Changelog
---------

### template-library-core
* [Use github actions for tests](https://github.com/quattor/template-library-core/pull/206)
* [panc 10.7 is now the minimum supported compiler](https://github.com/quattor/template-library-core/pull/205)
* [**quattor/functions/hardware:** Provide function to get total system RAM](https://github.com/quattor/template-library-core/pull/204)

### configuration-modules-core
* [Replace travis checks with github action](https://github.com/quattor/configuration-modules-core/pull/1484)
* [**gh action test:** first download all maven dependencies](https://github.com/quattor/configuration-modules-core/pull/1495)
* [**ncm-authconfig:** sssd: remove unsupported force_timeout domain option](https://github.com/quattor/configuration-modules-core/pull/1421)
* [**ncm-ceph:** v1 no longer exists, switch to v2 as default](https://github.com/quattor/configuration-modules-core/pull/1506)
* [**ncm-grub:** set grubby rpm dependency](https://github.com/quattor/configuration-modules-core/pull/1505)
* [**ncm-metaconfig:** add geoip filter for logstash + fix tests](https://github.com/quattor/configuration-modules-core/pull/1485)
* [**ncm-metaconfig:** add support for slurm 20.11](https://github.com/quattor/configuration-modules-core/pull/1493)
* [**ncm-metaconfig:** dynaFile (rsyslog) is a name of a template, not a path](https://github.com/quattor/configuration-modules-core/pull/1486)
* [**ncm-metaconfig:** haproxy - add TLS ALPN extension options](https://github.com/quattor/configuration-modules-core/pull/1497)
* [**ncm-metaconfig:** haproxy add ssl-dh-param-file option](https://github.com/quattor/configuration-modules-core/pull/1503)
* [**ncm-metaconfig:** haproxy: add backend http-check support](https://github.com/quattor/configuration-modules-core/pull/1488)
* [**ncm-metaconfig:** httpd - add h2 options](https://github.com/quattor/configuration-modules-core/pull/1498)
* [**ncm-metaconfig:** mailrc - add missing ssl-verify option](https://github.com/quattor/configuration-modules-core/pull/1499)
* [**ncm-metaconfig:** nginx - add TLSv1.3 and dhparam options](https://github.com/quattor/configuration-modules-core/pull/1504)
* [**ncm-metaconfig:** pstats rsyslog input module](https://github.com/quattor/configuration-modules-core/pull/1491)
* [**ncm-metaconfig:** slurm setting escape fix](https://github.com/quattor/configuration-modules-core/pull/1422)
* [**ncm-metaconfig:** support running arbitrary commands in various steps](https://github.com/quattor/configuration-modules-core/pull/1451)
* [**ncm-network:** support IPIP tunnel](https://github.com/quattor/configuration-modules-core/pull/1501)
* [**ncm-opennebula:** RDM datastore support](https://github.com/quattor/configuration-modules-core/pull/1427)
* [**ncm-opennebula:** include 5.12.x support](https://github.com/quattor/configuration-modules-core/pull/1456)
* [**ncm-opennebula:** include OpenNebula 5.8.x and vmgroups support](https://github.com/quattor/configuration-modules-core/pull/1391)
* [**ncm-postgresql:** Add SSL certificate options to schema](https://github.com/quattor/configuration-modules-core/pull/1476)
* [**ncm-systemd:** Add support for mount, automount and timer units](https://github.com/quattor/configuration-modules-core/pull/1500)
* [**ncm-systemd:** Do not try to restart sevices which cannot](https://github.com/quattor/configuration-modules-core/pull/1407)
* [**ncm-systemd:** Perform actions one unit at a time](https://github.com/quattor/configuration-modules-core/pull/1376)
* [**ncm-systemd:** add support for resource control in units](https://github.com/quattor/configuration-modules-core/pull/1489)

### template-library-standard
* [merge ugent hardware templates](https://github.com/quattor/template-library-standard/pull/121)

### template-library-grid
* [Ensure GSISSH_PORT is a string](https://github.com/quattor/template-library-grid/pull/239)

### CCM
* [**TextRender:** support yaml multi document](https://github.com/quattor/CCM/pull/203)

### maven-tools
* [panc 10.7 is now the minimum supported compiler](https://github.com/quattor/maven-tools/pull/186)

### aii
* [Document use of RewriteRules to restrict access](https://github.com/quattor/aii/pull/329)

### release
* [panc 10.7 is now the minimum supported compiler](https://github.com/quattor/release/pull/337)

### CAF
* [**TextRender:** support yaml multi doc rendering](https://github.com/quattor/CAF/pull/274)
