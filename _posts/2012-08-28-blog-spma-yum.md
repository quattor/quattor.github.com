---
layout: article
title: SPMA with Yum as backend
category: blog
---

SPMA is the package manager in Quattor. Essentially, it is a framework
that can use any package manager as its backend. However, the only
real backend is based on direct invocations of the RPM library, and it
cannot cope with the needs of a large site. As a result, package
handling in Quattor is time consuming, and the largest source of
problems for users.

So, this is a proposal for replacing the RPM backend with a Yum one.

## Migration phase

In the first stage, repository and package resolutions in Pan will
work just the same.

### Package descriptions in Pan

In the first stage, descriptions of packages shall be identical. That
is, they all must specify the version and the architecture.

In the future we *may* relax these requirements, and only enforce the
name.

### Repository descriptions in Pan

In the first phase, *all* packages must be listed in some repository
template.  This will allow the administrators to guarantee that all
desired packages exist.

The current `/software/repositories` will become a list of Yum
repositories to use.  The SPMA-Yum backend will use it to populate
`/etc/yum.repos.d`.  At this stage, all repositories will be enabled,
and no GPG key enforcing will be done.

### Dry-runs

When run with `--noaction`, Yum will just solve the transaction, but
*not* execute it.

### Caveats

In this first stage, SPMA will *not* be able to revert all packages to
a previous state.  The second iteration will be able to use the
`history` command.

## Future developments

The following developments will follow shortly after:

### History tracking and reverting

On systems where Yum's `history` command is available, it will be
possible to revert to a previous state.  This will require to
associate a Yum transaction ID with a Quattor tag.

*Warning*: If you actively clean up your repositories, you won't be
able to reproduce some points in your distant history.

### Simplification of package specifications

The versions and architectures of all packages will become
optional. If present, Yum will enforce them. If none is present, Yum
will assume _the latest version that satisfies all dependencies_.

### Repository descriptions

Repository descriptions will become closer to Yum's. We will allow to
define GPG keys, choose whether they should be enforced, which
repositories will be disabled...

### Backwards-incompatible changes

None is foreseen. Some fields may change names in the distant future.
