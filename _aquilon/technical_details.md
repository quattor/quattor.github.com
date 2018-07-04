---
layout: article
title: Aquilon Concepts and Technical Details
author: Michel Jouvin
menu: Technical Details
---

{% include link_definitions.md %}

This page provides details on some Aquilon important concepts but is not a description on how to use
Aquilon to manage a site. For this, see the dedicated pages on
[Initialising an Aquilon site][aquilon_configuration] and on
[Management Workflow and Advanced Topics][aquilon_management].

## Aquilon and Pan Templates

Aquilon relies on a (relational) database to describe the hardware and software configuration of site hosts but
the information used to actually configure a host, called a `host profile` (or `profile`), is based on
the [Pan language][pan language]. A host configuration description in Pan language is made of
building blocks called `pan templates`. Some of the pan templates reflect the database object description
when others are used to configure a `feature` and have to be written by humans.

### Plenary Templates

The Aquilon broker takes care of converting the database object descriptions into pan templates, updating them
when the corresponding objects are added. These templates are generated and **must not be edited**. For this
reason, they are stored in a specific area called the `plenary templates`. When using the standard Aquilon
directory layout, the plenary templates are stored under `/var/quattor/cfg/plenary`. The plenary templates
directory contains a sub-directory for each type of object in the Aquilon database (machine, network, ...).

A specific set of templates is also stored in the plenary templates: [the template library][tl_intro].
The template library is a set of generic templates that help to build host descriptions. They are
produced and maintained by the Quattor community, avoiding that every site has to reinvent the wheel.
As they are not intended to be modified directly, they are also stored in the plenary templates, despite
they are not maintained by the broker. See the page on [Initial Site Configuration][aquilon_tl] for details
on how to manged the template library in Aquilon.

### Template King Git Repository

In addition to the features provided by the template library, every site has to develop some site-specific
templates. It is important that the version history of these templates is kept: for this reason, they are
stored in a Git repository. Their development generally occurs in the context of sandboxes but a reference
version of the site-specific templates is stored in a specific Git repository called the `template king`.
With the standard Aquilon directory layout, it is stored in `/var/quattor/template-king`.

This repository contains one branch for each [domain][aquilon_domains] and each [sandbox][aquilon_sandboxes].
The branches are created and deleted
by the broker when a domain or sandbox is created or deleted with the relevant `aq` commands.

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


## Archetypes and Personalities

Archetypes is the highest level of host grouping in Aquilon. They typically allow to group all hosts
sharing the same base environment. It is up to the site to define the granularity of archetypes. It is
possible to bind some features with the archetype rather than with a specific personality, so that all
personalities in the archetype will have these features configured.

Personalities are used to define the list of features that are configured on a host. 
Every host has one personality and only one but it is possible to change the personality of a host. 
Personalities used to define the host configuration are bound to an archetype. As a consequence, there is
no easy way to share personality definitions between archetypes.


## Services

An Aquilon service object defines the end point of a service for a given host, all hosts of a personality
or all hosts of an archetype. It doesn't describe how to configure the service itself but allow to select
the endpoint of a service instance based on the location, the host name, the cluster name... In general the
site configuration templates use this information to configure the service on a given node. The information
related to the service instance is available in the Pan templates under `/system/services/servicename` where 
`servicename` is the name of the service. For example, one could define a `dns` service with different instances
according to the host rack corresponding to the servers to use for hosts in the rack. In the site templates,
it is then possible to use `/system/services/dns/server_ips` to retrieve the name server list for any host.

One specific service is `bootserver`. It is used by the command `aq pxeswitch` to select the host providing
the AII service used for the initial installation of an Aquilon host.


## Clusters

Clusters are collections of hosts that have a similar role/function. They are typically used describe 
a cluster of hypervisors, like those provided by VMware ESX or clouds. Aquilon can provide some monitoring
thresholds associated with the cluster, like the minimum or maximum number of hosts that must be running at
any time. Clusters can also be used to describe a HA cluster. Note that Aquilon is not a replacement for the
cluster middleware: it just allows to represent a group of machines managed by such a middleware.

Once a cluster is defined, it can be used as an alternative to a machine object to describe where is running
a host. In this case, Aquilon doesn't track on which cluster node the host is running: it lets the middleware
do the scheduling, assuming that all hosts in the cluster are equivalent.


## Metaclusters

A metacluster in Aquilon is a group of cluster. They are used to group distinct clusters with a similar configuration
(e.g. for VMware ESX, same vCenter, same storage back-end, same network connections). When a virtual machine is
moved between two different clusters that are part of the same metacluster, Aquilon is able to drive the migration
as only the virtual machine definition has to be migrated.

Currently metaclusters can be used only with VMware ESX clusters.
