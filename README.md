Quattor Web Site
================

This is the Quattor web site that contains information for *users*. Please do
not put information here that is intended for the developers of Quattor.

The site is hosted through GitHub pages and can be modified by cloning this
repository, making changes, and pushing the changes back into the repository.
Generally, you should only add new articles to the __posts subdirectory. Do
not change the skeletons or styles without discussing the changes first on the
developers' mailing list.

Guidelines for Content
----------------------

Again, the content on this web site is intended for users of Quattor. If it is
not of interest to users, then put the information on the 
[Quattor wiki][https://trac.lal.in2p3.fr/Quattor] instead.

The naming scheme for the items in the __posts subdirectory is the date,
followed by the category (news, blog, documentation), followed by a short
title. The content of the post should be done in [markdown
format](http://daringfireball.net/projects/markdown/) preceeded by a small
amount of metadata. Use the existing posts as guidelines for the metadata.
(There is another category, "review", that is supported; see below for how to
use this category.)

**News**: This is intended for short announcements that would interest users,
such as release announcements and invitations to meetings of general interest.

**Blog**: This category should contain longer articles of general interest
that would interest users and people in the fabric management community.

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
<code>
    jekyll --base-url=file:///`pwd`/_site/
</code>
With this command all of the links on the site will function correctly. 

Review of Content
-----------------

Ideally new content should be reviewed by others in the Quattor development
team. Please put new posts into the "review" category. Material marked as
review will appear on a separate list that is *not visibly linked* on the
website. You can see the articles undergoing review at the /review/index.html
page. Content you write should be posted there first with an invitation for
review sent to the developers' mailing list.

News items probably need only minimal review. Blog and Documentation entries
may need longer and more detailed review by others in the developer community.
Use your best judgement on how long to leave something in review before moving
it into a visible category.
