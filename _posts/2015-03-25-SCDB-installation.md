---
layout: article
title: Bootstrapping and Troubleshooting SCDB
category: documentation
author: Michel Jouvin
---

This page contains a step-by-step installation guide for Quattor SCDB, the second generation of Quattor configuration database,
and its associated deployment tools. It also contains some instructions to troubleshoot SCDB issues, in particular failure to deploy changes.

***SCDB is now considered a legacy configuration database. If you start a new site you are encouraged to look at [Aquilon](/documentation/2012/10/31/install-aquilon.html), the new configuration
database, that provides more flexible workflows and an improved scalability.***

SCDB relies on several underlying services not specific to Quattor, like Apache, Subversion,
DHCP, TFTP. Installing SCDB involves installing these services and configure them for Quattor use. As these services can be used for
other purposes than Quattor, the actual details of the service configurations can be potentially site-specific and instructions given here
may need to be adapted. For the sake of simplicity, the configuration steps for the underlying services assume that these services are
dedicated to Quattor.

The instructions in this documentation assume the following conventions:

* SVN server is `svn.example.org`. This clearly needs to be updated to reflect your host/domain name.
* The URL of the associated SVN repository is `http://svn.example.org/svn/quattor`: may be changed to suit your needs.
* TFTP server root directory is the default one, `/tftpboot`.

Having these services dedicated to Quattor is not at all a requirement. If you want to use an already existing instances of these services,
you'll need to tweak the proposed configuration to fit in your existing configuration. This may require information not present in this guide:
in this case refer to the service documentation. If you have no specific constraint and you aren't familiar with these services,
you are probably better to stick with a configuration as close as possible with the one used in examples.

*Note: this documentation tries to be as generic as possible as far as OS versions are concerned, but the commands used in examples have
been tested only on Scientific Linux 6.
They may need to be modified when underlying services like SVN or DHCP are hosted on another platform.*

**Important: when you will have succeeded in installing and configuring Quattor, it is recommended to add a profile for your deployment server so
that it will be managed by Quattor! This will help to keep it consistent and up-to-date.**


## OS Installation

To proceed with the next steps, you need to install a basic RHEL or derivative
server configuration by any means appropriate to you (CD-Rom, Kickstart, imaging...).
Configure the network according to your site requirements and ensure that you have
a network connection with the outside world.

### YUM Repositories

After doing the base OS installation, configure the two following YUM repositories by adding
the following files to `/etc/yum.repos.d`:

* EPEL

  ```bash
  # Adapt to your OS version if not using EL6
  # You may also want to use another EPEL mirror closer to you
  cat >/etc/yum.repos.d/epel.repo <<EOF
  [sl6_epel]
  name=sl6_epel
  baseurl=http://mirrors.ircam.fr/pub/fedora/epel/6/x86_64/enabled=1
  gpgcheck=0
  EOF
  ```

* Quattor

  ```bash
  cat >/etc/yum.repos.d/quattor.repo <<EOF
  [quattor_release]
  name=Quattor current release
  baseurl=    http://yum.quattor.org/current
  gpgcheck=0
  EOF
  ```

### Quattor RPMs

Use YUM to install the RPM required on a Quattor deployment server:

```bash
yum install aii-pxelinux ncm-ncd ncm-ccm
```

## Web Server Installation

The Quattor server needs to run a Web server to serve profiles,
kickstart configuration files and execute the CGI script at the end of
a host installation to change PXE boot to local disk. In addition,
you may want to use this Web server for serving YUM repositories if you
don't already have one for this purpose.

Web server installation requires nothing specific, just the
configuration of a document root with enough space if you plan to
serve RPMs and the configuration of the CGI script. This Web server can be
shared with other usages and you can use an Apache virtual host.

Apache is the recommended Web server (installation instructions in this documentation
refer to Apache) but nothing prevent you from using another one if you prefer and if
you know how to achieve the same configuration.

### Apache Recommended Settings

SCDB has no strong requirement concerning Apache configuration. It
needs two distinct URLs for two different purposes :

 * Profiles: host profiles are all stored under the same parent URL, for
   example `/var/www/quattor/profiles`.
   The files in this area are produced by the pan
   compiler when executing `ant deploy`.
 * Kickstart configuration files: this URL is used to store the
   Kickstart configuration file for each host, for example `/var/www/quattor/ks`. These files are
   produced by `aii-shellfe --configure`.

In addition, you may want to configure the area (*directory*) used for serving
YUM repositories if you use the same server for this.

Recommended setting for these areas are :

 * Restrict access to profile and Kickstart configuration to IP
   adresses (or subnets) matching Quattor-managed hosts, as these files may
   contain sensitive information like encrypted passwords or MySQL
   passwords (cleartext).
 * Configure all these areas to ignore any `index.html` file and
   auto-indexing.

Configuration for these areas is normally done by creating a file
`/etc/httpd/conf.d/quattor.conf` with directives like the following
ones (adjust to the path you are using):

```apacheconf
<Directory /var/www/quattor/profiles>
    Options Indexes
    DirectoryIndex VeryUnlikelyDirectoryIndex.none
    AllowOverride None
</Directory>

<Directory /var/www/quattor/ks>
    Options Indexes
    DirectoryIndex VeryUnlikelyDirectoryIndex.none
    AllowOverride None
</Directory>
```

*Note: if you are installing a new Apache server, don't forget to
edit `DocumentRoot` in `/etc/httpd/conf/httpd.conf` to reflect your
local configuration.*

*Note: even though it is generally easy to rebuild it, it is recommended to backup
`quattor.conf` file.*

## Subversion Server

There is no need for a Subversion server dedicated to Quattor. SCDB is
just one repository from the Subversion point of view. If you already
run a Subversion server, you can skip the installation part and go
directly to the configuration part.

### Subversion Installation and Configuration

There are many possible installation options for a Subversion
server. Our recommendation is to install it as an Apache module. There is
no requirement for the Subversion server to run on a Linux server,
even though that is the only installation option documented here. You can even
choose to use a Subversion server outside of your site, if you think
the network connection is good enough.

*Note: Quattor has no requirement regarding the name of the directory where SVN repository is located and
the URL associated with the repository. Even a repository non dedicated to SCDB (with already existing contents) can be used.
The examples in this page are based on a repository created as part of the SCDB installation and associated with URL
`http://svn.example.org/svn/quattor`. If you are not familiar with SVN and SVN management, you are probably better to use a configuration
as close as possible to the examples.*

If you need to install a Subversion server, use YUM. Don't forget to install the Apache module which is
in a separate RPM. A typical SVN installation is done with the following command:

```bash
yum install subversion mod_dav_svn
```

After installing, you have to configure the Subversion server. Refer to Subversion [web site](https://subversion.apache.org)
for details. Configuration the SVN server typically involves:
* Creation of directory which will be the parent for SVN repositories (this example uses `/var/svn`):

  ```bash
  mkdir -p /var/svn
  ```

* Create Subversion repository that will be used for the Quattor SCDB (don't forget to **backup this directory**):
  ```bash
  svnadmin create /var/svn/quattor
  # Repository must be owned by Apache account
  chown -R apache:apache /var/svn/quattor
  ```

Apache SVN module configuration (`/etc/httpd/conf.d/subversion.conf`)
must be edited to configure URL used by SVN (examples in this page assume this is `/svn`)
and bind it to the directory created at the previous step. A typical example, based on previously created repository
(adjust paths to reflect your configuration) is:

```apacheconf
<Location /svn>
   DAV svn
   SVNParentPath /var/svn

   AuthzSVNAccessFile security/svn-repositories-access

   AuthType        Basic
   AuthUserFile    security/passwd
   AuthGroupFile   security/group
   AuthName        "SCDB SVN server"

   # Limit write permission to list of valid users.
   <LimitExcept GET PROPFIND OPTIONS REPORT>
      # Require SSL connection for password protection.
      # SSLRequireSSL

      Require valid-user
   </LimitExcept>
</Location>
```

To configure SVN authentication for the SCDB repository, you need to
create one or more accounts in `/etc/httpd/security/passwd`. You can
use `htpasswd` or `openssl passwd -apr1` to generate an encrypted
password.

You also need to define SVN ACLs in
`/etc/httpd/security/svn-repositories-access`. To start, a typical file
is (it assumes the account you created is called `quattormgr`):

```cfg
[groups]
quattor-mgrs = quattormgr

[/]
* = r
@quattor-mgrs = rw
```

*Note: even though it is easily rebuilt, it is better to backup `subversion.conf` file and files in `/etc/httpd/security`.*

### Subversion repository configuration

For Quattor, you need to create a repository with the usual structure inside it (or inside a branch) :

 * `trunk`: where you make the changes to your running configuration
 * `tags`: used by SCDB administration tool to do deployment
 * `branches` (optional): for alternative developments

Assuming the repository has already been created (see previous step) and that its URL is `http://svn.example.org/quattor`,
one of the possible methods to initialise this structure is:

```bash
mkdir /tmp/scdb
cd /tmp/scdb
mkdir trunk
mkdir tags
mkdir branches
svn import . http://svn.example.org/svn/quattor --message 'Quattor repository layout initialised'
```

*Note: as stated previously, there is no need to dedicate a repository to SCDB and the same commands can be used to import a specific branch
in an existing repository.*

### SCDB Initialisation

If you followed this documentation and executed the step about [Subversion initialisation](#subversion-installation-and-configuration), you should have a Subversion
repository ready for use by SCDB. Be sure to use http/https to access the repository as  the standalone access won't work (this is a limitation of the build
script).

To create your initial SCDB with the standard templates and the associated examples, follow the following steps:

* In another directory, for example `scdb_src`, clone the `scdb` Git repository from [GitHub](http://github.com/quattor/scdb):

  ```bash
  git clone https://github.com/quattor/scdb.git scdb_src
  ```

* Go into the directory containing the clone and execute the command below to create your initial configuration database with SCDB tools,
the template library and the site template examples. The configuration database will be createad in directory `scdb` (you may use another name
but the next steps in documentation assumes this name). The directory must not exist (use option `-F` to remove it if it exists):

  ```bash
  cd scdb_src
  utils/scdb/create-vanilla-SCDB.sh -d ../scdb
  ```

* Checkout the empty SCDB trunk created during [Subversion configuration](#subversion-repository-configuration) in the same directory:

  ```bash
  cd ../scdb
  svn co http://svn.example.org/svn/quattor/trunk .
  ```

* Configure the repository to ignore some files produced when compiling, using the following command :

  ```bash
  cat > /tmp/ignore <<EOF
  .settings
  build
  build.saved
  deploy
  .project
  EOF
  svn propset svn:ignore -F /tmp/ignore .
  svn ci -m 'Add a .svnignore file appropriate for Quattor'
  ```

* Add everything to your repository with command :

  ```bash
  svn add *
  ```

* Commit your vanilla SDCB with :

  ```bash
  svn ci -m 'Create initial SCDB'
  ```


## SCDB Deployment Service Configuration

This section explains how to install and configure the scripts
use by SCDB deployment service. These two scripts communicate using either SSH
if they are executed on
different hosts or sudo if both run on the same host. Depending on
the method used, you will need to configure one or the other.

### Installation of deployment scripts

SCDB deployment uses a pair of cooperating scripts:

* SVN post-commit hook script: this script is launched when `ant deploy` creates a new deployment tag. This scripts run on the SVN server.
* Deployment script: this script is launched by the post-commit hook script to do the real work. It runs on the Quattor deployment server (which
may be different from the SVN server).

Both scripts are distributed as part of [SCDB](https://github.com/quattor/scdb) (directory `src/hooks`). They need to be copied at the appropriate
location on the appropriate server:

* The SVN hook script [src/hooks/post-commit.py](https://github.com/quattor/scdb/blob/master/src/hooks/post-commit.py) must be copied to the `hook`
directory of the SVN repository on the SVN server (using the naming convention of this guide, it would be `/var/svn/quattor/hooks`)
and given executable permission for Apache user.
* The other script, [src/hooks/build-tag.py](https://github.com/quattor/scdb/blob/master/src/hooks/build-tag.py) must be installed (root executable)
in `/root/quattor/scripts` on the Quattor server.

Both scripts use the same configuration file, `/etc/quattor-deploy.conf`, see SCDB
[server-side customisations](#scdb-server-side-scripts) for details. The configuration file is **required** (one must exist on each host
if you run SVN server and Quattor deployment server on different hosts).
If you use a configuration based on suggested defaults and a SVN server and Quattor deployment server co-located on the same host, a typical
configuration file is:

```cfg
[scdb]
# Update to reflect your configuration
repository_url=http://svn.example.org/svn/quattor

[build-tag]
# If not defined, defaults to parent of this build-tag script directory.
# If not starting with /, relative to parent of this build-tag script directory.
# Ensure the path exists.
svn_cache: /scratch/quattor-deployment/svncache
```

*Note: there used to be a Shell/Perl version of these scripts. These scripts are now **obsolete**. The configuration file format of the
new scripts is **different**, even though the name may be the same. Please upgrade to the last version if you are still using the old scripts.*

`build-tag.py` also requires the file `quattor.build.properties` to be created in the parent of the directory specified in `svn_cache` paramater
of the above configuration file.
A [template](https://github.com/quattor/scdb/blob/master/src/hooks/quattor.build.properties) of this file is available in SCDB distribution, in `src/hooks` directory.
It must be edited to reflect your local configuration.


### Creation of SSH Keys

*Note: this step is necessary only if the SVN server and the Quattor deployment server are not the same host.
Otherwise, it is recommended to use [#sudoConfiguration sudo] instead.*

When `ssh` is used between the SVN server and the Quattor server, it is necessary to configure SSH keys
to allow a password-less ssh connection (there is no way to enter a password in the script).
To configure these keys, you need to:

* Log under the deployment account on the Quattor deployment server, as specified in `/etc/quattor-deploy.conf` (`root` by default), and run the command:

  ```bash
  ssh -b 2048
  ```

* Log in to the Subversion server as the same user as your SVN server (generally Apache account), copy the file with extension `.pub`
generated in the previous step (to the directory `~/.ssh`)
* Try to ssh to the Quattor deployment server from the SVN server using the same account as
the one used by the deployment script. If it doesn't successfully to login without password, check your SSH configuration.

### sudo configuration

*Note: this step is necessary only if you use `sudo` for the communication between the SVN server and the Quattor deployment server.
This requires both services to run on the same host and is the recommended communication method in this situation. If both services
run on different hosts, you need to use and configure [ssh](#creation-of-ssh-keys) instead.*

To configure `sudo` for SCDB, use the `visudo` utility and enter the following lines in the `sudo ` configuration (be sure to
use the appropriate path and account in your configuration):

```
Cmnd_Alias   QUATTORDEPLOY=/root/quattor/scripts/build-tag.py *
apache ALL = NOPASSWD: QUATTORDEPLOY
Defaults:apache !requiretty
```

*Note: the last line is required:  if it is not given, `sudo` will silently fail.*

## Site Configuration

The parameters common to all hosts of several clusters are defined in a `site`. The examples used
to initialise SCDB previously will have created a site called `example`. To create your own site, the easiest method
is to copy the `example` site and customise a few files, as described below.

### RPM Repositories

Pan templates are used to define the YUM repositories that will be used install packages. You can find in the
[cfg/sites/examples/repository](https://github.com/quattor/template-library-examples/tree/master/sites/example/repository)
URLs of YUM repositories: they should provide a good starting poing for upstream repositories (and they should have
been copied to your site if you created it from the examples) but feel free to update the URLs if you know sources
more appropriate to your site. You should keep the same template name as they are the name expected by default
by other parts of the template library.

When you have successfully
configured your first node, you may want to look at how to use
[YUM repository snapshots](/documentation/2014/03/24/spma-yum-migration.html#managing-yum-snapshots) with Quattor.

*Note: if you use YUM snapshots that are not under the same path, be sure to add the required Apache configuration to serve them.*

### Basic System Configuration

Basic system configuration (network parameters, DNS servers, ...) are
grouped in templates `config.pan` and `global_variables.pan`  in the `site` subdirectory for
your site. Look at comments to understand what you need to modify.

### Middleware Configuration

If you wish to use Quattor to manage hosts running the EMI/UMD middleware, you need to define your
grid site configuration. This is done in the template
`site/glite/config.pan` found in your site directory. Look at
comments to understand what you need to modify.

*Note: do not be afraid of putting incorrect values in your gLite parameters, this can easily be refined later. As a general rule, keep the example values
if you don't understand how to change them.*


## Cluster Configuration

After creating your site, you need to create your first cluster. You
can do this by copying the `clusters/grid/umd-3` directory (or the cluster examples relevant to your use case), removing all profiles from `clusters/grid/umd-3/profiles` and customising a
few templates.

### Customise the associated site name

In each cluster, the file `cluster.build.properties` defines the site (or even sites) associated with the cluster.
Edit the file coming from the examples and replace site `example` by your site name (this is the name of the directory
under `site`).

*`cluster.build.properties` file allows to configure the Ant environment (properties) used to compile the cluster. One property that __must__ be
defined in this file is `cluster.pan.includes` which set the path used by the panc compiler to locate the templates.*

### Hardware description

You need to create a template describing the hardware configuration of
your machines. This is generally placed in the `hardware` sub-directory of
the site directory. Look at the examples, copy one with a configuration close to yours as a starting point. The name of the hardware template
is is internal and merely for convenience, it will be associated with a host name later. If your site has a convention for naming or tagging pieces of
hardware, it would make sense to use that here.

*Note: our recommendation is to derive the names of machines from their location rather than their hostnames as hostnames may be migrated
to different hardware later on.*

### Adding a machine to site/databases.pan

Before being able to configure the machine, you need to create an
entry for the machine name in both variables of
[databases.pan](https://github.com/quattor/template-library-examples/blob/master/sites/example/site/databases.pan). First variable defines the address associated
with the machine name, second variable defines the hardware template
associated with the machine.

In both variables, the key is the escaped host name. In the first case the value is an IP address, in the second it is the name of the template (relative to your site
name in sites directory) that you created in the previous step.

### Creating a Machine Profile

Copy an existing profile from examples corresponding to the machine type
you want to create.

*Note: when you have successfully configured a site BDII, the next recommended steps are a CE and a single WN.*

### Compiling and deploying the first profile

At this point you should be able to compile and deploy your first profile! With SCDB, this is
done with the command `ant deploy`. To execute successfully this command, you must first commit
your changes to Subversion. Good practice is to take the following steps to avoid committing
broken changes:

```bash
external/ant/bin/ant
# If/when compilation succeeded
svn commit -m 'Initial site configuration + first profile added'
external/ant/bin/ant deploy
```

*Note: you can also use `ant deploy` for the first step. Deployment will be blocked until the changes are committed.*

If the `ant deploy` succeeded, you should find a profile file created on the Quattor deployment server for the host
in the directory that you configured to store the profiles during Apache configuration (`/var/www/quattor/profiles`
based on the example provided). The profile name starts with the hostname, followed by the extension `.json`
(or `.xml` if you chose to use XML profiles). If you don't find a profile in this directory after a successful
execution of `ant deploy`, follow the instructions at the end of this page to troubleshoot the deployment
scripts.


## Configuration of Installation Service

AII, the Quattor service for automated installations, has a front-end, `aii-shellfe`, which
is responsible for configuring:

* DHCP and TFTP for PXE boot
* Kickstart for driving the installation process

In addition, it uses a CGI script which is called at the end of host installation to change the boot from
the installer to the local disk.


### DHCP configuraton

Install the DHCP server with the following YUM command:

```bash
yum install dhcp
```

If you had no DHCP server before, a basic DHCP configuration (`/etc/dhcp/dhcpd.conf`) follows
(update hosts/domain name/addresses appropriately):

```
# DHCP server configuration

authoritative;
allow bootp;
ddns-update-style none;

# Edit to reflect your DNS domain name and name servers (a comma-separated list is allowed)
option domain-name "example.org";
option domain-name-servers dns.example.org;
option netbios-node-type 2;

# Update to reflect your IP subnet
subnet 123.456.789.0 netmask 255.255.255.0 {
  option routers 123.456.789.1;
}

group {
  # Entries managed by Quattor and PXE parameters
  include "/etc/dhcp/dhcpd.quattor.conf";
}
```

We recommend using `/etc/dhcp/dhcpd.quattor.conf` for declaring static parameters related to PXE
or specific to DHCP usage by Quattor and including another file (`/etc/dhcp/dhcpd.aii.conf`) that
will contain the host entries managed by Quattor AII:

```
group {
  # Parameters for the installation via PXE using pxelinux
  filename                           "quattor/pxelinux.0";
  option vendor-encapsulated-options 01:04:00:00:00:00:ff;

  # This is required on RHEL/SL/SLC/CentOS 5.X
  next-server  tftp.server.example.org;

  # This is now a required line in DHCP configuration.  This
  # option gives the behavior of the previous versions.
  ddns-update-style ad-hoc;

  # Host entries managed by AII
  include "/etc/dhcp/dhcpd.aii.conf";
```

Create `/etc/dhcp/dhcpd.aii.conf` as an empty file. This file is the one you'll need to add in
`/etc/aii/aii-dhcp.conf` (see [below](#aii-shellfe-configuration)).

There is absolutely no reason to run a dedicated DHCP server for Quattor. Using the recommended
layout of DHCP configuration file makes easy to share a DHCP
server between Quattor and non Quattor usage. If you already have a DHCP server configured and running,
the proposed configuration should be easy to add: just include the proposed `/etc/dhcp/dhcpd.quattor.conf`
in your existing configuration.

See `man dhcpd` and `man dhcpd.conf` for details about DHCP server
configuration, in particular to support multiple subnets and other
advanced features.

### TFTPD configuration

Install the TFTP server with the following YUM command:

```bash
yum install tftp-server
```

The TFTP server is run by `xinetd`. In the default configuration provided by the OS installation, it is generally
disabled. Enable it by editing `/etc/xinetd.d/tftp`, modifying `disable` parameter from `yes` to `no`.

The option `server_args` allows the TFTP root directory to be defined. By default, it is `/tftpboot`. If you wish to use another location you will need
to update this option and to define the variable `AII_NBP_DIR` to refer to this directory during the [next step](#aii-shellfe-configuration).


### aii-shellfe configuration

This involves two separate steps :

* customisation of `/etc/aii/aii*.conf` files
* customisation of AII-related variables in templates

There are two AII configuration files that need to be customised to reflect your site configuration:

* `/etc/aii/aii-shellfe.conf`: a typical file follows, edit paths to reflect your configuration.

  ```
  # URL corresponding to compiled profiles generated by ant deploy
  cdburl=http://quattor.example.org/profiles
  # use_fqdn must be set to true
  use_fqdn=true
  # Directory where Kickstart configuration files produced by aii-shellfe should be written.
  # Must match the file system path served by the URL defined in the template variable `QUATTOR_PROFILE_URL`.
  osinstalldir = /var/www/quattor/ks
  # Directory where pxelinux.cfg is installed. The default location is recommended.
  nbpdir = /tftpboot/quattor/pxelinux.cfg
  ```

* `/etc/aii/aii-dhcp.conf`: check that `dhcpconf` and `restartcmd` commands match your configuration and edit them if necessary.
The file referred toby `dhcpconf` (`/etc/dhcp/dhcpd.aii.conf` if you used the suggested name when configuring DHCP server)
must be writable from the AII server. `restartcmd` may execute a command on a remote host
through appropriate means (for example, a SSH command without password).

In addition, there are a few variables to customise in site templates to reflect
your Quattor and AII configuration, mainly :

* `QUATTOR_PROFILE_URL` : URL to fetch host profiles from.
* `AII_OSINSTALL_SRV` : Fully-qualified domain name of the Web server serving OS rpms for the initial install (can be same as main repository server).
* `AII_KS_SRV` : Fully-qualified domain name of the Web server serving kickstart files. Defaults to `AII_OSINSTALL_SRV`
* `AII_ACKSRV` : Fully-qualified domain name of the Web server to use for the
   post-installation CGI. Defaults to `AII_OSINSTALL_SRV`
* `AII_ACKCGI` : post-installation CGI URL relative to the host part of `QUATTOR_PROFILE_URL`. Defaults to
   `/cgi-bin/aii-installack.cgi`.
* `AII_NBP_DIR` : path of the directory containing the PXE configuration for each host. Default: `/tftpboot/quattor/pxelinux.cfg`.

These variables are generally defined site-wide, in the template `global_variables.pan` located in the site directory. Examples are provided
in the SCDB distribution.

### Downloading the OS distribution's images

For every OS version you plan to deploy with Quattor, you should mirror the upstream YUM repository with appropriate tools if you don't have it already at your
site. Note that an OS-related YUM repository
is not made of single directory, so `wget` will not make a usable mirror. `reposync` is a better option. You may also look at
[sync_yum_repos](https://github.com/quattor/scdb/blob/master/utils/yum/sync_yum_repos) in SCDB which is a wrapper above `reposync` that
helps to automate repository mirroring or [mrepo](http://dag.wiee.rs/home-made/mrepo/)
which provides a framework for mirroring repositories from various sources.

Once you have the OS repository mirror available, you need to add the boot files used for the PXE installation to the AII server. They consist of two
files (`vmlinuz` and `initrd.img`)
generally located in the `images/pxeboot` directory of the distribution. You need to copy these files to a directory specific to the OS version/architecture that must be created in the
same directory as the `pxelinux.cfg` directory under the TFTP server root (see variable `AII_NBP_DIR` configured in  previous step for the exact path).
The directory name must have the usual Quattor format for OS version/architecture with all `-` replaced by `_` (e.g. sl530_x86_64).

### Post-installation CGI Script

At the end of a successful installation, as part of the Kickstart
post-installation script, a CGI script on the Quattor server is called by the host to change its PXE configuration to "boot from local disk".

*Note: it is recommended to define the PXE-enabled network interface as the first boot
device in the BIOS. Quattor will properly configure PXE to boot either from the local disk or from the installer
as requested by the `aii-shellfe` command.*

The script, [aii-installack.cgi](https://github.com/quattor/scdb/blob/master/src/cgis/aii-installack.cgi),
can be found in the SCDB directory `src/cgis`. It must be placed on the Web server running on the Quattor
server, in the directory for CGI scripts (by default `/var/www/cgi-bin/`).

The apache server must be able to run the script as root. The recommended configuration is to
have `sudo` installed and use `visudo` to add the following to
`/etc/sudoers`:

```
Cmnd_Alias   AIIACKCGI=/usr/sbin/aii-shellfe
apache ALL = NOPASSWD: AIIACKCGI
```


### Testing the installation service

On the AII server, run the following commands to test the installation service with the profile built
at the end of the [cluster configuration](#compiling-and-deploying-the-first-profile):

* Creation of Kickstart configuration file for the host: after a successful execution of the command, you should
find a file whose name is the hostname and whose extension is `.ks` in the directory referred to by `osinstalldir` in
`/etc/aii/aii-shellfe.conf`.

  ```bash
  aii-shellfe --configure your.host.domain
  ```

* Update of DHCP and PXE to have the host installed at next boot. Then reboot your host and check
that it installs properly.

  ```bash
  aii-shellfe --install your.host.domain
  ```

*Note: you can safely ignore any warnings from `aii-shellfe` about `base_url` not being defined.*

If the installation of your first host completes successfully, you have completed the installation of Quattor SCDB!

## SCDB Server-Side Scripts

This section describes the two scripts used by SCDB to trigger a Quattor deployment from the SVN server, how to customize them and how to
troubleshoot them. Refer to the previous sections for information on how to install them. These scripts are executed as a result of
entering command `ant deploy`.

### Subversion Hook Script

This script is triggered at the end of every commit: it is called a *post-commit* hook. It does nothing, except if called as a result of the command
`ant deploy`, when creating the deployment tag. Note that, as it is a *post-commit* hook, the commit succeeds even if the script encounters
an error. The main role of this script to launch the [deployment script](#deployment-script) after performing a few checks.

It must be installed on the Subversion server, inside the `hooks` directory of the SCDB repository (the storage directory of the repository itself,
not a working copy).
For this, you need a write access to the directory containing the repository on the Subversion server.
This script *must be* named `post-commit` and be executable by the account the SVN server is running under (typically the Apache account).
This script is released as part of [SCDB](https://github.com/quattor/scdb/blob/master/src/hooks/post-commit.py).

This script requires a configuration file, `/etc/quattor-deploy.conf` (common with the [deployment script](#deployment-script) when running on the
same host).
All the configuration options supported and their default values are defined at the beginning of the script. The configuration file has several sections.
One of them, `[scdb]`, is common to the hook script and the deployment script. The main options available and their default values are:

```cfg
[post-commit]
# Script launched by the script to actually do the deployment
deploy_script : /root/quattor/scripts/build-tag.py
# Name of the deployment server where to run the deploy_script. Used only with ssh.
# This can be a space-separated list (not yet implemented, see https://trac.lal.in2p3.fr/LCGQWG/ticket/46).
#deploy_server : quattorsrv.example.org
# Userid to use to run deploy_script
deploy_user : root
# notify_xxx are used to configure email notification in case of errors.
# If notif_from or notif_to is undefined, email notification is disabled
notif_mailer : localhost
#notif_from=Quattor Deployment <noreply@lal.in2p3.fr>
#notif_to=root@localhost
notif_subject_prefix : [Quattor-Deploy]
notif_subject : Failed to deploy revision %s of SCDB configuration
# Default should be appropriate. Set to false if your client doesn't handle properly returned output.
# When set to false, no message is printed on stdout, except if verbose is > 0.
report_error_to_svn: yes
# When false, ssh is used instead. This requires deploy_server to be defined too.
use_sudo : yes
# Log operations in /tmp/quattor-post-commit.log
verbose: 0

[ssh]
cmd: /usr/bin/ssh
options: -o PasswordAuthentication=no

[sudo]
cmd: /usr/bin/sudo
options: -H

[scdb]
# URL associated with the repository root
#repository_url: http://svn.example.com/scdb
# Branch where to create SCDB deployment tags
# Keep consistent with quattor.build.properties if not using default values.
tags_branch: /tags
# Branch corresponding to SCDB trunk (only branch allowed to deploy)
# Keep consistent with quattor.build.properties if not using default values.
trunk_branch: /trunk
```

The only required options for which no default value is provided is `repository_url` in the `[scdb]` section, which must match the root URL
of your SVN repository (as returned by `svn info`).

*Note on using `sudo`: recent versions of `sudo` disable the use of `sudo` without a tty by default. This **must** be changed in order to use `sudo`
in the context of the deployement script. To do this, run `visudo` and comment out the line `Defaults    requiretty`.*

### Deployment Script

This script is launched by the [hook script](#subversion-hook-script) and does the real work by updating the working copy of the SCDB repository on the Quattor server to the tag to created
by `ant deploy` and by calling the appropriate `ant` tasks.

It needs to be installed on the Quattor server and will be called through sudo or ssh by the hook script (you need to configure a SSH key without password between
your Subversion server and your Quattor server if ssh is used). The default location to install the script is `/root/quattor/scripts` but you can put it wherever you want
as long as you update the hook script configuration accordingly (see previous section). The source of this script is in [SCDB](https://github.com/quattor/scdb/blob/master/src/hooks/build-tag.py).

This script requires a configuration file, `/etc/quattor-deploy.conf` (common with the [hook script](#subversion-hook-script) when running on the
same host).
All the configuration options supported and their default values are defined at the beginning of the script. The configuration file has several sections. One of them, `[scdb]`,
is common to the hook script and the deployment script. The main options available and their default values are:

```
[build-tag]
# If not starting with /, relative to directory specified by option svn_cache
ant_cmd: external/ant/bin/ant
# ant options (passed through env variable ANT_OPTS)
#ant_opts: -Xmx2048M
# ant stdout: allow to redirect ant output to a file for debugging purposes (default is PIPE)
# Default changed to a file because of problem in subprocess module if the
# output is very large (Python 2.4) leading to the parent/child communication
# to hang.
ant_stdout: /tmp/ant-deploy-notify.log
#ant_stdout: PIPE
# ant target to do the deployment. Default should be appropriate.
ant_target: deploy.and.notify
# If not starting with /, relative to /usr/java.
java_version: latest
# If not starting with /, relative to parent of this directory script
svn_cache: svncache
# Number of retries for SVN switch to new tag in case of error
switch_retry_count: 1
# Verbosity level
verbose: 0

[scdb]
# URL associated with the repository root. Required parameter without default value.
#repository_url: http://svn.example.com/scdb
# Branch where to create SCDB deployment tags
# Keep consistent with quattor.build.properties if not using default values.
tags_branch: /tags
# Branch corresponding to SCDB trunk (only branch allowed to deploy)
# Keep consistent with quattor.build.properties if not using default values.
trunk_branch: /trunk
```

The only required options for which no default value is provided is `repository_url` in the `[scdb]` section, which must match the root URL
of your SVN repository (as returned by `svn info`).

This script needs to be able to find the file [quattor.build.properties](https://github.com/quattor/scdb/blob/master/src/hooks/quattor.build.properties)
in the parent directory of
the SCDB local cache (by default, the parent directory for this script location, explicitly defined by `svn_cache` in the script configuration file).


## Troubleshooting Server-side Scripts

In addition to the specific problems mentioned below, you may look at the [SCDB FAQ](https://trac.lal.in2p3.fr/Quattor/wiki/Doc/SCDB/FAQ).

If there is a problem during deployment, after entering command `ant deploy`, the command should return an explicit error message. In addition,
it is possible to optionally define a list of people who will receive an email when an error occurs. This is done with
`notify_to` configuration option of the [hook script](#subversion-hook-script).
If the `notify_to` people don't receive an email about the deployment failure,
check your SMTP configuration and your notification parameters.

*Note : a common error message is about the deployment script already running: as stated in the message, it is necessary to retry later
as only one deployment can occur at any time.*

To troubleshoot server side configuration problems, it may be necessary to manually execute the server-side scripts. When doing this, start by
testing `build-tag.py` and then the hook script, as explained in the following sections.

### Troubleshooting the deployment script

**To troubleshoot the deployment script, `build-tag.py`, you must log on the Quattor server as the user configured to run the
deployment script (generally `root`).**

The step-by-step procedure to troubleshoot the deployment script is as follows (commands given assume that the script is installed in `/root/quattor/scripts`):

1. Look in `/etc/quattor-deploy.conf` the location of the SVN cache on the Quattor server. If it is not defined, the default location is `/root/quattor/svncache`.
In the following steps, replace this default location by whatever is appropriate at your site.
1. Check the last tag checked out with the following command:

  ```bash
  svn info /root/quattor/svncache
  ---> look at the current tag name, everything after /tags/ in the URL (without the leading /)
  ```

1. Check the tag has been successfully checked out. If the following command updates anything or returns an error, it means the script attempt to switch to this tag
was unsuccessful. If the command fails again, retry it until it is successful. Failure to switch to a tag is generally related to a Subversion server problem,
not to Quattor itself : check Subversion server logs for more information.

  ```bash
  svn update
  ```

1. Try to redeploy the same tag, enabling verbose output, with the following command:

  ```bash
  /root/quattor/scripts/build-tag.py --debug TAG-VALUE
  ```

If the SVN cache is empty (not recognized as a valid SVN working copy by `svn info`), you need to identify the
last tag in `tags` branch of the Quattor SCDB repository using:

```bash
# Replace REPOSITORY_URL by `repository_url` value in the configuration file.
# YEAR is the four digit year number and month the two digit month number.
svn ls REPOSITORY_URL/tags/YEAR/MONTH
```

*Note: if you are still using the obsolete deployment script, `build-tag.pl`, these troubleshooting steps do not apply. You need to upgrade to current scripts first.*

### Troubleshooting the SVN hook script

**Most of the deployment problems, after initial configuration, are related to the [deployment script](#troubleshooting-the-deployment-script). As the hook
script mainly launches the deployment script, it is important to complete the checks described in the previous section before troubleshooting the
SVN hook script.**

The main cause of problems in the hook script is related to launching the deployment script from the hook script. The reason for the problems and the troubleshooting
steps are different whether you use `sudo` or `ssh` to run the deployment script on the Quattor deployment server.
 * `ssh`: the most common reason is invalid SSH keys for communication between the SVN server and the Quattor server or an invalid configuration.
 To troubleshoot this, log in to the Subversion server as the same user as your SVN server (generally Apache account) and try to ssh to the
 Quattor deployment server using the same account as the one used by the deployment script (typically  `root` but check your configuration file).
 * `sudo`: log in to the Subversion server as the same user as your SVN server (generally Apache account) and try to sudo under the deployment account
 (the one used to run the deployment script, typically `root` but check your configuration). One well-known issue with recent versions of `sudo` is
 that you need to enable the use of `sudo` by processes without a tty (this must be done with `visudo`, see [sudo configuration](#sudo-configuration) for details).

When you have confirmed the ability to successfully launch the deployment script, try to execute the hook script under the SVN server account. This involves the following steps:
1. Log on to the Subversion server as the same user as your Subversion server (normally the `apache` account).
1. Retrieve the repository revision associated with the last deployment tag. For this, you need to run the following command:

  ```bash
  # Replace REPOSITORY_URL by `repository_url` value in the configuration file.
  svn log --limit 1 REPOSITORY_URL/tags
  ```

1. Go to the `hooks` directory of Subversion SCDB repository and run the following command (`REPOSITORY_PATH` is the filesystem path to the repository) :

  ```bash
  ./post-commit --debug REPOSITORY_PATH REVISION
  ```

