---
layout: article
title: Components Spring 2017 Cleaning
author: Stijn De Weirdt
category: documentation
---

# Goal

With the advent of build-tools version 1.52,
some code cleanup and refactoring is recommended.

This document explains how to cleanup the components;
the cleanup of the other core modules is not handled.

The minimal requirement is to bump `build-tools` in `pom.xml`
to at least 1.52 (under `/project/parent/version`) unsing

    mvn versions:update-parent

# Warnings fail tests

A warning raised during tests will make the test fail.
It is also recommended that all perl unit tests (the `.t` files in `src/test/perl`)
have following header (and no perl shebang):

    use strict;
    use warnings;


# 00-tqu

We introduce a new basic perl unit test called `00-tqu.t` referring to
the usage of the [`Test::Quattor::Unittest`][tqu] module.

Adding it is easy:

    echo 'use Test::Quattor::Unittest;' > src/test/perl/00-tqu.t

If the component has no dedicated `.pod` file(s)
(i.e. when all pod information is inline with the perl module),
you need to use

    echo 'use Test::Quattor::Unittest qw(nopod);' > src/test/perl/00-tqu.t

The unit tests replaces a number of (posisble) existsing tests that can be removed

1. `00-load`: basic load test. Typically (and by default), only the component module is loaded
2. `pod-syntax`: basic pod syntax test.
3. `00-tt`: when relevant, the TT unit test is replaced (looks for existence of `src/main/resources`)

It also adds a `critic` test and a `perltidy` test. (For now, the `perltidy` test always passes).

[tqu]: http://quattor-documentation.readthedocs.io/en/latest/Unittesting/Quattor::Unittest/

# Perl module cleanup

## Header
Replace header with maven template

    #${PMcomponent}

For comonents with their own namespace, use PMpre/post header
(space after `PMpre` is required)

    #${PMpre} NCM::Component::<namespace::modulename>${PMpost}

## Unused and duplicate code

Remove unused / duplicate code

 * header above includes `use strict` and `use warnings`
 * check for unused CCM modules
  * `CCM::Element` by default imports `unescape`, so check for its usage before removing

## Parenting
Replace old parenting construct `@ISA` with `use parent`, e.g.

    use NCM::Component;
    our @ISA = qw(NCM::Component);

with

    use parent qw(NCM::Component);

## CCM (un)escape
The CCM functions `escape` and/or `unescape`
have to be imported from `EDG::WP4::CCM::Path`
(instead of `CCM::Element`).


## Other changes
 * whitespace changes: switch to 4-space indent
 * for any other fixes/cleanup/refactor, ideally use other PR or at least separate commit to fix them

# Pan cleanup

## Remove legacy templates
No more `-common.pan` and / or `-rpms.pan`;
most components only have `config.pan` and `schema.pan`.
Make sure to double-check their content
so any non-standard definitions are added in the new `config.pan`

## `config.pan`
Start with the config header the maven template `${componentconfig}`.
This maven template includes the schema and the bind to `/software/components` and
adds the component as a versioned package to `/software/packages`.

It also generates pan component code with a prefix.
All values are set as default values, so they can be changed if needed.

`spma` is the only predependency and last entry in the maven template.
If you don't want this dependency or require others, you can use another
maven template `${componentconfignospma}` to avoid the spma-predependency.
(It is the only difference with `${componentconfig}`).

Most components will only have the maven template for the whole `config.pan`.

## `schema.pan`
Replace header (including `declaration template ...`) with `${componentschema}`

Try to get rid of `include 'quattor/schema';`.
Components typically only requires `include 'quattor/types/component';`.

Remove any `bind` stement (typically at the end)
and rename the main component type to `${project.artifactId}_component`
(this is the type used in by the bind in `config.pan`).

## Add a unittest
Check if there is a perl unit test that tests `config.pan`.

Look for an object template in `src/test/resources` that includes `config.pan` and
a perl unit test in `src/test/perl`
that has `use Test::Quattor qw(<unittestobjecttemplate>);`

If not, look for an object template that is used in a perl unittest
and add:

     function pkg_repl = { null; };
     include 'components/<componentname>/config';
     '/software/components/<componentname>/dependencies' = null;
