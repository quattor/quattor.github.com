---
layout: article
title: Testing needed! Yum backend for ncm-spma
category: news
---

The new version of ncm-spma is ready for *tests*. If you think the
following shortcomings won't affect you, your help will be greately
appreciated.

## Shortcomings

You need Yum 3.2.29 or higher. This is the version shipped in SL6.2,
but not with SL5. On SL5 you'll have to build it or download it from
[Fedoreapeople](http://repos.fedorapeople.org/repos/james/yum-rawhide/epel-5/).

AII is not yet adapted to the new SPMA. As a result, installations
using the new version will fail.  The adaptation will follow shortly.

The `spma` executable is obsolete.  The component communicates with Yum
directly, and thus there may be conflicts.

## How to test

Download the component from my GitHub:

    git clone git://github.com/piojo/ncm-components-core.git spma-yum

Build the component, as usual. I'd appreciate reports if the test
suite fails. See [the testing documentation][tests] to run the test
suite.

Finally, you just update the component in your CDB/SCDB/Aquilon as
usual.

[tests]: /documentation/2012/03/22/documentation-testing-code.html

### What to test

Interesting things (that I'm testing now, but hey, help is always
welcome):

* SL5 (but please, update your version of Yum before!!
* `userpkgs`
* `run` with different values

## Feedback

Please, send the feedback to the mailing lists, or to the G+ page.

Happy testing!
