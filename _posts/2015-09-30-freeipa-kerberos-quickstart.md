---
layout: article
title: FreeIPA with Aquilon quick start
category: documentation
author: Dimitrios Zilaskos
---

This page contains the steps for a quick EL6 FreeIPA installation and generation of a Kerberos keytab for use with Aquilon.

***This is just a quick start, security/reliability considerations are out of scope. The official FreeIPA documentation covers these topics. Refer to http://www.freeipa.org/page/Quick_Start_Guide***

* Install FreeIPA

```bash
yum install ipa-server

ipa-server-install -a VerySecretPassword --hostname=aquilon.example.com -r EXAMPLE.COM -p VerySecretPassword -n example.com -U
```

* Add a new principal (in our case:aquilon/aquilon.example.com)

```bash
ipa service-add --force
```

* Generate keytab

```bash
ipa-getkeytab -s aquilon.example.com -p aquilon/aquilon.example.com@EXAMPLE.COM -k /etc/krb5.keytab
Keytab successfully retrieved and stored in: /etc/krb5.keytab
```
