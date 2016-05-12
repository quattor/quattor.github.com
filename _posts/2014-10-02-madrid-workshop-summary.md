---
layout: article
title: 18th Quattor Workshop Summary (October 2014)
category: meeting
author: Michel Jouvin
---

# Summary of 18th Quattor workshop (30/9-2/10/2014, Madrid)


[Agenda](https://indico.cern.ch/event/328445/timetable/#all.detailed)


## Releases

Worked well since last workshop

* More and more automation, including list of pending issues by milesones at http://quattor.org/release (updated every 30 mn)

Jenkins not working for some of the Quattor components: lack of time at UGent to fix the problem, not clear why it happened

* Look at an alternative ? Travis, well integrated with GitHub ?
* Ability to test compatibility with several Perl versions?

Remove ability to skip tests if PERL5LIB is not defined?

Must keep in mind dependency of the release process against LAL nexus server

* Illustrated by last release happening during a power cut at LAL
* Long power cut at LAL was really exceptional (once in 60 years due to major refurbishement needed on power feed)... and scheduled

Build tools: a few minor issues

* author/contributor/developer processing
* Mocking of escape() and Debug()

quattor-repo and quattor-client RPM: put source files with appropriate variables and let Maven build the RPMs

current version update: manually done, must be set explictely in the release instructions

* Not really useful to configure machines but helps with mirroring

Planned reinstallation of stratuslab-srv01: save nexus and yum repository contents


## Site Report

### UGent

See [slides](https://indico.cern.ch/event/328445/session/0/contribution/0/material/slides/0.pdf)

No more EL5... but EL7 started

SCDB: repository moved to (private) GitHub

* Based on local modification not really shareable
* Allow per review of changes

AII remote logger

* Allow to send log files produced by AII (stdout/err redirection) to rsyslog via nc or /dev/tcp
   * %pre, %post scripts
* Handy for debugging installation problems
* Distinct from enabling syslog in Anaconda

Buildid in profiles (schema extended)

* Buildid is generated (timestamp) during compilation
* No other change required to make the profile new and enough to trig a ncm-spma run
* But every compilation triggers a full rebuild
* No ability to do a coordinated restart of services or reboot of machines: looking for ideas..
  * pre/post deployment hook in ncm-ncd?

Ceph evaluation still in progress, including integration with Quattor

Started with OpenNebula: writing a new configuration rather than reusing StratusLab one

* Too many different use cases to handle

Migration of hybrid Quattor/vendor tool to Quattor only

Still on hold

* IPA (Kerberos-based infrastructure for authentication from RH)
  * Done only for replacing Sindes but not yet for user accounts
* Aquilon: not yet there...
  * Would like to couple it with (private) GitHub workflow, e.g. Aquilon merge opening a pull request allowing peer review and closing the PR
  triggering the actual merge

EL7 compute cluster expected beginning of next year: need to sort out support in Quattor by then

Improved monitoring of Quattor deployments: would be good to provide standard plugins for doing it

* Idea is to parse (central) syslog files with logstash and process them with Kibana
* How to efficiently track the state of 500 machines

Open issues

* Schema: property to flag VMs
* Schema namespace for VM with information specific to hypervisors


## EL7 Support

See [slides](https://indico.cern.ch/event/328445/session/0/contribution/1/material/slides/0.pdf)

RHEL and CentOS already released, SL7 coming

* EPEL7 in production since August

Main changes relevant to Quattor

* perl 5.16
* systemd instead of chkconfig
* grub2

No modification required to most components

* But taint errors due to perl 5.16 being stricter

A few issues fixed

* tmpfs used for /var/run
* Stricter use of Net::SSL
* Some legacy packages required by Quattor no longer part of default packages
* ncm-spma having problems with packages providing features corresponding to other packages: need userpkgs_retry=true
  * Why not to set userpkgs_retry to true by default as there is no known drawback: just split the YUM transaction in 2 different transactions:
  to be discussed in an issue in GitHub

New AII features for EL7

* Use static network configuration in AII (pxe/setifnames=true)
* YUM issues with proxies (due to partial download handling)
  * Anaconda image patching is easy
  * define pxe/updates with the URL of the patched image
* Ability to postpone base_package installation in %post phase to have the necessary repo available
  * Not specific to EL7
  * Discuss on GitHub if ks/packagesinpost should be true by default

Major issues

* grub2 support: requires a new component
* systemd: totally different from the previous management of services
  * CAF::Service (/sbin/service) still works
  * ncm-chkconfig needs to be rewritten: looks difficult to have a unique component for chkconfig and systemd
  * Continue to interact via command line or via DBus API?
  * Would be good to have a systemd config (unit files) for ncm-cdispd and cdp-listend
* taint errors: some fatals

ncm-chkconfig vs. ncm-systemd

* Need to find a way to abstract the difference from the profiles
* Common schema? not necessarily easy as the paradigms are very different: target vs. run level
* Define a set of functions that would be exposed by both components and will abstract at a higher level the service description?
* Problem of dependency management: need to have one component able to work on all platforms to avoid a nightmare
  * Reuse the CAF::Service approach with a component that do whatever is appropriate on a specific platform, overloading the methods appropriately


## OpenNebula support

4 components

* ncm-opennebula
  * Hypervisors
  * Datastores
* AII hooks for ONE
  * Manages ONE templates
  * Images
  * Map VM disks to datastores
  * Mapping of network interfaces to vnets
* Metaconfig templates
* RPC calls to ONE via Net::Opennebula
  * This module is not yet distributed, should be soon in CPAN, could put the RPM in quattor_externals

Preliminary template library not on GitHub yet

* ncm-opennebula, AII hooks also to be commited
* Template library in a separate repo template-library-opennebula

RAL interested by having a look at OpenNebula components.


## Toward a larger use ncm-metaconfig

Configuration rendering format via existing Perl module

* Json
* Yaml
* Tiny (.ini)
* properties (java properties)
* general (similar to Apache)

Still some missing sophisticated rendering options like list of string rendered as a comma-separated string

Templating option through Template::Toolkit (TT)

* TT implemented in Perl and Python
* File format defined in .tt files
* Very powerful... but preserving whitespace can be tricky: normally ok for config files
* config-templates repo available on GitHub for many services (http://github.com/hpcugent)
* Also written json2tt to test template rendering with a profile

Would be good to add ability to unit test TT files

* A utility developed at UGent (but in Python): try to integrate it in our Maven build tools

Proposal to move the core functionality of ncm-metaconfig to a CAF module so that it could be used in other components

* Seen a good idea by all participants
* CAF::TextRender decided as a name

Template::Toolkit: migrate to Alloy

* Compatible but more featureful
* Better maintained
* Not available in EPEL5: distribute a recent version through quattor_externals?

Integration of UGent work into GitHub: under ncm-metaconfig in configuration-modules-core

* src/main/tt, src/main/pan/templates and src/test/tt


## Pan Compiler

v10.1 new features

* New functions: file_exists, substitute
  * substitute: allow to replace tokens by value
  * Dynamic bind/valid statements
* Lots of bug fixes

Future roadmap

* Very limited development expected...
* Release/doc simplification (v10.2)
  * Artifacts on GitHub, no longer on SF
  * Move the docbook to ReST + move the docs to http://quattor.readthedocs.org (source still living in GH current repository)
* Functional changes (v10.2)
  * version option and documentation changes
  * Use of java 1.6 base64 functions
* Clojure migration (v10.3+)
  * Persistent data structures
  * Native clojure task management



## Template Library

Detailed presentation by Michel of the current layout of the library.

No showstopper identified preventing the use of the template library by Aquilon

* Aquilon should ignore the ``personality`` and ``machine-types`` namespaces that are implemented through personality and OS definition in the database
* Some adjustements probably needed, mostly in ``template-library-grid``, between templates in ``personality`` and ``features`` namespaces
  * Some things currently in ``personality`` should be moved to ``features``: easy to do in a backward compatible way for SCDB users

Agreement that we should foster the adoption of the template library at every site

* OS + core + standard should really be useful/appropriate everywhere
* Paranoid checks (!!!) about backward-compatibility of changes: a strong requirement to allow confident upgrades between versions

## Documentation - Communication

Users should look at documentation and open issues against it

* If this is a configuration module doc, issue against the configuration module

Old web site: move all the valid contents (in particular dev related) to quattor.org

* Except the documentation of the template library that will be moved by annotation processing
* For next workshop: have everything except template library docs moved to GitHub/ReadTheDocs

quattor.org documentation

* Complete "Getting started" section: in particular document get-template-library usage to get the initial template library
* Missing bits in "Starting a site with Aquilon"
* RSS feeds for Blog posts, news...

Wikipedia: check contents, send remarks to the list or open issues

OpenHub.net (formerly Oloh): update description for Quattor Template Library to better reference Quattor project

* Need 2 projects because of pan language.

Twitter: not really useful

* May check if we can tweet news automatically when added to GitHub (through a hook?), else not worth the effort probably
* Associate a decidated email address with the twitter account rather than quattor-devel

Mail lists on SF: working well, no real alternative, no reason to change

* GitHub is not providing a mailing list service



## Quattor inside Containers and Chroots

Containers and chroots can be very useful on WNs to help avoiding side effects from one job on other things running on the machine

* Well integrated with Condor
* Would be great to have Quattor managing the chroot environment

Main issue is ability to bootstrap something that will pull a profile not bound to a host name

* Container contents could be managed similarly as a VM image: configure once, instantiate many times
  * Configure with Quattor again only to build a new version of the container
* Container reference could be passed to Condor: use Docker to store containers?

James: would like to create/maintain the chroot environment from Aquilon without any steps involed outside

Stijn: should be possible to use Anaconda to set up the initial environment

* Anaconda is just a set of scripts configuring a chrooted environment in fact... May a double chroot be a problem?
* In this case AII should work...

Shipping the container: look at CVMFS as a possibility

* Also possible to use ncm-download or similar thing to bring the container to the bare metal machine

Possible issue with grid WN: CVMFS access from the chrooted environment

* Possibility to share the cache between the bare metal machine and all the containers?

ncm-spma: add ability to manage chrooted environment

* Pass the reference to the chroot environment to YUM?
* Also look at ``schroot`` utility that can create a chrooted environment from the current environment

Luis: ncm-cdispd can work in a chroot environment if the directory where initialized and the chroot environment was initialized

* Easiest way to initialized the container is to use a "magic tarball" available from openvz (or Docker?)

## Aquilon

Aquilon console: allows to display machines characteristics and change characteristics of machines in the sandbox (e.g. personality)

* Consume the JSON profiles

Increasing adoption: what is needed?

* Assess template library readiness for Aquilon: RAL may try to help
* Provide scripts to build Aquilon inventory and define Aquilon objects from existing (SCDB) profiles: some examples/starting points done by Luis at UGent, push them to Aquilon
repo as ``contrib``
* Review the [Getting Started](http://www.quattor.org/documentation/2013/10/25/aquilon-site.html) and update the contents to match last version of
Aquilon

## Other Core Components

### perl-LC

Author recommended to get rid of it as it is now unmaintained

* Suggested perl [No-Worries](http://search.cpan.org/dist/No-Worries) as a replacement
  * Also done by Lionel, with a pretty similar API
  * Perl 5 License (Artistic 1 & GPL 1) should be ok for us
  * Checked with Lionel: No-Worries is really a public module, conversely to perl-LC, with open sources and (best-effort) support
    * Last release: April 2014

Strategy proposed

* No new usage of perl-LC in existing or new components
* When updating existing components, replace perl-LC calls by relevant perl-CAF calls
* Add a CAF::FileReader API to open a file with modifications disabled
  * Trivial but better than asking people to set the no update flag themselves
* Update perl-CAF to use something else than perl-LC internally
  * Transparent to CAF users

Open a master issue for perl-LC replacement with sub-issues per perl-LC areas (files, processes, exceptions, syslog...)

## Main Issues and Next Milestones

Review of 14.10 issues done.

## Conclusion

Next workshop in Grenoble (France), March 3-5, 2015.

