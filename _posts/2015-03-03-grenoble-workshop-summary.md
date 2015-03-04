---
layout: article
title: Summary of 19th Quattor workshop (3-5/3/2015, Grenoble)
category: news
author: Michel Jouvin
---

# 19th Quattor Workshop Summary


[Agenda](https://indico.cern.ch/event/372683/timetable/)


## Round table - Expectations

* Release: solve the issues with release process
* RH 7 support
* Information on how to use Quattor more efficiently

## Site news

RAL: Aquilon is now in production
* Private cloud, including a VM provisionning prototype service
  * Also need to do some cleanup in Aquilon when the VM is shut down
* Ceph
* Template library used
* Interest of new groups for Aquilon: idea is to share the Aquilon instance

MS
* Focus on support finer granularity changes: main challenge is allowing non expert user to use Aquilon/Quattor
* Quattor Remote Deployer: still used for virtualization but no manpower to implement the necessary improvements


## Platform Support

UGent manages RHEL7 machines since last summer. Several minor issues with pull requests open:
- AII Kickstart config
  - KS variant available but misnamed `rhel7rc` instead of `el7`
- LVM: several commands require --force flag

Major issue: `ncm-chkconfig`, started to work `ncm-systemd`
* RHEL7 provides a `chkconfig` wrapper but `--list` doesn't work
* `ncm-systemd` can digest the `ncm-chkconfig` configuration, opening the path for some "backward compatibility": details still to be figured out
* Gabor: the service configuration should be independent of a particular component, as it is the case for interfaces...
  * Preference for `/software/services`
  * Service description should be as generic/high-level as possible: enable/disable components
* New schema: see https://github.com/quattor/configuration-modules-core/pull/424/files
   * Agreement to start with this schema for the component specific schema
   * For `/software/services`, no ability to define unit type (only `service` can be configured) or target (default target only)
   
Grub2: no need to write a new component to start but will probably be needed to support reverting or definining explicit versions of 
kernel, kernel arguments
* Main issue is to get the mapping between a grub entry value and a kernel version: no trivial match between kernel version in Quattor config and
the kernel title in Grub conf

UGent deadline for solving all issues: June

MS reports problems with `ncm-pam`: should open an issue

## ncm-spma new approach by MS - J. Novy

A different `yum.pm` to ensure convergence to the defined state in one run, like it was the case wit `SPMA`
* MS runs `ncm-spma` only at boot time, so very rarely
* All packages not need must be removed at the first run

Use a first fake install (in fact only the transaction contents is generated) in a test chroot to know what the list should be.
* Performance similar to current `yum.pm` implementation
* Also use YUM `FastestMirror` plugin

Complete rewrite of `yum.pm`: need to be exposed on GitHub for further discussions


## Release process and current release status

14.12 didn't come out because of the changes in the way unit tests are run during the build process
* Before: RPMs were built, unit tests were run and then release was tagged
* Now: unit tests are required to run successfully for the release being tagged
  * Required to build templates for metaconfig modules
  * In principle a good change: unit tests have to succeed on all supported platforms or they are not useful.
  
Supported platforms at this time: EL5, EL6, EL7
* Solaris: should add it as a supported platform starting with 15.4
  * Do not build packages but run the unit tests as part of the release process

There is also the issue of providing versions more recent than EPEL for some package in Quattor externals: general agreement that is should be avoided
as much as possible
* Providing our own version of a package create an obligation to maintain it
* Open question: TTConfig. Version in EPEL doesn't work for some metaconfig services, need to see if we can work around.

Currently, the release is blocked by a couple of metaconfig services that don't pass the unit tests
* Move these services to next release to unblock the release process
* Still the problem of EL5: more tests failing...
  * Release without EL5 tests: check and list problematic services on EL5, acceptable to have metaconfig services unsupported in EL5
  
Nexus central repo: need to ensure that enough people have the right to do new releases of build tools
* Michel to check

### Quattor externals

Agreement to replace existing `externals` repo on `yum.quattor.org` by the new structure`currently under `.externals
* Add EL5 and EL7
* Duplicate panc for every platform

perl-AppConfig-caf: move to last 13.1 release

Update the template library to use these new repos instead of `quattorsrv.lal.in2p3.fr`



## Fine grained access control to configuration modification

SCDB: GRIF experienced with access control based on SVN but did not prove to add any real value and had drawbacks, in particular causing 
unnecessary forks
* In fact template access control doesn't bring much control on configuration changes: any template can change any part of the config

RAL: would be interested to give admin rights on some machines to people with little admin expertise or not well integrated with the core team
* Currently, protect the standard library from direct modifications through commit hooks: a pull request is required
  * Requiring a pull request/peer review for everything doesn't seem desirable and would not scale
* No real need for restricting changes to some part of the configuration, rather to limit changes to some machines
  * This should be implemented after the compilation and before deployment, looking at affected machines: may be doable a the broker level, not
  requiring compiler changes
  * But this would require some sort of host grouping and ownership in Aquilon
  * Difficult in SCDB as no real authentication against the deployment server: only SVN transaction is authenticated
  

## CCM

JSON and types: JSON has untyped data which is a problem when building configuration files where the data should be types
* Stijn added a the ability to do a "typed interpretation" of JSON data (open PR): giving the same results as an XML profiles for unit tests
  * Can be enabled/disabled by a property in CCM
* Agreement to put it disabled in 15.2 and enabled by default in 15.4 after testing by sites

ncm-query: need to support more output formats (like JSON) and add unit tests for output formats
* Proposal
  * move output formatting to a CCM module (CCMFormatter?)
  * Move ncm-query to CCM repo

ncm-query tab completion: current implementation is killed by the time to get the information from the database
* Proposal: cache all paths present in the profile in a text file and use this file for time completion
  * Could be done transparently fy `CCM/Fetch.pm`
    
XML profile support remains and no intention to drop it!
* Problem with XML profiles fixed in December: will be part of next release

  
## TextRender and metaconfig

Getting Started doc for `TextRender` available at https://github.com/stdweird/maven-tools/blob/getting_started/TextRender.md
* Final repository for the doc to be discussed: `TextRender` is a `CAF` componennt but its unit tests are in `maven-tools` repo...

`TextRender` is based on the engine of first version of `ncm-metaconfig`
* `ncm-metaconfig` now uses `TextRender` and provide an higher level to it

`TextRender` can either auto-stringify the contents from the configuration or generate a contents that can be manipulated with a `FileWriter`
* Contents defined in a pan dict

Rendering can be done in several formats, defined by the *module*
* Several built-in formats supported: json, yaml, properties, tiny, general
  * Some modules have issues with reproducibility: a timestamp is added and sometimes ordering is not preserved
* Additional rendering can be defined if using a module name other than a built-in format: interpreted as a TT Toolkit template
  * Template location is defined by `includepath` and `relpath`
  * When using `metaconfig` they are pre-defined
  * See examples in the doc for TT Toolkit usage. A basic example is:
  
    ```
    perl -e 'use Template; my $tttext="Hello [% world %]\n"; Template->new()->process(\$tttext, { world => "Quattor" });'
    ```
  * Several advanced features: loops, newline management
  * Possibility to expose to the TT template some pan configuration properties or some functions defined in the component
  
TT Toolkit template are very powerfull and can replace perl codes... but they may also be a source of bugs! Thus the need for unit tests
* A test framework developed: `Test::Quattor::RegexpTest`
  * Part of the test framework provided in `maven-tools`
* Allow regexp pattern matching on `TextRender` output: ordered list of regexp can be defined
  * By default, regexp are compiled multilines
  * Possibility to negate regexps, either all of thems or a single one (COUNT statement)
  
`ncm-metaconfig`: high level interface to `TextRender`
* Files managed by `metaconfig` are called `services`
  * File name can now be defined in a global variable: see examples
* Can bind the contents to a schema
* Can restart a daemon (or a list of daemons) in case of changes using `CAF::Service`
  * When using the list of daemons (`daemons` property), an action can be specified on the daemon
* Support usual `FileWriter` attributes
* Includes ability to unit test service TT templates
  * Uses `Test::Quattor::TextRender::metaconfig` internally
  * Requires one or more profiles in the service `tests/profile` directory and one or more files containing regexps to apply to the profiles
  * Also requires a Perl test file for the service under `ncm-metaconfig` `src/test/perl` directory (by convention `service-name.t`)
  
Defining site-specific services: currently TT files have to be shipped with `ncm-metaconfig` RPM, thus they have to be developed under `ncm-metaconfig`
directory
* `includepath` currently hardcoded and restricted to one value
* Today restricted to developing services that are shared with the community: good side, will improve the quality by exposing the code! But need to see
how to allow site-specific services
  * Will require at least the ability to ship TT files independently of `ncm-metaconfig`: this also implies the required support in maven tools...
  * This must maintain the ability to unit test things
  * More discussion needed: see https://github.com/quattor/configuration-modules-core/issues/436
  * James: must not lead to less site sharing and a bigger mess...
  
Issue to be addressed with the building process of TT files: currently done in the `test` phase which is not intended to produce anything required to
build the package: need to enhance the build toools to allow doing it in the  `compile` phase.
* See https://github.com/quattor/maven-tools/issues/40

### First candidates for ncm-metaconfig replacement

Core configuration modules
* ncm-aiiserver
* ncm-cdp
* ncm-ganglia / ncm-gmetad / ncm-gmond
* ncm-hostaccess
* ncm-icinga: to be checked (doing some chkconfig stuff)
* ncm-libvirtd
* ncm-nagios
* ncm-nsca
* ncm-ofed?
* ncm-openldap
* ncm-openvpn
* ncm-pnp4nagios
* ncm-postfix: already using TT files
* ncm-sysconfig: prologue/epilogue handling could be a problem

Deprecated: ncm-fsprobe

Need to do the same review for grid components.
* Start with the components still relying on ncm-templates: use `CAF::TextRender` when a component remains needed (e.g. `glitestartup`)

Some components may required the ability to configure path where part of the path is a variable
* See https://github.com/quattor/pan/issues/77
  
## Documentation - W. Depypere

Currently
* 14.6 and 14.8: configuration modules doc on quattor.org
* 14.10: first attempt at using readthedocs.org

Documentation source: currently a mix of inline documentation for Perl modules and separate pod files for the config modules schema
* Config modules schema could be moved to annotations but will require a tool to process pan annotations to generate a documentation file
  * Review Nick's tool to see if it is a good basis: see https://github.com/quattor/release/issues/46
  * Michel: will attempt to annotate one schema file to help agreeing on the tags
* Config modules pod files
  * Broken link and reference to bugs, dependencies
  * Hard coded references to people / email addresses
  * Special characters are often not properly escaped wit `C<< >>`

Current build tools don't check the pod syntax for pod files
* Only for the .pm files

Repo to use with readthedocs.org: create a separate repo not maintained by humans
* Contents updated by scripts from other repos


## Cloud Support

### OpenStack Support Status - J. Pansanel

OpenStack versions used: Havana and Icehouse
* Icehouse support currently in a pull request

Components that can be configured: Nova, Glance, Cipher Keystone
* Nova and Glance used in prod at IPHC
* Includes mysql backend and RabbitMQ
  * memcache to be added in the future
  
IPHC uses standard OpenStack RPM

Quattor configuration relies on filecopy/metaconfig
* Puppet modules not really worth using... not offering the same level of flexibility as Quattor

OpenStack templates will be put in a repo `template-library-openstack`
* Examples to be put in the `template-library-examples` master branch
  * `create-vanilla-SCDB` will need to be adjusted to download it, ideally selectively
  * Need to tag it as part of the release
  
### Other cloud platforms

StratusLab available and maintained

OpenNebula: UGent has a set of private templates, used partly by RAL
* Will try to start a `template-library-opennebula` repo in 15.4
  * Also required a `ncm-opennebula` update: currently a pull request is open
  
  
## Dashboards

Current dashboard prototype allowing to browse information in SCDB and/or Aquilon and to report the nodes that in install state in AII/PXE
* Also lists and gives access to Aquilon sandboxes
* Currently working mainly by greping templates: an improvement would be to use ElasticSearch to issue request on JSON profiles
* Base version in repo `dashboard`
  * Aquilon info is not in this version

RAL also developed an Aquilon web console that allows to execute any Aquilon command
* Based on CherryPy
  * See https://github.com/amazerfrazer/aquilonconsole
* Dashboard prototype could be merged with it

ULB started also some developments based on the initial dashboard prototype
* Need to pull a request to get it merged in to the  `dashboard` repo



  
To be discussed - Thursday
- metaconfig: why service test files are not under src/test/metaconfig?
  