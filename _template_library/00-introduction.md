---
layout: article
title: How To Use The Template Library
author: Michel Jouvin
redirect_from: /documentation/2014/06/06/how-to-use-template-library.html
menu: What Is It?
---

[tl_development]: /development/template_library.html
[quattor_rtd_documentation]: http://quattor-documentation.readthedocs.io/en/latest
[get_tl]: /template_library/get_tl.html

This page describes what is the Quattor template library and how to use it.

## What Is The Template Library?

The Quattor template library is a set of generic pan templates that allow to configure a machine
without writing a detailed configuration description.
A site administrator using the template library to configure supported services
has mainly to provide the necessary information specific to the site/machine to customize the behaviour
of the standard templates. Depending on the type of configuration database used, this site is
provided through site-specific pan templates (SCDB) that
contain mainly variable declarations or through a relational database (Aquilon).

One of the key design principle for the template library is that every modification is made with
backward compatibility in mind. A site relying on the
template library should not have to modify anything in its site configuration when upgrading
to a new version of the template library: the resulting
configuration should remain the same, except for bug fixes and necessary configuration
updates. __Every exception to this rule (unfortunately there are
a few...) is always documented and well advertised.__ On the other hand, it is expected
that sites don't modify the template library without
pushing back their changes (see [How to contribute?](#how-to-contribute)). Site customization
must be done through variables documented in [Quattor documentation][quattor_rtd_documentation].
If a configuration option that you require is
missing, you are welcome to open an issue in the appropriate Git repository on GitHub.

*Note: variable documentation is being migrated from the [legacy Quattor Wiki](https://trac.lal.in2p3.fr/Quattor/wiki/Doc):
check on this site if you don't find the information in the [Quattor documentation][quattor_rtd_documentation]).*

The template library is integrated into the Quattor release. That means that:

* It is going through the
standard testing and Q/A workflow used for the whole Quattor release.
* It is easy to get a consistent state of the whole template library, that guarantees
that each component will properly interact with the others.
* The way the template library is organized make pretty easy to implement a staged
deployment strategy if a site wants to go through a strong validation
process of new releases.

Despite being part of the Quattor release, the template library is not distributed as
RPMs. You can find information on how to get it [here][get_md].

## Template Library Layout

The template library is organised in several subsets, each one mapped to a specific
Git repository in GitHub. 4 of these subsets constitute the core
part of the template library, necessary for configuring the base OS on any machine.
The other subsets provide standard templates for configuring
specific services like grid EMI/UMD middleware, StratusLab cloud middleware and are
useful only if you want to configure these services.

Each subset is made of several templates, organized in different directories. Among
these directories, some of them have specific purposes and represent
the public interface to the subset:

* `features`: configure a particular service (one directory per feature),
intended to be included with other features to a base OS configuration to define a specific machine
configuration, generally through set of features defined as `personality`.
* `personality`: a set of features used together to provide a higher-level service
(e.g. nfs-server). Used mainly with SCDB as Aquilon defines
personality in the relational database rather than with pan templates.
* `repository`: templates used to configure the YUM repositories normally associated
with the subet. Present in (almost) each subset.

### Template Library Core

The core part of the template library is made of the 4 following subsets (the name
given matches the directory name under `cfg/`in SCDB):

* `standard` (repository [template-library-standard](https://github.com/quattor/template-library-standard)):
this subset provides templates used to
describe hardware, to determine OS/kernel version/architecture, configure file systems. It also provides
some standard personalities like perfSonar,
Pakiti or standard features like fetch-crl, cvmfs...
* `quattor` (repository [template-library-core](https://github.com/quattor/template-library-core)): this
subset contains one directory per Quattor release. For each version, it provides all the templates to
configure a Quattor client
and all the configuration modules part of the release.
* `os` (repository [template-library-os](https://github.com/quattor/template-library-os)): this subet
contains one directory per OS (major) version.
The main template in this subset is `config/core/base` that does the base OS configuration. In the
`rpms` directory (pan namespace) of each version,
you can find templates defining some useful groups of packages.
* `monitoring` (repository [template-library-monitoring](https://github.com/quattor/template-library-monitoring)):
this subset contains template to
configure various monitoring tools (Nagios, Ganglia, ...). Even though using this part is mostly optional, it is
currently required to have it present
to satisfy one dependency of the `quattor` subset.


### Grid Middleware

Stored under `cfg/grid` in SCDB, this subset contains one directory per EMI/UMD version. The associated Git repo is
[template-library-grid](https://github.com/quattor/template-library-grid)). This subset is entirely optional.

It provides all the templates, particularly `personalities` and `features` required to configure the grid services.


### OpenStack

Stored under `cfg/cloud` in SCDB, this subset contains one directory per OpenStack version. The associated Git repo is
[template-library-openstack](https://github.com/quattor/template-library-openstack)). This subset is entirely optional.

It provides all the templates, particularly `personalities` and `features` required to configure OpenStack services.


### Examples

This subset is SCDB-specific and provides an example of site configuration, stored under `cfg/sites` and `cfg/clusters`.
The associated Git repo for this subset is
[template-library-examples](https://github.com/quattor/template-library-examples)). This subset is entirely optional and is normally
not used in a production SCDB.

In addition to provide site/cluster examples, this subset is used to validate the other subsets during the release process
during the test phase of every pull request.


## How to Contribute?

The objective of the template library is to avoid every site to reinvent the wheel and
to be a framework to share the developments of each site that could benefit others.
For this reason, you are welcome to contribute a bug fix, an improvement or the support
of a new service.

When doing developments for the template library, be sure to follow advices in the template
library [development guide][tl_development]. Once you are ready to share your modifications,
open a pull request against the appropriate repository or
repositories (some modifications may involve several repositories) so that they can
be peer reviewed by other template library developers. As part of the pull request review,
your changes will be tested against the SCDB examples described above: be sure to check
the status of this test on GitHub.

Some template library repositories have no master branch but a branch per OS or middleware
version. This is the case for:

* `os`
* `grid`
* `stratuslab`

When opening a pull request, be sure to do it against the appropriate branch.
