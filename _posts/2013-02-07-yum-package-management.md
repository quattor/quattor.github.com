---
layout: article
title: Managing packages at scale with Yum-based SPMA
category: documentation
---

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

## Less important repositories

Some of these repositories will be listed only for debugging
purposes.  This way, we may allow an administrator to run

```
yum  --enablerepo=* install <some-debugging-tool>
```

that will be cleaned up after he's done his operations.

Those will be disabled in the repository template, like this:

    structure template repository/foo;

    ...
    "url" = "http://...";
    "enabled" = false;
    ...

## Blocking a repository except for a few RPMs: the case of RPMforge

A more frequent use case is `RPMforge`.  It has many useful packages
that your distribution does not provide.  But it will also collide
with the distribution for many other packages, and we usually want to
follow the distribution.

In those cases, we want to install *only* an explicit set of packages
from `RPMforge`.  And not even consider it for the rest of our system.

That's where Yum's `includepkgs` comes in handy.  You just give the
list of packages you need from that repository, and for the rest of it
it will be effectively disabled.  In your repository template:

    structure template repository/rpmforge;

    ...
    "url" = "http://...";
    "enabled" = true; # This is the default
    "includepkgs" = list("foo", "bar", "baz");

Wildcards are allowed in the `includepkgs` list.

## Blacklisting packages from a repository

You can use Yum's `exclude` directive for blacklisting packages from a
repository.  In your repository template, that would be the
`excludepkgs` directive.

## Repository priorities

I don't really recommend using priorities.  They will interact in many
surprising ways when you want to use specific versions for some
packages.  Selectively enabling or blacklisting some packages usually
works better.

In any case, should you really want them, just set a `priority` for
your repository template.
