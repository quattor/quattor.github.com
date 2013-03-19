---
layout: article
title: Quattor 13.3 is out!!
category: news
---

We have just tagged and uploaded to the
[Yum repositories](http://yum.quattor.org) Quattor 13.3.  Special
changes include:

## Configuration modules

### ncm-network

The old `ncm-network` is part of this release.  It is shipped for
completitude.  While it will be replaced by a more maintainable
component, we need to be able to configure the network now.

### ncm-openldap

UGent's fork of `ncm-openldap` has made it into this release.  The
schema is slightly different from the old version, but it adds the
ability to handle multiple databases, better defined access
restrictions and much more.

### Other changes

* `cron`: remove whitespace from log file names, even if the job name
  has them.
* `sendmail`: bug fixes
* `spma`: many bug fixes.  Users of the Yum-based SPMA are
  **strongly** recommended to upgrade to this release.

## CCM

* `ccm-fetch` can ignore `/etc/noquattor` by passing `--force-quattor`
  on the command line.
* Some spurious dependencies have been dropped.  This version should
  be easier to install on very old platforms.
* CCM can now download profiles from dynamic URLs.  For instance,
  `https://my.quattor.srv/profiles?profile_name=node.doma.in&version=1.2`

## AII

* It is now possible to enable SSH during the Anaconda phase, making it
  easier to debug installation problems.
