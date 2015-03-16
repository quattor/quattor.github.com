---
layout: article
title: How To Use The Template Library
category: documentation
author: Michel Jouvin
---


This page describes the Quattor template library and how to use it.

## What Is The Template Library?

The Quattor template library is a set of generic pan templates that allow to configure a machine without writing a detailed configuration description.
A site administrator using the template library to configure supported services
has mainly to provide the necessary information specific to the site/machine to customize the behaviour
of the standard templates. Depending on the type of configuration database used, this site is provided through site-specific pan templates (SCDB) that
contain mainly variable declarations or through a relational database (Aquilon). 

One of the key design principle for the template library is that every modification is made with backward compatibility in mind. A site relying on the
template library should not have to modify anything in its site configuration when upgrading to a new version of the template library: the resulting
configuration should remain the same, except for bug fixes and necessary configuration updates. __Every exception to this rule (unfortunately there are
a few...) is always documented and well advertised.__ On the other hand, it is expected that sites don't modify the template library without
pushing back their changes (see [How to contribute?](#how-to-contribute?)). Site customization must be done through documented variables 
(the main source of information is the [Quattor Wiki](https://trac.lal.in2p3.fr/Quattor/wiki/Doc)). If a configuration option that you require is
missing, you are welcome to open an issue in the appropriate Git repository on GitHub.

The template library has been integrated as a component of each Quattor release since version `14.5.0`. That means that:

* It is going through the
standard testing and Q/A workflow used for the whole Quattor release.
* It is easy to get a consistent state of the whole template library, that guarantees that each component will properly interact with the others.
* The way the template library is organized make pretty easy to implement a staged deployment strategy if a site wants to go through a strong validation
process of new releases.

## Template Library Layout

The template library is organised in several subsets, each one mapped to a specific Git repository in GitHub. 4 of these subsets constitute the core
part of the template library, necessary for configuring the base OS on any machine. The other subsets provide standard templates for configuring
specific services like grid EMI/UMD middleware, StratusLab cloud middleware and are useful only if you want to configure these services.

Each subset is made of several templates, organized in different directories. Among these directories, some of them have specific purposes and represent
the public interface to the subset:

* `features`: configure a particular service (one directory per feature), 
intended to be included with other features to a base OS configuration to define a specific machine
configuration, generally through set of features defined as `personality`.
* `personality`: a set of features used together to provide a higher-level service (e.g. nfs-server). Used mainly with SCDB as Aquilon defines
personality in the relational database rather than with pan templates.
* `repository`: templates used to configure the YUM repositories normally associated with the subet. Present in (almost) each subset.

### Template Library Core

The core part of the template library is made of the 4 following subsets (the name given matches the directory name under `cfg/`in SCDB):

* `standard` (repository [template-library-standard](https://github.com/quattor/template-library-standard)): this subset provides templates used to
describe hardware, to determine OS/kernel version/architecture, configure file systems. It also provides some standard personalities like perfSonar,
Pakiti or standard features like fetch-crl, cvmfs...
* `quattor` (repository [template-library-core](https://github.com/quattor/template-library-core)): this subset contains one directory per Quattor release. For each version, it provides all the templates to configure a Quattor client
and all the configuration modules part of the release.
* `os` (repository [template-library-os](https://github.com/quattor/template-library-os)): this subet contains one directory per OS (major) version.
The main template in this subset is `config/core/base` that does the base OS configuration. In the `rpms` directory (pan namespace) of each version,
you can find templates defining some useful groups of packages.
* `monitoring` (repository [template-library-monitoring](https://github.com/quattor/template-library-monitoring)): this subset contains template to
configure various monitoring tools (Nagios, Ganglia, ...). Even though using this part is mostly optional, it is currently required to have it present
to satisfy one dependency of the `quattor` subset.


### Grid Middleware

Stored under `cfg/grid` in SCDB, this subset contains one directory per EMI/UMD version. The associated Git repo is 
[template-library-grid](https://github.com/quattor/template-library-grid)). This subset is entirely optional.

It provides all the templates, particularly `personalities` and `features` required to configure the grid services.


### StratusLab

Stored under `cfg/cloud` in SCDB, this subset contains one directory per StratusLab version. The associated Git repo is 
[template-library-stratuslab](https://github.com/quattor/template-library-stratuslab)). This subset is entirely optional.

It provides all the templates, particularly `personalities` and `features` required to configure StratusLab services.


### Examples

This subset is SCDB-specific and provides an example of site configuration, stored under `cfg/sites` and `cfg/clusters`.
The associated Git repo for this subset is 
[template-library-examples](https://github.com/quattor/template-library-examples)). This subset is entirely optional and is normally
not used in a production SCDB.

In addition to provide site/cluster examples, this subset is used to validate the other subsets during the release process.


## How to Get It?

The layout of some of the Git repositories is not really appropriate for a direct use. Two tools have been developped to download the template
library as a ready-to-use set of templates :

* `get-template-library`: download the template library itself organized in a way suitable for importing it in SCDB or Aquilon.
* `create-vanilla-SCDB.sh`: create a new SCDB configuration database, with all the SCDB tools and the template library. This script uses
`get-template-library` internally and compiles SCDB examples at the end of the download.

### get-template-library

`get-template-library` is located in GitHub [release](https://github.com/quattor/release) repository (in `src/scripts`). By default, this script
downloads the whole template library in `/tmp/quattor-template-library`. Then the downloaded contents can be imported into an existing SCDB or
Aquilon installation, by the appropriate tools (e.g. [directory-sync](https://trac.lal.in2p3.fr/Quattor/wiki/Download/QWGTemplates/Install#In-placeUpgrade) for SCDB).

Before using `get-template-library`, clone the GitHub [release](https://github.com/quattor/release) repository. If you already have a clone, be sure to
refresh it before using the script (typically with `git pull`).

Use `--help` to get a list of all the available options. A typical use of `get-template-library` (to download Quattor version 14.5.0) is:

```bash
get-template-library -F 14.5.0
```

Option `--pull-request` allows to integrate a pull request not yet merged, typically for testing, in the downloaded template library. 
When using this option, the quattor version should be `HEAD` rather than a specific release, else it will generally lead to unpredictable
results. The option value has the format `repository:user:source_branch:[target_branch]` with:

* `repository`: the name of the repository (without the GitHub user) the pull request belongs to. The repository name is assumed to be the same
for the source and target branches.
* `user`: the userid of the user who created the pull request (whose source repository belongs to).
* `source_branch`: the source branch of the pull request in `user` repository.
* `target_branch`: the name of the target branch or tag of the pull request in the `quattor` repository. For a repository with a master branch it can
be ommitted and will be the `master` branch if the version is `HEAD` else it will be the tag corresponding to the version ( `template-library-` prefix
in the tag name can be ommitted). For a repository without a master branch, `target_branch` is required and must be the branch to use if the version
is `HEAD` else it must be `branch-version`.

### create-vanilla-SCDB.sh

Another way to download the template library is to
use the script [create-vanilla-SCDB.sh](https://github.com/quattor/scdb/blob/master/utils/scdb/create-vanilla-SCDB.sh) in repository 
(scdb[https://github.com/quattor/scdb/blob/master/utils/scdb]. This script will create a new SCDB with all the SCDB tools, use the previous script
to download the template library and compile the SCDB examples. The new SCDB, by default, is in `/tmp/scdb-vanilla` and the template library itself
is in the `cfg` subdirectory of this directory.

_Note: if you are interested by getting the template library validation resulting from the compilation of the examples, it is recommended to use 
this script whether you are using SCDB or not._

A typical use of this script involves the following steps:

* Clone the  SCDB repository located on GitHub (`git clone https://github.com/quattor/scdb.git`) or update your working copy (e.g. `git pull`) if
you already clone it.
* Move into the top directory in the clone
* Execute utils/scdb/create-vanilla-SCDB.sh (use --help for more informations about possible options), typically (for downloading Quattor version 14.5.0):

```bash
utils/scdb/create-vanilla-SCDB.sh -F 14.5.0
```

This script accept all the valid options in `get-template-library`, in addition to the options specific to the script.


## Upgrade

As any other components in the Quattor toolkit, the template library evolves to fix issues, to support new functionalities or services and to increase
the flexibility in the configuration options. Thus it is important to upgrade it regularly, when a new Quattor release is announced.

When upgrading, it is important to upgrade the whole template library, not just one subset, else you are at risk of inconsistencies between subsets.
This is especially true of the `standard` subset that all the other subsets depend on. Except if there is a special announcement, it is better
to install the template from a Quattor release than from the master of the Git repositories: despite our attempt to have the master always
working, only Quattor releases go through the whole testing process.

To do the upgrade, the easiest is to get a fresh version of the template library following the [procedure](#how-to-get-it?) described above. Then
from the directory `/tmp/scdb-vanilla/cfg, the template library can be imported to a production SCDB or Aquilon. For SCDB, a script
helping with the update is available: see [Quattor Wiki](https://trac.lal.in2p3.fr/Quattor/wiki/Download/QWGTemplates/Install).


## How to Contribute?

If you'd like to contribute a bug fix, an improvement or the support of a new service, raise a pull request against the appropriate repository or
repositories (some modifications may involve several repositories). Before raising the pull request, it is important that you validate your modification
against:

* Your site
* The template library examples

Validation includes checking that everything (in particular the template library examples!) compiles without errors and that the changes in the
profiles are those expected.

While normally the pull request is raised against the master branch of the reference repository, there are a few exceptions. This concerns the
following repositories:

* `os`
* `grid`
* `stratuslab`

In these directories, there is no master branch but one branch per OS version, grid middleware version, StratusLab version. Be sure to raise
the pull request against the appropriate branch or if necessary to raise a pull requests against several branches (in this case, this is recommended
to start with one branch, wait for the peer review and then open the other pull requests).
