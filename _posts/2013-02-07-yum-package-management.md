---
layout: article
title: Managing packages at scale with Yum-based SPMA
category: documentation
---

## Introduction

The Yum-based SPMA alleviates greatly the RPM dependency hell.
This is done by shifting the burden on maintaining each package to
maintaining properly our repositories.

If you used to just download many repositories into the same
directory, or put RPMs from many different sources in the same
repository, you will find yourself in a lot of troubles with the new
SPMA.

These are some recommendations to avoid such a situation.

## Repository layout

Each upstream repository you choose to follow must become a separate
repository in your site.  Combining repositories is a very bad idea.

You will also need a set of repositories for your home-grown software.

At UGent we do it like this, for SL6:

* Base
* Updates
* Fastbugs
* EPEL
* RPMForge
* atrpms
* jpackage
* quattor
* Private from vendor 1
* Private from vendor 2
* Home-grown
* Quattor

That's a fair number of repositories.  And we are considering whether
to split the home-grown repository.
