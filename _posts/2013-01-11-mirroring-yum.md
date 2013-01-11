---
layout: article
title: Mirroring the Quattor Yum repositories
category: documentation
---

Since Quattor 12.12 we have an
[official Yum repository](http://yum.quattor.org).  These are the
steps to mirror it:

## Declare a Yum repository in your software server

This is either your Quattor server, or your `swrep` server if you have
them separated.  Add the following file:

    [quattor-upstream]
    enabled=0
    baseurl=http://yum.quattor.org/12.12/
    gpgcheck=0

to your /etc/yum.repos.d .

## Run the mirroring

We recommend using `reposync`.  Just do:

```
$ reposync -p /path/to/repo/path -r quattor-upstream
```

And that's it!

## Getting updates

For now, we won't produce any _errata_ updates.  Instead we'll release
often.

So, you'll have to update the `baseurl` in your repository to the
release you want to mirror.
