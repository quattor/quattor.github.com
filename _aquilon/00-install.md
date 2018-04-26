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


The instruction below describes how to install Aquilon from the sources and run it as a non-root user. Some
of the installation steps described here require that you can become `root` on the machine.

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


In addition, you need the following packages for Kerberos, depending on your
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

## Getting Aquilon sources

```bash
cd /opt/
git clone https://github.com/quattor/aquilon.git
```

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

Set up the aquilon broker configuration file.  There is an example
in `/opt/aquilon/etc/aqd.conf.defaults`.  Move this file to `/etc/aqd.conf`
and create a empty `/opt/aquilon/etc/aqd.conf.defaults` file
(or define the `AQDCONF` environment variable to point wherever it is
installed). The default will use a sqlite database back-end. Main required
changes are:

* `dsdb`: change to `/bin/true`
* `git_daemon`: change to `/usr/libexec/git-core/git-daemon`
* `ant_contrib_jar`: change to `/usr/share/java/ant/ant-contrib.jar`
* Comment out every else in the `tool_locations` section that point to a path
starting with `/ms`
* `pan_compiler`: change to `/usr/lib/panc.jar`
* `directory`(in `protocols`section): change to `/var/quattor/aquilon-venv/lib/python2.7/site-packages` if a
VirutalEnv is used else to `/usr/lib/python2.7/site-packages`

You may also want to adjust `basedir`, `quattordir` and `dbfile` to reflect your configuration if you don't locate
Aquilon-related data under `/var/quattor`.

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

`msktutil` reinitialize the Active Directory account password with a random value, thus this account
cannot be used to run Aquilon client (`aq` command). To workaround this and enable another existing
AD account (Kerberos principal) to act as the Aquilon admin, you will need to execute the following
steps once the broker has been started (see below):

* Execute `kinit` for the principal that you want to add as an Aquilon admin
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
* Restart the Aquilon broker

### Initialise the Aquilon Database

To create the Aquilon database:

```bash
mkdir -p /var/quattor/aquilondb
chown -R aquilon:aquilon /var/quattor
su - aquilon
# Activate the VirtualEnv is one is used
. /var/quattor/aquilon-venv/bin/activate
# kinit user must be either `aquilon` if you use a standalone Kerberos server or
# a valid principal if you have a central infrastructure (including Active Directory)
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
(`[broker]' section) as follow:
* Change `-run_git_daemon` to `True`
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
## Aquilon DB Configuration

See [starting a site with aquilon](http://www.quattor.org/documentation/2013/10/25/aquilon-site.html).
