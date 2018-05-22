---
layout: article
title: Aquilon Technical Details
author: Michel Jouvin
menu: Technical Details
---

{% include link_definitions.md %}

This page provides details on some Aquilon important concepts but is not a description on how to use
Aquilon to manage a site. For this, see the dedicated pages on
[Initializing an Aquilon site][aquilon_configuration] and on
[Management Workflow and Advanced Topics][aquilon_management].

## Aquilon and Pan Templates

Aquilon relies on a (relational) database to describe the hardware and software configurion of site hosts but
the information used to actually configure a host, called a `host profile` (or `profile`), is based on
the [Pan language][pan language]. A host configuration description in Pan language is made of
building blocks called `pan templates`. Some of the pan templates reflect the database object description
when others are used to configure a `feature` and have to be written by humans.

### Plenary Templates

The Aquilon broker takes care of converting the dabatase object descriptions into pan templates, updating them
when the corresponding objects are added. These templates are generated and **must not be edited**. For this
reason, they are stored in a specific area called the `plenary templates`. When using the standard Aquilon
directory layout, the plenary templates are stored under `/var/quattor/cfg/plenary`. The plenary templates
directory contains a subdirectory for each type of object in the Aquilon database (machine, network, ...).

A specific set of templates is also stored in the plenary templates: [the template library][tl_intro].
The template library is a set of generic templates that help to build host descriptions. They are
produced and maintained by the Quattor community, avoiding that every site has to reinvent the wheel.
As they are not intended to be modified directly, they are also stored in the plenary templates, despite
they are not maintained by the broker. See the page on [Initial Site Configuration][aquilon_tl] for details
on how to manged the template library in Aquilon.

### Template King Git Repository

In addition to the features provided by the template library, every site has to develop some site-specific
templates. It is important that the version history of these templates is kept: for this reason, theay are
stored in a Git repository. Their development generally occurs in the context of sandboxes but a reference
version of the site-specific templates is stored in a specific Git repository called the `template king`.
With the standard Aquilon directory layout, it is stored in `/var/quattor/template-king`.

This repository contains one branch for each [domain][aquilon_domains] and each [sandbox][aquilon_sandboxes].
The branches are created and deleted
by the broker whan a domain or sandbox is created or deleted with the relevant `aq` commands.

The template king repository is the Git origin of every other Git repository created by the broker.

## Domains and Sandboxes

Domains and sandboxes are the Aquilon objects that allow to group hosts according to various
needs and to implement a staged development and deployment cycle.

Every host in Aquilon has to belong to either a domain or a sandbox. Hosts are moved between
domains and sandboxes with the `aq manage` command.



### Domains

Domains are used to implement a staged deployment of hosts. They allow to test changes on
some hosts associated with the domain before deploying them into production on all hosts affected
by the configuration change. They reflect the different stages implemented in the deployment workflow
(`dev`, `prod`...). Changes made and tested in one domain can be deployed in another domain using
the `aq deploy` command.

Domains are not connected to a specific Aquilon user and are visible to each one.

Each domain is a separate Git repository under `/var/quattor/domains` (when using the standard
directory layout). This repository is a template king clone, created by the broker, whose current branch
is mirroring the domain branch in the template king.

### Sandboxes

Sandboxes are similar to domains but they are connected with one specific Aquilon user. This is where
the site template development normally occurs. Hosts in a sandbox can be compiled as any other hosts.
One the changes made by a user in the context of a sandbox are ready to go through the review process,
they can be published with `aq publish`: at this point the changes becomes visible to other users. When
they are ready to go through the staged deployment, they can be moved to the first development stage
with `aq deploy`.

Each sandbox is a separate Git repository under `/var/quattor/templates/user` (when using the standard
directory layout), with `user` the Aquilon user the sandbox belongs to. As for domains, this repository
is a template king clone, created by the broker, whose current branch
is mirroring the sandbox branch in the template king.


## Archetypes

Archetypes is the highest level of host grouping in Aquilon. They typically allow to group all hosts
sharing the same base environment, in particular the operating system.

Personalities used to define the host configuration are bound to an archetype. As a consequence, there is
no easy way to share personality definitions between archetypes.


## Clusters

Clusters are mostly useful for defining HA services (perhaps with floating IPs) that exist on a set of hosts,
rather than on individual hosts. They get their own profiles in addition to the hosts.