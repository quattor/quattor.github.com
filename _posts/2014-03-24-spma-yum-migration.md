---
layout: article
title: Migrating from SPMA-based to YUM-based deployments
author: Michel Jouvin
category: documentation
---

**We apologize but we are fighting with formatting issues in Jekyll: in the meantime, you may want to look at
https://github.com/quattor/quattor.github.com/blob/master/_posts/2014-03-24-spma-yum-migration.md.**

This documentation is a step-by-step migration guide from legcay SPMA-based package deployment to the new YUM-based deployment, covering both Quattor
configuration, OS configruation and grid MW configuration.

## Introduction

Starting with release Quattor 13.2, Quattor switched from legacy SPMA-based deployments to YUM-based deployments. One year later, YUM-based deployment is
the only supported method for several components of the template library, in particular OS templates and grid templates. 

Despite what may suggest the unchanged configuration module name for software deployment, ncm-spma, you cannot run both SPMA and YUM on the same machine.
Quattor 13.2 and later supports only YM-based deployments. Quattor 13.1.x series is the last version to
support SPMA-based deployment.

SPMA allowed a very tight control of the package list but at a very high price: you should provide a complete package list of all the main packages and
all their dependencies (and dependencies of their dependencies...). The maintenance cost of such list became to high to be sustainable and was a major
barrier for using Quattor for usages not covered for the template library.

On the other hand, YUM allows to build package list that contain only the (main) packages required for a service and is able to find all the required dependencies
and install them. In addition, at each run it can upgrade the packages to the last version available in the repositories. This simplifies a lot deployment of 
updates. But this changes a little bit the way you achieve a controlled deployment of packages with well defined upgrade times. What used to be done
by updating package list is now achieved through the use of immutable package repositories (also called YUM snapshots).

This documentation describes the main steps needed to update a machine from Quattor 13.1 and SPMA-based deployment to Quattor 14.2.1 or later) and 
YUM-based deployment. It also describes how to keep a unified deployment server for both Quattor versions. And it introduces some tools developed by the 
Quattor community to help managing YUM repositories and YUM snapshots.

__Short summary: all Quattor sites are encouraged to move quickly to Quattor 14.2.1 (or later) release and YUM-based deployment. Apart from a few operational
changes for a sustainable management of YUM snapshots, the change should be easy, with very few modifications required to your site configuration.__

_Most of the examples provided below assume a SCDB context. With small variations they apply the same way to Aquilon, except that the path where you put the templates may differ._


## Before Starting...

The first step is get a fresh copy of all the standard template libraries that will be used through the rest of this documentation. The easiest way to
do it is:

1. Clone SCDB repository from GitHub:

```bash
git clone https://github.com/quattor/scdb.git
```
1. Download the different template libraries that provide support for Quattor releases, OS versions, grid MW... (use --help for options but without options
this will put the downloaded materials in /tmp)

```bash
scdb/utils/scdb/create-vanilla-SCDB.sh --add-legacy
```

After this step, all the templates downloaded will be found under /tmp/scdb-vanilla/cfg (if you used the default location at previous step). This will be
referred to in this location as the "reference template directory". The cfg directory of your SCDB installation will be referred to as your "local configuration
database". And the examples also assume that you run commands fromthe parent of this directory, unless instructed otherwise.


## Upgrading to Quattor 13.1.3

If you know that all your existing machines are already configured with Quattor 13.1.3, you can skip this step.

Check if your local configuration database is already using the last template layout: if this is the case, you should have a quattor directory with one 
subdirectory per Quattor version in it (one of these directory could be called "legacy" and contain Quattor version older than 13.1). If you don't have 
this directory in your configuration database, you are still using the old configuration database layout. 

In both cases, proceed as follows:

1. Update the working copy of your local configuration database to last revision and compile it
```bash
svn update
external/ant/bin/ant
rm -Rf build.saved
cp -R build build.saved
```
1. Copy reference template directory "quattor" to your local configuration database or if you have it already, copy from the reference template directory
contents for version 13.1.3.
```bash
svn mkdir cfg/quattor       -----> If it doesn't exist yet
cp -R /tmp/scdb-vanilla/cfg/quattor/* cfg/quattor   ---> (you may want to restrict the copy to a particular directory
```
1. Add all the files to SVN:
```bash
svn add cfg/quattor (or svn add cfg/quattor/13.1.3)
```
1. Remove from standard directory in your local configuration database all templates now provided by the Quattor release templates:
```bash
svn rm cfg/standard/quattor
svn rm cfg/standard/pan
svn rm cfg/standard/components
```
1. Update repository/config/quattor.pan in your local standard directory with the reference version
```bash
cp /tmp/scdb-vanilla/cfg/standard/repository/config/quattor.pan cfg/standard/repository/config
```
1. From reference templates, copy sites/example/site/repository/quattor_13.1.2.pan to your sites/your_site/repository, review it for local customization
than may be required (but example should work) and add to SVN
```bash
cp /tmp/scdb-vanilla/cfg/sites/example/site/repository/quattor_13.1.2.pan cfg/sites/your_site/repository
svn add cfg/sites/your_site/repository/quattor_13.1.2
```
1. Update the file cluster.build.properties in all your cluster and add quattor/13.1.3 to the include path, just before standard, if you are converting
from the old layout or update the existing quattor/xxx to this version.
1. Compile the updated configuration and check that it completes successfully
```bash
external/ant/bin/ant
```
1. Compare the resulting profiles: differences should concern packages provided by Quattor release.
```bash
utils/profiles/compare_xml [-v]
```

Note that you can safely upgrade from Quattor versions prior to 13.1.3, including the so called legacy version, to 13.1.3 without any particular precaution.
This version is entirely compatible with previous one and the upgrade has already been done successfully at many different sites.


### Upgrade your Quattor deployment server to 13.1.3

To be able to deploy with the same deployment server both Quattor 13.1 and Quattor 14.2.1 nodes, you deployment server __must run__ version 13.1.3.
A deployment server running 14.2.1 (anything later than 13.1.x) __will not be able__ to deploy machines using Quattor 13.1.3 (or before).

_Note: an alternative is to have two deployment servers: one running 13.1.3 for nodes configured with Quattor 13.1.x (or before), one running 14.2.1 for nodes
configured with Quattor 14.2.1. As this may lead to some management complexity, this is not the recommended option and it is not described here._

If your deployment server is managed by Quattor (by itself!), this step should have already been completed as part of previous step. If this is not the case
you should consider doing it: this is the easiest way to maintain the Quattor deployment server after its initial installation.

If your deployment server is not managed by Quattor, the easiest way to upgrade it is to configure a YUM repository for the Quattor release. You can do this 
by creating a quattor.repo file in /etc/yum.repo.d with the following contents (repository for 13.1.3 is the same as for 13.1.2):
```
[quattor]
name=quattor
baseurl=http://yum.quattor.org/13.1.2
enabled=1
gpgcheck=0
```

Then run command:
```bash
yum update aii-server
```

## Upgrade templates from last version of the template library

### Upgrade cfg/standard to last version

A second step is to ensure that your local configuration database standard/ directory holds the last version of the template-library-standard repository.
As all the standard templates have been renamed with the .pan extension (instead of .tpl), you are recommended to follow the following steps for upgrading
your local copy of standard/:

1. Update the working copy of your local configuration database to last revision and compile it
```bash
svn update
external/ant/bin/ant
rm -Rf build.saved
cp -R build build.saved
```
1. Rename all your .tpl templates in standard/ into .pan. You can use the following command (ensure you are in a bash shell):
```bash
for file in `find cfg/standard -name '*.tpl'`; do svn mv "$file" "${file/%.tpl/.pan}"; done 
```
1. Recompile, check that no changes were involved in profiles and commit your renamed templates
```bash
external/ant/bin/ant
utils/profiles/compare_profiles    ---> should display no changed profiles
svn commit -m 'standard/ .tpl files renamed into .pan'
```
1. Replace your standard/ contents by the reference templates: this starts by deleting all the existing .pan files to allow further identification of removed
templates through SVN.
```bash
find cfg/standard -name \*.pan -exec rm {} \;
cp -R /tmp/scdb-vanilla/cfg/standard/* cfg/standard
svn revert --recursive cfg/standard/monitoring    ----> Version provided as part of the template library is unmaintained
svn status
# Review the changes:
#   - new templates: svn add
#   - missing templates: if they are site-specific (like HW description templates), "svn revert" them. Else "svn rm" them. 
```
1. Recompile, check that no unexpected changes were involved in profiles and commit your renamed templates. In particular check that there is
no change in the OS version used or in the kernel version (if there is something wrong, report it as an issue in repository template-library-standard).
```bash
external/ant/bin/ant
utils/profiles/compare_xml [-v]    ---> should display no changed profiles
svn commit -m 'standard/ .tpl files renamed into .pan'
```


### Add templates for Quattor 14.2.1

If you have not done it yet as part of the first steps, you need to add templates for configuring Quattor version 14.2.1. If you already have them,
you may want to ensure that you have the last version following the same procedure. This is easily done with:

1. Update the working copy of your local configuration database to last revision and compile it
```bash
svn update
external/ant/bin/ant
rm -Rf build.saved
cp -R build build.saved
```
1. Copy reference template directory "quattor/14.2.1" to your local configuration database quattor/ directory
```bash
cp -R /tmp/scdb-vanilla/cfg/quattor/14.2.1 cfg/quattor
```
1. Add all the files to SVN:
```bash
svn add cfg/quattor/14.2.1
```
1. Compile the updated configuration and check that it completes successfully
```bash
external/ant/bin/ant
```
1. Compare the resulting profiles: no profiles should be affected at this point.
```bash
utils/profiles/compare_xml [-v]
```
1. Commit changes
```bash
svn commit -m 'Add templates for Quattor 14.2.1'
```

### Add/update OS templates sl5.x and sl6.x

For managing deployment of machines with YUM, you also need a new generation of OS templates. There is one set of template per major OS version. Despite the
name, these templates should be usable to deploy any flavor of RH derivatives (SL, CentOS, RHEL). To install in your local configuration database these
templates, you need to:

1. Update the working copy of your local configuration database to last revision and compile it
```bash
svn update
external/ant/bin/ant
rm -Rf build.saved
cp -R build build.saved
```
1. Copy reference template directory "os/sl5.x-x86_64" and "os/sl6.x-x86_64" to your local configuration database os/ directory
```bash
cp -R /tmp/scdb-vanilla/cfg/os/sl5.x-x86_64 cfg/os
cp -R /tmp/scdb-vanilla/cfg/os/sl6.x-x86_64 cfg/os
```
1. Add all the files to SVN:
```bash
svn add cfg/os/sl5.x
svn add cfg/os/sl6.x
```
1. Compile the updated configuration and check that it completes successfully
```bash
external/ant/bin/ant
```
1. Compare the resulting profiles: no profiles should be affected at this point.
```bash
utils/profiles/compare_xml [-v]
```
1. Commit changes
```bash
svn commit -m 'Add new templates for SL5 and SL6'
```

### Add/update templates for EMI-3

If you are using Quattor to manage machines running the EMI grid MW, you'll have to upgrade your machine to the last version of the middleware, EMI-3.
To do this, you need to upgrade to a new generation of templates called umd-3. Despite the name, they deploy EMI-3 MW (which is basically the same as UMD-3).
The name has been changed to avoid confusion with the previous generation of templates, emi-1 and emi-2.

To install in your local configuration database these
templates, you need to:

1. Update the working copy of your local configuration database to last revision and compile it
```bash
svn update
external/ant/bin/ant
rm -Rf build.saved
cp -R build build.saved
```
1. Copy reference template directory "grid/umd-3" to your local configuration database grid/ directory
```bash
cp -R /tmp/scdb-vanilla/grid/umd-3 cfg/grid
```
1. Add all the files to SVN:
```bash
svn add cfg/grid/umd-3
```
1. Compile the updated configuration and check that it completes successfully
```bash
external/ant/bin/ant
```
1. Compare the resulting profiles: no profiles should be affected at this point.
```bash
utils/profiles/compare_xml [-v]
```
1. Commit changes
```bash
svn commit -m 'Add templates for EMI-3'
```


## Managing YUM Snapshots

While Quattor users generally would like to get rid of package lists difficult to maintain, they generally want to keep a full control of what version
of a package is deployed  and when an upgrade should happen. With YUM, if you use directly YUM repository mirrors they will be updated days after days
and machines will receive the updates when for some reasons ncm-spma runs as a result of some configuration changes. This is clearly not an expected
behaviour if you think that controlled deployment of packages is a critical feature for your configuration management tool.

With YUM, you can achieve a control of package deployment similar to SPMA by using YUM repository snapshots, referred as YUM snapshots in this documentation.
A YUM snapshot should be seen as an **immutable** YUM repository: as a result a machine associated with a YUM snapshot will never receive any 
package change, until you move it to a new snapshot. In fact this is a great concept and a great feature!

The drawback is that you need a tool to manage snapshots, else they will quickly turn into a management nightmare. There is no tools provided by YUM
directly to manage the snapshots but there are different possible technics. One possibility is to rely on filesystem-level snapshots (ZFS, LVM...): this
has the advantage that these snapshots are by definition immutable and zero-byte. But this is not always possible/desirable to use these features. For
example you may have to remount your file systems and find it not the appropriate method for you.

Another approach is to create snapshots as hard links to the YUM repository mirror. This way this is transparent to YUM and also zero-byte. It is not
immutable by design but you can decide not to update a snapshot. This approach is described here, based on using a script developed as part of Quattor
and part of SCDB repository, even though it has nothing specific to SCDB. This tools is `yum_snapshot`, located in directory `utils/misc` of the SCDB
repository.

Another decision you will have to make with snapshots is how you organize them. Generally they are organised by the date they were created. 
You may be temptated by having separate snapshot dates for different repositories. This is really up to you to decide. But you should keep in mind
that snapshots are essentially zero-byte and pretty quick to create. Thus, as a recommended starting point, it is better to snapshot all the repositories
you are using in the same operation, at the same date, as a consistent set of packages that are known to work properly with each others.

*Immutable* is the key word here. If something goes wrong with one of your snapshot (for example a problem in one of your repository, a package conflicting
with others...), you should resist updating the snapshot (meaning that you will have no way to trig a deployment of a new package) and just create
a new snapshot with the fixed repository (and all the others). Then you can move your machines to the new snapshot, this will be seen as a configuration
change and the package deployment will happen immediately at the time you have choosen for the deployment.

### yum_snapshot script 

This script developed as part of Quattor to help with the YUM snapshot management has nothing Quattor specific. It is build over the idea that you have a
local mirror of all the YUM repository you are using and if builds *in the same file system* as the mirror a snapshot for the mirror you specify.
This is done by reproducing the repository structure of the mirror and creating a hard link for every file found. At the end, except if it is an 
OS repository, YUM metadata are updated using another script, `update_yum_repos` (at the same location), that you need to install at the same place as 
`yum_snapshot`.

_Note: how to manage mirrors is outside the scope of this documentation. If you are using a SL6 machine to manage your YUM mirros, you can use `yum-repo`
tool that can be installed from EPEL. If you are using a SL5 machine, you can use  `wget --mirror` for repositories accessible by http. You can also
have a look to the Quattor tool, `yum_mirror_upstream` (also at the same location as other scripts mentionned here).

yum_snapshot accepts the following options:
```
Usage:    yum_snapshot [--snapshot-dir /path/to/snapshot] [--update] [--previous snapshot] [--verbose] --snapshot-name snap_name repository_path
```
* `--snapshot-dir` specificies the directory parent of every snapshot. Under this parent, the script creates one directory per day a snapshot is created.
And the snapshot itself is put under this date directory (flat directory for all snapshots). 
* The YUM snapshot name, specified by 
`--snapshot-name`, is the YUM repository name of the snapshot.
* `repository_path` is the path of the YUM mirror
* `--previous-snapshot` can be used to start the new snapshot from the contents of a previous one, including the metadata. This may speed up the
metadata update.

'Note: for OS repositories, the YUM mirror path specified must be the directory containing the repodata and Packages directory, not the Packages
directory itself.'

## Updating machines to YUM-based deployment

The procedure below describes how to set up a test environment for the new version and then proceed with the upgrade. Not that there is very little
things really specific to upgrading to YUM-based deployment. And this upgrade, as showed below, should only very limited changes to your local
configuration.

_Note: in addition to the steps described below, you may want to rename your .tpl files to .pan. Follow the instructions given above for standard/
directory._

As uusal, before starting, prepare your local working copy:
```bash
svn update
external/ant/bin/ant
rm -Rf build.saved
cp -R build build.saved
```

### Creating a new cluster

The easiest way to test the new configuration is to create a new cluster from an existing one. Assuming you have a cluster called emi-2 that you
want to upgrade to emi-3, you can do the following:

1. Copy the existing cluster (adapt to your local configuration)
```bash
svn cp cfg/clusters/emi-2 cfg/clusters/emi-3
```
1. Remove profiles (change .pan to .tpl in the following command if you have not done the rename)
```bash
svn rm --force cfg/clusters/emi-3/profiles/*.pan
```
1. Edit the cluster cluster-info.pan (in cfg/clusters/emi-3/site/) and add the following variables:
```
# Use OS templates for generic major version (required)
variable OS_FLAVOUR_ENABLED ?= true;

# Better defined a the node profile but you can define it here
# for simplicity to start...
variable AII_V2_INSTALL ?= true;

# YUM Repository snapshots (match your local configuration, see previous section on YUM snapshots)
# YUM_SNAPSHOT_DATE is typically used in repository templates to build the full URL of the snapshot
# See template-library-examples repository
variable YUM_SNAPSHOT_DATE ?= '20140316';
# Allows to use the same snapshot for initial installation and later deployments.
variable AII_OSINSTALL_ROOT = '/yum/snapshots/'+YUM_SNAPSHOT_DATE;
```
1. Commit the new cluster (required before next step)
```bash
svn commit -m 'Adding cluster emi-3'
```
1. Choose one test machine in your original cluster and move it to the new one   
```bash
svn mv cfg/clusters/emi-2/profiles/mytest.dom.ain.pan cfg/clusters/emi-3/profiles
```

### Updating the new cluster build properties

Edit the new cluster file cluster.build.properties with the following changes
* In the include patch, change the grid version used to grid/umd-3 and the Quattor version to quattor/14.2.1
* Add the following line:
```
cluster.pan.dep.ignore=""
```

This new line is required to ensure that any change to a template defining a YUM repository will trig a profile recompilation. This is not the default
behaviour as it was useless with SPMA. For this to work, you may have to update quattor.build.xml from /tmp/scdb-vanilla in the top directory of your 
SCDB installation.


### Updating node OS version

In the template defining the machine OS versions (by default cfg/sites/yoursite/site/os/version_db.pan), change the OS version used by your machine to
the actual version you want to use. It can be something like "sl640-x86_64" or "sl6x-x86_64" if you want to use the SL6x version (no dot between 6 and x).

_Note: sl5.x-x86_64 and sl6.x-x86-64 are not valid OS versions. They are only template sets that are used to install respectively any SL5 or SL6 version
when variable OS_FLAVOUR_ENABLED is true._

### Testing

You should be done and ready for testing. For the initial machine, it is recommended to reinstall it to test the full chain. Testing includes:

1. Compile the profile of your test machine
```bash
external/ant/bin/ant
```
1. Compare the resulting profiles: only the test machine should be affected, changes should affect mostly package list.
```bash
utils/profiles/compare_xml [-v]
```
1. Commit changes
```bash
svn commit -m 'Test machine for emi-3 cluster'
```
1. Deploy changes
```bash
external/ant/bin/ant deploy
```

To reinstall the machine, connect to the deployment server and run aii-shellfe as usual.

### Migrating other nodes

This is no more  than moving profiles from the old cluster to the new one.


### Upgrading rather than reinstalling

For some nodes, like disk servers, you may want to avoid reinstallation. This is possible but will require a manual intervention on the node (thus it is
not appropriate to a large number of WNs for example). To do this, you should keep the same OS version deployed on the machine, compile the new profiles
and deploy them. Once they have been deployed, connect to the machine, that should have received the new profile and failed to deploy it as the package
list is not compatible with SPMA that is still running on the machine. Then:

1. On SL5, remove perl-AppConfig-caf and upgrade YUM (URL given for SL5x, update to your version if necessary but should work with any SL5)
```bash
rpm -e --nodeps perl-AppConfig-caf
rpm -e --nodeps yum-conf
rpm -U http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl5_addons/yum-3.2.29-9.el5.noarch.rpm \
       http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl5_addons/yum-utils-1.1.31-4.noarch.rpm \
       http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl5x-x86_64/SL/yum-priorities-1.1.16-21.el5.noarch.rpm \
       http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl5x-x86_64/SL/yum-versionlock-1.1.16-21.el5.noarch.rpm \
       http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl5_epel/python-kitchen-1.1.1-1.el5.noarch.rpm
```
1. If libtorque is installed on the system, remove it:
```bash
rpm -e --nodeps libtorque
```
1. Install new ncm-spma dependencies from EPEL
```bash
# SL5
rpm -U http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl5_epel/perl-Set-Scalar-1.25-1.el5.noarch.rpm \
       http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl5_epel/perl-AppConfig-1.64-1.el5.noarch.rpm \
       http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl5_epel/perl-File-HomeDir-0.86-1.el5.noarch.rpm
# SL6
rpm -U http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl6x-x86_64/Packages/perl-AppConfig-1.66-6.el6.noarch.rpm \
       http://quattorsrv.lal.in2p3.fr/yum/snapshots/20140316/sl6_epel/perl-Set-Scalar-1.25-2.el6.noarch.rpm
```
1. Upgrade ncm-spma to last version:
```bash
rpm -U http://yum.quattor.org/14.2.1/ncm-spma-14.2.1-1.noarch.rpm
```
1. Reconfigure the node with the last profile
```bash
ncm-ncd --configure --all
```
_Note: when upgrading, it will take several YUM runs to get a stable package list. This is an expected behaviour. You may just wait for these runs
to happen as part of other deployment operations or rerun ncm-spma several times manually._ 

Depending on the history of the node you are trying to upgrade, you may have YUM errors when first deploying because of conflicts with already installed
RPMs that YUM has not desinstalled yet. You may have to remove these RPMs manually. Among the problematic packages found on some nodes, there was tomcat that had
to be removed with:

```bash
rpm -e --nodeps --noscripts `rpm -qa|grep tomcat`
```
    
## Changes to local templates

The new generation of OS templates and grid MW templates, as well as the use of YUM, may require some adaptations in the site-specific templates.
This will be  necessary if you build some site-specific "machine-types" or "personality" due to some changes in the template namespaces used and the need
to remove as much as possible versions from package list. The main issues that you could face are described below with suggested changes:

### OS templates

* Old OS templates used to provide templates to configuring additional OS features in `config/os` (and for grid MW, in `config/emi`). These namespaces
no longer exists. Instead additional features are provided as package list in `rpms` namespace. A few standard package lists are provided. Every
site can build its owns list. There is also an `rpms/group` providing templates reflecting a few YUM gorups. You should avoid relying on them as they
are just workaround until ncm-spma can manage YUM groups directly.
* To include the base OS configuration in a local machine type, just include:
```
include { 'config/core/base` };
```
The base configuration is very minimal. Basically it includes only the Base YUM group.

If you want to have site-specific templates that include additional OS features working both with the old generation and the new generation of OS templates,
you can use the following trick:
```
# For old generation templates
include { if_exists('config/lal/latex') };
include { if_exists('config/lal/gnumeric') };
include { if_exists('config/lal/xwhep-client') };
include { if_exists('config/lal/gsl') };
# For new generation templates
include { if_exists('rpms/group/development') };
include { if_exists('rpms/nfs-client') };
include { if_exists('rpms/editors') };
include { if_exists('rpms/gnumeric') };
include { if_exists('rpms/latex') };
include { if_exists('rpms/scientific-libraries') };
include { if_exists('rpms/interactive-server') };
```

There is no namespace conflict between the old and new generation of templates. As a result, only one of the `if_exists` series will match.


### Grid MW templates

The new generation of grid MW templates, `umd-3`, has a slightly modified layout compared to the old templates. This results in a few namespaces changes:
 * `services` has been renamed `personality`
 * `common` has been renamed `feature`
 * `machine-types` has been renamed `machine-types/grid`
 * `defaults/glite` has been renamed `defaults/grid`
 
Normally, only the change of `machine-types` namespace should really affect local site configuration. If you want to have site templates working
with both old and new templates, you can use the same trick as described for OS templates:
```
# umd-3 templates
include { if_exists('machine-types/grid/wn') };
# Previous templates
include { if_exists('machine-types/wn') };
```
 
### YUM-compliant package lists

If you have some site-specific service definition that contain locally maintained package lists, you should remove versions (and architecture) from
the package list. It may work with the original list but you will quickly have problems if the package list contains packages that are dependencies for
packages in the configuration as this may result in conflicting requirements between your locked version and YUM calculation. As mentionned before,
if you want to lock a version, the easiest is often to have a YUM snapshot with the desired version as the latest version.

If you want your service definition to work both with SPMA and YUM, you cannot provide the same list. The recommended approach is to have two
different package lists implemented as two different templates, 
the existing one for SPMA and a new list that will contain only the main package(s) for YUM. The template for YUM should have the smae name as
the SPMA one with suffix `-yd`. For example is you have a template `feature/myservice/rpms/config.pan`for SPMA, you should create a `feature/myservice/rpms/config-yd.pan`. In the 
service configuration template that will include the package list, you should use the following statement:
```
variable RPMS_CONFIG_SUFFIX ?= '';
include { 'feature/myservice/rpms/config'+RPMS_CONFIG_SUFFIX };
```

To add a package for YUM, you should not use `pkg_repl()` that requires a version but the following assignment:
```
prefix '/software/packages';
'{mypackage}' = nlist();
```
