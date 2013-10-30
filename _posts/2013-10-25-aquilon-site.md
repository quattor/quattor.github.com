---
layout: article
title: Starting a site with Aquilon
category: documentation
modified: 2013-10-25
author: Luis Fernando Muñoz Mejías
---

**THIS IS WORK IN PROGRESS**

## Introduction

After
[installing Aquilon](/documentation/2012/10/31/install-aquilon.html), we
want to add hosts to our instance, and produce some useful
configuration.

We'll explain in this document the steps to set up the clusters
for the Daily Planet, Superman's employer.

### Aquilon terminology

These are the basic terms in Aquilon operations:

* `archetype`: The highest possible grouping of hosts into distinctly
    seperate types, analogous to a QWG site. Archetypes are a bundle
    that expresses how to build something. It defines what set of
    templates to use (for example, what operating systems are
    available, etc).  Hosts therefore require an archetype to define
    how they are compiled.
* `broker`: The backend which the aq client communicates with and the
    owner of all object and production templates.  We'll refer to it
    also as `aqd`.
* `cluster`: A group of hosts related in some way, different to an
    archetype in that hosts may or may not be in a cluster. When
    grouping hosts into a cluster, an object profile is also built for
    the cluster, as well as the hosts. Clusters go through a
    completely different schema and build process to how hosts are
    built and therefore have a different archetypes.
* `domain`: A high level grouping of hosts eg. prod
* `feature`: A chunk of code for configuring a specific thing, similar
    to Puppet recipes.
* `personality`: Analogous to QWG machine types, describes the
    services required but not the instance (selected using plenary
    template information).
* `plenary`: Template generated on the fly from an external
    source.
* `sandbox`: A working area owned by a specific user and associated
    with a group of systems.
* `service`:   ...

### Before proceeding

We'll interact with the broker using the `aq` command, which has lots
of sub-commands.  Each sub-command has a detailed help, and man pages
can be found in the appendix of the [Aquilon book](http://FIXME).

In this stage we will be adding a site, so we will use `add_*`
commands.  Most of the commands we'll use have `show_`, `update_` and
`del_` counterparts.

## Storing your inventory

The Aquilon database contains the entire inventory of your
infrastructure.  You may use it as your asset management database, or
feed it from your existing one.  You will have to store all your
hardware, its characteristics and locations, which may be an annoying
process.

### Geographical locations

Before starting, you have to add the geographical locations of your
infrastructure.  The meanings of the commands to run should be
obvious.  We list here an example:

```bash
aq add_organization --organization daily_planet
aq add_hub --hub pacific --organization daily_planet
aq add_continent --continent america --hub pacific
aq add_country --country us --continent
aq add_city --city metropolis --fullname Metropolis --country us --timezone dct
aq add_building --building hq --city metropolis --address '355, 1000 Broadway'
aq add_room --room supersecret --building hq
```

List your own addresses, rooms...  but remember that each step depends
on the previous ones.  If you want to add European countries, you have
to insert Europe as a continent first!

### Your hardware inventory

Next comes your hardware.  At the very least, your racks, chassis and
servers will be stored here.  It is a good place to store other
hardware such as switches.

For racks, you'll have to specify on which row and column inside that
row they are.

```sh
aq add_rack --rackid forlexluthor --row R --column C --building hq
```

Next come servers, switches, routers... we'll go for servers,
_machine_s in Aquilon terms.  Aquilon has to know the exact vendor and
model for each server, so here we go:

```sh
aq add_vendor --vendor luthorindustries --comments "Bad guys make good sells"
aq add_model --model spyserver --vendor luthorindustries --type rackmount
aq add_machine --machine illegaltapper --model spyserver --rack forlexluthor
```

### Declaring networks

Once we have the hardware in place, it's time to declare the networks
our hosts live in.



## Declaring your first host

### Personalities and features

## Importing your first templates

## Declaring your first sandbox

## Compiling the first host

## Deploying the first configuration

**TODO**: Document the notifysock in /var/quattor/run/sockets!!

## Conclusion
