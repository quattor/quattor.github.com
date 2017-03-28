Quattor Web Site
================

The site is hosted through GitHub pages and can be modified by cloning this
repository, making changes, and pushing the changes back into the repository.
Generally, you should only add new articles to the \_posts subdirectory or one
of the documentation category (directory starting by \_ with an explicit name
matching one of the documnetation category in the Documentation page. All the
changes to the web site must be submitted as a pull request to allow a peer
review of the changes. No change must be merged by the author.

Guidelines for Content
----------------------

The naming scheme for the items in the __posts subdirectory is the date,
followed by the category (`news` or `documentation`), followed by a short
title. The content of the post should be done in [markdown
format](http://daringfireball.net/projects/markdown/) preceeded by a small
amount of metadata. Use the existing posts as guidelines for the metadata.
(There is another category, "review", that is supported; see below for how to
use this category.)

**News**: This is intended for short announcements that would interest users,
such as release announcements and invitations to meetings of general interest.

**Documentation**: This category contains short articles documenting the
features of the Quattor toolkit, for example, a getting started guide or
high-level documentation of the architecture. Comprehensive documentation for
a core tool should be provided in a separate document, ideally generated from
DocBook as part of the build process. Links to the longer documents should be
available in the shorter articles here.

Note: All of the content should also be reasonably formatted in the source
markdown file. This allows the content to be easily reused in other
distribution channels. For example, the news items posted here will likely be
automatically forwarded to the general Quattor mailing list.

Local Testing of Content
------------------------

GitHub pages uses Jekyll to generate the website after each pushed change. You
can install Jekyll locally to see how the site will look with your changes
and/or contributions. Many editors, such as TextMate on the Mac, can render
markdown documents. This may be an easier solution than installing Jekyll if
you are only adding content.

To generate the site locally use the following command:

```bash
jekyll --base-url=file:///`pwd`/_site/
```

for old versions of Jekyll, or

```bash
jekyll build
```

for newer versions of Jekyll.


With this command all of the links on the site will function correctly.

