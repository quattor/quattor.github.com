---
layout: article
title: Installing and removing packages with Quattor
category: documentation
image: img/quattor-logo.png
---

We describe here the basic Pan statements and data structures for
installing, removing and upgrading software packages.  Other documents
describe the implementation and the client-side details.  We focus now
on the user-visible interface: the Pan code.

## Package management

### Installing a package ###

In their simplest version, we may install a package by just creating
an empty entry under `/software/packages`:

```
"/software/packages/{perl-JSON}" ?= nlist();
```

With this, we tell the package manager that we want `perl-JSON`
installed. Note that the curly braces are mandatory as package names
can contain characters that must be escaped in the PAN syntax.
We don't care about the version or architecture (yum will determine
that for us) and the use of conditional assignment (?=) ensures that
any existing, more specific setting is not over-written.
Also, if we trust Yum for choosing the correct dependencies, we don't
need to specify anything more.

To specify particular versions and/or architectures, the simplest way
to declare that is to use a function. Imagine we wanted to install
`perl-JSON` version 1.2.3, only in its x86_64 architecture.
The `pkg_repl` function is the preferred way to declare that:

```
"/software/packages" = pkg_repl("perl-JSON", "1.2.3", "x86_64");
```

Note that the package name must be passed to pkg_repl _unescaped_.
Again, Yum will take care of the dependencies, and will lock only the
version of `perl-JSON`.

If you prefer you can specify all packages using functions, see the section
[Helper functions for package management](#helper-functions-for-package-management).

### Keeping a family of packages at the same version ###

The `pkg_repl` form accepts wildcards, and may be used for ensuring
some packages move together.  For instance, a package and its
libraries, the kernel and many modules...

```
"/software/packages" = pkg_repl("openldap*", "2.6.24", "x86_64");
```

This will ensure that any packages matching `openldap` will be kept to
version 2.6.24, if such a version exists.  Now we can keep `openldap`,
`openldap-client`, `openldap-servers` and `openldap-devel` in line!

The above statement will only install `openldap` and its dependencies.
If we want to install `openldap-devel` we still have to declare it:

```
"/software/packages/{openldap-devel}" ?= nlist();
```

Now we are sure that we'll get the correct version.

### Deleting a package ###

Just remove its entry from the profile:

```
"/software/packages/{perl-JSON}" = null;
```

this will make the backend remove `perl-JSON` only if no other package
in the profile depends on it.

## Repository management

The `/software/repositories` is a **list** of repositories.  Each
entry may declare:

* `name`: repository name
* `owner`: a contact person or e-mail address
* `priority`: an integer between 1 and 99. Defaults to 99.  The lower
  the number the more priority the repository has.
* `enabled`: a boolean indicating whether the repository should be
  enabled or not.  Defaults to true.
* `gpgcheck`: whether to check the GPG signature of the packages that
  come from this repository.  Defaults to false.
* `includepkgs`: list of packages authorised from this repository.  If
  present, only packages in this list may be taken from this
  repository.  Wildcards are allowed in this field.
* `excludepkgs`: list of packages  from this repository that are
  banned.  If present, no package from this list will be taken from
  this repository.  Wildcards are allowed in this field.
* `skip_if_unavailable`: whether Yum (and thus SPMA) should fail if it
  cannot access this repository.  Defaults to false.  Use with
  caution, or network glitches may remove software you truly want!
* `protocols`: list of ways to access this repository.  In the new
  SPMA it should contain only one entry, with the following data
  structure:
  * `name`: protocol name.  Unused currently.
  * `url`: URL where the repository is located.  Maps to Yum's
    `baseurl`.
  * `cacert`: If the repository is to be accessed over HTTPS, path to
    the CA certificates.
  * `clientkey`: if the repository is to be accessed over HTTPS, path
    to the client's private key.
  * `clientcert`: if the repository is to be accessed over HTTPS, path
    to the client's certificate.
  * `verify`: if the repository is to be accessed over HTTPS, whether
    or not verify the server's certificate..

Yum can do even more than this.  We'll add support for more features
as their need arises.

## Helper functions for package management

There are several functions to help with complex package
manipulations.  The `components/spma/functions` template contains
their full descriptions.  We list here the simplest (and most
frequent) uses.

They all take the following form:

```
"/software/packages" = pkg_<op>("package-name", "package-version",
    "architecture", list("flags"));
```

where only the package name is mandatory. Each function also takes
care of escaping the package name for you.


### pkg_del

Deletes a package from the profile.  In most cases this is equivalent to

```
"/software/packages/{a-package}" = null;
```

This function allows to remove only one **version** or
**architecture** of such a package, while preserving all others.

Given the way we can now simplify our Pan code, the use of this
function is probably a
[code smell](https://en.wikipedia.org/wiki/Code_smell).

### pkg_add

Adds a package to the profile, raising an error if it was already
defined.  You usually prefer `pkg_repl`, which is idempotent.

### pkg_repl

Adds a package to the profile.  Typically, it replaces any other
versions of this package.

If given the `multi` flag, versions already defined in the profile are
preserved.  This is useful if you need to declare multiple kernel
versions, for instance.

### pkg_ronly

If the package given as an argument exists in the profile, replaces
its version and/or architecture.  It doesn't add or remove any
packages.
