---
layout: article
title: Best Practices for Contributing to the QWG Library
author: Michel Jouvin
menu: Template Library
---

[template_lib_intro]: /template_library/00-introduction.html
[quattor_rtd_documentation]: http://quattor-documentation.readthedocs.io/en/latest
[pan_book]: https://quattor-pan.readthedocs.io/en/latest/
[get_tl]: /template_library/get_tl.html

The [Template Library][template_lib_intro] is a set of templates covering various aspect
of a host configuration that are intended to be used without modification by every site
which needs to configure a given service. Site customization is made by defining variables
that are used as input by the templates in the template library. The template library
is part of the Quattor release.

## Machine types, Personalities and Features

The template library can be used both with SCDB and Aquilon configuration datastores
but some parts of the template library are used only in the SCDB context to provide the
services provided by Aquilon databases. This is particularly the case for everything
in the `machine-types` and `personality` namespaces.

- `personality` namespace in the template library is roughly the equivalent of a *personality*
in the Aquilon context: it is made of a set of *features* defined in the `features`
namespace. The main difference is that inclusion of features in a template library personality
is ordered when the order is not guaranteed in Aquilon.

- `machine-types` namespace in the template library is the association of a hardware,
an OS version/configuration (including the network configuration)and one or more personalities.
It implements what is done with the Aquilon commands to define a host configuration.

The main part of the template library developments occurs in the `features` namespace
and in the `personality` namespace if SCDB support is needed. For both namespaces,
one sub-namespace (directory) is created for each feature or personality.

## Template names

There are a few conventions about template names:

- `features`: the main template describing the configuration must be
called `config.pan`. The configuration part related to required packages
is generally put in a separate template, called `rpms.pan`, included by
`config.pan`.

- `personality`: depending on the complexity, the main template is called
  `service.pan` or `config.pan`. The idea behind having a separate `service.pan`
  and `config.pan` is that the configuration is broken between the inclusion
  of features (`service.pan`) and some actions specific to the personality
  (feature-like) but not making sense as a distinct feature. For the package
  part, a separate `rpms.pan`, included by `service.pan` is generally used
  as for features.

For features or personalities that may have different package configurations
depending on the context (for example a server and a client), the packages
may be described in different templates for each context with these templates
put into a `rpms` namespace.

For some features or personalities, it is sometimes necessary to have a first
stage in their configuration occuring very early, typically during the OS
configuration. In this case, these actions must be put into a template called
`init.pan` that will be called **before** `config.pan`.

## Variables

The template library makes an intensive use of global variables, internally
and to allow sites to customize the template behaviors according to their
needs. As variables have no namespace, to avoid name
collisions, the following convention has been established:

- As for every global variable in Pan language, their name must be
in uppercase.
-   The variable name **must** start with the name of the feature or
personality they apply to followed by an `_` (underscore). For historical
reasons, some variables don't adhere to this convention but
*new variables must*.
- The variable name prefix used must be consistent across the whole
service configuration for example: `DPM`, `LCGCE`, `CREAM`, `NFS`...

Some variables have a specific purpose and can be found in many
different features and personalities. One typical exameple is `xxx_CONFIG_SITE`:
the value is typically a template name describing the
site-specific configuration for the feature/personality, loaded early in the
configuration. This allows in particular to override default value for
the variables.

Variables intended to be customized by sites **must** have an annotation attached,
instead of a comment: this annotation is used to produced the
[Quattor documentation][quattor_rtd_documentation].
An annotation must be on the line before the variable declaration and must have the
following format:

```
@{
desc =  a description of the variable. If multiple lines are needed, use `\ ` as \
the continuation character.
values = the list of possible values for the variable or the type it must adhere to
default = the default value if any
required = yes or no (if there is a default value, it should be no)
}
variable MYFEATURE_MYVAR = ...
```

## Coding Style

It is very important for a template, like for any other piece of code,
to be well presented so that others can understand it and contribute to it,
as this is the ultimate goal of the template libary: allow people to share
the effort to describe service configurations.
For this reason, a set of conventions have been defined and are now
enforced by the `panlint` utility as part of any template library contribution.
`panlint` is executed during the test phase of any pull request submitted for
any of the templates modified in the pull request.

*Note: a lot of existing templates in the template library don't adhere
yet to these conventions. If you modify one of them, you may need to
do some changes not related to your contribution to make the modified
template compliant.*

The main conventions are:

-  Use 4 spaces for each indentation level. Do not use tabs as they
are not displayed the same way in all editors. The 4 space indentation is
enforced by `panlint`: if the template you are modifying still has a
2 space indentation, you will need to update it to 4 space indentation.
- Any `=` sign (or (`?=`) must be surrounded by exactly one space.
- Indent properly `list` and `dict`, with one element per line, each line
(including the last one) followed by a `,` and the closing parenthesis on its own line,
vertically aligned with the opening one.
- Use `dict` instead of the deprecated `nlist`. This is also enfroced by `panlin` and
this may require updating a template you are modifying.
- When using a DML to assign a value, the opening `{` must follow the `=` sign (preceded
by a space) and the closing `}` must be on a line of its own, vertically aligned with
the beginning of the line where the opening `{` is.
- with `foreach`, `if` and similar statements, the rule for `{` and `}` placement is
  the same as for the DML block.
- As with any languages comments must be used only to clarify something not trivial
or to give the background information justifying a particular configuration or choice.
It should never be an alternative to meaningful variable names.
- As said in the previous section, a variable intended for use by other templates must
be documented with an annotation and not a comment: the annotation is used to produce
the [Quattor Documentation][quattor_rtd_documentation]. On the other hand, internal variables
must be documented with a comment.


## Testing your Development

As soon as you open a pull request with your changes, it will be tested by GitHub/Travis against
the SCDB examples to ensure that they don't break anything. If you'd like to test your
changes outside of GitHub, you can use the [create-vanilla-SCDB.sh][get_tl] utility with
the `--pull-request` option (a [get-template-library][get_tl] option passed by `create-vanilla-SCDB.sh).

Option `--pull-request` allows to integrate a pull request not yet merged, typically for testing,
in the downloaded template library.
When using this option, the quattor version should be `HEAD` rather than a specific release,
else it will generally lead to unpredictable
results. The option value has the format `repository:user:source_branch:[target_branch]` with:

* `repository`: the name of the repository (without the GitHub user) the pull request belongs to. The repository name is assumed to be the same
for the source and target branches.
* `user`: the userid of the user who created the pull request (whose source repository belongs to).
* `source_branch`: the source branch of the pull request in the `user` repository.
* `target_branch`: the name of the target branch or tag of the pull request in the `quattor` repository. For a repository
with a master branch it can
be ommitted and will be the `master` branch if the version is `HEAD` else it will be the tag corresponding to
the version. For a repository without a master branch, `target_branch` is required and must be the branch
to use if the version is `HEAD` else it must be `branch-version`.


## Debugging Templates

This section describes the debugging options available when developing templates.

### Adding messages with debug()

To help troubleshooting problems, it is important to let templates produce some information
about what they are doing and their internal state, if requested. This is done by using
the `debug()` function. As every Pan function, it can be called only on the right side
of an assignment or in a DML. See Pan compiler documentation for details. To print a
debug message outside of a DML, use something like:

```
variable DEBUG = debug('this is a debug message');
```

### Printing the debug messages

The message passed as argument to `debug()` will be printed only if the Pan compiler
has been instructed to do so. The activation is controlled with the Pan compiler
ant task options `debugNsInclude` and `debugNsExclude`. The value for these option
must be a *namespace* regexp, i.e. the
value will be match with the string in the template initial line (`unique template....`).

`debugNsInclude` selects all the templates where debug messages must be enabled and
`debugNsExclude` is the list of templates to exclude in the selected list.

Depending on whether you use SCDB or the `panc` command, the options to use are:

|| ant task option || SCDB option || panc option ||
|| debugNsInclude || -Dpan.debug.include || \-\-debug-ns-include ||
|| debugNsExclude || -Dpan.debug.exclude || \-\-debug-ns-exclude ||
{: .table }

For example to only output debug from templates with name starting
"xen/" with SCDB:

```bash
ant -Dpan.debug.include='xen/.*'
```

Or to exclude debugging from all the spma and pan templates but display
it from all the rest:

```bash
ant -Dpan.debug.exclude='.*/spma/.*|pan/.*' -Dpan.debug.include='.*'
```

Check `panc` [cocumentation][pan_book] for more details.

### panc logging

Pan compiler features some useful logging facilities
that are helpful for debugging (for example, the order of template
inclusion and function calls can be logged).  Logging is enabled with the following
compiler ant task options:

Option | Possible values | Default
------ | --------------- | --------
logging | `all`, `none`, `include`, `call`, `task` or `memory` | `none`
logfile | Any filename you can write to | /tmp/panc.log
{: .table }

With SCDB, set these option values, using `-D`. The SCDB option has the `pan.` prefix.
For example:

```bash
external/ant/bin/ant -Dpan.logging=call -Dpan.logfile=/home/myuser/mypanc.log
```

With the `panc` command, use options `--loging` and `--log-file` respectively.

Check `panc` [cocumentation][pan_book] for more details.
