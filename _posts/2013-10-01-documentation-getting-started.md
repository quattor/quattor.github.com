---
layout: article
title: Getting Started with Quattor
category: documentation
---

Quattor is a complete, but somewhat complex, set of tools for
automated machine management.  This document provides a gentle
introduction that highlights the main capabilities of Quattor by
showing you how to install a server and take partial control of
another machine.  Production use will require a good knowledge of the
toolset and your site configuration.

Scenario
--------

This mini-tutorial will show you how to install an Aquilon server and
then take partial control of another machine.  To demonstrate the
basic machine configuration workflow, you will add a user account to
the client machine.

Prerequisities
--------------

There are some prerequisites to complete this tutorial.  For hardware,
you will need:

* One machine to act as the Aquilon server.  This machine should be
  running a minimal, updated version of a RHEL 6 (or compatible).

* One machine to act as the client.  This machine should also be
  running a minimal, updated version of RHEL 6 (or compatible).

You will need to have root access to both of these machines.

You will also need some basic information about these machines:

* DNS hostnames for the machines
* IP addresses of the machines
* An open network between the two machines
* Access from these machines to external repositories

The access to the external repositories are critical to allow the
Quattor software to be installed easily on the tutorial machines.

Installing Aquilon
------------------

Add Aquilon yum repository to the machine.
Create `/etc/yum.repos.d/aquilon.repo` with the following contents:

    [aquilon]
    name=Quattor - aquilon
    baseurl=http://yum.quattor.org/aquilon/
    enabled=1
    gpgcheck=1

Then afterwards, install the server with:

    $ yum install aquilon-postgresql

To start the server, just do the following:

    $ service aqd start

Voila!  You have a working Aquilon service.

Basic Site Configuration
------------------------

Taking Control of Client Machine
--------------------------------

Add User Account
----------------

Next Steps
----------

Now you have seen how the Quattor server and client software are
installed and used.  Running Quattor in production will require more
detailed knowledge about the Quattor Toolkit and Quattor best
practices.

In particular, you will need to investigate further the following
topics:

* Using Quattor to install a machine from scratch.
* Configuring the security for the Quattor system.

You can find additional documentation concerning these topics and
others in the [documentation][qdocs] part of the Quattor web site.

Feedback
--------

Comments, bug reports, and feature requests are welcome.  Please
subscribe to the Quattor discussion list and raise issues there.  See
the [contact][qcontacts] area of the Quattor web site.

[qdocs]: http://quattor.org/documentation/
[qcontacts]: http://quattor.org/contacts/
[aqyum]: http://yum.quattor.org/aquilon/
