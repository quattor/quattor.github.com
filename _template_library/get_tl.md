---
layout: article
title: How To Get The Template Library
author: Michel Jouvin
redirect_from: /documentation/2014/06/06/how-to-use-template-library.html
menu: How to Get It?
---

[tl_introduction]: /template_library/00-introduction.html
[get-tl-script]: https://github.com/quattor/release/blob/master/src/scripts/get-template-library
[create-scdb-script]: https://github.com/quattor/scdb/blob/master/utils/scdb/create-vanilla-SCDB.sh
[dir-sync-script]: https://trac.lal.in2p3.fr/Quattor/wiki/Download/QWGTemplates/Install#In-placeUpgrade
[release-repo]: https://github.com/quattor/release

This page describes how to get the Quattor [template library][tl_introduction].

## How to Get It?

The layout of some of the Git repositories is not really appropriate for a direct use. Two tools
have been developped to download the template library as a ready-to-use set of templates :

* `get-template-library`: download the template library itself organized in a way
  suitable for importing it in SCDB or Aquilon.
* `create-vanilla-SCDB.sh`: create a new SCDB configuration database, with all the
  SCDB tools and the template library. This script uses `get-template-library` internally
  and compiles SCDB examples at the end of the download.

### get-template-library

[get-template-library][get-tl-script] is located in GitHub [release][release-repo]
repository (in `src/scripts`). By default, this script
downloads the whole template library in `/tmp/quattor-template-library`. The downloaded
contents can then be imported into an existing SCDB or
Aquilon installation.

*Note: for SCDB, you can use [directory-sync][dir-sync-script]
to import the new version of the template library).*

Before using `get-template-library`, clone the GitHub [release][release-repo]
repository. If you already have a clone, be sure to
refresh it before using the script (typically with `git pull`).

Use `--help` to get a list of all the available options. The script needs the version
to download as a parameter. A typical use of `get-template-library`
(to download Quattor version 14.5.0, after removing `/tmp/quattor-template-library` if it exists) is:

```bash
get-template-library -F 14.5.0
```

### create-vanilla-SCDB.sh

If you are interested by getting the template library validation resulting from the
compilation of the examples, it is recommended to use
this script whether you are using SCDB or not. The library part of SCDB (under
`cfg` directory) is exactly the same as the one created by `get-template-library`.
The only reasons to use this script are the creation of the new SCDB or to validate the
template library against the SCDB examples.

This script [create-vanilla-SCDB.sh][create-scdb-script] is in repository
[scdb](https://github.com/quattor/scdb/blob/master/utils/scdb). It creates a new SCDB with all the SCDB tools, uses
[get-template-library][get-tl-script] to download the template library and then compiles the SCDB examples.
The new SCDB, by default, is in `/tmp/scdb-vanilla`.

A typical use of this script involves the following steps (in the example, to downlaod
version 14.5.0 of the template library after removing `/tmp/scdb-vanilla`):

```bash
git clone https://github.com/quattor/scdb.git
cd scdb
utils/scdb/create-vanilla-SCDB.sh -F 14.5.0
```

This script accept all the options valid in `get-template-library`, in addition to its
specific options.

*Note: if you already have a clone of SCDB repository, you can update it. Be sure to
do it as the script is regularly updated.*

## Upgrade

As any other components in the Quattor toolkit, the template library evolves to fix issues, to support new functionalities or services and to increase
the flexibility in the configuration options. Thus it is important to upgrade it regularly, when a new Quattor release is announced.

When upgrading, it is important to upgrade the whole template library, not just one subset, else you are at risk of inconsistencies between subsets.
This is especially true of the `standard` subset that all the other subsets depend on. Except if there is a special announcement, it is better
to install the template from a Quattor release than from the master of the Git repositories: despite our attempt to have the master always
working, only Quattor releases go through the whole testing process.

To do the upgrade, the easiest is to get a fresh version of the template library following the [procedure](#how-to-get-it) described above. Then
from the directory where the new template library resides (this depends on the tool
used to download it, see above), the template library can be imported to a production SCDB or Aquilon. For SCDB, a script
helping with the update is available: [directory-sync][dir-sync-script].

