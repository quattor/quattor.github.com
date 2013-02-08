---
layout: article
title: A possible package repository architecture for upgrading with Yum
category: blog
---

## Introduction

The new SPMA makes it easy to install new packages, and their
dependencies.  However, there may be dependencies that are not part of
the profile and that might get updated at random times.

We want to avoid such uncontrolled upgrades.  One way to avoid them is
to do the old-style package management: specify everything in the
profile, and fix the dependency hell "manually".  This document
proposes a different way to prevent these random upgrades, by taking
snapshots of the Yum repositories.

Granted, some packages must stay at the same version independently of
the contents of the current Yum repositories.  For those we'll use the
old API, and lock down their versions.  But I suspect we'll benefit
from letting some dependencies free.

## Repository mirroring process

The diagram below shows how we could mirror one repository:

![Repository mirroring and snapshotting](img/repository-mirrors.png)

The upstream repo would be mirrored with `rsync`, `reposync`, `wget`,
or whatever other tool.

After this mirroring is completed, a snapshot would be taken.  You can
use use LVM snapshots, store the software in a snapshotting filesystem
like ZFS, BTRFS or GPFS, or whatever fits your organisation.

## Mapping nodes to snapshots

We can map nodes to snapshots in two ways:

### In the profiles

Nodes would choose in their profile which snapshot they are
"subscribed" to.

The repository templates would specify the URL like this:

    structure template repository/foo;
    ...
    "url" = format("http://server/packages/%s/repo_name", OS_SNAPSHOT_ID);

where `OS_SNAPSHOT_ID` is some global variable that reflects the date,
or something similar.  Rolling an upgrade would mean changing this
variable.

We can even find a way for defining different snapshots for different
repositories.  For instance, _use last week's snapshot of EPEL but
last month's snapshot of SL_.

This has the disadvantage of requiring editing Pan code for routine
operations.  But it offers any desired granularity:

* For the entire organisation
* Per cluster
* Per node
* Per machine type.
* Per repository
* Any other.

### In the repository server

Another approach would be to set symbolic links or bind mounts to each
snapshot.

The `OS_SNAPSHOT_ID` variable above would contain any link present in
the server.  The software managing the mirrors and snapshots would
also set up these symlinks according to the organisation's policy.

Handling these symlinks in a consistent way may not be trivial.

Also, it's unclear how friendly this would be to caching proxies that
users might put in front of the repository.
