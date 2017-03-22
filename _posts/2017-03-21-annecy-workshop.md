---
layout: article
title: Summary of 23nd Quattor workshop (2017-03-21 to 2017-03-23, Annecy)
category: meeting
author: Michel Jouvin
---

# Summary of 23nd Quattor Workshop


[Agenda](https://indico.cern.ch/event/607604/)


## Site News

### LAL

Main project remains migration to Aquilon: no time to really work on it
* A driver for moving forward could be the starting distributed Ceph project

### RAL

ECHO storage project, based on Ceph, going to production these days and entirely managed by Aquilon
* Gave up with `ceph deploy` and thus with `ncm-ceph`: now using `ncm-metaconfig` to manage `ceph.conf`
  * LAL doing the same
  * May be worth a standard schema for Ceph in `ncm-metaconfig`: in fact reusing `ncm-ceph` schema
  * May be time for a standard set of templates for configuring Ceph or at least to 
    share them as examples
  
Move to OpenStack in progress: OpenNebula still alive but OpenStack ready for production
* Partly related to the fact that there is a distinct Ceph instance for each cloud: 
  too limited power

SL5 almost decommissionned

SCDB kept only for CASTOR

Expecting soon switches running Cumulus Linux, a Debian based distribution
* Plan to manage them with Quattor: need apt backend

Aquilon usage increasing: another department managing its HPC system with Aquilon
* New management of plenary templates will ensure that template library is not forked locally and that fixes are pushed upstream

Continuous Integration with Aquilon: a "fake" machine for each personality

### UGent

Releasing a new storage platform

Also working on an iRods platform

Will increase the OpenNebula cluster


### Bruxelles

Still fighting to get Aquilon working
* A new sysadmin interesting to use it at VUB

Running OpenNebula with Shibboleth authentication (from Gent)

Relying more and more on metaconfig: would be useful to have more working examples

IPv6 support: would like to see some progress

Also have plans with Ceph but no time to do something yet


### LAPP

Mainly rely on the grid template library

Also looking at Ceph and IPv6
* But Ceph is managed with Puppet

Quattor upgraded regularly, even if not necessarily at the latest version


### MS

EL5 : still a few hundred nodes but going down
* EL7 increasing: in fact skipping one version for many services

Virtualization: moving away from our in-house developed Perl for configuring ESX that was consuming Quattor profiles 
to using Salt Stack. Data flows from Aquilon to Salt using Quattor profiles since XML/JSON remains a highly scalable 
way to distribute data from the Aquilon database.

Plan to move from AFS to Docker or rkt (aka Rocket) for SW distribution
* Containerizing the grid infrastructure: interested by sharing experience on Quattor with containers
  * RAL (Andrew) has a good experience

Running 17.2 on our EL7 plant but EL5 and EL6 are using CAF 14.10 with a variety of different versions of 
newer components. Plan to move rest of plant to 17.2 in the next few months now we have tested it via EL7 roll out.

OS version lifecycle now managed in Aquilon: different templates for different stages of the lifecycle

2 new persons on Quattor/Aquilon: one in London and one in Montreal


## Aquilon

Python requirement: 2.7
* RAL assessed that it is working on EL7: probably a better solution than installing Python 2.7 on EL6 (in Software Collections)
* RAL not planning to upgrade its production broker currently using EL6

Creating the RPM seems not to be a major problems: dependencies available as RPM

James: no known blocking issue, schedule a hands on session during the workshop to start an instance from scratch and identify the problems
* Tomorrow afternoon
* Decide which version to use: building RPM for the last version may require to merge some patches to get it to build successfully

Development process less transparent than other parts of Quattor: first happen at MS and then pushed to gitHub
* Makes more difficult to identify changes and impact of upgrades, also difficult to 
contribute outside MS...
  * Chicken & egg pb: MS doesn't receive feedback so not much motivation so far to address 
  this problem but no opposition to evolve
* Probably need to improve the communication around planned changes before implementation
* Proposal: MS pushes changes as soon as possible as PR on GitHub exposing the change 
and allowing the community asking clarifications if needed
  * MS cannot directly develop on GH: would make the process too slow for internal needs
* [Weekly meetings](http://www.quattor.org/contacts/) could also be used to discuss issues or present ideas MS are working 
on
* Need to work out how PR contributed by the community can be imported by MS
  * GH allow to download a PR as a patch file
  * A few open PRs open by RAL need to be rebased on last version and reviewed by MS

Would be good to be able to run the unit tests for Aquilon on Travis: should be feasible


## Pan Compiler

Several stability fixes and a few new features added since 10.3: time to release 10.4
* How to release `panlint`: in `panc` package or as a separate one
  * Probably better to release as a separate package to manage Python dependencies
  * Also easier to produce the RPM with `setup.py`
  
  
## Next Release

Backward incompatible changes: distinguish between those internal to Quattor code delivered as part of the release 
(maintained on GitHub) and those affecting users
* Need a long deprecation period if users are affected

Do we need 17.3? Help to reduce the number of PR/changes per release and deprecate things progressively
* Reduce to the PR that are introducing critical changes that are necessary to fix/add other things in further releases
* Release panc 10.4 at the same time to be able to use its new features in 17.4
  * panc 10.4 may become a requirement starting in 17.4
  
  
## Pending Issues

IPv6 support in Aquilon
* Pan: need built-in functions in the compiler to manipulate IPv6 addresses, in the same way as we have for IPv4
  * Current schema is working and validating: not a blocking issue. But required for the broker
* Broker: potential problem if a FQDN has both an IPv4 and an IPv6 address (expect one address per FQDN)
* AII: not required as long as hosts are dual-stacked

[Configuration module deprecation](https://github.com/quattor/configuration-modules-core/pull/1051)
* `mcx`, `directoryservices`: agreement to remove them
* `fmonagent`: MS still using it, will add a deprecation warning
* `syslogng`: still needed

Moving to separate packages (and repos) per OS version: a long term goal
* Would make easier testing all the OS version and their dependencies

[aii-core DHCP.pm vs. aii-dhcp](https://github.com/quattor/aii/issues/166)
* Agreement that aii-dhcp (DHCP plugin) is the right way to go: need to merge the code
* `aii-dhcp` command line not used by anybody: remove it

CCM: MS working on a Python CCM implementation to support developping Python configuration 
modules
* Driven by the Quattor Remote Dispatcher (QRD) use case
* An alternative, probably more complex, would be to develop a CCM web service with 
  a REST API


## Documentation

Progress with annotations: more and more available

Bad side: "looks ugly", search doesn't work
* Due to the use of Markdown: should move to ReST
  * Almost done

Minor issues
* default values are not included in pan annotations: see https://github.com/quattor/pan/issues/132
* metaconfig files are produced only `maven test`: should not be a major problem if 
documentation is produced during the release

Also need to clarify what need to be in the pod for Perl Modules
* For example do not document as pod internal functions so that they don't end-up in 
the documentation
  * Or remove from what is pushed to the doc, any pod entry for an `_` method

Would be good to also put some structure in packages with a lot of functions
* Last version of the script to produce the documentation is now sorting the headings 
at level 2+

Other action: complete the move of the developer documentation from Trac wiki to the 
web site


## Development Tools

* run pylint on Python scripts in release repo
* Consider running ShellCheck on bash scripts
* Enable approval requirement by one of the repo owner for each repo: James will look 
at doing it through the API
* Enable CodeClimate on the release repo
  * Currently enabled on pan repo in an open PR
  * Alternative to running pylint for Python  scripts
  * Also runs the ShellCheck backend so this is a good way of running it
* [SonarQube](http://sonarqube.com) is a similar solution that could complement CodeClimate, 
if needed for some parts of our code base


### Remote discussion

We trialled the use of [slack](http://quattor.slack.com) during the meeting which proved useful 
for sharing of links and watching ongoing GitHub activity. Anyone who would like an invite to join 
should ask an existing slack team member to invite them.


