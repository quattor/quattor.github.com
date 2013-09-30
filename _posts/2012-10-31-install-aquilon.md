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
described in
[Aquilon Prerequisites](/documentation/2012/10/31/aquilon-prerequisites.html).

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
broker.  In PostgreSQL it would look like this:

```bash
$ su -l postgres
$ createuser -SRD aquilon
$ createdb --owner aquilon aquilon
```

The last portion can be replaced by a schema in an existing database.

### Initialising the database for the first time

After this, we have to create the structure of our database.  To do
it, first, get a Kerberos ticket as yourself.  **Warning!** This
principal will be granted full power over your Aquilon instance!
Next, we need a clone of the Git repository.  We'll edit the
`tests/aqdb/data/unittest.dump` to our liking.  It's just an example,
but try to add something that is already useful.

Finally, build the database:

```bash
cd aquilon/tests/aqdb
python build_db.py -D -p data/unittest.dump
```

**Warning!** The `-D` flag will erase an existing database!

**NOTE:** Should we package this initialisation script?

### Filling in the database

The Aquilon database is a real inventory of your systems.  The first
time you fill it in will be a painful experience.  You'll have to
provide it with:

* Organization name
* Continent(s)
* Hub(s)
* Country(ies)
* City(ies)
* Building(s)
* Room(s)
* Racks, with their location
* Vendors for different hardware components
* Models of different hardware components
* Chassis
* Machines
* Interfaces attached to each machine
* Hosts

A script to import most of this information from existing profiles is
under work.


### Upgrading the database schemas

New versions of Aquilon may change the database schemas.  The Git
repository contains an `upgrade` directory with scripts for guiding
the upgrade.  Follow the instructions in the README of that directory.

**NOTE** Should we include these scripts in the package?

## Quattor templates

**TODO** How should we share the templates we have at UGent?
