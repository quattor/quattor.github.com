---
layout: article
title: Installing Aquilon
modified: 2015-10-02
author: Luis Fernando Muñoz Mejías
menu: Installation
redirect_from:
  - /documentation/2012/10/31/install-aquilon.html
  - /documentation/2012/10/31/aquilon-prerequisites.html
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
[setting up your site][using_aquilon]
with Aquilon.

[using_aquilon]: /aquilon/site_configuration.html

You will need an EL7 machine with kerberos authentication working, either
with your own server or one provided by your institution.  
This is out of the scope of this document.

You will need a kerberos keytab for your server for service "cdb". You
can change it with environnement variable AQSERVICE.

## Installing Aquilon

With your basic OS installed you should add the
[Aquilon](http://yum.quattor.org/aquilon) and
[externals](http://yum.quattor.org/externals) Yum repositories to Yum:

Create the `/etc/yum.repos.d/aquilon.repo` file with the following content:
```
[aquilon]
name=Quattor - aquilon
baseurl=http://yum.quattor.org/aquilon/
enabled=1
gpgcheck=0
```

Create the `/etc/yum.repos.d/quattor_externals.repo` file with the following content:
```
[quattor_externals_x86_64]
name=Quattor - externals - x86_64
baseurl=http://yum.quattor.org/externals/x86_64/el7
enabled=1
gpgcheck=0
```

and then

```sh
$ yum -y install python-cdb python-twisted-web git postgresql-server aquilon-postgresql
```

Note:
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
$ exit
```

The last portion can be replaced by a schema in an existing database.

## Preparing the Kerberos authentication
Example using freeIPA:

Add the aqd service to your host and extract the keytab
```
kinit admin
ipa service-add aqd/AQUILON_SERVER_FQDN
ipa-getkeytab -s IPA_SERVER -p host/AQUILON_SERVER_FQDN@MY_REALM -k /etc/krb5.keytab
chgrp aquilon /etc/krb5.keytab
```
## Configuring the daemon

Next, edit `/etc/sysconfig/aqd` and adjust it to your needs.  The
default values should work on most EL7 setups.

Create the broker configuration file `/etc/aqd.conf`
Note:
You can find all the
available parameters and their defaults in
`/usr/share/aquilon/etc/aqd.conf.defaults`.  If any setting is not
correct for your environment, put the overriding value into the created configuration file.

Under the `broker` section, you have to declare the path to your
Keytab and the URL to the Git repository containing your Pan templates:

```ini
[broker]
keytab=/etc/krb5.keytab
git_templates_url=aquilon@localhost:/var/quattor/template-king
templatesdir=/var/lib/templates
```

Configure the connection to the database.  In
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
databases. The environment in this example is the "purpose" of this
broker and its associated database: production, unit testing,
end-to-end testing...

A final configuration file example:
```ini
[broker]
default_organization = MY_ORGANISATION
version = MY_BROKER_VERSION
keytab=/etc/krb5.keytab
#git_templates_url=aquilon@localhost:/var/quattor/template-king
templatesdir=/var/lib/templates
run_git_daemon=True
bind_address=IP_TO_BIND_TO
ant_options = -Xmx2560m -server

[database]
database_section=database_postgresql

[database_postgresql]
dbuser=aquilon
environment=prod
server=localhost

[tool_locations]
knc = /usr/local/bin/knc
klist = /usr/bin/klist
git = /usr/bin/git
git_path =/usr/libexec/git-core/
git_daemon = /usr/libexec/git-core/git-daemon
dsdb = /usr/bin/true
ssh = /usr/bin/ssh
java_home = /usr/lib/jvm/java-1.7.0
mean = /usr/bin/true
ant = /usr/bin/ant
ant_contrib_jar = /usr/share/java/ant/ant-contrib.jar
ant_home = /usr/share/ant

[panc]
pan_compiler = /var/quattor/panc/panc-10.3-jar-with-dependencies.jar
xml_profiles = false
json_profiles = true

# This can be used for any components that use python logging
# Valid values are INFO, DEBUG, and WARNING
# For sqlalchemy, only INFO and DEBUG produce log messages.
[logging]
sqlalchemy.engine = WARNING
sqlalchemy.pool   = WARNING
sqlalchemy.orm    = WARNING
aquilon = WARNING

[protocols]
directory = /usr/lib64/python2.7/site-packages/twisted/protocols

```

## Edit the startup script
Add the following code at the beginning of the file `/etc/init.d/aqd`
```bash
if [ ! -d /var/run/aquilon ];then
    mkdir -p /var/run/aquilon
    chown -R aquilon:aquilon /var/run/aquilon
fi
```
## Create required directories

Create log directory:

```bash
mkdir -p /var/log/aquilon
chown -R aquilon:aquilon /var/log/aquilon
```

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
designated by the `templatesdir` option specified in the aquilon config file and ensure that both the broker and the
user can write to it.  If all your users belong to the `aquilon`
group:

```bash
mkdir -p /var/lib/templates/{bart,homer,lisa,maggie,marge}
chown -R aquilon:aquilon /var/lib/templates
chmod -R 0770 /var/lib/templates/
```

## Filling in the database

The Aquilon database is a real inventory of your systems.  The first
time you fill it in will be a painful experience.  Check
[the guide on starting a site][using_aquilon]
for more information.

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
[have a site][using_aquilon].

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
