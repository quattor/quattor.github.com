---
layout: article
title: Contributing to Aquilon
modified: 2018-05-13
author: Michel Jouvin
menu: Contributing
---

Contributions to Aquilon are welcome, as for any other parts of Quattor, but have stricter requirements
for commit messages.

[gerrit-commit-hook]: https://gerrit.googlesource.com/gerrit/+/master/resources/com/google/gerrit/server/tools/root/hooks/commit-msg
{:target="_gerrit_commit_hook"}

## Commit Messages

Commit messages require a `Change-Id:` line. To achieve this, simply add the Gerrit
[`commit-msg` hook][gerrit-commit-hook]

You can use following commands to install it:

```bash
wget -q -O - "https://gerrit.googlesource.com/gerrit/+/master/resources/com/google/gerrit/server/tools/root/hooks/commit-msg?format=TEXT" | base64 --decode > .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

*Warning: executing the command above will overwrite the previous `commit-msg` hook, if any.*

Once the commit hook is installed, just enter your commit message as usual. During the commit operation, the
`Change-Id` line will be added by the hook. If looking at commit message with `git log`,
it should typically look like:

```
Short summary of the change

- Details what was done
- More details

Change-Id: I9f8d7d0f656e72877c436727d0e4a8d8a62a4b89
```

## Contributing your Changes

Once you have validated your changes and edited the appropriate commit messages, you need to open a pull request
against the relevant Aquilon repository on GitHub. There are two repositories:

- [Aquilon](https://github.com/quattor/aquilon) itself (the main one)
- Aquilon [protocols](https://github.com/quattor/aquilon-protocols): Python modules used to interface to the database

*Note: each commit **must** have a different `Change-ID`, even they are part of the same pull request*

