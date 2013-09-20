---
layout: article
title: Installing Aquilon
category: documentation
---

## An introduction to installing Aquilon

This guide describes the manual installation of an Aquilon broker on a
Scientific Linux 6 host (It should work for any RedHat 6 clone), with
a PostgreSQL backend.  Pan templates automating this will be provided.

With your basic OS installed you should add the prerequisites
described in [Aquilon Prerequisites]({% post_url 2012-10-31-aquilon-prerequisites %}).

You will need kerberos authentication working, either with your own
server or one provided by your institution.  This is out of the scope
of this document.

You will need a kerberos keytab for your server.

## Installing Aquilon itself

The Aquilon broker and the protocol buffers associated to it can be
found [somewhere](http://some/one/has/the/rpm).

## Creating an account for aquilon

Aquilon shouldn't run with root privileges.  Just create an account
and a group for it.  In this guide will use `aquilon:aquilon`, and
we'll place its home directory in `/var/quattor`.

## Configuring the daemon

Next, edit `/etc/sysconfig/aqd` and adjust it to your needs.

Then, edit the broker configuration itself.  You can find all the
available parameters and their defaults in
`/usr/share/aquilon/etc/aqd.conf.defaults`.  If any setting is not
correct for your environment, put the overriding value into
`/etc/aqd.conf`.

## Setting up the database

You have to create a role in your database server for the Aquilon
broker.  For instance:

```bash
# su -l postgres
$ createuser -SRD aquilon
$ createdb --owner aquilon aquilon
```

The last portion can be replaced by a schema in an existing database.

### Filling in the database
