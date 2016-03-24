---
layout: article
title: Summary of 21th Quattor workshop (2016-03-22 to 2016-03-24, Bruxelles)
category: news
author: Michel Jouvin
---

# Summary of 21th Quattor Workshop


[Agenda](https://indico.cern.ch/event/491377/timetable/#20160322.detailed)


## Site News

Bruxelles

* Moving the grid site to HTCondor
* Very old SCDB desynchronized with mainstream SCDB: will restart a new one from scratch
 * Or maybe restart with Aquilon if it is ready for production with the template library
 
RAL

* Work on Ceph: configured with Aquilon + ncm-ceph
* Reworked configuration description for Quattor to disentangle feature configuration and OS configuration
* Effort to get new people using Aquilon, in other groups
* Aquilon: 75% of resources, SCDB: 25%


## panc compiler

Not much work in the last month

Threading issue seen at MS mainly: so far never succeeded to find a way to reproduce it in an helpful way

* Clojure migration may have helped but will no append in a foreseeable feature

Possibility to have a documentation explaining the panc architecture and internals to help contributions 

* Cal agrees to do it

Suppression of escaping: basically ready in the compiler, need to add the metadata in the profile about it

* /metadata/panc
* Will require a new major version

.tpl removal: also basically ready

* Also require a new major version

Next releases: James will try to learn the panc release process

* Soon: a next minor release with stuff currently merged in master
* Later: a next major release with new metadata for escaping and the .tpl removal


## Configuration module status

ncm-metaconfig: support for many services

* No list available in the doc : look at the source tree...
  * See how we can improve exposure of available modules
* Plan to extract annotation from schema
* moab: obsoletes ncm-maui and ncm-moab
* One missing feature: ability to run a service-specific validation command on the configuration built before restarting the daemon. 
  * See https://github.com/quattor/configuration-modules-core/issues/739.


## Aquilon

Aquilon and template library for grid components

* No major problem foreseen
* Some work required to turn current personality in the template library into features

Aquilon release: no real progress

* RAL still working on a proper documentation to setup a new Aquilon box
* A package exists but is untested and difficult to test in an existing installation

Aquilon documentation

* Duplication installation documentation: repository README and quattor.org documentation
  * Merge contents in documentation, remove it from repo README
  * Ensure that the documentation is complete enough to get a working broken usable with the documentation 'Using Aquilon'
  
Aquilon configuration development organized around sandboxes which are Git clone of the configuration

* Each sandbox is a branch in the broker Git repo: ability to rebase on production branch or push (publish) changes to production (`aq deploy`)
  * Git commands used to rebase a snapshot on something else (e.g. production)
  * You can also deploy a node from a sandbox for testing (`aq manage --sandbox`)
  * Changes cannot be made directly into the production branch
* `aq show_sandbox --all`

archetype: used to define disconnected subsets of the configuration, must provide a `base` and a `final` template 

* `base` included at the very beginning of the configuration
* `final` included at the end
* Ability to share the template library between archetypes putting the template library in a separate Git repo
  * Included in the load path
  * Cannot be modified but templates in the template library can be replaced by one in the sandbox/main repo

Quattor version defined as a `final` variable in one template: ensures that all nodes are running the same version

* New version testing: create a new snapshot, associate a few test nodes with the snapshot and deploy on them only

clusters: set of different machines sharing the same configuration

features: Aquilon looks for a template `config.pan` in the template directory (can contains several directories)

* features are located in the  `features/` directory
* Order of feature inclusions is not guaranteed but 2 stages (pre and post) in the inclusion process
  * Create a meta-feature that includes other features in the appropriate order if necessary and the 2 stages are not enough
  * Including features in others features means that their usage cannot be tracked by Aquilon: normally they are added under /metadata in the profile
  * Things included by features are generally placed in `common/` directory
  
service: defines relationship between hosts, for example DNS server to used, based on a "service map"

* A service map defines the criteria to select the host belonging to one location, for example the network


## Hardware Templates

For network card, need a manufacturer part in the namespace as in for CPUs

* Agreement to do the necessary changes and cleanup the template names to be devices rather than driver names

In Aquilon, this information is improperly as vendor (--vendor): suggest deprecated this option and adding a --manufacturer option


## FreeIPA support

Goal: replace SINDES

FreeIPA will bring Kerberos support.

* Uses LDAP as its db backend
* Provides a one-time password to allows initialization of keytab: no longer usable as soon as the machine has its keytab
  * FreeIPA has its own Kerberos infrastructure/realm: to use interact with another Kerberos realm, the recommended approach is a bi-directional trust (machines are put in the FreeIPA realm)

Impact: CCM for profile download, ncm-download for file download, AII for initial configuration

* ncm-download already Kerberos-ready
* AII : already has a hook to initialize/register in IPA
* CCM : need to support the new authentication methods

Proposal: move the download logic to CAF::Download that could be used by all the components that need it (including CCM).

* Stijn working on it, no timeline yet for the full support but 16.4 should bring the basic support allowing FreeIPA initialization and downloading profiles from trusted Kerberized web server
  * No support for FreeIPA vault in this initial version (no use of future CAF::Download)
* A [PR](https://github.com/quattor/CAF/pull/110) is already open with preliminary code (not doing the actual download) for CAF::Download

Server-side: any Kerberized web server can act as a server for downloading profiles and files, no need to set up a IPA server (but this is also possible to do it)

* Need to document how to set up a properly configured server for serving profiles
* freeIPA server is required to do the secret management


## Ceph support

Examples about to be added to template-library-examples repo (currently in [PR[(https://github.com/quattor/template-library-examples/pull/29))

* Part of these templates could become part of template-library-standard
* Support defining different pools corresponding to different crushmap buckets
* All disks on the machine except sda are considered OSDs
* Component currently don't use ceph-disk but it may be a useful addition for disks dedicated to Ceph
  * Disk properly initialized with the Ceph-related data (like LVM, MD...)
  * Would allow to keep disk management outside Quattor: easier for Ceph admins  
  * Control by Quattor allows to use only a disk partition rather than a full disk for Ceph: useful when using SSD shared between OS and Ceph journal for example

ncm-ceph runs on only one node and connects to all Ceph nodes through ssh to do the appropriate actions

* Not optimal but no easy other way...
* May look at Jewell coming release to see new possibilities: ideally run the component on each Ceph node and do only what is relevant to the node
* In the short term, would be good to allow to disable some part of the configuration in the profile (for example configuration of a specific OSD)
* New ceph-prepare could also help, allowing to assign ID on OSDs rather than trying to retrieve the assigned ID


## Cloud

OpenStack support

* Support for all core services available, including Cinder, Ceilometer
  * Everything managed with ncm-metacopy but TT files delivered with filecopy: need to add unit tests before putting as a standard metaconfig service
  * No specific OpenStack tree in the configuration
  
VM management with Quattor

* LAL way: a very basic image with a contextualization script that triggers Quattor installation and configuration
  * No impact on Quattor except removing network information from the profile
  * RAL doing a similar approach: goal is to hide the configuration system from the user provisioning the resource
* UGent: profile contains the information that the profile is a VM and aii-configure instantiate and configure the new VM with the profile

Schema extension for VMs

* Currently used by UGent to pass information to AII about some aspects of the VM configuration: networks to use, datastore, graphics...
* Proposal: /system/cloud defined as an open dict in the schema and binded to something more specific based on the cloud MW used
* Discuss if an abstract description common to all cloud MW make sense

Cloud resource provisioning: RAL integrated it into their cloud dashboard 

* Interaction with Aquilon behind the scene


## CAF

Proposal to add support for event tracking (CAF::History, See [PR](https://github.com/quattor/CAF/pull/117))

* Objective: makes components using CAF modules to be able to report about what was done by CAF
  * For example track/report changed files
  * Will also allow to remove files created by Quattor when a configuration module (or a metaconfig service) is removed, if desirable
* CAF::History allows to build a list of event that can be processed later
  * ncm-ncd [PR](https://github.com/quattor/ncm-ncd/pull/51) demonstrates the use of CAF::History to report all the touched files at the end of a component run
  * Could imagine to flush the event list to a database at the end of a ncm-ncd run to keep track of modifications made by Quattor
  * Nathan would prefer immediate reporting of the events rather than a deferred one (in case a component crashes before reporting occurred)
    * Improve current implementation to track if an event has already been reported and makes possible to call the report method several times still reporting event once. 
    * A global property could be taken into account to decide when an event is added to the list whether immediate reporting should occur.

CAF::Check: a wrapper around LC:Check that allows proper reporting, suppresses raising exceptions and implements CAF::NoAction

* May help moving out of LC::Check at some point

## Miscellanous issues

See discuss@workshop issues in GitHub

ncm-query: `ccm` is a functional replacement and has a `--format ncmquery` that is mostly compatible with ncm-query

* Pb: ncm-query format is undefined so difficult to assess compatibility
* Discussion about `--format ncmquery`: agreement to remove it as it creates a dependency on this undefined format in the future
  * In script, it is recommended to move to the json output of `ccm`
  
ncm-spma:

* PR open to move YUM repo definition to a non standard directory (/etc/yum.quattor.repo.d), defined as the default one in /etc/yum.conf, to avoid problems due to RPMs installing repo file that will interfere with Quattor deployment later
*  yumng plugin: agreement to merge it as soon as MS has merged the last changes
* yum plugin: run `yum clean` for a repo about to be removed (else it will not be clean by later runs of `yum clean`)

push() imporperly works in for loop in some circumstances: see https://github.com/quattor/template-library-core/issues/104

* Agreement that the behavior exhibited in the issue is incorrect
* Test the PR against the template library and checks that it produces no difference (that nothing depends on the wrong behavior
  * PR uses append internally
  
ncm-fstab/ncm-filesystems: duplicated code that cannot be easily removed (https://github.com/quattor/configuration-modules-core/pull/600)

* Proposal: incorporate ncm-filesystems features into ncm-fstab as an optional feature, disabled by default
* Agreement that something should be done, proposed approach reasonable but ncm-fstab may become quite misleading
  * Need to ensure that the new component addresses all the corner cases in term of /etc/fstab management
  
RPMs more compliant with rpmlint (https://github.com/quattor/maven-tools/pull/78): will require a ChangeLog but agreement that the real value of the ChangeLog will be very limited

* One minimalistic option would be to put a link to the web site but is it adding any real value? Nobody considering that it adds any value, may just ship an empty one

Duplication between aii-dhcp (from aii-core) and aii-dhcp dhcp.pm module (not used anywhere): https://github.com/quattor/aii/issues/166

* Probably some uncompleted work: need more investigation

Template library PR testing: explore using Travis instead of Jenkins

* Check the test setup in template-library-core (pan linter)


## Documentation

* Complete the development documentation

ReadtheDocs documentation

* latest contains the last version of configuration-modules-core, ccm and a few other things
  * Need to add configuration-modules-grid
  * schema parsed to retrieved type of properties and whether they are required or optional (may want to add the default value in the future)
* Attempt to integrate it into the release process for next release
  * When this is done, update web site documentation to redirect to ReadTheDocs
   

## Next release

16.4 planned end of April

* RC expected to start around the 25th


 
