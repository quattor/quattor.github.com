---
layout: article
title: Installing Aquilon
category: documentation
modified: 2015-10-02
author: Luis Fernando Muñoz Mejías
---

## Introduction

Aquilon is the third generation configuration datastore for Quattor
(The first generation being CDB and the second being SCDB).

It features a broker daemon which has overall ownership of the system
including template compilation. The broker stores specifc
configuration in a relational database, generating object templates
on-the-fly at compile time.

All user interaction takes place over a kerberos secured connection to
the broker, which delegates sandboxes (taking the form of git
repositories) when changes to pan templates are needed.

This guide describes the process to install and have an Aquilon broker
started.  After reading this guide, you may want to continue
[setting up your site](/documentation/2013/10/25/aquilon-site.html)
with Aquilon.

You will need an EL7 machine with kerberos authentication working, either
with your own server or one provided by your institution.  
This is out of the scope of this document.

You will need a kerberos keytab for your server for service "cdb". You
can change it with environnement variable AQSERVICE.

## Installing Aquilon

With your basic OS installed you should add the
[Aquilon](http://yum.quattor.org/aquilon) and
[externals](http://yum.quattor.org/externals) Yum repositories to Yum,
and then

```sh
$ yum -y install aquilon
```

If you want a different database backend, you may simply install the
`aquilon` RPM and then install the Python bindings to your database.
Currently, Oracle and PostgreSQL are supported, and SQLite is expected
to work for development environments.

## Setting up the database

You have to initialize the database and create a role in your database server for the Aquilon
broker. If you are using a local PostgreSQL instance, you'll probably do:

```sh
# su -l postgres
$ pg_ctl init
$ exit
# systemctl restart postgresql
# su -l postgres
$ createuser -SRD aquilon
$ createdb --owner aquilon aquilon
```

The last portion can be replaced by a schema in an existing database.

## Configuring the daemon

Next, edit `/etc/sysconfig/aqd` and adjust it to your needs.  The
default values should work on most EL7 setups.

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
git_templates_url=aquilon@localhost:/var/quattor/template-king
templatesdir=/var/lib/templates
```

Finally, configure the connection to the database.  In
`/etc/aqd.conf`, declare the section that configures your database,
like this for PostgreSQL:

```ini
[database]
database_section=database_postgresql
```

And fill the `database_postgresql` section with the appropriate
information.  For instance:

```ini
[database_postgresql]
dbuser=aquilon
environment=prod
server=localhost
```

The defaults file contains all possible parameters for the supported
databases.  The environment in this example is the "purpose" of this
broker and its associated database: production, unit testing,
end-to-end testing...

## Filling in the database

The Aquilon database is a real inventory of your systems.  The first
time you fill it in will be a painful experience.  Check
[the guide on starting a site](/documentation/2013/10/25/aquilon-site.html)
for more information.

## Initialising the repositories

Next is to initialise the 'template king', the "canonical" Git
repository controlled by the broker.  This is a bare repository in the
location specified by the `git_templates_url` configuration parameter
above.  In our case:

```bash
mkdir /var/quattor
cd /var/quattor
git init --bare template-king
chown -R aquilon:aquilon /var/quattor
```

After that, you have to prepare the directory that will contain your
sandboxes.  Create one directory per Aquilon user inside the directory
designated by `templatesdir`, and ensure that both the broker and the
user can write to it.  If all your users belong to the `aquilon`
group:

```bash
mkdir -p /var/lib/templates/{bart,homer,lisa,maggie,marge}
chown -R aquilon:aquilon /var/lib/templates
chmod -R 0770 /var/lib/templates/
```

Create missing run directory

```bash
mkdir -p /var/run/aquilon
chown -R aquilon:aquilon /var/run/aquilon
```

Create missing log directory

```bash
mkdir -p /var/log/aquilon
chown -R aquilon:aquilon /var/log/aquilon
```

## What's next

You can now start your broker daemon, with

```bash
service aqd start
```

Initialize the database

```bash
# aqdb_shell.py
aquilon@localhost> Base.metadata.create_all()
```

You can now test your installation with the following command

```bash
# aq.py status --noauth
Aquilon Broker Unknown
Server: aquilon.lal.in2p3.fr
Database: postgresql+psycopg2://aquilon:PASSWORD@localhost/
Sandboxes: /var/lib/templates
```

Next, you should learn how to
[have a site](/documentation/2013/10/25/aquilon-site.html).

## Adding more users

**TODO: move to  section dedicated to authentication and authorisation**

Authentication and authorisation are handled with `aq.py permission`.
You can see the already defined roles with `aq.py show_principal --all`.
And you can add and adjust permissions with:

```bash
aq.py permission --principal me@QUATTOR.ORG --role nobody --createuser
```

## FAQ

* `aq.py` gives me an error like `aq.py status exit with error : Server not found in Kerberos database`

  Your keytab is probably incorrect. Verify it with command

  ```bash
  [root@aquilon ~]# klist -k /etc/krb5.keytab
  ```

  You should see output similar to the following example:

  ```
  Keytab name: FILE:/etc/krb5.keytab
  KVNO Principal
  ---- --------------------------------------------------------------------------
     3 aquilon$@LAL.IN2P3.FR
     3 aquilon$@LAL.IN2P3.FR
     3 aquilon$@LAL.IN2P3.FR
     3 cdb/aquilon.lal.in2p3.fr@LAL.IN2P3.FR
     3 cdb/aquilon.lal.in2p3.fr@LAL.IN2P3.FR
     3 cdb/aquilon.lal.in2p3.fr@LAL.IN2P3.FR
```
