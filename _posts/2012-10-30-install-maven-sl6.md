---
layout: article
title: How to install maven in SL6
category: blog
---

Maven is not present in default repositories for SL6. For many people administrating and doing development with quattor it is convenient to develop in the same platform as the machines that are managed.

## Yum Repository configuration

	cat /etc/yum.repos.d/maven.repo

	# Note: Replaced $releasever with 6Server since SL's "6.2" doesn't work

	[epel-apache-maven]
	name=maven from apache foundation.
	baseurl=http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-6Server/$basearch/
	enabled=1
	skip_if_unavailable=1
	gpgcheck=0

	[epel-apache-maven-source]
	name=maven from apache foundation. - Source
	baseurl=http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-6Server/SRPMS
	enabled=0
	skip_if_unavailable=1
	gpgcheck=0

## How to install

Run:
	yum install apache-maven

You may need to relog for maven to be added to your enviroment variables.

### HTTP proxies

If you are behind proxy you need to edit  /usr/lib/jvm/java-1.6.0-openjdk-1.6.0.0.x86_64/jre/lib/net.properties or its equivalent. There are some environment variables too but they did not work for me. java.net.useSystemProxies=true with http__proxy environment variable worked.

