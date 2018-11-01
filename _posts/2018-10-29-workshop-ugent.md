---
layout: article
title: Summary of 2th Quattor workshop (2018-10-29 to 2018-10-31, University of Gent)
category: meeting
author: Michel Jouvin
---

# Quattor Workshop - UGent - 29-31/10/2018


## Site Reports

### UGent

Considering looking at Aquilon but for the time being still will SCDB
* Tweaked it more in the meantime...

OpenStack: wrote a component that can manage/configure most of OpenStack services

### RAL

More and more Quattor/Aquilon usage
* HPC on board
* Other system groups suggested to use it: want to promote commonality across the department

Aquilon: working well but with a few local tweaks

Ceph: less and less configuration to do at each new release, easier to support in Quattor

Work in progress with FreeIPA but still a long journey...
* Need to cleanup LDAP and NIS services first...

James now more involved in HTC configuration/management
* Batch system: HTCondor
* Also managing the teams in charge of grid GOCDB and APEL

### MS

Big challenge: integrate new teams, teach them best practices
* Code review is a key (Gerrit)
* panlint helps
* More documentation on how to right proper pan would help

Looking at integrating Docker/Kubernetes as the provisioning infrastructure for grid

Move out of AFS impacts Kerberos: which alternatives? FreeIPA? Active Directory?

Still has to support `RHEL5`: impacts ability to upgrade AII servers
* Plan to look at `RHEL8` impact on Quattor when it is available: hopefully nothing disruptive (based on Fedora)...

Working on pushing upstream MS modifications to components.

### LAL

Still running SCDB but Aquilon production instance started!
* Manages a few nodes: need time to review/migrate site templates
* Using Active Directory as the Kerberos infrastructure
* Deployment server shared with SCDB
* Very impressed by Aquilon quality
* Documentation updated on quattor.org: should be pretty complete to start
  * A preliminary SCDB migration guide available

Aquilon: several contributions... and open issues
* Good collaboration with MS after initial definition of the process

Open question: how to model/integrate the cloud infrastructure in Aquilon
* Don't want to track in Aquilon what is tracked in the cloud, like VM placement
* The OpenStack cloud is our base infrastructure: more and more virtualised services with system image
managed with Quattor
  * Service data in a persistent disk
  * Image built from a base image + Quattor customisation
  
Another wish for Aquilon: be able to define site-specific key/value pairs in Aquilon that will be passed to
the plenary templates in some ways


## Debian Support

No progress since last workshop. Basically working except the network configuration.
* Debian packaging done from RPM after unpacking them: hacky at this time, limited functionality (no pre and post script support)
  * Files are properly relocated to be at the standard place in Debian
* No initial install support
  * Debian said to support Kickstart files: is it worth exploring?
  * RAL focus: management of (CumulusOS) switches where initial install is not an issue.
  * Same use case at UGent: currently using `metaconfig` to generate the appropriate config file and push them manually
  to the switch
  
Main issue currently: a bug in `ncm-spma` apt back-end leading to packages not installed or with the wrong version.
* See https://github.com/quattor/configuration-modules-core/pull/1258


## OpenStack Support

2 approaches currently for OpenStack configuration
* The template library based on `metaconfig` to produce the required configuration
  * Makes easy to support different OpenStack version with a different branch of the templates, like it was done for
  grid middleware
  * Used by RAL, LAL and Strasbourg
* `ncm-openstack` by UGent that does everything: used to support `Ocata`, now supports Pike
  * Internally based on `CAFRender` and Template Toolkit files: makes easy to add a new service (highly based on `metaconfig` code)
  * The component is sensitive to OpenStack configuration changes with new versions: often significant changes
  * Endpoints managed by Quattor
  * Keystone users for the OpenStack services managed by Quattor
  
It would be good to see if the configuration module could be used with the template library
* Main challenge is the support of multiple versions in the configuration module: impact on the schema and Template Toolkit files
* Alex interested to have a look

Work in progress at UGent on OpenID support but it will remain necessary to create users manually in OpenStack

Also started with Manilla: some issues related to the fact that the NFS server needs to be managed outside OpenStack
* Need to ensure that network routing is properly configured from the VM network to the NFS server
* UGent: NFS server is based on Ganesha in front of Ceph
  * No performance figures yet

  
## Quattor Releases

Next one planned: 18.12
* By Christmas
* 3 releases a year seems a good rhythm
  * 18.9 will not happen: not enough availability during summer
  
New layout for template library repositories: need to experiment with several ideas first, no planned soon...
* See https://github.com/quattor/release/issues/309
* Also needed to configuration modules
* Approach foreseen: pull request from the source repository to the destination one, possibly after moving a branch content
 in a directory (in the source repository?)
* Also need to move open issues and pull requests to new repository (will not preserve numbers)
  * A tool exists at GitHub for doing it (with cross references in both repositories)
