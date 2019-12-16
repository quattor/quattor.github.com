---
layout: article
title: Site Management Workflow and Operations
author: Michel Jouvin
menu: Using Aquilon
---

{% include link_definitions.md %}

## Managing Users

At installation time, Aquilon is initialised with the Kerberos principal `aquilon` declared as the
Aquilon administrator, meaning that it can use all the Aquilon commands. Normally, at a real site, you
will have several users interacting with Aquilon and you want all of them to interact with its own
Kerberos principal. This is done by adding new Aquilon users and defining their roles.

### Define user role

To have a user account created automatically, have the user connect to the broker and run a read-only command, 
e.g. `aq status`. Once their Kerberos principal appears in the output of `aq show_principal`, 
they can be assigned a more specific role with `aq permission`. An unknown principal can also 
be created by passing `--createuser` to the `aq permission` command.

When a user first connect to Aquilon, its role is set to `nobody`. As a result, it is restricted to 
a few Aquilon commands, typically those who allow to display existing objects in the database. To administer
objects, a user must have a role that allows to do it. It is possible to define as many role as needed and
to specify explicitly what are the allowed commands for the role. The role `aqdadmin` is created at
installation time and allows to use any Aquilon command.

## Using Sandboxes

A sandbox is Git repository and a working directories that are associated with the Aquilon user who create it.
This where the pan template development occurs.

As the Aquilon users typically  don't have access to the machine where the Aquilon broker runs, the sandbox area
on the broker is generally put on a distributed file system, like NFS (see the 
[installation guide][aquilon_install] for more details). The sandbox area
must be writable by any machine used by Aquilon users.

To allow the user to access its sandbox
files, it is necessary to provide the broker with a script that will define the appropriate owner, based
on the UID defined for the user in the Aquilon database. See installation 
[documentation][aquilon_nfs_sandboxes] for more details.

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

### Define Aquilon user UID

*This section is only required if you are using using NFS for sandbox development but
user accounts are not defined on the broker.*

The broker needs to set the sandbox owner to user creating it. As the broker cannot retrieve
the user UID from the user account when it is not defined on the broker host, it uses the user
information defined in the Aquilon database to retrieve the UID to use.

To list existing users, use:

```bash
aq show_user --all
```

The Aquilon user defines the Linux UID, GID and home
directory associated with the Aquilon user but in standard installation, only the UID is actually
used. The Aquilon user name **must match** the Kerberos principal name used by the user to interact
with the broker (typically its Linux userid) and the UID **must match** the actual UID of the user account.

If there is no entry yet for the user, one must be created with `aq add_user`. If the existing
entry doesn't have the right UID, use command `aq update_user` instead.

For example, to create an account for user `johndoe`, use the following commands:

```bash
# Retrieve the Linux `uid` and `gid` for this account
id johndoe
# Create the Aquilon account
aq add_user --user johndoe --uid uid_retrieved --gid gid_retrieved --home aquilon_account_dir
```

### Sandbox creation

The command below will create the sandbox object and the Git repository associated in
`/var/quattor/templates/user/sandbox_name` with `user` the Aquilon user matching the Kerberos principal
used and `sandbox_name` the name of the sandbox create. The sandbox is a Git repository
created as a clone of the `template-king` repository (`template-king` is the Git remote
`origin` for the sandbox repository). The Aquilon user (in fact the UID associated with him) 
executing the command will own the sandbox working directory.

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


## Accessing Plenary Templates

Plenary templates are all the templates generated and owned by the broker. They cannot be edited: their
content is  modified by the Aquilon commands used to update the host configuration. For this reason, they
cannot be accessed directly, for example in the sandbox. The content of these templates can be displayed
with the `aq cat` command. Command options can be used to select the template to display: use `aq cat --help`
to get the list of all the possible options. The main ones are:

* `--hostname xxx.dom.ain`: object template for host `xxx.dom.ain`
* `--hostname xxx.dom.ain --data`: host data template (archetype, hardware configuration, network configuration)
for host `xxx.dom.ain`
* `--machine xxx`: machine template for machine `xxx`
* `--cluster xxx`: object template for cluster `xxx`
* `--cluster xxx --data`: template describing members and location of cluster `xxx`
* `--cluster xxx --client`: cluster configuration included in hosts who are members of cluster `xxx`
* `--personality xxx --archetype yyy [--personality_stage stage]`: template describing personality `xxx`
of archetype `yyy` (`--archetype` can be omitted if personality `xxx` exists only in one archetype).
If `--personality_stage` is omitted, it defaults to `current`: specify it if you want to see the template
for other stages (`previous` or `next`)
* `--service xxx`: template describing the configuration common to all instances of service `xxx`
* `--service xxx --instance yyy`: template describing instance `yyy` configuration of service `xxx`
* `--service xxx --server`: template describing the common configuration all servers for service `xxx`
* `--service xxx --server --instance yyy`: template describing the server configuration of instance `yyy`
for service `xxx`

*Note: the template library is also installed in the plenary template area and is not visible outside the
broker. Currently, the `aq cat` command doesn't allow to display the template library contents. If you need
to check the content of a template in the template library, refer to the
appropriate GitHub repository or download a private copy of the template library (outside of any sandbox) using
the [standard procedure][aquilon_tl].*

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

*Note: it is possible to bind a feature to an archetype if you want all the personalities in the archetype
to have this feature. To do this, just remove `--personality`.*


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


## Host and Machine Parameters

### Changing the IP address of a host

Once a host has been created, it is possible to update its IP address but the command to use depends on whether it is
the primary network address or not.


### Primary network address:

```bash
aq update_machine --machine HOST_MACHINE --ip NEW_IP_ADDRESS
```

or:
```bash
aq update_machine --hostname HOST_NAME --ip NEW_IP_ADDRESS
```

where:
* `HOST_MACHINE` is the name of the machine the host is bound to.
* `HOST_NAME` is the primary FQDN of the host.
* `NEW_IP_ADDRESS` is the desired IP address of the host.


### Any another (non-primary) network address:

```bash
aq del_interface_address --machine HOST_MACHINE --interface INT_NAME --ip OLD_IP_ADDRESS
aq add_interface_address --machine HOST_MACHINE --interface INT_NAME --ip NEW_IP_ADDRESS
```

where:
* `HOST_MACHINE` is the name of the machine the host is bound to.
* `INT_NAME` is the interface name (e.g. `eth0`).
* `OLD_IP_ADDRESS` is the IP address to remove.
* `NEW_IP_ADDRESS` is the desired IP address of the host.

## Services

An Aquilon [service][aquilon_details] allows to define different endpoints for a given service based
on the host location information (country, city, room, rack...) or the host network subnet. A host
can be bound to the service and the appropriate instance will be selected by the Aquilon broker and passed
to the host configuration in `/system/services/servicename` where 
`servicename` is the name of the service. The 2 main configuration properties accessible are:

* `servers`: the endpoint FQDNs of the appropriate service instance, as a Pan list of string
* `server_ips`: the endpoint IP addresses of the appropriate service instance, as a Pan list of string

### Defining a service

Defining a service typically involves creating a service instance and mapping it to specific
hosts, personalities or archetypes. When mapped to a personality or archetype, the service will be
used for all nodes in this personality or archetype for which there is no explicit mapping.

To create the service `dns` (to define the DNS server to use), 
use the following command:

```bash
aq add service --service dns
```

Then create a service instance (the instance can have a different setting for --need_client_list`),
defining its associated endpoint. The associated endpoint must be a host entry in the Aquilon
database. If the endpoint is not managed by Aquilon, define it in a non-compilable archetype:

```bash
aq add service --service dns --instance metropolis1
aq bind server --service dns --instance metropolis1  --hostname ns.deilyplanet.com
```

### Assigning hosts to a service instance

Once a service has been defined, it is necessary to define which hosts are
configured to use it. This is done by marking the service as required for 
a given archetype or personality with the command `aq add_required_service` which
means that all the hosts with this archetype of personality will have the service
configured, using the appropriate instance for the host.
For example, to define the `dns` service as required for the archetype `web_servers`, use:

```bash
aq add required service --service dns --archetype web_servers
```

Hosts are assigned to service instance using service maps.
A service map define the criteria to use to select an instance. They are typically
based on the geographical locations but it also possible to use network subnets. When
using the location information, it is possible to define different instances for different
parts of the location hierarchy. For example, it is possible to define an instance that will
be used for a city with the exception of one building that will have its own service mapping.
This is done with the command `aq map_service`. For example:

```bash
aq map service --service dns --instance metropolis1  --city metropolis
# Instance metropolis2 needs to be defined before
aq map service --service dns --instance metropolis2  --building hq
```

You need to run the command `aq reconfigure` for a host for the service configuration
changes to be actually taken into account in host profile. Note that
this command will fail if there is
no service instance that can serve a host for which the service is required, i.e. 
if the service mapping has not
been properly defined to handle the location or network of the host.

After running `aq reconfigure` for some hosts assigned to the service, `aq show service`
should show a non-zero number for the service `Client Count`.

### Checking if a host has been assigned to a service

To check if a node has been assigned to a service and to know which instance will be used,
use the command `aq show service --client clientname` where `clientname` is the host name to check.

### Unbinding a client from a service

To unbind a client from a service instance, it is necessary to 
remove the service requirement matching the host with the command
`aq del required service`.

The mapping is actually removed at the next `aq reconfigure` for the host after modifying
the service requirements.

## Using Aquilon clusters

[Clusters][aquilon_details] are intended to represent in Aquilon a group of hosts that must be configured in
the same way. It may be hypervisors in a cloud, disk servers in a distributed storage infrastructure like Hadoop
or Ceph, or hosts behind proxy. 

Clusters, like hosts, have an archetype and personality attached. It allows for cluster-wide configuration
to be applied after most of the host configuration is done, just before including the host archetype `final.pan`
(the last thing done in any plenary object template). Thus the cluster personality is added to the host
personality. Depending on the cluster type, the host personality of a clustered host may be as minimal
as providing the basic OS configuration (typically the case for hypervisors in a cloud)or also 
configure some features specific to the host (e.g. the hosts
behind a proxy may not all run the same services).

Configuring a cluster involves:
* Creating the cluster archetype and personality
* Creating the cluster
* Adding hosts (hypervisors) to the cluster
* Building the cluster and its hosts
* Optionally, using the cluster as the "machine location" for virtual machines

### Creating the cluster archetype and personality

A cluster archetype is created the same way as as [host archetype](#adding-archetypes),
with the exception that `--cluster_type compute` option must be added.. Depending if the
archetype is defined as compilable or not, a profile will be created for the cluster (or not).
 
A typical example would be:

```bash
aq add_archetype --archetype cluster_test --cluster_type compute
```

Option `--compilable` must be added to define the archetype as compilable and get a cluster profile
object created. If you want the archetype to be compilable, you must create the same templates for
the cluster archetype as for a 
[host archetype](/aquilon/configuration.html#creating-the-archetypebase-and-archetypefinal-templates), as well
as a [archetype/declaration.pan](/aquilon/configuration.html#enabling-the-template-library)
if it is enabled for host archetypes. `declaration.pan` must be similar to the one used in a host archetype
if you are using the template library. The exact content of `base.pan` and `final.pan`depend on what is required
by the personality and features bound to the archetype: you should in particular make available all the information
normally accessible to the features in the context of a host archetype.

Personality is created and managed the same way as for a [host personality](#personalities)). The same personality
(and archetype) can be used with several clusters.

Like for host archetypes, it is possible to [bind](#binding-features-to-personalities) a feature to a cluster
archetype instead of the cluster personality. 

### Creating the cluster

A cluster is created with `aq add_cluster`. For example, to create a cluster `cluster_test` that will
use the personality `os_hv_test` from archetype `mycloud`, use the following command:

```bash
aq add cluster --cluster cluster_test --archetype mycloud --personality os_hv_test 
               --down_hosts 0 --building hq --sandbox your/sandbox
```

In the previous command, `--down_hosts` is set to 0 as Aquilon doesn't make a direct use of this value
(an external monitoring tool would be required). For `--building` and `--sandbox`, use values appropriate
to your site (sandbox name must be in the form `user/sandbox_name`). 

### Adding hosts to the cluster

After creating the cluster, it is necessary to add or more hosts as the cluster members (e.g. hypervisors in a 
cluster representing a cloud). The host must have been created with the [standard procedure](/aquilon/configuration.html#declaring-hosts)
before adding it to the cluster. This is done with the command `aq cluster`.

For example, to add a node `hv1.example.com` in the cluster `cluster_test`:

```bash
aq cluster --cluster cluster_test --hostname hv1.example.com
```

Note that if the host was previously part of another cluster, it will be removed from the original cluster.


### Building the cluster and its hosts

The command `aq reconfigure --membersof` allows to rebuild the host profile for each
member of the cluster.

For example, to rebuild the cluster `cluster_test` and its hosts, use:

```bash
aq reconfigure --membersof cluster_test
```

This command must be used after every change affecting the cluster configuration (in particular the cluster
personality) to ensure that all the configuration (profile) of each cluster member is updated.

In addition, there is a specific profile built for cluster itself if the archetype is compilable. To
build or rebuild this cluster profile, use the command:

```bash
aq make cluster --cluster cluster_test
```


### Binding virtual machines to the cluster

If the cluster is describing a virtualisation infrastructure like a cluster, hosts that are not part of the cluster
may be associated with it through the (virtual) machine they use.  When creating the machine, use the
option `--cluster` instead of `--rack`, `--desk` or `--chassis`. One the machine is configured,
[add the hosts][aquilon_hosts] to Aquilon using the same procedure as for hosts using bare metal machines. 

It is not possible to update a machine that was initially configured to use a bare metal machine to become
a virtual machine. But it is possible to change the cluster hosting a machine (or change a virtual machine hosted
by a host to a VM hosted by a cluster) with `aq update_machine` command with the `--cluster` option.

To be able to bind a virtual machine to a cluster, it is necessary that the virtual machine has no local disk.
Use `virtual_disk` as the disk type when creating the machine model that will be used by the virtual machine.

## Initial Installation

Initial installation of a node in Quattor is managed by the AII component that generally runs on
a dedicated node. A site can use multiple AII servers, typically one per network subnet.

In Aquilon, the AII server that is used for a given host is defined by the Aquilon 
[service][aquilon_details] `bootserver` service. To define it, follow the instructions 
above to create the service and configure it. In particular declare one or more instances of 
the service and map them to hosts, for example based on their locations.

Once the service is configured, the AII configuration for a host is generated by 
command when command `aq pxeswitch` is run. Use this command with the option `--install` to
get the host installed at next boot and `--status` to inquire what will happen for the host
at next boot (`--localboot` reset `--install`, defining that next boot must be done from local disk).

{% comment %}
FIXME: to be removed once fixes are merged.
{% endcomment %}
*Note: it is possible to share the deployment (AII) server between SCDB (Quattor legacy configuration database)
and Aquilon (or between several Aquilon brokers) but with Aquilon 1.12.62 and Quattor 18.6.0, it requires
2 fixes: https://github.com/quattor/aquilon/pull/114 and https://github.com/quattor/aii/pull/291.*


## Implementing Modifications in the Template Library

The [template library][tl_intro] provides the base templates for configuring the host operating system and
some features, in particular for OpenStack cloud and for UMD grid middleware. It has been designed to
highly configurable without any modification, using variables. The templates are developed by the
Quattor community. They help to lower the management effort required at each site.

The template library is not intended to be modified directly by a site. This is the reason it is
part of the plenary templates that are not visible to Aquilon users and that they are not versioned.
See the [dedicated section][aquilon_tl] for more information on how to integrate the template
library into Aquilon.

It may happen that some of the templates need to be enhanced or that a site develops a new feature 
that may be useful to other sites. In this case, it is recommended to create at the top level of
the site templates a `template-library` directory. In this directory, create a sub-directory whose
name is the template library version the modification apply to. This is the same directory structure
as the one used in the plenary templates.

Then for each template that you need to modify or add, place it in the same directory as it would be
in the template library: the site version will be used instead of the standard one, without any modification
to the other templates.

When a new version of the template library is released, it is easy to compare the new templates with
the local modifications to decide what still needs to be ported to the new version, using the same approach
(a directory corresponding to the new version).

It is important to submit your modification upstream, using GitHub pull requests against the relevant
repositories. Avoid submitting one big pull request with all your changes: prefer submitting one
pull request per change set.

## Implementing Peer-Review and Quality Assessment with Aquilon

Implementing a stage deployment workflow, Aquilon makes easy to validate changes through peer-review and
a quality assessment process.

Peer-review is generally implemented when the changes are published from a sandbox.
Since the template-king repository is a standard Git repository, you can set up a simple system just
by adding an post-receive hook that sends an email to the peer-review team.

Quality assessment can be implemented in various ways. One common practice is to have a domain with a set of
hosts representing the various services managed in Aquilon where changes are deployed after the initial validation
(e.g. in domain `dev`) and before being moved to the production domain
