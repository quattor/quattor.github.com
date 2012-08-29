---
layout: article
title: Testing Quattor code
category: documentation
pygments: true
image: img/quattor-logo.png
---

Developers seeking more information on how to write their tests,
please click
[here](https://trac.lal.in2p3.fr/Quattor/wiki/Development/TestingComponents)

## Testing Quattor code with the new build tools

For running the automated test suite of a Quattor module, you will
need:

1. A checkout of perl-LC, perl-CAF, CCM and ncm-ncd, since they are
   not in the standard library.
1. Set up `PERL5LIB` environment variable so that the Perl interpreter
   is able to find LC, CAF, CCM and NCM modules. If it is not set,
   Maven will skip all tests.

Afterwards, just run

	mvn test

from the top-leve directory, of from the component's subdirectory if
you are testing a single NCM component.

You can find a JUnit-friendly summary in the junit_output.xml file.

### Testing before packaging

The test phase is executed before the package one. So, if you have set
`PERL5LIB`, running

	mvn package

will execute all tests before actually creating the packages. If a
test fails Maven will refuse to create the packages.

### Disabling tests

Finally, you may disable the tests if you don't want to alter your
existing `PERL5LIB`. Just do pass `-P!module-test` to the mvn command:

	mvn '-P!module-test' package

### More details

If you are interested in coverage reports or other gory details, please check the [developers testing documentation](https://trac.lal.in2p3.fr/Quattor/wiki/Development/TestingComponents)

### CPAN dependencies

Some tests may depend on additional Perl modules. An example would be
`Test::Deep`, which simplifies the validation of complex data
structures.

Such modules are always available from CPAN, or in your distribution's
packages.
