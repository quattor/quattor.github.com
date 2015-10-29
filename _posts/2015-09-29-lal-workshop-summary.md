---
layout: article
title: Summary of 20th Quattor workshop (2015-09-29 to 2015-10-01, LAL)
category: news
author: Michel Jouvin
---

# 20th Quattor Workshop Summary


[Agenda](https://indico.cern.ch/event/440152/timetable/#all.detailed)



## Release Process and Unit Tests

Unit tests are run on EL5, EL6 and EL7 as part of the release process

 * [build_all_repos](https://raw.githubusercontent.com/quattor/release/master/src/scripts/build_all_repos.sh) script takes care of setting the environment required on a freshly installed machine (VM)
 * This script basically sets up a clean environment for Quattor development: could be used for other things
 
 
## Documentation

Julien: initial installation issues

 * No default filesystem layout: do we need to add one in the core template library rather than direct people to look at examples?
 * Aquilon: not clear how to use it without Kerberos, if possible?
   * No it is not possible: no real alternative to Kerberos for a central, strong authentication system that can be used by every Aquilon component
   * Need to better document how to use Active Directory Kerberos with Aquilon
     * Aquilon documentation already contains references (links) on how to set up  a simple Kerberos realm
     
ReadTheDocs as the central place for documentation

 * Because pan compiler and Aquilon are not part of the Quattor release, keep them separate for the moment but everything else in one ReadTheDocs container/project
 * PR open to build config module doc from pod text inside the perl files or from Pan annotation: get rid of the pod files that tend to be unmaintained

On the web site, remove the connection to Disqus?

 * No comment added since it has been activated
 * Got some SPAM
 * Has the risk to be used instead of GitHub, lacking traceability of discussions
 * So remove it! Replace with an invitation to report on GitHub issues with the documentation...
 
Add a RSS feed from GitHub on the web site to show the activity going on there as this is where most of the things happen

 * Currently the web site gives the idea of an inactive/dead project...
  
Review distinction between `Blog` and `Documentation` (other)

 * Need to better exposed stuff: `All articles` in `Documentation`
 
LAL wiki migration: try `pandoc`

 * Seems also possible to do a `trac-admin dump`
 
## Mailing List
   
Reduce the number to two: devel and discuss.

 * See if can just close them to keep the archive or if we need to delete them
 * Close all lists and open 2 new ones on Google? SourceForge now has a negative reputation...
 

## Quattor Components

### Quattor Dashboard
 
Developed by Samir based on the Quattor dashboard by James and the Aquilon console by Frazer

 * Directly parsing JSON profiles
   * If using XML profiles for deployment and other tools, just add generation of JSON in addition to XML
 * Display summary information, ask for a node to be reinstalled
 * Provides some statistics (OS installed, kernel...)
 * Some Aquilon-specific features  if `AQ_URL` is defined
 
Improvements suggested

 * `Boot configuration`: use the same terminology as `aii-shellfe --status` (possibly use it!)
 * Use a specific color for nodes set to install more than a certain number of days ago (e.g. 7)
 
 
### Aquilon

New release every ~3 weeks

Recent changes: implementation of staged deployment of personalities in the broker

* 3 stages defined: next (test), current (production), previous
* Ability to move hosts from one stage to another one
* Ability to "promote" test (`next`) as production (`current`) (and production as previous): all hosts affected

Python 2.7 is recommended but should work with Python 2.6

 * Working with EL7 but still using init scripts
   
ULB tested Aquilon deployment but failed

 * Kerberos configuration: no Kerberos available at ULB
 * Config files provided by the RPM refer to /ms filesystem
 * Used the last version available as a RPM: pretty old...
 
Actions:

 * Clean the quattor repository branches: master very obsolete, develop and pkg-tests unidenfied...
   * Same situation in aquilon-protocols
 * Check if the current upstream contains all the necessary patches to build a RPM 
 * Check that a minimum version of protocols dependency is specified by the broker RPM

Template library

 * Main issue is that some features depends on another feature being included first but AQ broker doesn't guarantee the order of features in a personality
   * Workaround: include the feature in the other feature but will not work if feature A behaviour depends on feature B being loaded or not.
 * Presence of a personality directory is confusing at it is not used by AQ
 

### CAF

Stijn working on a Download module to implement the core features required by ncm-download, ccm... in a consistent way and to provide integration with Kerberos

  * MS has a ncm-download private extension that is using kerberos authentication with a URL to retrieve the machine root password and to avoid having it in the profile
   
TextRender: Remove support for Config::General

 * No guarantee about the line order: better replaced with a TT file called `general`.
 * This ordering issue is a problem for unit testing and also triggers unnecessary restart of daemons, if any associated with changes
 
CCM namespace added to TT files allowing to check profile data, for exemple test the type of resource/property

* `CCM.is_list()`, `CCM.is_hash()`...
  * Allow to base the output on the type defined in the schema rather than duplicate the information in the code with the risk of inconsistency
* `CCM.element()` allows some control on what `getTree()` is doing like the string value to use for booleans
* Makes it possible to replicate `ncm-query` style output with a TT file... (currently implemented for the `--pan` format)

When metaconfig is not appropriate, it is easy to build a new component that uses CAF::TextRender to produce the output files from the profile

 * See the documentation about the steps involved
 * In particular error handling must be implemented by the component: TextRender is not doing anything with errors (even no logging)

Very detailed article for quattor.org web site contributed by Stijn

* Very nice doc: should merge it ASAP
* Long-term: restructure some of this into documentation that is kept with the related source code (CAF, ncm-metaconfig) pushed to ReadTheDocs and a blog entry summarizing the topic and containing references to ReadTheDocs.


### CCM

New `ccm` command allows users to read part of or all of a profile: alternative to `ncm-query`

 * Based on TextRender
 * Supports additional output formats such as json, yaml and pan style xml
 

### Configuration Modules

Define `our $VERSION` with the `no-snapshot-version` and add `no-snapshot-version` as the minimum version required for CAF

* Write a script to do the mass modification
* Similar modification already done in CCM
* The version information allows to also refer versions in the RPM dependencies
* See [the pull-request](https://github.com/quattor/maven-tools/pull/62/files) for details

LAL has a use case for a component that ensures a specific file does not exist (deleting it if it does): typically to remove a file that could have been installed by a RPM and that for some reason is considered a source of problems

* No real use case seen for such a feature by the community: if this is only for a file installed by a RPM, better to modify the RPM (does not apply to the particular case mentionned by LAL). If the file can be added by other means, better to configure a cron job.
* A better approach for this particular need would be to use the YUM `post-transaction-actions` plugin that allows to define actions to do after the installation of some (or all) RPMs (fine control possible on the situation that triggers the action).


