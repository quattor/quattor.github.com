---
layout: article
title: Summary of 24th Quattor workshop (2017-10-25 to 2017-10-27, RAL)
category: meeting
author: Michel Jouvin
---

# Summary of 24th Quattor Workshop - RAL - 25-27/10/2017


## Site News

### RAL

Trying to get the last version of the broker in production
* Reduced size of the database by over 30GB by purging old audit log entries

Releasing a new OpenStack infrastructure
* Need for Debian/Ubuntu-based VMs so trying to sort out the the `spma`/`apt` back-end
  * Also the desire to manage [Cumulus Linux](https://cumulusnetworks.com/products/cumulus-linux/) switches
  * Still missing: network management on Debian
  * Currently using the Quattor RPM converted on the fly: looking at the [`jdeb` plug-in](https://github.com/tcurdt/jdeb) for Maven
* Working on template library changes required for last OpenStack version
  * UGent also interested
* Found that running services in fail-over mode was a source of complication
* Deployed IPv6 in production with Quattor, using Pan to calculate an IPv6 address for every IPv4 address.
> See [HEPiX talk](https://indico.cern.ch/event/595396/contributions/2558578/attachments/1448031/2231673/jrha-hepix-2017-ipv6.pdf) for details.

### Bruxelles

IPv6 configured and working

Need to adapt the current approach for provisioning resources in the OpenNebula cloud:
currently based on AII hooks

No progress with Aquilon: no time to deal with it

### LAL

No time to work on Aquilon since Annecy, despite a working broker

Main focus in the last months
* OpenStack cloud scale up
* Design/procurement phase for a new distributed Ceph infrastructure
* Fixing of some Quattor configuration modules for EL7


### MS

Salt used to manage VM: working on integration with Aquilon broker

Working on replacing previous "dump zone files" approach to managing DNS with a system that pushes changes into DNS in real time using the PowerDNS API.

`ncm-systemd`: would like to be able to disable everything that is not appearing in the
profile
* Used to do it with `ncm-chkconfig`
* In fact work in progress by Stijn: see https://github.com/quattor/configuration-modules-core/pull/1119


## Releases

17.8 out this morning: main change is a almost complete rewrite of `ncm-network`
* Requires some careful testing by sites, despite it has been extensively tested

Skip 17.10, next release will be 17.12
* Nothing urgent in the backlog
* Release candidate mid-November, release first week of December

Proposal for next year: one release every 3 months
* Does not prevent additional releases if urgently needed or to release one particular
  new feature/change (like the `ncm-network` rewrite)

## Open Issues

Discussion of issues marked as `discuss at workshop`

### Configuration modules

`ncm-chkconfig`
* Fix the pan issue #163 (applying defaults in `dict`) rather than implement a function
  in `ncm-chkconfig` to work around the problem

`ncm-systemd`
* How to manage `xinet` services, something that used to be doable with `ncm-chkconfig`
  and is no longer with `ncm-systemd`
  * Write a new component `ncm-xinetd`
  * Other solution is to reconfigure `xinet` to use a non standard directory for services and manage services with `ncm-metaconfig` but seen as a little bit hacky

`ncm-sysconfig`
* Implement service restart: still the feeling that `ncm-metaconfig` could be a replacement
  if it (or `ncm-ncd`) was able to remove no longer used files
  * Agreement to keep this document for the time being and enhance it
  * Implement restart as it is done in metaconfig by listing the daemons to restart

### `ncm-ncd`

Clean up of `noaction` handling: Stijn will try to look more closely at what is involved
* Seems a good thing to do if it is not too much effort and has no risk to break less
  maintained components

### CCM

Store downloaded profiles in Git
* Looks as a good idea
* No real reason to keep the current directory structure in the Git repository: will allow
  to really benefit from the change (remove the need to purge)
  * Use commit message to handle the meta-data associated with a revision, like CID
  * Need to check what is the impacted code but should be pretty well contained in CCM

Removing `CCM:Element`
* Not used by any standard configuration modules any more
* MS is still relying on it: let's wait for their green light!
  * No drawback to keep it without using it

### AII

Support active configuration for plug-ins: still no consensus reached
* Not seen as urgent, keep for another workshop where we have all the experts in the
  room (Stijn, Gabor)

### CAF

Implement restart-if-running logic in `CAF::Service`: agreement to do it using standard
behaviour with `systemd` and `condrestart` with `chkconfig`
* Up to the component developer to check that `condrestart` is supported by the init
  script


## Aquilon

Support JSON in the API (aka JSON formatter): protobuf v3 would make it easy/easier
to support JSON, so probably the right way to go.

See issues.

## `panc`

Problem doing releases... only release candidate can be done
* Not clear why and what could have changed since 10.3

10.4: already tagged despite the releasing problem
* Do not change it

Already a few things for a next release (10.5)

Dependency management: how to improve the handling of a dependency moved in the load
path, currently undetected
* A difficult problem as the dependency is registered at a time the `loadpath` is not
known

Support for keys starting by a number
* Would be great to have: should be allowed with the back-ends we use nowadays (only
the deprecated XML back-end had a problem, in `panxml` keys are stored as attributes)
* Interfere with escaping/auto-escaping discussion: to be followed up

Internal implementation of `push`/`npush`(`dpush`)
* Agreement
* Keep the `npush()` name for backward compatibility and add `dpush()` to match `dict`

Continue with the same numbering scheme, distinct from Quattor releases: makes sense
for the language, quite independent from the other components


## Release Process

Merge configuration-modules-core and configuration-modules-grid: no opposition
* Either create a new repository and merge both to it or merge grid into core
* Keep history using `git subtree`

Merge all template-library repositories into one?
* Current branches per version are confusing for users and adding complexity to the
release process
  * Multiple masters
* It is impossible to open issues against a specific branch: only against a repository
* Contributing patches to several branches requires several pull-requests when one PR could update
several directories
* Often one PR in one repository depends on another PR in another one and this cannot be well
expressed
* Start by template-library-core and -standard
* The new repository top-level directories will reflect where the templates are coming from:
standard, core...

Merge CAF and LC repositories?
* LC is now sort of a "private code" in the way we use it and it is becoming an internal
tool used by CAF, mainly
* Even consider merging all the Perl repository into one?
  * quattor-framework?

Open question: how to move the open issues or to make the existing repositories read-only?

> Note: Two weeks after the workshop GitHub added functionality for [archiving repositories](https://github.com/blog/2460-archiving-repositories) which solves the problem of preserving old repositories in a read-only state.

## Quattor and SELinux (Michel)

* SELinux has come a long way. Now supports permissive mode which makes things work just as they were unless you explicitly enable it (e.g. can enable it to prevent `httpd` doing evil things without effecting rest of box). Also get some audit logging by default.
* Permissive mode does not work if `SELinux=disabled` is set which is what we all do today
* Most important change in Quattor is to ensure we are preserving the appropriate context for files and directories managed by Quattor.
* `CAF::FileWriter` already runs `restorecon` after modifying a file (https://github.com/quattor/CAF/blob/master/src/main/perl/FileWriter.pm#L31)
* Proposed creating a new component (`ncm-selinux`) to allow managing SE Linux enforcement, managing properties of policies but not full policies which are very complex (they could be downloaded with `ncm-download` or packaged as RPMs).

## `packuilon` (RAL)
A collection of scripts to allow OpenStack VM images to be automatically built based on personalities from Aquilon. It uses Packer (https://www.packer.io) to do the image building. Open sourced python scripts: https://github.com/stfc/packuilon

Depends on RabbitMQ but then so does OpenStack so you have one running anyway. Receives servers notifications from Aquilon.

Installation instructions include `aq bind server` which invokes a Quattor template: that template just installs some RPMs (packer and what's in the git repository).

## Aquilon GitHub Repository
All issues were reviewed and a number of older ones found to be already fixed. Gintare worked on validating the install process on RH7.

## Backlog Review
All open pull-requests with no milestone were reviewed. All pull-requests without external dependencies were assigned to 17.12 which has made the release quite large now. Some pull-requests are ready for merging now 17.8 is out, these should be handled by the weekly stand ups.
