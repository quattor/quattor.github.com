---
layout: article
title: Experiences with package cleanup
author: Luis Fernando Muñoz Mejías
category: blog
---

At UGent we are starting to prune down our systems.  This is bringing
significant advantages in the speed and reliability of our
operations.  Let's see where our bottlenecks were, and how we are
getting rid of them.

## First bottleneck: dependency handling

This is the main reason behind re-implementing our package manager.

The old package manager in Quattor was very rigid.  We had to specify
every package in our system.  With its exact version(s) and
architecture(s).  And we couldn't really know what would be missing or
conflicting until we deployed our systems.

This forced each new service and most upgrades to go through
time-consuming trial and error cycles: list the expected packages,
deploy, read the error messages, fix those messages, iterate.

### Fix: Yum

With the proper configuration, Yum will handle dependencies in the way
we want them.

It also allows to lock the versions of some packages, when needed.
This way we gain the best of both worlds: the ability to control the
changes that are important to us, and flexibility and speed for
those packages that we trust to the upstream distribution.

## Second bottleneck: package bloat

Since we were forced to provide all packages at compilation time, and
we couldn't know about dependencies back then, we resorted to
pre-defined package lists.

These package lists were very generic, and were used as a base for
most services we could ever need.  This meant they had to provide
dependencies for virtually anything.  And the way to do that is to
install everything under the sun.

For instance, a compute node would probably get a full KDE
installation, and Firefox.

### Fix: per-service package lists.

Our approach is to associate a small package list to each service (or
feature, in Aquilon terms).  It contains the packages that provide
that service.  For an nginx web server, that would be `nginx`.  And
that's it.  Whenever possible we don't specify any versions or
architectures.  We let Yum discover what packages are needed to
satisfy such installation.

In addition to that, there are some packages that are needed
everywhere.  All machines will probably require `grep` and `cat` and a
few more things.  We have a template with the packages we deem basic
and all our systems include it.

In an ordinary computation node we have reduced the amount of packages
from 1272 to X.  Only 174 are actually listed in the profile, and Yum
has derived the rest.

## Third bottleneck: complicated workflows

Adding a new RPM to the infrastructure would require:

1. Put the RPM in the corresponding package repository.
1. Regenerate the repository templates.  Usually `ant
   update.rep.templates` or `swrep-soap-template`.
1. Add the RPM to some template(s).  Sometimes we would do this only
   to bump the version.
1. Re-compile.
1. Deploy.

That's a lot.  Especially if the new RPM is just a version bump.

### Fix: Yum

The new workflow is simpler:

1. Put the RPM in the corresponding package repository.
1. Run `createrepo --update` on that repository.

If the new RPM is just an update for some existing package, we are
done!  Just ensure that Yum runs where it is relevant.

We only perform steps 4-6 when we need to add a really new package.
Not for version bumps anymore.

Even better, we can remove the "contents" part of our repository
templates.  Suddenly, our repository templates have turned into small
and understandable files.

## Fourth bottle neck: compilation times

At the end of every compilation, there was a phase that assigned each
package to a repository.  For most profiles, this was the largest hot
spot in compilation time.

For users of the QWG template there was another hot spot right before
that: the application of errata updates.  Before resolving the
repositories, a template would be included listing the "desired"
versions for every package.  This template had tens of thousands of
calls to `pkg_ronly`, most of them doing nothing.  This was another
huge hot spot.

Finally, there were many redundant calls to `pkg_repl` and `pkg_del`.

### Fix: removing the the hot spots

Thanks to Yum, we can simply delete the two large hotspots.  Delete
the errata and repository_cleanup templates and any `include`
statements that referenced them.

Addressing the package bloat as explained above gives us yet another
big speedup.

## Conclusion

Our workflows at UGent are becoming even simpler.  We have gone from
installing 1500 packages in a batch server to just above 700, with
only 200 specified in the profile.  And our compilation times are
halved.

Of course, this comes at a cost.  Once you have committed to the new
package manager, you **must clean up your package lists** very
quickly.
