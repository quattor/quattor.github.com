---
layout: article
title: Configuring Quattor YUM repositories
category: documentation
author: Michel Jouvin
---

This article explains how to configure the required YUM repositories for Quattor components.

## Quattor YUM repositories

Quattor uses mainly one specific YUM repository containing all the Quattor components that are part of a Quattor release. There is one YUM repository *per release*. As a
consequence, after the release, no modification is made to this repository and thus there is no need to snapshot it as a standard YUM repository. These repositories are hosted on
http://yum.quattor.org (release candidates, which all have their own repository too, are under http://yum.quattor.org/testing).

In addition, Quattor has a few dependencies that are not provided by the OS standard repositories or EPEL. We try to keep this list as minimal as possible but when required we put
them in a, `externals` repository. At the time this article was written, we are transitioning from an old YUM repository hosted at 
http://quattorsrv.lal.in2p3.fr/packages/quattor/externals/ to a new `externals` repository hosted at http://yum.quattor.org (not yet ready for production use, see
https://github.com/quattor/release/issues/62 for progress).

## Configuring the repositories with the template library

The [template library](http://www.quattor.org/documentation/2014/06/06/how-to-use-template-library.html) provides an easy way to both get all the templates required to configure a
give Quattor version ([template-library-core](https://github.com/quattor/template-library-core)) and to configure the YUM repositories required
([template-library-standard](https://github.com/quattor/template-library-standard)) without creating/maintaining any site specific templates. 

When using these two parts of the
template library, configuring the required repositories for a given release is as simple as adding the following line in one of your site specific template (in SCDB, this is
typically done in the cluster `repository/config.pan`):

```
include repository/config/quattor;
```

Note that this line is independent of the Quattor version and will do what is appropriate for the Quattor version actually used to configure the machine (in SCDB, according to the
version of Quattor associated with the cluster in `cluster.build.properties`).
 
