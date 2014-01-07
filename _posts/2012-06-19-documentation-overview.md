---
layout: article
title: Quattor Overview
category: documentation
modified: 2013-12-17
---

Quattor is a distribution of tools aimed at complete system management, this document aims to provide an overview of the tools and how they fit together.

There are three high level building blocks:

1. The <abbr title="Configuration Management Data Base">CMDB</abbr> server.
2. The <abbr title="Automated Installation Infrastructure">AII</abbr> server.
3. Managed Clients.

N.B. The CMDB and AII servers can of course reside on the same system.

# Tools on Quattor Servers

****************************************************************
## CMDB
The Configuration Management Data Base has changed the most noticably during the evolution of Quattor,
it is the single component that admins and users interact with the most during day to day operations and therefore the place where scalability issues cause the most pain.

### CDB
#### 1st Generation
* CVS based Pan template store.
* Deployment workflow integrated with [ELFms](http://elfms.web.cern.ch/elfms/).
* Quickly reached scaling limits and was abandoned by the community, but remains in use at CERN for legacy systems.

### SCDB
#### 2nd Generation
* Subversion based Pan template store.
* Additional tooling for tagged deployment based on ant and SVN repository hooks.
* Suffers from scaling problems above 2500 systems.
* Deprecated - Used widely in the community but no further development will be supported.

### Aquilon
#### 3rd Generation
* New model based around a RDBMS-backed broker and Git repositories.
* Broker (`aqd`) stores and manipulates asset objects and the relationships between them.
    * Admins and Users communicate with broker using the `aq` client.
    * Owns and writes some configuration itself.
    * Implemented in Python.
* Pan template changes made in Git branch "sandboxes" and merged into production.
* Designed for hyper scalability, i.e. single production instance managing hundreds of thousands of systems.


****************************************************************
## panc

`panc` is the Pan language compiler, it compiles the declarative Pan language to a nested tree structure in a variety of output formats including XML and JSON.

The Quattor toolkit can use both XML and JSON both plain and gzipped, gzipped JSON is recommended due to small size and clarity.

The compiler is normally invoked by some part of the tooling that makes up a CMDB, but can also be used standalone, see [the Pan book](http://sourceforge.net/projects/quattor/files/Panc/10.0/pan-book.pdf/download) for more details.

`panc` is implemented in a mixture of Java and Clojure and runs in a standard JVM, see [Cal's blog post](blog/2012/05/07/review-pan-in-clojure.html) for a peek at the internals.


****************************************************************
## AII - Automated Installation Infrastructure

Uses a set of plugins to manage the configuration and state of:

* `aii-dhcp`
    * Writes a file in `dhcpd.conf` syntax which can be included in the root level configuration of `dhcpd`.
    * Can reload `dhcpd` when the configuration changes.

* `aii-pxelinux`
    * Configures and maintains symlinks to manage pxe-booting of systems and subsequent installation with Kickstart.
    * A cgi script called `installack.cgi` is called by nodes at the end of installation to switch back to booting from local disk.

* `aii-ks`
    * Writes Kickstart files for Anaconda for EL derived systems.
    * Uses information from profiles to partition drives.


****************************************************************
## Tools on Managed Clients

### Configuration Cache Manager
* `ccm-fetch`
    * Fetches updated profile for system from upstream webserver, validates it and stores the new profile in the local cache.

* `ccm-purge`
    * Cleans up the configuration cache directory removing unused configuration profiles, temporary files, and unused cached files.

* `ccm-initialise`
    * Creates an initial directory hierarchy for the local config cache, along with the necessary lock files.
    * Should only be called during or immediately following the fresh installation of a new system.

### Node Configuration Management Subsystem
* `ncm-ncd` - Node Configuration Dispatcher
    * Front end for invoking NCM configuration components.
    * Called with a list of components to be invoked as an argument.
      Based on this list, the ncd looks up the inter-component dependencies, orders the components, and invokes each component sequentially.
    * If no component is specified, the ncd will invoke all components which are marked as active in the node configuration profile.
      These are considered to be the ’default’ components to run.

* `ncm-cdispd` - Configuration Dispatch Daemon.
    * Waits for new incoming configuration profiles and monitors the CCM cache.
    * Invokes components with changed configuration trees components via `ncm-ncd`.

* `cdp-listend` - Notfication Listener Daemon.
    * Listens for UDP packets on port 7777, when one is recieved it launches `ccm-fetch` to fetch new profiles and `ncm-cdispd` to apply them.

* Configuration Components
    * Perl modules that are used by `ncm-ncd` to configure a specific service or subsystem on a client system.
    * Contain any special logic required to interact with a particular service, e.g. special restart handlers.
    * Two general purpose components are used to handle the majority of services with simple configuration requirements:
        * `ncm-metaconfig`
        * `ncm-filecopy`
    * Components are grouped into two categories:
        * Components for [core](https://github.com/quattor/configuration-modules-core) services.
        * Components for services relating specifically for [grid computing](https://github.com/quattor/configuration-modules-grid).


****************************************************************
## Detailed Overview

The diagram below shows how all these pieces fit together. As long as the interfaces are preserved any of the components can be replaced.
For example, a site with an existing installation system could choose to use AII for DHCP only and modify their existing system to install and run the quattor client during initial installation.

![Quattor Interprocess Flow](img/quattor-interprocess-flow.png)


****************************************************************
## Feedback

Comments, bug reports, patches and feature requests [are welcome](/contacts/).

