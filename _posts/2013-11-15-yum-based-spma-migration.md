---
layout: article
title: Yum based SPMA migration, putting it all together
author: Victor Mendoza
category: blog
---

Since several people have asked for pointers, here is a brief summary of our experience so far migrating our Quattor managed systems to the Yum based SPMA.

Intended audience: system administrators who already have Quattor managed systems.

## Required reading:

At the very least, you should read:

* [SPMA with Yum as backend](blog/2012/08/28/blog-spma-yum.html)
* [Mirroring the Quattor Yum repositories](documentation/2013/01/11/mirroring-yum.html)
* [A possible package repository architecture for upgrading with Yum](blog/2013/01/29/package-layout-proposal.html) 
* [Upgrading to the Yum-based SPMA](documentation/2013/01/29/spma-yum-upgrade.html)
* [Release notes for Quattor 13.02](documentation/2013/02/07/quattor-13.02-notes.html)
* [Managing packages at scale with Yum-based SPMA](documentation/2013/02/07/yum-package-management.html)
* [Experiences with package cleanup](blog/2013/03/27/cleaning-up-packages.html)
* [Installing and removing packages with Quattor](documentation/2013/04/05/package-management.html)

Before starting you should understand ...

* what is going to happen,
* what is going to change,
* and what are the consequences,

... otherwise start over.

## Templates:

We started by creating a new test cluster with a lone test server, it's main difference being having precedence for recent Quattor components in the include path.

I won't dwell on the gory details here, because things have evolved and much of what we did is no longer necessary.

### Workaround, alternate package lists:

To be able to have alternative package lists next to our existing ones, we added a global variable:

```bash
variable RPMS_SUFFIX ?= '-yd'; # in our test test cluster
...
variable RPMS_SUFFIX ?= '';    # everywhere else
```

Which we then used wherever needed by replacing existing includes, e.g.:

```bash
- include { 'rpms/config' };
+ include { 'rpms/config' + RPMS_SUFFIX };
```

This allowed us to start with cleaner package lists right away, although we did have to add a couple dozen rpms/config-yd templates just to get started.

## Tests:

### Install:

Installation worked almost immediately, although our AII/PXE server still running an older Quattor release, forced us to do some minor fixes to the generated kickstart files (e.g. removing volgroup entries).

### Upgrades:

To trigger ncm-spma to run on repository changes we added:

```bash
'/software/components/spma/register_change' = append('/software/repositories');
```

Supported upgrades worked beautifully, we tested:

* OS security updates
* SL6.3 to SL6.4
* Quattor 13.5 to 13.9

Our test machine immediately became and stayed our most up-to-date and least vulnerable Quattor managed system.

### Migration:

Migrating from the old SPMA to the new Yum based one also worked nicely.

Since our target configuration already had cleaner package lists, we used a temporary cluster to ease the migration which had the new Quattor components but continued to use the old package lists (RPMS_SUFFIX = '').

We migrated a second test host by:

* moving it's object profile to the temporary cluster
* 1st deploy
* moving it's object profile to the final Yum based cluster
* 2nd deploy

Once all test profiles were on the final Yum based cluster, the temporary cluster was removed.

### Failures:

We were unable to break the test systems through:

* repository unavailabilities or outages
* repository metadata corruption
* broken RPMs

Mixing up repositories did indeed create quite a nice but recoverable mess.

## Repository mirrors:

We created local repositories mirrors (with reposync), mostly because we wanted to have repository snapshots, which are very advisable once your are managing hundreds of systems:

* Quattor, OS:
  * Quattor (13.9)
  * SL 6.4
  * EPEL6
* Grid middleware:
  * Certificate authorities
  * EMI-3
  * CernVM-FS
* We also plan to add:
  * SL 5.10
  * EPEL5
  * EMI-2
  * HEP_OSlibs
  * Perfsonar-PS (internet2 + web100)

## Repository snapshots:

We also created repository snapshots, because we wanted to be able to keep controlling when and where updates happen and also to keep repository consistency:

* based on the date
* all mirrors are included
* metadata is generated locally on each new snapshot (with createrepo)
* with hardlinks (we plan to switch to filesystem snapshots asap)

## More templates:

Our test nodes didn't do much, just sitting pretty. So once we decided to start using the new Yum based SPMA for production nodes, we needed to create another couple dozen alternate package lists, again using the RPMS_SUFFIX variable.

Since we were going to re-install all our Grid worker-nodes with SL6, most of these new package lists were Grid related.

Several difficult to maintain package lists (SL5, SL6, i386, x86_64, noarch, updates), could be collapsed into refreshingly simple templates, e.g.:

```bash
unique template emi/wn/rpms/config-yd;

# EMI WN
'/software/packages/{emi-wn}' ?= nlist();

```

After some cleanup, the new templates will surely be added to the standard template libraries, although probably in separate/clean branches as the default package lists (without the RPMS_SUFFIX trick).

## Production use:

### Initial install:

Our initial install did not go as well as planned.

Most issues were SL6 related:

* block device name changes
* network device name changes
* libraries moved to /usr/lib64

One issue was repository related (due to a corrupted RPM):

* the RPM had to be re-downloaded
* new snapshots were created
   * the alternative was manually purging repository metadata from Squid servers

No problems were strictly related to Quattor.

### Upgrade:

As soon as we experienced the huge difference of this new simpler work-flow, almost immediately we started wanting to upgrade everything else.

So far, recently drained DPM_disk servers and the BDII_top were also upgraded (re-installed).

### Grid middleware update:

Since the initial upgrade, Grid middleware updates and OS security alerts have been published, these were easily managed by:

* updating & verifying our mirrors
* creating new snapshots
* updating test nodes to the new snapshots
* configuration changes (if any)
* updating the remaining nodes
* purging obsolete snapshots

### Live migration:

Since we can't re-install everything, we've started doing live migration, which still seems crazy but works:

* create new alternate package lists, if needed for each node type
* migrate using the double deployment described above
* the systems are migrated while in production and without downtime

Naturally, this was we tested first on idling nodes that were to be re-installed anyway.

And of course, we are doing this very slowly and carefully, almost one system at a time, we plan/hope to have finished migrating all our nodes in a couple of months.

## Lessons learned:

Repository mirrors should be verified and reliable (rsync?)

Don't manually manage repositories, keep things safe through automation, mirroring and snapshotting.

Write things down. We completely forgot about filesystem snapshots.

## Conclusions:

Having to manage both old and new Quattor releases side by side does not add any severely time consuming workloads, but is much more bothersome, because you must continue to suffer through the dependency hell, and now only for some of your systems.

Sites that don't internally produce OS security or Grid middleware update templates are the ones who stand to benefit the most if they upgrade, since they won't have to continue hoping and waiting for somebody else to share templates.

We should have done this earlier.

## The bad news:

As soon as we finish migrating and upgrading all our hosts, I'll undoubtedly stop contributing OS security and Grid middleware update templates.

The few other people who also share these templates will maybe notice the added workload, and probably also consider upgrading to avoid it altogether.

Best case scenario, the old package lists will be available even less often and even later, maybe you should also start planning to upgrade.
