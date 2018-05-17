---
layout: article
title: Installing Aquilon
modified: 2018-05-13
author: Luis Fernando Muñoz Mejías
menu: Installation
redirect_from:
  - /documentation/2012/10/31/install-aquilon.html
  - /documentation/2012/10/31/aquilon-prerequisites.html
---

{% include link_definitions.md %}

The instruction below describes how to install Aquilon from the sources and run it as a non-root user. Some
of the installation steps described here require that you can become `root` on the machine. The configuration of a
site with Aquilon is covered in a [specific page][aquilon_configuration].

*Note: the commands provided in this documentation are intended to be copy/pasted.*

## Install Required Packages

There are two set of packages required by Aquilon: the base OS packages and the Python dependencies. For the latter,
you have the choice between using RPM to install them **or** using the Python `pip` command, preferably in a Python
Virtual Environment. Both methods should work but `pip` is probably the easiest way to use the last version for
all dependencies as the RPMs are not always in sync with them.

Before starting with the package installation, you should ensure you have the following YUM repositories configured
on your machine:
* OS YUM repository
* EPEL7
* [Quattor EL7 x86_64 externals](http://yum.quattor.org/externals/x86_64/el7/)
* [Quattor EL7 noarch externals](http://yum.quattor.org/externals/noarch/el7/)

### Mandatory RPM Packages

Aquilon requires an EL7 system with at least the following RPMs installed. Use the `yum` command below to
check it they are installed and install the missing ones:

```bash
yum install ant-apache-regexp ant-contrib \
  gcc git git-daemon java-1.8.0-openjdk-devel libxslt libxml2 make panc \
  knc krb5-workstation \
  protobuf-compiler protobuf-devel \
  python-devel python-setuptools
```

You also need the following packages for Kerberos, depending on your
Kerberos infrastructure:
* If you don't use an external Kerberos server, you need to install the
server package:

    ```bash
    yum install krb5-server
    ```

* If you rely on Microsoft Active Directory:

    ```bash
    yum install msktutil
    ```

In addition, you need the package appropriate for the database backend that you choose. There are 2 options:

* SQLite: this is the easiest choice, as there is no configuration involved, if you want to build
quickly an Aquilon configuration for testing purposes but it is not recommended
for a production installation, especially a large one. In addition to the scalability limits, SQLite as no
incremental backup features and only a limited support for database upgrades (not all the features Aquilon rely
on for these upgrades, in particular for defining constraints, are available). To use SQLite, you need the
following package:

    ```bash
    yum install sqlite
    ```

* PostgresQL: this is a real database service, recommended for a production installation. It offers many advanced
administration features, including continuous backup. It requires an additional step to configure the server,
documented below. The required packages are:

    ```bash
    yum install postgres-devel postgres-server postgres-contrib
    ```

*Note: this is (almost) impossible to change the configuration backend of an existing database as there is
no easy way to dump the database with one backend and import it in another backend. Changing the backend
basically involves rebuilding the site configuration from scratch.*

If using a distribution other than EL7, you will need python 2.7.x (with virtualenv support installed) and git
1.7+.

### Using RPM

The first option to install the Aquilon Python dependencies is to use the `rpm` command. In this case, you
need to be `root` to install Aquilon.

RPMs to install are:

```bash
yum install python-dateutil python-lxml python-psycopg2 \
  python-coverage python-ipaddr python-mako python-jsonschema \
  PyYAML python-cdb python-twisted-runner python-twisted-web \
  protobuf-python python-pip
```

In addition install the `sqlalchemy` module from PyPI (the EPEL version is too old):

```bash
pip install sqlalchemy
```

### Using a Python Virtual Environment

The alternative to installing Python dependencies RPMs is to build a Python VirtualEnv. One advantage is rely on
the `PyPi` repository which contains the most recent version of all Python modules. It is also not
required to be `root` (but this is necessary for several other steps described here).

The main steps involved in the creation of the VirtualEnv are:

* Ensure that your system has the following packages installed or install them if it is not the case (the packages
  are required only during the installation process):
  * gcc
  * libxslt-devel (and its dependencies)
  * libyaml-devel
  * postgresql-devel
  * python-virtualenv

* Create the Python Virtual Environment and activate it. In this documentation,
we assume that the Virtual Environment is created
in `/var/quattor/aquilon-venv` directory but you can adapt the instructions in this documentation to the directory
you actually want to use:

    ```bash
    virtualenv --prompt="(aquilon) " /var/quattor/aquilon-venv
    . /var/quattor/aquilon-venv/bin/activate
    ```

* Ensure that you have the latest `setuptools`:

    ```bash
    pip install --upgrade setuptools
    ```
* Install Python dependencies with the `pip` command:

    ```bash
    pip install coverage
    pip install functools32
    pip install ipaddress
    pip install lxml
    pip install mako
    pip install jsonschema
    pip install psycopg2
    pip install protobuf
    pip install python-cdb
    pip install python-dateutil
    pip install pyyaml
    pip install sqlalchemy
    pip install twisted
    pip install virtualenv
    ```

## Configuring Database

This step applies only for installation using Postgres as their database backend (recommended, see above). After
installing the RPMs, it is necessary to initialize the Postgres environment and to create a database for Aquilon.
The main steps are:

* Initializing the Postgres environment:

```bash
/usr/bin/postgresql-setup
```

* Create a Postgres account for Aquilon. This must match the Linux user that will be used by the broker,
typically `aquilon`:

```bash
su - postgres -c 'createuser aquilon'
```

* Create the Aquilon database and define the account created previously as its owner:

```bash
su - postgres -c 'createdb -O aquilon aquilon'
```

* Enable and start the `postgresql` service:

```bash
systemctl enable postgresql
systemctl start postgresql
```

## Building Aquilon protocols

You need to build the Aquilon protocols Python module from sources with the following commands (**if using a VirtualEnv,
be sure that it is activated**):

```bash
cd your_work_directory
git clone https://github.com/quattor/aquilon-protocols.git
cd aquilon-protocols
./setup.py install
```

If you want the Python module to be installed in a location other than the default one for your Python
installation, add `--prefix` or `--install-base` option. The files other than the Python modules are not
really needed to run Aquilon.

## Installing Aquilon

To install Aquilon, clone its source repository. The following command will install Aquilon in
`/opt/aquilon`.

```bash
cd /opt/
git clone https://github.com/quattor/aquilon.git
```

It is possible to install Aquilon in another location: in this case, you must define `/opt/aquilon` as
a symlink to the directory containing the Aquilon repository.

### Installation Test

If the installation is done as root and all the dependencies (listed in `/opt/aquilon/setup.py`) have been installed
as RPM or using the `pip` command, there are no more installation steps to do and you should be able to run the
`/opt/aquilon/tests/dev_aqd.sh`. This command should fail with:

```
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) unable to open database file
```

Any other error means that something is wrong in the installation

## Broker Configuration


### Create the Broker Configuration

The Aquilon broker configuration file is `/etc/aqd.conf`.
A configuration template is distributed with Aquilon, `/opt/aquilon/etc/aqd.conf.noms`, and should work
as is if you use the standard directory layout for Aquilon and its data and a SQLite database:

* `/opt/aquilon`: Aquilon code
* `/var/quattor`: parent directory for all the Aquilon data directories (database, log files, templates...)

All the possible configuration options can be found in `/opt/aquilon/etc/aqd.conf.defaults`. To change
a default, define the corresponding setting in `/etc/aqd.conf` (but don't modify `/opt/aquilon/etc/aqd.conf.defaults`).
The main configuration options that you may want to change are:

* Database
  * SQLite: this is the default database backend, use `dbfile` in `[database_sqlite]` to specify a
  non standard database file by adding the following in `/etc/aqd.conf`:

    ```
    [database_sqlite]
    dbfile = /path/to/your/aquilon.db
    ```

  * Postgres: change the database backend and define the database name by adding the following sections to
  `/etc/aqd.conf`:

    ```
    [database]
    database_section = database_postgresql

    [database_postgresql]
    dbname = aquilon
    ```

* Directories for Aquilon data directories: `logdir`, `rundir`
* Pan compiler location: `pan_compiler`. It must be the path of panc jar file.
* Installation path of Aquilon protocols: `directory` in `protocols`section. It must reflect the
  installation path used previously, at the installation of the protocols. This is typically
  `/var/quattor/aquilon-venv/lib/python2.7/site-packages` if a
  VirutalEnv is used or `/usr/lib/python2.7/site-packages` otherwhise.

When defining paths, you can use variables défined in the `[DEFAULT]` section with the following syntax:

```
%(variable)s
```

The default configuration defines 2 such variables:

* `basedir`: Aquilon installation path (`/opt/aquilon`)
* `quattordir`: Aquilon data parent directory (`var/quattor`)

You can define other variables if convenient for your site and use them around the configuration.

### Configure the Kerberos Server

If you don't rely on an existing Kerberos server, you need to set up one. See the
following [instructions](http://tldp.org/HOWTO/Kerberos-Infrastructure-HOWTO/install.html).
In `/etc/krb5.conf`, change `server` to `servername` in [realms] section.*

*Note: if you install the Kerberos on a new machine with not a lot of activity, it may take
a while for the Kerberos database creation to complete, due to its need to wait for enough
randomness entropy. To speed up this process, you can follow the recipe in the following
[blog post](http://championofcyrodiil.blogspot.fr/2014/01/increasing-entropy-in-vm-for-kerberos.html.*).

Be sure to define properly the domain associated with your realm: it must match your actual
domain.

If you don't run as `root`, be sure to create a keytab for the current user.

### Create a User to Run the Broker

It is recommended not to run the broker as root. This cause quite a number of problem with
Kerberos in particular. This documentation assumes that the user is called `aquilon`
and it is recommended to keep this name.

First create a user with the `adduser` command, if you don't use a specific tool for this purpose:

```bash
adduser aquilon
mkdir /var/spool/keytabs
chown aquilon:aquilon /var/spool/keytabs
```

Then you need to create a Kerberos principal that will be used by the broker and create a
keytab that will be readable by the broker account. How to do this depends on the Kerberos
implementation used.

__MIT Kerberos__

If you use a standalone Kerberos instance, use the `kadmin.local` command. If you have
a central Kerberos infrastructure (the server is not on the Aquilon broker machine), use
`kadmin` instead.

```bash
bash> kadmin.local
kadmin.local: addprinc aquilon
kadmin.local: addprinc aquilon/your.host.fqdn
kadmin.local: ktadd -k /var/spool/keytabs/aquilon
kadmin.local: quit
bash> chown aquilon:aquilon /var/spool/keytabs/aquilon
```

The created principal can be used to execute `aq` commends, in particular to give admin rigths to
other principal with `aq permission`.

__Microsoft Active Directory__

If you use Microsoft Active Directory as your Kerberos infrastructure, you need to use the `msktutil`
tool.

* Create an Active Directory user that will be used by the broker, using the standard Active Directory tools
to create users. In this documentation, we assume that this account is `aquilon` but you can use whatever
name you want.

* Create the keytab for the broker account:

    ```bash
    su - aquilon
    kinit with a principal who has Active Directory admin rights
    msktutil --update --use-service-account --keytab /var/spool/keytabs/aquilon --service aquilon \
             --account-name aquilon --user-creds-only
    ```

* Restart the Aquilon broker

*Note: `msktutil` reinitializes the Active Directory account password with a random value, thus this account
cannot be used to run Aquilon client (`aq` command). **Be sure to use another principal** when initializing
the Aquilon database (next step) to ensure that you have at least one usable Aquilon administrator.*

### Create the Aquilon directories

Aquilon requires a few directories to be created for its internal data, the log files, the templates and, if
SQLite is used, for the database. All theses directories must be own by the `aquilon` account created before.
Based on the default configuration proposed, use the following commands to create those directories. Adapt
the directory paths to what you put in `/etc/aqd.conf` before.

    ```bash
    mkdir /var/quattor
    mkdir /var/quattor/domains
    # The following directory is needed only if the SQLite backend is used
    mkdir /var/quattor/aquilondb
    chown -R aquilon:aquilon /var/quattor
    ```


### Initialise the Aquilon Database

To create the Aquilon database:

```bash
mkdir -p /var/quattor/aquilondb
chown -R aquilon:aquilon /var/quattor
su - aquilon
# Activate the VirtualEnv is one is used
. /var/quattor/aquilon-venv/bin/activate
# kinit user must be either `aquilon` if you use a standalone Kerberos server or
# another valid principal if you have a central infrastructure (including Active Directory)
kinit        # Enter the password you set previously
/opt/aquilon/tests/aqdb/build_db.py
```

### Test The Broker

To test the broker, run `/opt/aquilon/tests/dev_aqd.sh` that must run successfully if your
installation is correct. Before running this script, you need to define `AQDCONF` environment
variable to `/etc/aqd.conf` (the script uses `/etc/aqd.conf.dev` by default).

To check that the broker is working properly, in another window, execute the
following command:

```bash
/opt/aquilon/bin/aq.py status
```

The command should return some information on your current Aquilon environment, without any error.
If this is the case, stop the broker started by the `dev_aqd.sh` script.


### Start the Production Broker

To start the production broker, a systemd unit file must be added. A template is provided in
`/opt/aquilon/etc/systemd/aquilon-broker.service`. Review its contents, in particular the
Python interpreter path, before copying the file to `/etc/systemd/system/multi-user.target.wants`.

*Note: if `/opt/aquilon/etc/systemd/aquilon-broker.service` doesn't exist, you may have to
retrieve it from [GitHub pull request](https://github.com/quattor/aquilon/pull/75).*

The aquilon broker service relies on `/etc/sysconfig/aqd` for its configuration. Create it from
the template in `/opt/aquilon/etc/sysconfig/aqd`, changing `TWISTD` to `/opt/aquilon/sbin/aqd.py` and ensuring
that other variables have a definition consistent with what is in `/etc/aqd.conf`.

Once this is done, use the following commands to add and start the broker service:

```bash
systemctl daemon-reload
systemctl start aquilon-broker
systemctl status aquilon-broker
```

Check the log file specified in `/etc/sysconfig/aqd` if `systemctl status` reports errors.

### Git Daemon Configuration

Create a bare Git repository in ``/var/quattor/template-king` that will be the master repository for
the templates and create its `prod` branch (which is expected to exist after the database
initialisation but is not created):

```bash
git init --bare /var/quattor/template-king
cd /tmp
git clone /var/quattor/template-king
cd template-king
# You can adjust the README contents if you want
echo "Aquilon templates master repository" > README.md
git add README.md
# If Git complains about missing user.email and user.name, define them (actual value does not matter)
git commit -am 'README added'
git push origin master:prod
```

By default Aquilon broker uses `trash` branch to take a snapshot of a domain before deleting it.
If you wish to disable this functionality, leave `trash_branch` option in the `[broker]` configuration section blank.
To use this feature (enabled by default), `trash` branch will need to be manually created as part of initial Git set up:

```bash
git push origin master:trash
```

Then start the Git daemon and test it:

```bash
git daemon --export-all --base-path=/var /var/quattor/template-king &
# The following command must return something other than an error...
git ls-remote /quattor/template-king
```

When the `git-daemon` has been successfully tested, stop it (kill the process) and edit `/etc/aqd.conf`
(`[broker]` section) to add the following configuration options if their default in
`/opt/aquilon/etc/aqd.conf.defaults` is not appropriate:
* Change `run_git_daemon` to `True`
* Check that `kingdir` value resolves to the actual location of the `template-king` repository created
previously
* Check the `git_daemon_basedir` value: it must be the `template-king` repository path prefix to remove for the
repository be accessible with the URL specified in `git_templates_url` (by default,
`//current_server/quattor/template_king`)


## Enabling SELinux

SELinux can be used in enforcing mode on the server hosting the Aquilon broker. In addition to all the steps described
above, it is necessary to adjust the SELinux type of a few directories, mainly:

* The directory containing the template-king Git repository must have the SELinux type `git_sys_content_t`. This can
be set with:

    ```bash
    chcon -R -t git_sys_content_t /var/quattor/template-king
    ```

* The `rundir` directory (defined in `/etc/aqd.conf`) must have the SELinux type `var_run_t`. This can
be set with:

    ```bash
    chcon -R -t var_run_t /var/quattor/run
    ```

## Upgrading Aquilon

Upgrading Aquilon involves mainly updating both Aquilon protocols and Aquilon itself and sometimes a database
schema upgrade. First step if to get the current version of Aquilon installed, using:

```bash
aq status
```

To upgrade Aquilon protocos and Aquilon itself, use Git to
get the last version of each one, executing the following command in the directory containing the
protocols sources and in `/opt/aquilon`:

```bash
git pull
```

For Aquilon protocols, follow the installation procedure above to rebuild and install the new version. Then, after
updating Aquilon itself, restart the broker:

```bash
systemctl restart aquilon-broker
```

To determine if a database upgrade is needed, go to directory `/opt/aquilon/upgrades` and look for directory names
matching a version greater than the one that was previously installed. If such directories exist, you need to execute
the SQL scripts (and sometimes Python scripts) they contain in sequence. Look at the `README` for more details.

*Note: up to version 1.12.58, the SQL script is only for Oracle and may require some tweaking for SQLite and
Postgres. In particular, SQLite has a very limited support for `ALTER TABLE` and doesn't support in particular
`ATLER TABLE table MODIFY` statement used to define a constraint. This produces an error that can be ignored.'

## Aquilon DB Configuration

See [starting a site with Aquilon][aquilon_configuration].


## Troubleshooting

### No known Aquilon administrator authorized

This may happend particularly if you executed `build_db` (database initialization) with the `aquilon` principal
when using Active Directory, as adding the entry in the `keytab` file will reset it password and changing the
password afterward will make the `keytab` file unsynchronized with Kerberos realm.

To workaround this and enable another existing
AD account (Kerberos principal) to act as the Aquilon admin, you will need to execute the following
steps on the database server using a user with modification rights on the Aquilon database. The broker must
be running. The database commands given are for SQLite backend, adapt them to your backend (for Postgres, this
typically involves executing `psql -d aquilon -c "sql command"` insted of
`sqlite3 /var/quattor/aquilondb` "sql command").

* `su -` to the `aquilon` account and execute `kinit` for the principal that you want to add as an Aquilon admin
* Execute command `aq.py status`: it should return that the principal is mapped to role `nobody`
* Assuming that the Aquilon DB is located in `/var/quattor/aquilondb` (see below) and that the
principal userid is `aqadm`, execute the following
commands:
    ```bash
    # Retrieve the ID associated with the role `aqd_admin`
    admin_role_id=$(sqlite3 /var/quattor/aquilondb "select id from role where name='aqd_admin';")
    # Retrive the ID associated with the principal that you want to modify
    admin_pri_id=$(sqlite3 /var/quattor/aquilondb "select id from user_principal where name='aqadm';")
    # Check that both IDs are defined (non empty value)
    echo $admin_role_id
    echo $admin_pri_id
    # If they are defined, update the role associated with the principal
    sqlite3 /var/quattor/aquilondb "update user_principal set role_id=${admin_role_id} where id=${admin_pri_id};"
    ```

