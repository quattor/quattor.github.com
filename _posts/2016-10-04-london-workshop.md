---
layout: article
title: Summary of 22th Quattor workshop (2016-10-04 to 2016-10-06, London)
category: news
author: Michel Jouvin
---

# Summary of 22th Quattor Workshop


[Agenda](https://indico.cern.ch/event/560421/)


## Site News

MS
* Some reorganization: SW distribution added to configruation management group under Nathan responsibility, Dave taking over from Nathan and Gabor now in charge of Operating System/Linux support (handing over to Dave the Aquilon broker development)
* Main challenge: upgrading the configuration modules and core libraries, many still very old
  * Currently working on using 16.8 as the basis for RHEL7 with the hope to use it for EL5/6 too
* Working on monthly upgrades of OS (and related tools): using YUM snapshots
  * Using yumng rather than yum ncm-spma plugin
* Solaris: Solaris 11 support, AII extended to support Sparc obp rather than pxe/dhcp  
  * Solaris 12: not yet looked at it but no major issue expected
* Still running ~500 EL5 systems: hope get it down to ~200 in the coming months but expect a long tail after that
* Difficulties to stay up to date with all the dependencies that are required to run configuration module tests
  * Michel: using template `quattor-development.pan` from OS `rmps` directory may help to deploy or identify required dependencies
* Maven also seen as a difficulty as there is no source RPM build and it makes difficult to insert MS patches
  * Currently maintaining a MS branch, having to do a lot of merging
  * Would like to get away from patches but may need to have some and would prefer to rebuild the official version a different minor version after applying the patches
* AII should handle partition alignment
* Any plan to support `systemd-resolved` in replace of `/etc/resolv.conf` for configuring DNS resolver?

RAL
* CentOS 7 work started: pushed by Ceph
* Still trying to get rid of SCDB but not yet complete
* Active work on virtualisation through container: about to release a lot of services in a Apache Mesos cluster
* James suggests to build as part of the release a plenary template library whose root directory will be the Quattor version number. Allow to easily switch from one version to another one and reduces the risk of a fork (as local changes to the plenary version will be lost in the next version)...

ULB
* Working on UEFI support in AII, required by last systems purchased (EL7)
  * Requires at least one additional partition `/boot/uefi`: would be great to add it to `filesystem_layout` and be able to define a variable triggering whatever is required in the configuration for UEFI support
* Still fighting with Aquilon installation because of MS dependencies: an up-to-date documentation is required
* Interested by EL7 support for grid services
  * Michel: umd-4 branch was started but never merged... some preliminary work at LAL. Will be added to next version.
* Problem with ncm-chkconfig not stopping/removing configuration of services no longer part of the configuration
  * In fact the more general problem of unconfiguring/restoring previous state when something is removed from the configuration: what is the state to restore
  * Non trivial but worth a discussion: CAF::History may help but is not necessarily the complete solution
  * James: another variation of the problem is changes in config file names with the old one left (for example under `conf.d`)
  
  
LAL
* Installation on systems with system disks larger than 2 TB: requires a small partitions with type `biosboot`.
* WIP: use ncm-ceph for Ceph deployment
  * Currently Quattor only deploys the packages and the basic configuration
  

## Configuration Modules

### ncm-metaconfig

ncm-metaconfig seen as a component that can run many things with the risk of one of them failing and preventing other dependencies to run
* One workaround is to define a separate configuration path for the critical things and alias it to metaconfig: will result in ncm-metaconfig running twice

Sometimes would like to run an arbitrary command but not allowed
* Was a design choice in metaconfig
* One possibility is to subclass it and add the support for an arbitrary command

### ncm-systemd

Support for instances
* Instances need to be created from templates
* To manage all instances as a group, create a target with all the instances
* This has to be done through `/software/components/systemd`  rather than `/software/components/chkconfig`

Start/restart of services
* Kept the original chkconfig behaviour where the service is started/stopped only if the service was previously stopped/started and the desired state was changed
* To be checked: is the service restarted if its configuration is changed 

'replace` property: when true, says to ignore any configuration for the service shipped by the system or provided by a RPM

### ncm-spma

APT plugin available as a [PR](https://github.com/quattor/configuration-modules-core/pull/821).
* Used at RAL to manage a few Ubuntu VMs
* Several comments to address before merging the PR
* Worth testing: should work for most cases

### Exceptions

Agreement to move away from `LC::Exception` and have a `CAF::Die` that will do the proper logging before raising a standard exception through `croak`.

## Aquilon

Packaging is critical for adoption
* Agreement that getting setuptools to work for Aquilon installation/upgrade would be great step forward

### Tooling around Aquilon

MS developed several related tools that may be useful for the community and may be upstreamed...
* `aqs`: a wrapper over `aq show` with short options
* `ckey`: utility to put colours on key/value display for easier reading. Receive input on stdin
* `getprof`: dowload a host or cluster profile from the broker. Sent on stdout.
* `rifle`: parses a profile and renders it as key/value pairs (similar to CCM but without requiring it). Can unescape keys. Can contain `*` in configuration paths. Option to display multi-line values on several lines. List indexes (generally not meaningful) can be replaced by `#` for easier comparison between profiles.
  * `trifle`: C version of `rifle` processing only JSON profiles without using any JSON parser (streaming in and out). 15x to 20x faster.
* `prdiff`: print differences between 2 profiles parsed by `rifle`.
* `diffuniq`: find unique differences into a set of differences. Option to ignore some differences, based on a regexp.
* `diffprof`: in a recursive diff, identify all unique differences and a display the number of occurences of them. 
  * Needs two directories containing the same profile names
  * Diff done in // for good performances with a large number of profiles
* `make-diff-complete`: a set of tools to display profile differences between the current sandbox and the version without the mods introduced by the sandbox: walk through the git history to identify the sandbox parent commit, rebuild the profiles for this version, build the sandbox and run `diffprof`. Can work with a specific set of profiles (static profiles or sample of live profiles) or all live profiles.
  * Splitting the compilation of a large number of profiles into several // panc instances: showed a significant speedup
  * JSON turned out to be much faster to parse by the (Python) tools: JSON used internally by the tools whatever is used for the deployment
  * Currently based on a Makefile that does the proper glue between tools and is MS specific... Anyway underlying tools are generic.
  * MS plans to use these tools through CI (Jenkins) as part of the `aq publish` workflow

Agreement to open source these tools in a `aquilon-tools` repo
* Some of the tools could also be used in the SCDB context to replace the current (very basic) `compare_profile` or other site-specific tools
* Should work on improving `aq compare` to use these tools internally


### Atomic and Test Deployments

Objectives: rock-solid deployments and back-outs
* Be confident in the knowledge of the effects of deploying a change: really push it without applying the changes
* Quickly and 100% reliably remove a change
* List of changes recently applied to a host
* Identify which changes caused a particular artefact
* List all the manual steps required to back out a change in case of emergency (machine no longer manageable by Quattor)

Proposed changes
* `aq deploy --compile`: current `deploy` then `compile` with the risk of interleaving deployments. The broker can block any other deployment until the end of the compilation and the notification of the clients
  * In the notification, add a change id that will be passed to ncm-cdispd and will be used to produce a deployment log for this change id. The change id could be use on the git commit id (with possibly additional data). Need to ensure that this doesn't lead to recompiling every profile each time.
  * Not clear how you ensure that all the intermediate changes are deployed: currently `ccm-fetch` is picking the last profile, not the intermediate ones if any. And in fact not necessarily desirable to apply all the intermediate changes one by one: often one change introduces problems fixed by the next change/profile.
  * An alternative could be to track the set of change ids associated with a particular deployment
* `aq undeploy`: undeploy a change id. Done by reverting associated Git changes and producing new profiles but a new type of notification (`ccu` for undeploy) that instruct `ncm-cdispd` to do a rollback rather than a deploy, using the change id deployment log.
  * Would imply undeploying any change after the reverted change id
  * Some actions may be marked as 'not undoable'
  * Possible to add `--redeploy` to redeploy those later changes after undeploying the buggy change id
  * yum changes are difficult to track: not necessarily associated with changes in profiles
  
Discussion
* Agreement that `ad deploy --compile` should be implemented
* Skepticism about the undeploy idea: the problem is too general to be solvable...
  * James: concentrate on the file use case. Track file changes (CAF::History) and decide/implement what must be done to undo a file modification action (not trivial, depends on cases)
  * Stijn/Luis: first try to make something of CAF::History. Currently only used for logging events but those events could be consumed by `ncm-ncd` to maintain a component-agnostic database of modified files for example.
  * On the other hand, improving the logging of actions done to ease troubleshooting and give a chance to understand what must be done to "undeploy" the change would be a good step forward
  * CAF::History could be associated with change ids and help to store file backups in diff formats rather than multiple version of the entire file.
  

Test deployments: `--test` option to `ad deploy`
* Produces temporary profiles
* Notification with a `cct` event
* `ccm-fetch` fetches the profile as a test profile rather than a production one
* `ncm-cdispd` dispatches components with `--noaction` and produces a deployment log sent back to the AQ web server, that can be viewed with `aq show testing --change id`.
  * `ncm-ncd` actually responsible to push the deployment log back to the web server rather than `ncm-cdispd` which has `ncm-ncd` dispatching as its only responsibility
  
Suggestion to use JSON as the format of deployment logs to make them machine parsable
* Nathan suggests to put the verbose information in the deployment logs and use syslog to produce the file (will take of serialization between event sources) 
* A DB on the machine for keeping the history may use another format like sqlite


## Quattor Building Tools and Releases

MS interested in getting source RPMs for easier integration of their patches in MS-specific RPMs
* James will try to produce them as part of the next release

Component config.pan: MS needs to patch them to include a MS specific template at the end
* Proposal: include a site specific template at the end of the standard config.pan
* Proposal 2: generate the config.pan from Maven rather than having one per component.

panc: Cal was clear he has no longer the time to review pull request
* Gabor is the main panc expert, let's rely on him!
* Ensure that we add unit test covering proposed changes
* Release is produced with Maven the same way as the Quattor release


## Discussion of Open Issues  

https on quattor.org: no real solution until proper support for https on custom domains is provided by GitHub

Validation of variables by a schema: in fact, raise the questions of what is the interface to the template library
* Action: Michel should start a documentation on how variables are used in the template library, how they are named, `config.pan` as the entry point for features...
* Need to make progress with adding annotations to the variables in the template library and to processing them to build a documentation
  * MS has a couple of script doing some processing that may be used as a starting point
  
  
## Conclusions

Next workshop: Annecy?
* Michel discussing with the local people

[FOSDEM](https://fosdem.org/2017/) participation: interesting to meet people but quite difficult to get a talk
* DevOps and Config Mgt track has 10x more talks submitted than what can fit into the agenda...
  * FOSDEM talks are generally not about a specific technology or implementation but more about what was learn from a concrete experience: could we present how we enable a high level of sharing through the releases containing configuration modules and the template library, avoiding the sites to fork with difficulties to integrate further development by the community...
* Submission usually before December  

