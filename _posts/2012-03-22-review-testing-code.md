---
layout: article
title: Testing Quattor code
category: blog
pygments: true
image: img/quattor-logo.png
---

Developers willing more information on how to write their tests,
please click [here](https://trac.lal.in2p3.fr/Quattor/wiki/Development/TestingComponents)

## Testing Quattor code with the new build tools

For running the automated test suite of a module, you will need:

1. A checkout of perl-LC and perl-CAF, since they are not in CPAN.
1. Set up `PERL5LIB` environment variable so that the Perl interpreter
   is able to find LC and CAF modules. If it is not set, Maven will
   skip all tests.

Afterwards, just run

	mvn test

The test phase is usually executed before the package one. So, if you
have set `PERL5LIB`, running

	mvn package

will execute all tests before actually creating the packages. If a
test fails, Maven will refuse to create the packages. You can find a
detailed summary in JUnit-friendly format in the junit_output.xml
file.

Finally, you may disable the tests if your `PERL5LIB` doesn't provide LC
or CAF. Just do pass `-P!module-test` to the mvn command:

	mvn '-P!module-test' package
