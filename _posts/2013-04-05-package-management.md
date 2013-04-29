---
layout: article
title: Installing and removing packages with Quattor
category: review
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
"/software/packages/{perl-JSON}" = nlist();
```

With this, we tell the package manager that we want `perl-JSON`
installed.  We don't care about the version or architecture.  We let
Yum decide that for us.  Also, if we trust Yum for choosing the
correct dependencies, we don't need to specify anything more.

Imagine we wanted to install `perl-JSON` version 1.2.3, only in its
x86_64 architecture.  The `pkg_repl` function is the preferred way to
declare that:

```
"/software/packages" = pkg_repl("perl-JSON", "1.2.3", "x86_64");
```

Again, Yum will take care of the dependencies, and will lock only the
version of `perl-JSON`.

### Complicated layouts

Imagine our code base is terribly complicated, and some templates
might have declared a specific version for `perl-JSON`, while others
just don't care.  The templates that care about the version have used
the `pkg_repl` form above.

Templates that don't care will probably use the `?=` operator for the
assignment:

```
"/software/packages/{perl-JSON}" ?= nlist();
```

**TODO:** What does `pkg_repl("perl-JSON")` actually do?

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
"/software/packages/{openldap-devel}" = nlist();
```

Now we are sure that we'll get the correct version.

### Deleting a package ###

Just remove its entry from the profile:

```
"/software/packages/{perl-JSON}" = null;
```

this will make the backend remove `perl-JSON` only if it's safe to do
so.  That is, if no other package in the profile depends on it.

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

We still can do more things with Yum.  This is an
