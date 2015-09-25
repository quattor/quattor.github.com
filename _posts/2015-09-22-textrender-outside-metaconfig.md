---
layout: article
title: TextRender outside metaconfig
author: Stijn De Weirdt
category: blog
---

# TextRender outside metaconfig

The 3rd part of this series deals with usage of `TextRender` in e.g.
components other than metaconfig or other perl modules.

[Metaconfig][metaconfig_blog] can handle most configuration work where
generating a configuration file combined with restarting/reloading/... a sysvinit/systemd
service is sufficient, there are still quite a lot of cases where more logic
 or complicated action handling is required.

In these cases, a component or more general perl module is required. This was briefly touched upon
in the 1st part introducing [TextRender][textrender_blog].

This final part will go into more detail how to integrate the convenient way of writing `Template::Toolkit`
(TT for short) and unittests from `metaconfig` with regular component development and testing.

[textrender_blog]: http://quattor.github.io/blog/2015/09/20/textrender-basics.html
[metaconfig_blog]: http://quattor.github.io/blog/2015/09/21/textrender-metaconfig.html

# metaconfig migration

The main idea is that TT files and unittests can be moved easily to or from metaconfig,
if such opportunity or necessity would arise.

This allows for development in 2 directions:
* towards metaconfig: existing components that could be replaced by `ncm-metaconfig` usage,
can be migrated to metaconfig-only using an intermediate step by handling the rendering
of the configuration file(s) with `TextRender` in the existing component,
and deprecating the component in a later phase.
It is even possible to develop metaconfig support in parallel with the existence of the
component. All TT files from metaconfig can be used by any component (and the unittesting of these
TT files is done as part of metaconfig),
but refactoring the schema is then also required.
* away from metaconfig: starting out with metaconfig can be a considerable effort,
but, if the need ever arises, developing a new component can be done by reusing almost
all this effort in a transparent way.

## Differences with metaconfig development

### location and packaging
Create the `ncm-mycomponent/src/main/resources` directory and  with the TT files and a `tests`
subdirectory to hold the TT unittest profiles and `RegexpTests`.

(This directory should not be confused with the `src/test/resources` directory, which holds e.g.
the pan templates for the perl unittests).

### pan schema and other templates
The location directory is the equivalent of the `ncm-metaconfig/src/main/metaconfig/myservice`
directory for a ncm-metaconfig service,
with the main exception that there is **no** `ncm-mycomponent/src/main/resources/pan` subdirectory.

There is no need to create a TT-specific schema, one has to use the components schema
(located in e.g. `ncm-mycomponent/src/main/pan/component/mycomponent/schema.pan`)

### packaging
In order to package the TT files as part of the component,
a new build plugin needs to be added to the `pom.xml` under
```
  <build>
    <pluginManagement>
      <plugins>
```
The configuration of the plugin is 
```
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
```

(The `outputDirectory` has (part of) the `includepath` `/usr/share/templates/quattor` hardcoded;
one should never have to change the includepath either in the `pom.xml` or the perl `TextRender`
invocation).

### TT namespace

TT files used outside metaconfig should use their own namespace
and this should be the same as their `relpath`.
E.g. to include a TT file from this namespace in a `main.tt`,
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

(In metaconfig, the `relpath` is always `metaconfig`,
and the namespace is e.g. `metaconfig/myservice`)


### TT perl unittest:
A dedicated test module `Test::Quattor::TextRender::Component` exists to testing of
TT files outside metaconfig. It is advised to add a single perl unittests `01_tt.t`
under `ncm-mycomponent/src/test/perl`, with contents

```perl
use strict;
use warnings;

use Test::More;
use Test::Quattor::TextRender::Component;

my $t = Test::Quattor::TextRender::Component->new(
    component => 'mycomponent')->test();

done_testing();
```

This will look into `src/main/resources/tests` for profiles and RegexpTests.

### TextRender unittest profiles

The test profiles are compiled with both the `template-library-core`
and the component `target/pan` directory included, which allows you
to use e.g. the component schema or other templates in the TT unittest profiles.

### RegexpTests flags

A main difference with `metaconfig` are the `RegexpTest` flags. Because a metaconfig
service specifies the `module` and `contents` as part of the schema for each service,
a single `renderpath` is sufficient.

Outside metaconfig however, the module to be used is part of the components perl
code, and it can be very common that only a part of the full component schema
is used for rendering. Therefor the `renderpath` flag has lost almost
(if not all) of its functionality, and is typically just a (mandatory) placeholder flag
with value `/` (because a valid pan path is still required by the test framework).

The module to be used can be specified (and it precedes the default `<renderpath>/module`
value) via the `rendermodule` flag.
Similar, the `contentspath` flag defines the contents to use to render (and it precedes
the default '<renderpath>/contents').
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
also have to be passed set via the `element` flag as a comma-separated list.

E.g. the flags for the [pan example from the 1st series][textrender_blog_panexample]
```
renderpath=/
rendermodule=pan
contentspath=/
element=truefalse,doublequote
```

[textrender_blog_panexample]: http://quattor.github.io/blog/2015/09/20/textrender-basics.html#pan-format-example

### component perl unittests
Component perl unittests (other than the `01_tt.t` to test the TT files themself),
and that use the rendered text for during the test, need to mock `TextRender`
so it is able to find the TT files in the unittest target directory.

Mocking `TextRender` for this purpose is as trivial as adding 
```perl
use Test::Quattor::TextRender::Base;
my $caf_trd = mock_textrender();
```
early in the unittest file, i.e. before the actual testing is setup.

This is required because by default, `TextRender` looks for
TT files relative to the (absolute) includepath
`/usr/share/templates/quattor`, and the unittests would either not find the TT
files required to render, or pick up old/existing ones).

(Be aware that including TT from other components, including metaconfig,
during the unittests is not trivial, and outside the scope of this document.
If you want to achieve this, open an issue in the relevant github repository
to get help.)

# Example
