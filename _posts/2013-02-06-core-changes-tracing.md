---
layout: article
title: Getting more traces from component execution
category: documentation
image: assets/img/quattor-logo.png
---

Starting with version 2.0.0 of the core modules (`CAF`), components
complying with the
[coding style guide](/development/coding_style.html)
will be much more traceable:

* When running the component with `--noaction`, certain commands that
  are known to be safe (i.e. they don't modify the system's state)
  will be executed. This will provide more information to the operator
  about the current state, and how the component is expected to alter
  it.
* When running the component with `--verbose`, any files modified will
  display in the console a diff with the previous version. This will
  happen even with `--noaction`.

In order to prevent leaking confidential information, the diffs will
*not* be stored in logs.

This follows a request by our friends at Morgan Stanley. All feedback
will be appreciated!
