---
layout: article
title: Migrating to JSON profiles
category: review
pygments: true
---

Since Panc 9.2 it is possible to compile profiles in the more readable
JSON format.  And since 9.3 it is possible to use it with our standard
Ant tasks.  Here are the steps:

## Upgrade the compiler

If you are using SCDB, download the Ant jar from
[SourceForge](https://sourceforge.net/projects/quattor/files/panc/9.3/),
and place it in your working copy, under `externals/panc/lib/panc.jar`.

## Upgrade CCM

You'll need CCM as shipped with Quattor 12.12.  Just upgrade!

## Change the URL in your CDB to the JSON profile

Replace the contents of `/software/components/ccm/profile`.  In QWG,
that probably means editing `standard/quattor/client/config` and
replace the old `.xml` extension with `.json` or `.json.gz`.

At UGent it looks like this:

    "/software/components/ccm/profile" = format("%s/%s.json.gz",
        QUATTOR_PROFILE_URL, OBJECT);

## Change the compiled formats

Edit your `quattor.build.xml` file and fix any warnings the compiler
is showing.  Finally, edit the line `<property name="pan.xml.format"`,
and turn it into this:

    <property name="pan.xml.format value="json.gz,pan,dep"/>

Compression of the JSON profile is optional but suggested.

During a while (say, a week), you want to compile all your profiles
both in Pan and in JSON format.  That way, nodes that don't receive
updates (f.i, if they are down), will be able to access their profiles
from their old URLs and adapt to the new ones gradually.

You also have to declare the generation of dependency files.

## Update SCDB Ant task

In order to regenerate your `profile-info.xml` files, you'll need the
latest SDCB Ant tasks.  Get them from
[here](https://svn.lal.in2p3.fr/LCG/QWG/scdb-ant-utils/tags/9.0.1/).

Before you build, you may need to edit the `build.xml` file and ensure
your `javac` section looks like this: add

    <javac srcdir="${src}"
           destdir="${build.java}"
           includes="**/*.java"
           deprecation="on"
           debug="true"
           target="1.6"
           debuglevel="lines,vars,source"
           optimize="false">

This ensures your Ant task will work on Java 1.6 (as in SL) and 1.7
(as in more recent platforms).

## (Optional) adjust your Web server

If you have any `RewriteRule`s, this is a good moment to revisit
them.  Ensure they don't redirect to the XML files anymore.

Also, if you are enabling profile compression for the first time,
you'll want to add:

    AddEncoding x-gzip .gz .tgz

to your Apache configuration.

## Upgrade AII

Your clients work just fine.  But you'll need to upgrade the installer
to a version that can deal with the new format.  Just upgrade AII to
the version shipped with Quattor 12.12, and add

    profile_format=json # Or json.gz

to `/etc/aii/aii-shellfe.conf`.

## Conclusion

That's it!  Deploy, compile, install at your pleasure.

Eventually, you'll want to disable pan format output, and use only
JSON and dep.

At UGent, compressed JSON profiles take 1/30 the space of the.  This
pays off in the load of the Quattor servers during our deployments.
