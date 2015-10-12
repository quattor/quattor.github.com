---
layout: article
title: Migrating to JSON profiles
category: documentation
author: Luis Fernando Muñoz Meijas, Michel Jouvin
modified: 2014-03-29
---

Since the Quattor 12.12 release, it possible to use JSON-formatted
machine profiles instead of the standard XML profiles.  The JSON
format is much more readable for humans and its smaller size
(especially with compression) reduces the load significantly on the
Quattor server, even for small to medium-sized sites.

Reduced I/O may also speed up your compilations slightly.

This document describes the steps required for
migrating our from XML to (compressed) JSON
profiles.

## Software updates

### Quattor releases

You need Quattor version 13.1.4 (SPMA-based deployment) or a version >= 14.4.0 (YUM-based deployment). You must download the appropriate
templates from `template-library-core` if you don't have them already.

*Note: you can use `utils/scdb/create-vanilla-SCDB.sh` from `scdb` repository as an easy way to download them.*

If you are using SCDB, you move your clusters to these new versions by editing their `cluster.build.properties` file.


### SCDB

If you are using SCDB, you must be sure to use a recent version, typically the last one you get by running the script suggested above. The critical
components are:

* `scdb-ant-utils` >= 9.0.2
* `panc` >= 9.3

*Note: recent versions of SCDB changes the default directory for profiles from `build/xml` to `build/profiles`. If you want to retain the previous
setting, you need to define property `build.profiles` property to `xml` in your `quattor.build.properties` file (in root directory of your
configuration database).*

## Change the compiled formats

During a certain period, you will want to compile all your profiles
both in Pan and in JSON format.  That way, nodes that miss some
updates (for example, if they are down or have a `ncm-spma` error preventing execution
of `ncm-ccm`), will be able to access their
profiles from their old URLs (old XML format) and adapt to the new ones gradually.

Until you change
the profile URL, generating new profile formats doesn't affect your machines,
as long as the XML (pan) format is still produced. To have the machines switching to using the JSON profile, you
need to define the following variable in your site configuration (if you are using the standard template library):

```
variable QUATTOR_PROFILE_FORMAT ?= 'json';
```

After making this change, you'll have to deploy the new configuration twice to have the node picking its JSON profile: first deployment
will update the URL to be used for the next deployment. After doing these two deployments, you should be able to identify nodes that
are still picking their XML profiles by checking the `httpd` logs on your deployment server. Typically, a command like the following
one should give you the list of nodes that have not switched to JSON profiles:

```bash
# Adjust the date in the grep command to match the day/time you did the change
grep 'profiles/.*xml' /etc/httpd/logs/access_log | grep '10/May/2014:15' | awk '{print $7}' | sort -u
```

**It is strongly recommanded to fix all the problematic nodes before generating only JSON profiles, else you will loose control on these nodes.
You also need the period to be long enough to allow nodes which are down to get a chance to be restarted, as these nodes will not appear in the `httpd`logs.**

### SCDB

To generate the JSON format in addition to the XML format, you need to add or edit the
file `quattor.build.properties` in the root directory of your configuration database (same directory
as the one containing `quattor.build.xml`) and add the line:

```
pan.formats=pan,json,dep
```

*Note: adjust the format list to match your needs. Use `pan.gz` and/or `json.gz` if you want to use compressed profiles.*

When all your nodes have picked up their JSON profile (check your http logs on the deployment server), you can
remove `pan` from the property `pan.formats`.

*Note: avoid editing `quattor.build.xml` which is a standard file that is regularly updated to provide new features.*

## Adjust your Web server (optional)

If you have any `RewriteRule`s, this is a good moment to revisit
them.  Ensure they don't redirect to the XML files anymore.

Also, if you are enabling profile compression for the first time,
you'll want to add:

```
AddEncoding x-gzip .gz .tgz
```

to your Apache configuration.

## Upgrade AII

You need to upgrade your deployment server to one of the Quattor version mentioned above and then your need to
instruct AII to use JSON profile rather than the XML one. This is done by editing `/etc/aii/aii-shellfe.conf`.

```ini
profile_format=json # Or json.gz
```

If your deployment server is managed with Quattor using the standard template library (recommended), this is done automatically as soon as you
have defined the following variable:

```
variable QUATTOR_PROFILE_FORMAT ?= 'json';
```

## Conclusion

That's it!  Deploy, compile, install at your pleasure.

If any of your
internal tools parsed the XMLs directly (without CCM) you will have to
adapt it.  We recommend you to try
[Elasticsearch](https://www.elastic.co/) and our new
[data warehouse](https://github.com/quattor/data-warehouse) tool.

At UGent, compressed JSON profiles take 1/30 the space of the
equivalent XML profiles.
