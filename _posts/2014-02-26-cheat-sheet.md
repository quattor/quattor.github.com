---
layout: article
title: Configuration cheat sheet
category: documentation
author: James Adams
---

This article is intended as quick reference, or cheat sheet showing examples of a variety of common and simple configuration snippets in Quattor.

If you have any other examples, please add them!


Add default (latest) version of a package
=========================================
rpmt based spma (deprecated)
----------------------------

```sh
'/software/packages'=pkg_repl('ruby');
```

yum based ncm-spma
------------------

```sh
"/software/packages/{perl-Template-Toolkit}" ?= nlist();
```

<div class="alert alert-info">
  <p>Note the <code>{}</code> around the package name to tell the pan compiler to escape it.</p>
</div>


Pin the version or architecture of a package
============================================
Pin version:

```sh
"/software/packages/" = pkg_repl("config-templates-metaconfig", "0.1.19-1.el6");
```

Pin Architecture:

```sh
"/software/packages/{config-templates-metaconfig.noarch}" ?= nlist();
```

Pin both:

```sh
"/software/packages/" = pkg_repl("config-templates-metaconfig", "0.1.19-1.el6", "noarch");
```

You can also use wildcards for pinning.
Note that this will apply to packages which match and exist the specified version and architecture, others are silently ignored.

```sh
"/software/packages" = pkg_repl("python*", "2.6.19-1.el6", "x86_64");
```

This would pin `python-devel` and `python-libs` at `2.6.19-1.el6`, but leave `python-urlgrabber` at `3.1.0-6.el5`.

<div class="alert alert-info">
  <p>'noarch' could of course be 'x86_64', 'i686', PKG_ARCH_DEFAULT or a variable depending on your requirements!</p>
</div>


Add a repository
----------------

```sh
'/software/repositories' = append(create('repository/clockwork_angels'));
```

Ensure a directory exists (and has correct permissions)
-------------------------------------------------------

```sh
'/software/components/dirperm/paths' = append(
    nlist(
        'path', "/opt/temple",
        'owner', "syrinx:syrinx",
        'perm', '0755',
        'type', 'd',
    )
);
```


Include the contents of an arbitary file from the source tree
-------------------------------------------------------------

```sh
include 'components/filecopy/config';

prefix '/software/components/filecopy/services/{/etc/rsyslog.conf}/';
'config' = file_contents('site/logging/rsyslog/nameserver.conf');
```

Configure a service to start
----------------------------

```sh
include 'components/chkconfig/config';

prefix '/software/components/chkconfig/service/rsyslog';
'on' = '';
'startstop' = true;
```

Download a file from a webserver
--------------------------------

```sh
include 'components/download/config';

'/software/components/download/files{/opt/java-mess/horrible.jar}' = nlist(
    'href', 'https://download.example.com/java-mess/jar/horrible-1.2.3.jar',
    'owner', 'root',
    'group', 'root',
    'perm', '0644',
);
```

<div class="alert alert-info">
  <p>This is useful for files where you do not have control over the origin, in particular files that are frequently regenerated automatically.</p>
  <p>If the files do not change frequently and/or have other dependencies you should consider building real packages to ship the files.</p>
  <p>If you find yourself using this heavily you should definitely consider mirroring the files on a local server or at least using a caching proxy.</p>
</div>

Add a user group
-----------

```sh
'/software/components/accounts/groups/syrinx/gid' = 2112;

```


Add a user account
------------------

```sh
'/software/components/accounts/users/alex' = nlist(
    'uid', 760401,
    'groups', list('syrinx'),
    'comment', 'Everything is awesome',
    'homeDir', '/home/alex',
    'shell', '/bin/bash',
);
```
