---
layout: article
title: Summary of 17th Quattor workshop (17-19/3/2014, Amsterdam)
category: news
author: Michel Jouvin
---

[Agenda](https://indico.cern.ch/event/296548/timetable/#all.detailed)

## GitHub

To contribute, anyone should have a personal account and fork the
quattor repository, do its development and make a pull request for
others to review/comment the changes.

* As soon a pull request has been made, it is tested by Jenkins: green
  mark next to the commit
* Everything contributed must work: tested by Jenkins
* Do not merge your own pull requests without letting others have a
  chance to review them!
  * At least 24 hours
* If you are not a repository owner and want to be notified of pull
  requests to a repository, subscribe it
  * Notifications can be received as RSS feeds

Configuration modules: several (a lot?) unmaintained.

* Move them to a unmaintained/deprecated branch
* Deprecate some comments in favour of metaconfig, e.g. ncm-pakiti
* Release should contain only the configuration modules we are ready
  to support: if a config module is deprecated, this doesn't prevent a
  site to use it

Most repositories use the master branch for development

* A few (e.g. AII) have a master branch and a 13.1 branch when 13.1 is
  not compatible with master
* template-library-os, template-library-grid are a bit different:
  there is no master, each branch reflect the support for a specific
  OS/grid MW version

Aquilon in GitHub

* MS still has concerns that its contribution to GitHub may be
  forbidden at some point, despite it is possible today. Decision can
  be reverted at any point in case of security problem
  * In fact the same can happen with SF
* Agreement that from now GitHub is the reference place for Aquilon

Forking/contributing to a quattor repo

* Fork the quattor repo and keep the master branch only for tracking
  the quattor master branch
* Start a topical branch for your own development, push to your fork
* Issue pull requests from the topical branch to quattor master
  branch, don't merge directly your topical branch to your master
  branch

Weekly meeting moved Thursday 1pm CET

* 15 mn maximum
* Staying with Vidyo


## Packaging and Releases

Solaris IPS built by Jenkins?

* Too early
* Need to upstream changes to components made for IPS support but
  unfortunately done on a pre-GitHub version: not a trivial merge...
* Good news: most components can run both on RH and Solaris using a
  common code

Add template-library checking by create-vanilla-SCDB.sh to Jenking

* Tag the corresponding repository when a release is made
* Stijn will have a look

template-library-core: integrates its management to the release process

* In the meantime, maintain it manually: Michel agrees to do it

Release cycle every 2 months seems appropriate to deliver quickly new features, avoiding people to fork

Quattor 13.1.3: required for at least the change to aii-ks for
compatibility with YUM-based machines, the aii-shellfe taint mode
issue and the requirement not explicit for cdb-sync

* Better than sites doing their own mix on 13.1.2
* No configuration module update
* cdb-sync: remove it, no longer used by Aquilon
* taint mode issue: do not delay if we don't have the fix
* Not going for a full release: only a new release of AII (put
  in 13.1.2 branch) + a new tag in template-library-core (13.1.3?)
  with the AII RPMs updated


### ncm-puppet

Why? Grid community transitioning to Puppet

* YAIM no longer maintained
* CERN moving to Puppet
* DPM developers producing/supporting Puppet modules to configure DPM
* Take advantage of existing Puppet modules for grid MW to avoid
  duplication the effort in Quattor configuration modules

Idea: run a standalone Puppet getting its configuration from Quattor
profile and taking care of downloading the required Puppet modules

* Prototype has a simple schema: puppet config file
  (/etc/puppet.conf), modules to use, puppet configuration file

Tested as a prototype with DPM

* Base OS and grid services configured by Quattor template library
* DPM services configured by Puppet modules

Future work

* Add multiple source for Puppet modules
* Add support for Hiera-based modules: requires a specific input file
  format (yaml, json, xml)
 - Could also explore the direct use of node profile as a hiera
   source: drawback is a tight link with Puppet internal changes in
   Hiera format

Discussion

* Luis: why not to use metaconfig or filecopy (with an alternate
  configuration path) to download manifests and run puppet apply. The
  component could only take care of downloading the modules
* Agreement this is an interesting addition that may help to have a
  framework if there is some opportunity to reuse more Puppet modules

Next steps

* Andrea should issue a pull request to
  quattor/configuration-module-core so that the configuration module
  is tested by Jenkins and reviewed by others


### ncm-ceph


Presentation by K. Waegeman (UGent)

Main features

* Create a cluster
* Global config
* ceph-mon config
* ceph-mds config
* ceph-osd config
* cursh map
* Safety first
  - File system deletion are not done actually: the command to execute
    is returned

Requirement: password less ssh access from deployment server (an
arbitrary node in the Ceph cluster) to all nodes for ceph user

* It's the normal way a Ceph cluster is managed
* Current version of ncm-ceph is stopping if one node is offline:
  should not happen

Future work

* Configuration per OSD or host
* Pool support
* Client configuration
* Validation with last version of Ceph (Firefly)



### ncm-metaconfig

Long
[https://github.com/quattor/configuration-modules-core/pull/137 controversial discussion]
on a pull request for changing the metaconfig schema to make easier
definining file name from variable or reusing the file name defined in
metaconfig in other components.

* Rejected as it has a high risk of permitting to define several
  different contents for the same file
* Same goal is much better achieved by proper use of variables to
  define file names
* One specific issue is to bind a specific file to a schema: this has
  to be done with a bind command where the first parameter cannot
  contain a variable
  * Discuss with Cal the possibility to improve this

Discussion on wheter we need to be able to define daemon dependencies:
general agreement that not, can turn into a nightmare

* Same thing can be achieved with several instances of metaconfig
  defined in the configuration, associated with different
  configuration path: see last workshop presentation by Luis.

Provide a metaconfig standard file schema collection

* Provide with them unit tests for these standard schema

### ncm-condorconfig

Obsoleted. Not usable with any recent or not too old version of Condor

* Not used by grid templates

Replace by using metaconfig


### ncm-network

No longer plan for a full rewrite (see previous workshops)

NetworkManager is not good enough on SL5 to used as a base for a
replacement and even in SL6 it doesn't handle all the config (ex: IB)

Wait for SL7 to start something new, as network config will change
dramatically in RH7

### IPS support

IPS is the new Solaris package management tool, close to YUM in term
of concepts.

* Incorporation packages: similar to metapackage RPM, brings
  dependencies with possibility to define minimum or exact version
* Grouping packages: similar to YUM groups
* MS using package repository snapshots managed as ZFS snapshots and
  changing snapshots only when rebooting a machine
  * Using Solaris Boot Environment: available on a running system so
    that they can be configured/modified whithout booting into them

Worked out a new package description model

* Catalogues: similar to YUM groups, allow to request of group of
  packages known to work together through pan function `pkgcat_add()`
  * Currently catalogues are implemented as flat files
  * catalogues are versioned: a particular of the catalogue can be
    requested
  * Still possible to add individual packages through `pkg_repl()` or
    the new `pkg_request()` (default version/arch obtained from
    catalogue)
* Control what are the packages allowed to be deployed/updated on a
  live system and those which must wait a reboot
  * To be discussed in more details on the mailing list but may be a
    good use case for NCM hooks

IPS has no feature to help removing packages that become unnecessary:
wrote pkgtree to help identify them and added ability to explicitly
remove certain packages

New schema used:

* `/software/catalogues` A list of catalogues (package groups) to
  install
* `/software/requests` - A list of additional packages to install
* `/software/uninstall` - A list of packages to uninstall

* `/software/components/spma/packager` - Must contain 'ips' to use
  this module
* `/software/components/spma/run` - Set to yes to allow immediate
  changes to new boot environment
* `/software/components/spma/userpkgs` - Set to yes to allow user-installed packages
* `/software/components/spma/pkgpaths = list("/software/catalogues", "/software/requests");`
* `/software/components/spma/uninstpaths = list("/software/uninstall");`
* `/software/components/spma/cmdfile` - Where to save commands for the
  spma-run script
* `/software/components/spma/flagfile` - File to touch if there is
  work to do (and spma/run is no)

* `/software/components/spma/ips/bename` - Name of boot environment to create
* `/software/components/spma/ips/rejectidr` - reject Solaris IDRs if not explicitly requested
* `/software/components/spma/ips/freeze` - Ignore frozen packages

* `/software/requests` has been used to replace `/software/packages`
  because on Solaris `/software/packages` is full of irrelevant
  information (in particular configuration modules RPMS).
* Probably need to rework the way we configure components so that the
  components/xxx/config.pan is doing what is appropriate for any
  platform
* Another alternative would be make the components which are platform
  dependend part of the OS templates
* To be discussed in more details on the mailing list

Luis: uninstall idea is something that could be implemented in the
mainstream ncm-spma as blacklisted packages, indepedent of the
repository

* Currently blacklisting is done in the YUM repository configuration

### Componenent Status

Not many components have more than the 00-load.t test.

* In some cases, adding unit tests may require a significant rewrite
  of the components to comply with the coding style required by the
  testing infrastructure to mock the component...
* Unit tests will be required for future significant pull requests

Start by a few critical components: autofs, filesystems, grub, symlinks

Also move some components to the deprecated/unmaintained branch:
directoryservices, diskless\_server, drbd, fsprobe, hostaccess,
iscsitarget, krb5clt, linuxha, oramonserver, pakiti, php, pine, pvss,
rproxy, runlevel, serialclient, sindes_getcert, slocate, squid, state,
tomcat, zephyrclt

* Deprecate metad and gmond in favour of ganglia
* James taking care of the move

Configuration module documentation: generate an html file from the pod
file and put it on the wiki

* Do it as part of the release process (James)

Documentation: make a skeleton of a new documentation area on GitHub
and move contents from Trac wiki progressively

* To be discussed at a future weekly meeting

### Template libraries

Need feedback from people with Aquilon experience on what are the
issues using them in this context

* Clearly machine-types and personnality (formerly glite or services) should not be useful anymore but should not hurt to start or could be removed from Aquilon template library: nothing else should depend on them
* One issue is how the template library will get input from the Aquilon DB data: glue with variables used internally in templates of the template libraries


## Migrating away from 13.1

Detailed presentation by Michel, explaining/illustrating what was
already written on the mailing list about the recent changes that
should make 13.1 to 14.x migration easier if not easy...

* If you want only one quattor deployment server, it should stay
  with 13.1.3

Discussion will be summarized in a blog entry on http://quattor.org

## Distributed Configuration

Several services rely on a set of coordinated nodes: HA, Ceph,
monitoring...

Several specific issues

* Some configuration changes must be executed only on one host that
  will act as a master: currently manual selection
  * Automatic election?
* Some configuration changes require update on several nodes but
  update should not occur at the same time to avoid breaking quorum or
  the service
  * Rely on global lock that will prevent a configuration module to
    run on several hosts at the same time?
* Some actions may require to update the templates after they are
  succesfully executed, e.g. addition of a new Ceph node in the Ceph
  cluster node list defined in the templates
* Data sharing between nodes through profiles: how to enforce proper
  security on sensitive data

Proposal to use Zookeper as a data distribution/synchronism mechanism. A lot of interesting features for this use case but a few issues:

* SASL: only a java client, no server-server support
* perl binding not maintained by Zookeper
* Several Zookeeper alternatives considered but all with (more?) drawbacks


## Wrap Up

Next workshop between mid-September and mid-October

* Main option is Madrid: to be confirmed in the next weeks
* Backup option is Paris/Orsay
