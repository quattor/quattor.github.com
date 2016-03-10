---
layout: article
title: Quattor development basics
author: Stijn De Weirdt
category: documentation
---

[devel_unittests]: {% post_url 2016-03-09-development-unittests %}

# git / github

All quattor git repositories are part of the [quattor organisation on GitHub][quattor_gh]

[quattor_gh]: https://github.com/quattor


## Prerequisites

1. An account on [GitHub][github]
2. [Join][join_quattor] the quattor organisation and `developer` team
 * In case there is a problem, contact the mailinglist as [admins can also add new members][join_team_gh]
3. Join the [`quattor-devel` mailing list][quattor_devel_ml]

[github]: https://github.com
[join_quattor]: https://github.com/orgs/quattor/teams
[join_team_gh]: https://help.github.com/articles/adding-organization-members-to-a-team/
[quattor_devel_ml]: https://lists.sourceforge.net/lists/listinfo/quattor-devel

### Getting started with git

Lots of good introductions and tutorials using git and github already exists

* [Short animated introduction][lal_git_beginner_animation] (use left/right arrows to navigate)

[lal_git_beginner_animation]: https://ens.lal.in2p3.fr/NPAC/_static/slides/Git/slides/index.html#1

TODO: add more

## Workflow

1. Fork the repository you want to work on
2. Clone the forked repository locally using the `ssh` URL
 * Your fork is known as `origin`
3. Add the `upstream` repository using the `https` URL
4. Start with a new branch
 * Do not work in `master` branch
5. Make modifications, add and commit them
 * Try to use meaningfull messages
  * For the the `configuration-modules-core` (and other `configuration-modules`) repository, set the
    component name in the commit message when working on more then one component in same branch.
6. Push your changes to your fork (i.e. to `origin`)
 * Do not push to `upstream`
7. Run the unittests
 * Add new ones to cover your changes (or refine existing ones)
8. Open a pull request (PR)
 * Meaningful title; title will be part of the relase notes
  * For `configuration-modules` repository: start the title with the component that is being modified
   * When more then one component is modified, describe the general work in the title;
     the commit messages should have the component names.
 * Set `milestone` (i.e. the release you want this merged in)
  * Set a realistic milestone, e.g. if the PR is not urgent or not finished
    or you have no time to follow up, you might want to pick a later milestone.
9. The initial PR will trigger a [jenkins][quattor_jenkins] build of the unittests
 * The tests are run with the PR merged in current master
10. The PR will be reviewed, and after the reviewer is satisfied, it will be merged in.
11. Every 2 months, a release is made by the release manager that will contain your changes
 * Only for severe regressions / bugs, the release manager might consider an intermediate
   release to address the specific issue.
 * To start using your new code, you can make your own `package` and upload it to your own repository
  * Best to add a separate `testing` yum repository (no snapshots)
   * This repository should be empty most of the time, but you can put your self-built packages there
     until the new release is out that conatins your changes.

[quattor_jenkins]: https://jenkins1.ugent.be/view/Quattor/

# Maven

Quattor uses `maven` for its software project management.

All source code and unittests are kept under the `src` subdir.

 * `src/main/perl` for perl modules
 * `src/main/pan` for pan templates like `schema.pan`
 * `src/test/perl` for the perl unitttests (and any other perl helper modules that might required)
 * `src/test/resources` for pan templates that are used with the unittests
 * metaconfig services are an exception

During testing, a `target` subdir is created by the maven tool (and removed with `mvn clean`).

The process is steered via a `pom.xml` file, that is derived from a quattor maven atrifact.

These pom files require few changes, but typical ones are:

 * add developer / maintainer
 * set the project name (e.g. in case of a new component)
 * add custom plugins for specific projects
 * bump the version of the `build-profile` to the latest using `mvn update`

## maven commands

Most common commands are

0. `mvn clean` cleans any previous maven runs (in particular the `target` directory)
1. `mvn test` runs the unittests
 * best to run `mvn clean test`
2. `mvn package` Sometimes you will want to make a rpm or tarball to start
 using your code while waiting for the PR to be reviewed and merged. This command
 will create the rpm (and tarball).
 * `package` also runs the tests, and also here it is advised to use `mvn clean package`

When newer build tools are available, use `mvn update` to bump the version in the `pom.xml`
(do not edit by hand).

[More information on running the tests][devel_unittests_running]
[devel_unittests_running]: {% post_url 2016-03-09-development-unittests %}#running-the-tests


# Adding new component in configuration-modules or AII

TODO: more info

New components should be added to the parent `pom.xml` in order to be part of the release.

Copy initial `pom.xml` from other component/hook, change the project.
