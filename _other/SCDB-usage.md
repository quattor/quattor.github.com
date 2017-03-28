---
layout: article
title: SCDB User Guide
author: Michel Jouvin
---

[tl_intro]: /template_library/00-introduction.html

**Note: SCDB, the second generation of Quattor databases, is now deprecated in favor 
of [Aquilon][aquilon_intro] which provides more flexible workflows and an improved  
scalability.. As SCDB is still used as some sites, the information here 
is kept for reference but if you are a new Quattor user, condider using Aquilon rather 
than SCDB.**


## SCDB Architecture

SCDB configuration database is based on Subversion (SVN): everything is store in a Subversion 
repository. Any SVN client can be used to checkout/update/commit changes from/to
the configuration database and all the SVN features can be used to manage the history 
or to roll back changes. 

Profile compilation and deployment is done with `ant`, a 
tool available on any platform (Unix, OSX, Windows). With SCDB, all the work is done 
on the administrator machine. Except for the deployment, no network connection is required.

In SCDB, deployment of a new configuration is a 3-phase process :

1.  Template modification with your preferred editor and compile with `ant`. 
    This phase requires no network connection.
2.  Once compilation is successful, it can be committed with your preferred SVN
    client. And you can synchronize changes that were done by other administrators
    with `svn update`.
3.  After committing the changes, the new configuration can be deployed with `ant` deploy.
    Deploy phase starts by recompiling the configuration locally: this is almost immediate
    if no change happened since first step. It creates a SVN *tag* for the deployed configuration
    for an easier roll back.

`ant` enforces the following prerequisites for a successful deployment:
-   A successful local compilation of the new configuration
-   All the local changes must have been committed to the repository
-   All the changes made to the repository by others must have been imported in the 
    local copy (`svn update`).



### Template Library

In SCDB all the templates are stored in the `cfg/` directory of the configuration database/repository. 
Under this directory, a site typically import the [template library][tl_intro]. In addition, 
two site specific directories are available: `clusters` and `site`.

* `clusters`: this directory contains mainly host profiles organized by *clusters*. 
  A cluster is an arbitrary group of hosts that share some common parameters, typically 
  defined in the `site` directory of the cluster. There is one directory per cluster 
  under the `clusters` directory. Each cluster has one file `cluster.build.properties` 
  in its top directory that defines the other template parts that are used in the cluster 
  (every directory specified is relative to `cfg` directory) with `cluster.pan.includes` 
  property. See SCDB examples on GitHub 
  for more details.

* `site`: a set of configuration templates and parameters shared by several clusters. 
  There is typically one directory per site under the `site` directory. A configuration 
  database can contain as many site as needed. The cluster  `cluster.build.properties` 
  file defines which sites are used by a cluster

### Cluster groups

Clusters in the `clusters` directory can be organized in groups. To enable the cluster 
group features, is is necessary to define the property `clusters.groups.enable` 
in the file `quattor.build.properties` (in the top directory of the configuration database):

```
clusters.groups.enable=true
```

## Using SCDB

### Configuring SCDB Ant Tools

The main configuration file for SCDB and its Ant Tools is `quattor.build.properties` in 
the top directory of the configuration database. This file allows to customize default 
values defined in `quattor.build.xml`, the `ant` configuration file used by Quattor.
Lines in this file must have the format
`key=value`, with `#` as the comment delimiter. Not that everything
after `=` is considered part of the value, including leading spaces,
quotes and doubles quotes (quotes are not interpreted as a string
delimiter).

The configuration options (called `properties`) available are documented
at the beginning of `quattor.build.xml`. They allow to customize
the layout used to organize and locate templates. It is recommended to
avoid unnecessary changes as it may become more difficult to
troubleshoot problems. The most common options used are:

```cfg
# Define to true if you want to use cluster groups
clusters.groups.enable=true
# Define profile format to be json (recommended)
pan.formats=json,dep
# Disable pan deprecation warnings (not recommended in production)
pan.warnings=off
```


### Displaying Resulting Changes in Profile

When doing changes in configuration, this is often useful to check the
resulting profiles before deploying. There is a small tool to help doing
that, \[source:SCDB/trunk/utils/profiles/compare\_xml
utils/profiles/compare\_xml\]. This tool is part of \[source:SCDB/trunk
SCDB base\].

To use this tool, before compiling your changes, you need to copy your
current (or reference) `build` directory to something else, by example
`build.saved` (default name used by the script). After the compilation,
if you run the script without arguments, it will display the list of all
profiles that have changed. You can inspect the changes (require a bit
of knowledge of profile contents) using option `-v`. Or you can restrict
the check to one specific profile with option `-p`. By example :

    # utils/profiles/compare_xml

    Comparing XML files (*.xml)...
    Differences found in build/xml/profile_grid05.xml
    Differences found in build/xml/profile_grid06.xml
    Differences found in build/xml/profile_grid07.xml

    # utils/profiles/compare_xml -v -p profile_grid05

    Comparing XML files (profile_grid05.xml)...
    Differences found in build/xml/profile_grid05.xml
    --- build.saved/xml/profile_grid05.xml  2006-07-28 11:41:45.000000000 +0200
    +++ build/xml/profile_grid05.xml        2006-07-28 11:50:58.000000000 +0200
    @@ -960,7 +960,6 @@
             <options>
               <dpm>
                 <db>
    -              <adminpwd type="string">MyPrefPwd</adminpwd>
                   <adminuser type="string">root</adminuser>
                   <configfile type="string">/opt/lcg/etc/DPMCONFIG</configfile>
                   <password type="string">DpmMgrPwd</password>

Another option available, `-d`, extends the comparaison to profile
dependencies. This is generally not useful but can be used to do a
regression test with a new version of the compiler, for example.

### Using SCDB with an IDE

An IDE can be used to manage SCDB contents and trigger deployments as long as the IDE 
has an integrated support for `ant` and for executing Java applications. 
If this is the case, just add the `build.xml` file 
to your IDE Ant interface. Eclipse is such an IDE that has been used successfully by 
several sites.

If you are interested by this integration, contact the Quattor community on the `quattor-discuss` 
mailing list for example.


## Frequently Asked Questions about SCDB

### ant usage

#### java.lang.NoClassDefFoundError: org/apache/tools/ant/launch/Launcher (11/2/07)

If you get this error when trying to use `ant`, that probably means you
have a version conflict between `ant` version distributed as part of SCDB
(in `external/`) and another version installed on the same machine. This
happens if you have a file `/etc/ant.conf` created by the non SCDB
version.

To clear the problem, remove `/etc/ant.conf` or upgrade the non SCDB
`ant` to the same version as SCDB.

#### java.lang.NullPointerException during the deploy phase (11/2/07)

One possible reason for this error is an incompatibility between the
version of JavaSVN used by `ant deploy` and the version of the SVN
client you use to commit your changes. This happens is one of them is
older than SVN 1.4 and the other is greater or equal to 1.4, because of
a metadata format change in workspace introduced in SVN 1.4. As a result
a workspace cannot be read and modified by both pre 1.4 and 1.4 or later
SVN clients (this is clearly stated in SVN 1.4 release notes).

### Deploy failure

#### Failed to switch SVN cache to new tag: url1 is not the same repository as url2

This error means you have an existing working copy of your Quattor
repository on the Quattor deployment server that was checked out from a
repository different from the one defined in `/etc/quattor-deploy.conf`
(option `repository_url` in `[scdb]` section). A common mistake is to
use `http` in one case and `https` in the other one which leads SVN to
consider they are different repositories.

Depending on the URL you really want to use, either fix the
configuration file or remove the existing working copy. If removing the
working copy, be sure to remove the directory, not only its contents (as
you may leave some hidden directories).

The location of the working copy is defined in
`/etc/quattor-deploy.conf` (`svn_cache` option in `[build-tag]`
section). If not defined, the default location is `svncache` directory
in the parent directory of `build-tag.py` location
(`/root/quattor/svncache` by default).

#### Unable to get information on tags branch

If you get this error at the beginning of the deploy phase when
executing `ant deploy` and you have no compatibility problem between the
SVN client version you use and the one embedded in `ant tools`(
`external/svnkit`), this means you don't have valid cached credentials
to access the `tags` branch in your configuration database that can be
used by `svnkit`, the SVN client used by `ant`. To fix the problem, try
to write to `tags` branch using `jsvn` utility provided in
`external/svnkit`. You can use the following commands as an example,
changing the URLs to match your configuration database:

```bash
external/svnkit/jsvn cp htpp://quattorsrv.example.org/quattor/trunk htpp://quattorsrv.example.org/quattor/tags/test -m 'Deploy test'
```

When executing this command, you should be asked to enter your
credentials (userid and password). Note that depending on your exact
actual configuration, you may have to define environment variable
`JAVA_HOME` to reflect the directory containing `bin/java`.

After doing the previous step, check it works by trying to remove the
previously created branch. This should work without `jsvn` asking you
your credentials.

```bash
external/svnkit/jsvn rm htpp://quattorsrv.example.org/quattor/tags/test -m 'Remove test'
```

### AII Issues

AII is the Quattor subsystem handling initial installation of machines.
It has nothing specific to either SCDB or QWG templates, even though it
is well integrated with both of them (see \[/wiki/Doc/OS/Installation OS
Templates\] documentation about how to configure it). Entries in this
fact are only about interaction problems between SCDB and AII.

#### aii-shellfe: No node matches xxx

When using `aii-shellfe` to configure a machine for initial
installation, you may get an error message similar to the following one:

```bash
bash> aii-shellfe --configure mynode.example.org
[ERROR] No node matches mynode(.example.org)?
```

This usually means either that you forgot to deploy your configuration before
running the command or that you made a spelling error with the machine name.
You can check if a `.xml` or `.json` file for the machine name you entered exists
in the directory referred to by variable `osinstalldir` in
`/etc/aii/aii-shellfe.conf` on your deployment server.

Under very rare circumstances, it may happen the `.xml` or `.json` file exists but
you still get the error. In this particular case, try to remove the file
`profiles-info.xml` in the same directory and redeploy your
configuration with the command:

```bash
external/ant/bin/ant deploy
```


