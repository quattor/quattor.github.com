---
layout: article
title: Site Management Workflow and Operations
author: Michel Jouvin
menu: Using Aquilon
---

{% include link_definitions.md %}

## Using Sandboxes

Sandboxes are Git repositories that are associated with an Aquilon user where the pan template
development occurs.

### Define the Kerberos realm as trusted

To be able to add a sandbox, the Kerberos realm used to authenticate Aquilon users must
be trusted. This is not the default when a realm is added. To declare a realm as trusted,
use `aq update_realm` command.

The realm used is based on the Kerberos configuration that was done during Aquilon
[installation][aquilon_install]. Use `klist` command to get it, if you don't know it.

Assuming that your real is called `dailyplanet.com` (it often matches your DNS domain), the command
to use is:

```bash
aq update_realm --realm dailyplanet.com --trusted
```

### Add an Aquilon user

A sandbox is associated with an Aquilon user. The Aquilon user is associated with an existing Linux account
via the `uid` and `gid` but doesn't have to be Aquilon user name doesn't have to match the Linux user ID.
It must be created with the `aq add_user` command if the user doesn't exist already. To list existing
users, use:

```bash
aq show_user --all
```

If you are using the `aquilon` Linux user as suggested, use the following commands:

```bash
# Retrieve the Linux `uid` and `gid` for this account
id aquilon
# Create the Aquilon account
aq add_user --user aquilon --uid uid_retrieved --gid gid_retrieved --home aquilon_account_dir
```

### Sandbox creation

The following command will create the sandbox object and the Git repository associated in
`/var/quattor/templates/user/sandbox_name` with `user` the Aquilon user matching the Kerberos principal
used and `sandbox_name` the name of the sandbox create. The sandbox is a Git repository
created as a clone of the `template-king` repository (`template-king` is the Git remote
`origin` for the sandbox repository):

```bash
aq add_sandbox --sandbox site-init
```

Once the sandbox is created, it is necessary to associate the host we want to manage with the
sandbox. In all the Aquilon commands requiring a `--sandbox` option (except the `xxx_sandbox` commands),
the sandbox name is `user/sandbox`.

```bash
# The following command assumes that the Aquilon user has the same name as the current Linux user
aq manage --sandbox $USER/site-init --hostname 'testsrv.dailyplanet.com'
```

*Note: if you want to remove the host from the sandbox, you need to use the same command with the option
`--domain` instead of `--sandbox` to move it back to a domain. You can also move it to another sandbox.*

You are now ready to produce some useful pan code to define the configuration of the
host `testsrv.dailyplanet.com`.


## Why to Use Domains

[Domains][aquilon_domains] are used to implement a stage development workflow where changes are tested
first on a limited number of hosts, for example a `dev` domain, before going to production in a `prod`
domain that contains all the site hosts, except those used for testing in the `dev` domain. You can
implement as many stages as you want, for example a `q/a` or `preprod` domain, between `dev` and `prod`.

When validated in one domain, changes can be deployed into the domain representing the next stage with
`aq deploy`.

Hosts can also be moved from one domain to another one with `aq manage`.

## Adding Archetypes

### Compilable archetypes

Compilable archetypes are used for hosts managed directly by Aquilon. They are the most common
archetypes.

### Non-compilable archetypes

Non-compilable archetypes are used to store the inventory for your hardware not managed by
Aquilon. For example, you could create an archetype for all your IPMI hardware.

```bash
aq add_archetype --archetype 'ipmi' --nocompilable
```

## Adding New Hardware Models

Arbitrary hardware components (disks, NIC, machine...) can be used to describe machines in the
Aquilon database. But to be usable in host profiles, they have to be backed by Pan templates.
This section requires what you need to do if you want to use
hardware components with no template already existing in the [template library][tl_intro]. Once
you have validated the new hardware templates, it is a good practice to request their addition to
the template library so that other Aquilon sites can benefit from them.

## Defining New Features

### Adding a feature

We can now create a feature: this involves creating the feature object in the Aquilon database with the
`aq` command and adding a pan template defining the feature. When creating a feature, it is necessary
to define what action triggers its activation and deactivation. See `aq help add feature` for possible
values.

```bash
aq add_feature --feature demo --type host --activation dispatch --deactivation reboot --grn test
```

Once the feature has been added, it is necessary to create a template `config.pan` that will define what the
feature actually does. This template will first be added to the sandbox, `/var/quattor/templates/user/aquilon`,
to test it. This template must reside at the path `archetype/features/feature_name` in the sandbox,
with `archetype` the archetype the feature will belong to
(in our example `linux`) and `feature_name` equal to the feature name (her `demo`).
At this stage create a file with the following content:

```
unique template features/demo/config;
```

Once the template been created, it is necessary to commit it and push
to the `template-king` Git repository which is defined as the origin of the template master repository for the
domain, `test` here:

```bash
cd /var/quattor/domains/test
git add .
git commit -m 'Add features demon and rootpasswd'
git push
```

### Binding features to personalities

A feature can be bound to one or more personalities. It means that all using these
personalities will have the feature configured. The command to do it is
`aq bind_feature`. For example to bind the feature `demo` created previously to the personality `test`,
the command would be:

```bash
aq bind_feature --feature demo --personality test --archetype web_servers
```

*Note: despite the command help mentions that features can also be bound to archetypes, it is
highly recommended not to do it.*


## Personalities

Personalities are used to define the list of features that are configured on a host. Every host has one
personality and only one but it is possible to change the personality of a host. Personalities are attached
to one archetype (an archetype can be viewed as a group of possible personalities).

Personality configuration is *staged*. That means that when a personality is updated, the change is not
visible to the hosts using it until it is promoted as the `current` version with the `aq promote` command.
When a personality is created and when it is updated, its stage is defined to `next` (configuration that
will be applied to the personality when the new configuration is promoted as the production (`current`) one. 
After `aq promote` the previously current personality configuration becomes `previous`.

Unlike features, personalities are entirely defined in the Aquilon database (there
is no additional site template to create).

### Defining the new personality configuration as current

Based on the feature example above, to use the updated personality configuration for the hosts having this personality,
use the following command:

```bash
aq promote --personality test --archetype web_servers
```

### Changing the host personality

To change the personality of an existing host, use `aq reconfigure`:

```bash
aq reconfigure --hostname your_host --personality new_personality [--archetype new_archetype]
```

`--archetype` is necessary only if the new personality is not attached to the same archetype.

## Networks

### How to define the routers for my networks?

When we declare our networks, Aquilon will assume a fixed IP
(typically the first IP in the range) is the gateway in it.  If this
isn't correct, you have to modify the configuration for the broker.
Create a `network_unknown` section, and declare the default gateway offset.

```ini
[network_unknown]
default_gateway_offset=30
reserved_offsets=1,30,25
first_usable_offset=40
```

And finally we restart the broker:

```bash
systemctl restart aquilon-broker
```

If some of your networks don't adhere to this convention, you'll need
to declare their routers in Aquilon.  For instance, let's suppose that
the gateway in `reporters` network has offset 3:

```bash
aq add_router --ip '192.168.100.3' --fqdn 'router.reporters.metropolis.com'
```

If your network is an internal one (the default), some restrictions
apply:

* Routers must be part of the `reserved_offsets` list.
* Router offsets must be below the `first_usable_offset`, which the
  broker uses when assigning IP addresses automatically.

If you need an external network, you have to create it with
`--network_environment external` in its command line.


## Implementing Peer-Review and Quality Assessment with Aquilon

Implementing a stage deployment workflow, Aquilon makes easy to validate changes through peer-review and
a quality assessment process.

Peer-review is generally implemented when the changes are published from a sandbox.
Since the template-king repository is a standard Git repository, you can set up a simple system just
by adding an post-receive hook that sends an email to the peer-review team.

Quality assessment can be implemented in various ways. One common practice is to have a domain with a set of
hosts representing the various services managed in Aquilon where changes are deployed after the initial validation
(e.g. in domain `dev`) and before being moved to the production domain
