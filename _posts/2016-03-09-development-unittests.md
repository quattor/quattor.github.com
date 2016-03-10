---
layout: article
title: Quattor development unittests
author: Stijn De Weirdt
category: documentation
---

[devel_basics]: {% post_url 2016-03-08-development-basics %}

# Running the tests

All quattor projects have unittests. These are run via the `mvn test` command, and run the perl
unittests under the `src/test/perl` subdirectory.

Maven runs the tests via `prove` (the commandline tool from `TAP::Harness`), and the required
include paths are already set, except for any dependencies.

`prove` only runs files with a `.t` suffix; any other files are ignored. This allows you to create
any helper modules for the unittests themself under the `src/test/perl` directory (`src/test/perl`
is added to the perl `@INC` via the `prove` commandline).

The tests run the modules that are preprocessed by `mvn` in the `target/lib/perl` directory.
The preprocessing does e.g. the templating of the `${author}`. It also means that any perl messages
that have a line number in them, are from the templated files (so there's some offset to take into account).

If you want to run a single unittest, add `-Dunittest=name_of_test.t` to the `mvn` commandline.

## Logging

If you want more logging, you can set `-Dprove.args=-v` (the `verbose` flag of `prove`)

TODO: document the QUATTOR_TEST_ variables

## Wrapper scripts

TODO: document / distribute [bash_functions][mvn_bash_functions]
[mvn_bash_functions]: https://github.com/quattor/quattor.github.com/issues/146#issuecomment-144681288

## mvnprove.pl

TODO: run the unittests without maven adn using `-d` for logging control and support more than one selected unittest

# Dependencies

The main issue with the unittests is the large number of dependencies that are required by all the various
repositories.

Basic non-perl:

 * `maven`
 * `panc` (`>= 10.2`)

Optional non-perl:

 * `rpm-build` (for building rpms)

Perl dependencies:

 * number of quattor tools (`LC`, `CAF`, `CCM`)
 * perl modules required for runtime
 * perl modules required for testing

The quattor test framework `Test::Quattor` is controlled through maven
(this is the `build-profile` in the `pom.xml`).

TODO: add list from `build_all_repos`

*Note:* If your development environment is managed by Quattor, you can use the [quattor-development][template_qt_dev]
to add all required dependencies

[template_qt_dev]: https://github.com/quattor/template-library-os/blob/sl6.x-x86_64/rpms/quattor-development.pan

## Bootstrap yum-based system

The [`build_all_repos`][build_all_repos] script tries to build all rpms for most quattor repositories.
Repositories that are not build include `panc` and the template repositories.

One of it's features is that it resolves (or tries to) all dependencies (currenlty) using `yum`.
(`sudo` rights are required for `yum` and `repoquery`; it is __NOT__ recommended to run this as root)
Perl dependencies that can't be installed via yum, are installed from `CPAN` (using `cpanm`).

As it runs all unittests, the result of running the script is an environment where you can start developing.

By default, `build_all_repos` installs everything in a `quattordev` subdirectory, and has subdirectories

 * `repos` all the quattor git repos, with the remote `upstream` set.
  * you need to add your fork as the remote `origin`.
 * `install` contains the quattor repositories from unpacked tarballs and any dependencies installed via `CPAN`
 * `rpms` contains all build rpms
 * a number of logfiles with e.g. the installed dependencies

Running the script takes a while to complete. Best run it in a `screen` session and redirect the output to a logfile.
(Best to check the `sudo` command upfront, as it can prompt for passsword, and thus block the script).

TODO: check the sudo timeout (a.k.a when do the credentials expire).

TODO: use the `source $DEST/env.sh` to set initial PERL5LIB

[build_all_repos]: https://raw.githubusercontent.com/quattor/release/master/src/scripts/build_all_repos.sh

# Writing perl unittests

## Test::More

The basic test module

 * `ok($bool, "message");` tests if `$bool` is true
  * use `ok(! $bool, "message");` to test if `$bool` is false
 * `is($a, $value, "message")` tests if `$a` is `$value`
  * for comparing hash and array, use `is_deeply` to compare references
   * `is_deeply(\%hash, {expected => 'value'}, "message");`
   * `is_deeply(\@array, [qw(value1 value2)], "message");`
 * `isa_ok($instance, "Instance::Class::Name", "message")`  tests if `$instance` is an instance of class `Instance::Class::Name`
 * `like("text", qr{regexp}, "message");` tests if `"text"` matches the compiled regular rexpression `qr{regexp}`
  * complex texts can be tested with `Test::Quattor::RegexpTest` TODO add reference

## Test::MockModule

You can mock almost any module using `Test::MockModule` including the code you are working on.

E.g. by defining

```perl
my $mock = Test::MockModule->new('NCM::Component::mycomponent');
$mock->mock('do_something', sub () {return [qw(1 2 3)]} );
``

you have mocked the `do_something` method of the `mycomponent` component.

If you then initialise the component, any calls to the `do_something` method will
return the reference to the arrayref `[1, 2, 3]`.

`Test::Quattor` provides a mocked version of a number of `CAF` modules and their methods,
there is typically no need to not mock these yourself.

Caveat: there are a few perl builtins that can't be mocked, esp. tests like `-f $filename`.
TODO: `CAF::Check` will address all this
If you want to test and mock this sort of calls, it is best if you define a short private method in your code like

```perl
sub _test_file {
    my ($self, $filename) = @_;
    return -f $filename;
}
```

and use `$self->_test_file($some_file)` in the code. This can then be mocked as e.g.

```perl
my $mock = Test::MockModule->new('NCM::Component::myothercomponent');
$mock->mock('_test_file', sub () {
    my ($self,$fn) = @_;
    my $ans = 0; # does not exist
    if ($fn eq "/some/path") {
        # more logic
        $ans = 1;
    }
    return $ans;
}
```

# Test::Quattor

Quattor has it's own set of methods to help testing and mocking called [`Test::Quattor`][maven_tools_test_quattor_docs].

[maven_tools_test_quattor_docs]: http://docs-test-maven-tools.readthedocs.org/en/latest/maven-tools/Quattor/

## Compiled profiles

To test using a profile, you create the object template under `src/test/resources` (e.g. `src/test/resources/foo.pan`).

In the test, you then prepare a compiled and ready-to-use `EDG::WP4::CCM::Configuration` instance during the load of `Test::Quattor`

```perl
use Test::Quattor qw(foo);
```

and to get the configuration instance you then do

```perl
my $cfg = get_config_for_profile('foo');
```

e.g. to be used

```perl
use Test::Quattor qw(foo);
use NCM::Component::mycomponent;
my $cmp = NCM::Component::mycomponent->new('mycomponent');
my $cfg = get_config_for_profile('foo');
$cmp->Configure($cfg);
ok(!exists($cmp->{ERROR}), "Configure succeeds with any error logged");
```

All methods of `Test::Quattor` are exported, so no need to use the load for that (in fact, you can't use load for that).

Caveat: reusing the object template for different tests can lead to race conditions (and thus failures),
try to use unique profiles to avoid this buggy behaviour.

### CAF::Process

 * `set_command_status`, `set_desired_output`, `set_desired_err` mock the status, stdout and stderr of future `CAF::Process` call

```perl
set_desired_output("/usr/bin/command", "expected output");
```

 * `get_command` use to test if a  `CAF::Process` with exact commandline was called (and returns the `CAF::Process` instance).

```perl
ok(get_command("/usr/bin/someexecutable -l -s"), "Command was called");
```
   or if you need to access the instance

```perl
my $procinstance = get_command("/usr/bin/someexecutable -l -s");
```

 * `command_history_ok`, `command_history_reset` test ordered execution of `CAF::Process` instances

```perl
command_history_reset();
ok(command_history_ok(['pattern1','pattern2']), "message");
```

* additional logging environment variables
  * `QUATTOR_TEST_LOG_CMD=1` log each command that is run via CAF::Process
  * `QUATTOR_TEST_LOG_CMD_MISSING=1` reports that a process wanted output but non was set via the
    `set_desired_output`

### CAF::FileWriter (Editor,Reader)

 * `get_file` returns the instance that opened/modified a file

```perl
my $fh = get_file("/some/path");
```

 * `set_file_contents` set the content a future `CAF::File*` instance will see

```perl
set_file_contents("/some/path", $text);
```

 * `set_caf_file_close_diff` mock the `CAF::File*->close()` return behaviour to return a true value if the content changed.
   By default, this is false, and `close()` will return some garbage.

```perl
set_caf_file_close_diff(1);
```

TODO: why is this not default true?
