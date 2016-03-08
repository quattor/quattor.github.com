---
layout: article
title: TextRender outside metaconfig
author: Stijn De Weirdt
category: documentation
---

# TextRender outside metaconfig

The 3rd part of this series deals with usage of `TextRender` in e.g.
components other than metaconfig or other perl modules.

Altough [metaconfig][metaconfig_blog] can handle most configuration work where
generating a configuration file combined with restarting/reloading/... a sysvinit/systemd
service is sufficient, there are still quite a lot of cases where more logic
or complicated action is required.

In these cases, a component or perl module is required. This was briefly touched upon
in the 1st part introducing [TextRender][textrender_blog].

This final part will go into more detail how to integrate the convenient way of
writing `Template::Toolkit` (TT) and unittests from `metaconfig`
with regular component development and testing.

[textrender_blog]: {% post_url 2015-09-20-textrender-basics %}
[metaconfig_blog]: {% post_url 2015-09-21-textrender-metaconfig %}

# metaconfig migration

The main idea is that TT files and unittests can be moved easily to or from metaconfig,
if such opportunity or necessity would arise.

This allows for development in 2 directions:

* towards metaconfig: existing components that could be replaced by `ncm-metaconfig`,
can be migrated to metaconfig-only using an intermediate step by handling the rendering
of the configuration file(s) with `TextRender` in the existing component,
and deprecating the component in a later phase.
It is even possible to develop metaconfig support in parallel with the existence of the
component. All TT files from metaconfig can be used by any component
(and the unittesting of these TT files is done as part of metaconfig),
but refactoring the schema is then also required.
* away from metaconfig: starting out with metaconfig can be a considerable effort.
However, if the need ever arises, developing a new component can be done by reusing almost
all this effort in a transparent way.

## Differences with metaconfig development

### location and packaging
Create the `ncm-mycomponent/src/main/resources` directory with the TT files and a `tests`
subdirectory to hold the TT unittest profiles and `RegexpTests`.

(This directory should not be confused with the `src/test/resources` directory, which holds e.g.
the pan templates for the perl unittests).

### pan schema and other templates
The location directory is the equivalent of the `ncm-metaconfig/src/main/metaconfig/myservice`
directory for a ncm-metaconfig service,
with the main exception that there is **no** `ncm-mycomponent/src/main/resources/pan` subdirectory.

There is no need to create a TT-specific schema, one has to use the components schema
(located in e.g. `ncm-mycomponent/src/main/pan/component/mycomponent/schema.pan`).

### packaging
In order to package the TT files as part of the component,
a 2 build plugins need to be added to the `pom.xml` under

```xml
  <build>
    <pluginManagement>
      <plugins>
```
      
The configuration of the plugins is
      
```xml
<plugin>
  <artifactId>maven-resources-plugin</artifactId>
  <version>2.4.3</version>
  <executions>
    <execution>
      <id>filter-tt-sources</id>
      <phase>process-sources</phase>
      <goals>
        <goal>copy-resources</goal>
      </goals>
      <configuration>
        <encoding>UTF-8</encoding>
        <outputDirectory>${project.build.directory}/share/templates/quattor/${project.artifactId}</outputDirectory>
        <resources>
          <resource>
            <directory>src/main/resources</directory>
            <filtering>false</filtering>
            <includes>
              <include>**/*.tt</include>
            </includes>
          </resource>
        </resources>
      </configuration>
    </execution>
  </executions>
</plugin>
<plugin>
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>rpm-maven-plugin</artifactId>
  <configuration>
    <mappings combine.children="append">
      <mapping>
        <directory>/usr/share/templates/</directory>
        <filemode>644</filemode>
        <username>root</username>
        <groupname>root</groupname>
        <sources>
          <source>
            <location>${project.build.directory}/share/templates/</location>
          </source>
        </sources>
        <directoryIncluded>false</directoryIncluded>
      </mapping>
    </mappings>
  </configuration>
</plugin>
```

(The `outputDirectory` has (part of) the `includepath` `/usr/share/templates/quattor` hardcoded;
one should never have to change the includepath either in the `pom.xml` or the perl
`TextRender->new()`).

### TT namespace

TT files used outside metaconfig should use their own namespace
and this should be the same as their `relpath`.
E.g. to include a TT file from the `mycomponent` namespace in a `main.tt`,
one has to use

```
[% INCLUDE 'mycomponent/element.tt` %]
```

and the relevant `TextRender` perl code has

```perl
my $trd = EDG::WP4::CCM::TextRender->new(
    'main',
    $config->getElelement($self->prefix()."/subtree"),
    relpath => 'mycomponent',
    log => $self,
    );
```

In metaconfig, the `relpath` is always `metaconfig`,
and the namespace is e.g. `metaconfig/myservice`,
the equivalent of the example above would be

```
[% INCLUDE 'metaconfig/myservice/element.tt' %]
```


### Error handling

`TextRender` **never** logs any error, it is left entirely to the consumer to handle any errors.
The failure reason is held in a `fail` attribute of the `TextRender` instance.

There are 2 main ways to detect failures (`$trd` is the TextRender instance):

* using the [get_text][objecttext_get_text] method explicitly, which returns `undef` in case of rendering failure

```perl
if(! defined($trd->get_text())) {
    $self->error("Rendering XYZ failed: $trd->{fail}.");
}
```

* using [filewriter][objecttext_filewriter] method (if you are going to write the contents to file).
This returns `undef` in case of rendering failure (and a vaild `CAF::FileWriter` instance otherwise).

```perl
my $fh = $trd->filewriter('/path/to/file');
if(defined($fh)) {
    my $changed = $fh->close();
} else {
    $self->error("Rendering XYZ failed: $trd->{fail}.");
}
```

(The `defined($fh)` is required, do not simply use `if($fh)` due to stringification
of `CAF::FileWriter`, as explained in the example below).

[objecttext_get_text]: http://docs-test-comps.readthedocs.org/en/latest/CAF/objecttext/#get_text
[objecttext_filewriter]: http://docs-test-comps.readthedocs.org/en/latest/CAF/objecttext/#filewriter

### TT perl unittest
A dedicated test module `Test::Quattor::TextRender::Component` exists to testing of
TT files outside metaconfig. It is advised to add a single perl unittests `01_tt.t`
under `ncm-mycomponent/src/test/perl`, with contents

```perl
use strict;
use warnings;

use Test::More;
use Test::Quattor::TextRender::Component;

my $t = Test::Quattor::TextRender::Component->new(
    component => 'mycomponent'
)->test();

done_testing();
```

This will look into `src/main/resources/tests` for profiles and RegexpTests.

### TextRender unittest profiles

The test profiles in `src/main/resources/tests/profiles`
are compiled with both the `template-library-core`
and the component `target/pan` directory in the panc include path,
which allows you to use e.g. the component schema
or other templates in the TT unittest profiles.

### RegexpTests flags

An important difference with `metaconfig` are the `RegexpTest` flags.
Because a metaconfig
service specifies the `module` and `contents` as part of the schema for each service,
a single `renderpath` flag is sufficient.

Outside metaconfig however, the module to be used is part of the components perl
code, and it can be very common that only a part of the full component schema
is used for rendering. Therefor the `renderpath` flag has lost almost
(if not all) of its functionality, and is typically just a (mandatory) placeholder flag
with value `/` (because a valid pan path is still required as the `renderpath`
by the test framework).

The module to be used can be set using the `rendermodule` flag
(and it precedes the default `<renderpath>/module` value).
Similar, the `contentspath` flag defines the contents to use to render
(and it precedes the default `<renderpath>/contents`).
The `Element` instance `$config->getElement('<contentspath>')`
is passed as the contents.

Be aware of subtle differences between
the tests that use the `Element` instance as contents,
and the actual component perl code that you might actually pass
e.g. `$config->getTree($panpath)` (which is a perl hashref,
and has by default no type information).
In general, one should never use `getTree` contents in `TextRender`;
and always use an `Element` instance via `getElement` (or a
self constructed perl hashref).

Any `element` options passed to `TextRender` in the perl code,
also have to be set via the `element` flag as a comma-separated list.

E.g. the flags for the [pan example from the 1st series][textrender_blog_panexample]

```
renderpath=/
rendermodule=pan
contentspath=/
element=truefalse,doublequote
```

[textrender_blog_panexample]: {% post_url 2015-09-20-textrender-basics %}#pan-format-example

### component perl unittests
Component perl unittests (other than the `01_tt.t` to test the TT files),
and that use the rendered text during the test, need to mock `TextRender`
so it is able to find the TT files in the unittest target directory.

Mocking `TextRender` for this purpose is as trivial as adding

```perl
use Test::Quattor::TextRender::Base;
my $caf_trd = mock_textrender();
```

before the actual testing is setup, i.e. early in the unittest file.

This is required because by default, `TextRender` looks for
TT files relative to the (absolute) includepath
`/usr/share/templates/quattor`, and the unittests would either not find the TT
files required to render, or pick up old/existing ones).

(Be aware that including TT from other components, including metaconfig,
during the unittests is not trivial, and outside the scope of this document.
If you want to achieve this, open an issue in the relevant github repository
to get help.)

# Example

We will have a look at snippets of [ncm-authconfig][ncm_authconfig] (based on `15.8` version).
This component manages the system authentication services, one of them is [SSSD][sssd].

`SSSD` itself has a relative simple configuration, and in case of any changes, restarting the `sssd`
daemon is sufficient. So it could be handled by `metaconfig` on it's own,
but it is part of `authconfig` component
because it has impact on the whole authentication system. In particular, enabling/disabling `SSSD`
is done with the `authconfig` tool (which involves a lot more than simply enabling/disabling the `sssd`
daemon).

[ncm_authconfig]: http://docs-test-comps.readthedocs.org/en/latest/components/authconfig/
[sssd]: https://fedorahosted.org/sssd/

## Component

The following files (relative from the `configuration-modules-core` base directory)
are relevant for this example:

* the component `authconfig.pm` itself
* the TT files and regexptests in `ncm-authconfig/src/main/resources`
* the perl TT unittest `01_tt.t`
* a perl unittest `configure-sssd.t`

```
ncm-authconfig/src/test/perl/01_tt.t
ncm-authconfig/src/test/perl/configure-sssd.t
ncm-authconfig/src/main/perl/authconfig.pm
ncm-authconfig/src/main/resources/domains/ldap.tt
ncm-authconfig/src/main/resources/generic.tt
ncm-authconfig/src/main/resources/sssd.tt
ncm-authconfig/src/main/resources/tests/profiles/generic.pan
ncm-authconfig/src/main/resources/tests/profiles/ldap.pan
ncm-authconfig/src/main/resources/tests/profiles/basic.pan
ncm-authconfig/src/main/resources/tests/regexps/ldap/value
ncm-authconfig/src/main/resources/tests/regexps/generic/value
ncm-authconfig/src/main/resources/tests/regexps/basic/value
```

### Configure

The main `Configure` method has (related to the `SSSD` configuration itself)

```perl
...

sub Configure
{
    my ($self, $config) = @_;

    my $t = $config->getElement("/software/components/authconfig")->getTree();

...

    if ($t->{method}->{sssd}->{enable}) {
        $restart ||= $self->configure_sssd($t->{method}->{sssd});
    }

...

```

The `ncm-authconfig` schema has a boolean for each supported authentication method.
If `sssd` is enabled, the `enable_sssd` method is called and
adds the relevant arguments to the `authconfig` commandline.
Clearly this kind of logic lies outside the scope of `metaconfig`, and using a dedicated
component is the only solution.

(This is legacy code, a better way to get the profile configuration is to use

```perl
my $t = $config->getTree($self->prefix());
```
)

### SSSD configuration generation

```perl
...
use EDG::WP4::CCM::TextRender;
...
use constant SSSD_FILE => '/etc/sssd/sssd.conf';
use constant SSSD_TT_MODULE => 'sssd';
...
sub configure_sssd
{
    my ($self, $config) = @_;

    my $trd = EDG::WP4::CCM::TextRender->new(
            SSSD_TT_MODULE,
            $config,
            relpath => 'authconfig',
            log => $self,
        );

    # can't be empty string, is at least '[sssd]'
    if ($trd) {
        my $fh = $trd->filewriter(SSSD_FILE, log => $self, mode => 0600);
        my $changed = $fh->close();

        if ($changed) {
            CAF::Process->new([qw(/sbin/service sssd restart)],
                              log => $self)->run();
            if ($?) {
                $self->error("Failed to restart SSSD");
            }
        }

        return $changed;
    } else {
        $self->error("Unable to render template sssd: $trd->{fail}");
        return;
    }
}

```

In the `sssd` example, the rendering error is catched via `if($trd)`,
which is possible only for 2 reasons:

* the rendered `sssd` configfile is never empty (it contains at the very least the `[sssd]`)
* the `TextRender` instance has overloaded stringification (i.e. `"$trd"` is the content
of the rendering) and stringification is a fallback for the boolean overload via
[magic autogeneration][perl_overload_magic]. The `TextRender` stringification **always** produces a
string (even in case of rendering failure).
So when perl evaluates the `TextRender` instance in boolean context (due to the `if()`),
it will look for an overloaded `bool` first (which doesn't exist), and then evaluate the boolean value
following the fallbacks, of which stringification exists. An empty string is false in boolean context,
anything else it true.

(`CAF::FileWriter` also has auto stringification, and this is why `if(defined($fh))`
is required to correctly detect rendering errors when using `$trd->filewriter`.)

[perl_overload_magic]: http://perldoc.perl.org/overload.html#Magic-Autogeneration

(More legacy code:

* using `constant` for constants is discouraged,
we should switch to `Readonly`, in which case the code above becomes

```perl
...
use Readonly;

...

Readonly my $SSSD_FILE => '/etc/sssd/sssd.conf';

...
    my $fh = $trd->filewriter($SSSD_FILE, log => $self, mode => 0600);
...

```

* the restart should be handled by `CAF::Service` as follows

```perl
            CAF::Service->new(['sssd'], log => $self)->restart();
            if ($?) {
                $self->error("Failed to restart SSSD");
            }
```
)

### TT files

The configuration of `SSSD` is in `.ini` format, but `sssd` has a finer
substructue than what the builtin `tiny` module allows. This allows for
a detailed schema, which requires TT rendering.

The main `sssd.tt` TT file looks as follows

```
[sssd]
domains = [% domains.keys.join(',') %]

[% INCLUDE authconfig/generic.tt dict=global list=['services'] bool=["try_inotify"] %]
[pam]
[% INCLUDE authconfig/generic.tt dict=pam %]
[nss]
[% INCLUDE authconfig/generic.tt dict=nss bool=["filter_users_in_groups"] %]

[% FOREACH d IN domains.pairs -%]
[domain/[% d.key %]]
[%  FOREACH pair IN d.value.pairs -%]
[%-      SWITCH pair.key -%]
[%-          CASE ['local'] -%]
[%              INCLUDE "authconfig/generic.tt" dict=pair.value bool=["create_homedir", "remove_homedir"] %]
[%-          CASE ['simple'] -%]
[%              INCLUDE "authconfig/generic.tt" dict=pair.value prefix="${pair.key}_"
                                                list=['allow_users','deny_users','allow_groups','deny_groups'] %]
[%-          CASE ['ldap'] -%]
[%              INCLUDE "authconfig/domains/${pair.key}.tt" desc=pair.value %]
[%      END -%]
[%- END -%]
[% INCLUDE authconfig/generic.tt dict=d.value exclude=['ldap','local','simple']
                                 bool=["case_sensitive", "proxy_fast_alias", "enumerate", "cache_credentials"] %]
[%- END %]
```

(More legacy code: can probably be simplified a lot using e.g.
the type information if an element instance is passed).

### TT unittests

An example of a `RegexpTest` looks like

```
Value based regexp test
---
//software
rendermodule=sssd
contentspath=/software/components/authconfig/method/sssd
---
^\[sssd\]$
^domains = test1$
^config_file_version = 2$
^debug_level = 528$
^reconnection_retries = 3$
```

The `TextRender` module is set to `sssd`.
Only the profile information in `/software/components/authconfig/method/sssd` is relevant
and is passed as `contentspath`.

The corresponding perl unittest `01_tt.t` is

```perl
use strict;
use warnings;

use Test::More;
use Test::Quattor::TextRender::Component;

my $t = Test::Quattor::TextRender::Component->new(
    component => 'authconfig'
)->test();

done_testing();
```

### Perl unittests

There is a regular perl unittest to test the logic in `configure_sssd` method, e.g.
test if a the `sssd` daemon is restarted via `CAF::Service`.

```perl
...
use NCM::Component::authconfig;
use Test::MockModule;
use Test::Quattor::TextRender::Base;
...
my $caf_trd = mock_textrender();
my $close_return;
...
my $mock = Test::MockModule->new("CAF::FileWriter");

$mock->mock("close", sub {
   my ($self) = @_;
   return $close_return;
   });

my $cmp = NCM::Component::authconfig->new("authconfig");

$close_return = 1;
ok($cmp->configure_sssd({}), "First call changes something");
my $fh = get_file($SSSD_FILE);
isa_ok($fh, "CAF::FileWriter", "File was opened");
is(*$fh->{options}->{mode}, 0600, "File has correct permissions");
my $cmd = get_command($RESTART_CMD);
ok($cmd, "Daemon was restarted");
ok(!$cmp->{ERROR}, "No errors reported in basic execution");

set_command_status($RESTART_CMD, 1);
$cmp->configure_sssd({});
is($cmp->{ERROR}, 1, "Errors reported when the restart fails");
set_command_status($RESTART_CMD, 0);

$close_return = 0;
# Barfs due to no hashref or element instance
$cmp->configure_sssd(undef);
is($cmp->{ERROR}, 2, "Error while rendering the template is reported");
...
```

These unittests focus on the logic of the method instead of the rendered text:

* in the first test, the file returns a forced change,
and it is checked that this results in a call to the service restart command.
* the second test mocks a failed service restart, and it is verified that an error is logged
in that case.
* the third test verifies that an error is logged when `TextRender` fails

A `FileWriter` instance has a `close` method, that returns if the file
has changed or not. In this unittest, the `close` method is mocked to return the value
of the `$close_return` variable. This makes it very easy to mimic the behaviour of
the component.

Details of the `Test::Quattor` testsuite are beyond the scope of this document,
but following bits help to understand the internals:

* both `CAF::FileWriter` and `CAF::Process` are mocked by the `use Test::Quattor` call.
This results in easy methods to access the created `CAF::FileWriter` and `CAF::Process` instances
via `get_file` and `get_command`, respectively. There also exists methods to set e.g.
the exitcode of a `CAF::Process` instance via `set_command_status`.
* the `$cmp->{ERRORS}` (and similar `$cmp->{WARNINGS}`) counter exists
for any regular component instance, see the `Component` documentation.
It keeps track of the number of times an error was logged.
In the test environment however, the `Test::Quattor::Component` class
is used instead of real `NCM::Component`, and this test class has a counter for each log action
(e.g. `->{INFO}` keeps track of the number of times
an `->info()` log action was called).
This is a bit confusing and will be streamlined in a new release of the test tools.


TODO:

 * are link to the `Test::Quattor` documentation once added to the documentation generation.
 * add link to `Component` documentation as part of `ncm-ncd`
