---
layout: article
title: Installing Aquilon
category: documentation
modified: 2013-10-25
author: Luis Fernando Muñoz Mejías
---
## Introduction

This guide describes the process to install and have an Aquilon broker
started.  After reading this guide, you may want to continue
[setting up your site](/documentation/2013/10/25/aquilon-site.html)
with Aquilon.

You will need kerberos authentication working, either with your own
server or one provided by your institution.  This is out of the scope
of this document.

You will need a kerberos keytab for your server.

## Installing Aquilon

With your basic OS installed you should add the
[Aquilon Yum repository](http://yum.quattor.org/aquilon) to Yum, and
then

```sh
$ yum -y install aquilon-postgresql
```

If you want a different database backend, you may simply install the
`aquilon` RPM and then install the Python bindings to your database.
Currently, only Oracle and SQLite are supported.

## Dropping privileges

Aquilon shouldn't run with root privileges.  Just create an account
and a group for it.  In this guide will use `aquilon:aquilon`, and
we'll place its home directory in `/var/quattor`.  The account will
host our canonical Git repository, so we'll probably want to restrict
the shell to git-shell.

```sh
$ groupadd aquilon
$ useradd -s /usr/bin/git-shell -g aquilon -d /var/quattor aquilon
```
## Setting up the database

You have to create a role in your database server for the Aquilon
broker.  If you are using a local PostgreSQL instance, you'll probably do:

```sh
# su -l postgres
$ createuser -SRD aquilon
$ createdb --owner aquilon aquilon
```

The last portion can be replaced by a schema in an existing database.

## Configuring the daemon

Next, edit `/etc/sysconfig/aqd` and adjust it to your needs.  The
default values should work on most EL6 setups.

Then, edit the broker configuration itself.  You can find all the
available parameters and their defaults in
`/usr/share/aquilon/etc/aqd.conf.defaults`.  If any setting is not
correct for your environment, put the overriding value into
`/etc/aqd.conf`.

Under the `broker` section, you have to declare the path to your
Keytab and the URL to the Git repository containing your Pan templates:

```ini
[broker]
keytab=/etc/krb5.keytab
git_templates_url=someone@server:path/to/repo
```

Finally, configure the connection to the database.  In
`/etc/aqd.conf`, declare the section that configures your database,
like this for PostgreSQL:

```ini
[database]
database_section=database_postgresql
```

And fill the `database_postgresql` section with the appropriate
information:

```ini
[database_postgresql]
dbuser=aquilon
environment=prod
server=localhost
```

The defaults file contains all possible parameters for the supported
databases.

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
