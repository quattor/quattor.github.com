---
layout: article
title: Migrating to JSON profiles
category: documentation
pygments: true
---

Since the Quattor 12.12 release, it possible to use JSON-formatted
machine profiles instead of the standard XML profiles.  The JSON
format is much more readable for humans and its smaller size
(especially with compression) reduces the load significantly on the
Quattor server, even for small to medium-sized sites.

Reduced I/O may also speed up your compilations slightly.

This document describes the steps we took at Ghent University for
migrating our production infrastructure from XML to compressed JSON
profiles.

## Software updates

If you are using SCDB, download the Panc Ant jar from
[SourceForge](https://sourceforge.net/projects/quattor/files/panc/9.3/),
and place it in your working copy, under
`externals/panc/lib/panc.jar`.

You'll also need CCM as shipped with Quattor 12.12.

### Updating the SCDB ant tasks

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

You also have to change the filesets that will be copied and used for
sending the CCM notifications.  By default, SCDB notifies to any hosts
that have an XML profile.  But there is no XML profile anymore.  So
open your `quattor-build.xml` (or equivalent file), search the
`deploy.and.notify` target, and replace the filesets into something
like this:

    <copy todir="${deploy.xml}">
      <fileset dir="${build.xml}">
        <include name="**/*.json" />
        <include name="**/*.json.gz" />
      </fileset>
    </copy>
    [...]
    <quattor-notify message="ccm" port="7777">
      <fileset dir="${build.xml}">
        <include name="**/*.json.gz />
      </fileset>
    </quattor-notify>

## Change the URL in your CDB to the JSON profile

Replace the contents of `/software/components/ccm/profile`.  In QWG,
that probably means editing `standard/quattor/client/config` and
replace the old `.xml` extension with `.json` or `.json.gz`.

At UGent it looks like this:

    "/software/components/ccm/profile" = format("%s/%s.json.gz", QUATTOR_PROFILE_URL, OBJECT);

## Change the compiled formats

Edit your `quattor.build.xml` file and fix any warnings the compiler
is showing.  Finally, edit the line `<property name="pan.xml.format"`,
and turn it into this:

    <property name="formats" value="json.gz,pan,dep"/>

Compression of the JSON profile is optional but suggested.

During a while (say, a week), you want to compile all your profiles
both in Pan and in JSON format.  That way, nodes that miss some
updates updates (f.i, if they are down), will be able to access their
profiles from their old URLs and adapt to the new ones gradually.

You also have to declare the generation of dependency files.

## Adjust your Web server (optional)

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

to `/etc/aii/aii-shellfe.conf`.  The aiiserver component supports this
option, too.

## Conclusion

That's it!  Deploy, compile, install at your pleasure.  If any of your
internal tools parsed the XMLs directly (without CCM) you will have to
adapt it.  I recommend you to try
[Elasticsearch](www.elasticsearch.org) and our new
[data warehouse](https://github.com/quattor/data-warehouse) tool.

Eventually, you'll want to disable pan format output and use only
JSON and dep.

At UGent, compressed JSON profiles take 1/30 the space of the
equivalent XML profiles.
