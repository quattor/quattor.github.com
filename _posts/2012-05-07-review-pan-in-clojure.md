---
layout: article
title: Migrating to Clojure for Pan Language Implementation
author: Charles Loomis
category: review
---

Introduction
------------

What is pan? What is it good for?  What are the design goals and
features?  Pan is declarative with extensible validation, geared
toward data definition.

Current Java Implementation
---------------------------

Provide information about the size of the implementation.  Lines of
code, number of classes, footprint, etc.

Reasons to Move to Clojure
--------------------------

Describe that this wasn't the first implementation, that another
implementation was done in c before.  Reasons for moving was
essentially memory management, need to reimplement many things because
of lack of standard libraries.

  * Java interoperability allows for gradual transition to clojure.
    Critical given the large existing code base.  Also critical as
    other tools in Quattor toolkit use ant and maven extensively.
  * STM and immutable objects allows for cleaner multithreading.
    Already much of the code is immutable, but there are still issues
    with maintaining locks to various bits of code.
  * Functional nature of clojure is a good fit to the pan language
    itself.  Templates are essentially functions masquarading as
    classes because this is required in java.
  * Large memory use in pan is from keeping machine profiles in memory
    during a compilation.  Pan already does some sharing of duplicated
    data between profiles, but implements this by hand with
    copy-on-write.  Using clojure persistent data structures promises
    to be both more efficient and transparent to the pan compiler
    implementation. 
  * Pan is currently compiled to a custom instruction set that is then
    interpreted when building machine profiles.  Translation of the
    templates to functions and namespaces in clojure will also for the
    direct compilation into java byte code (and then into native
    machine instructions).  This may significantly speed up the pan
    compiler.  It will certainly simplify the implemetation by
    removing the interpretation code.
  * The pan templates are read from disk.  The large number of such
    templates means that a lot of time is spent "statting" the file
    system to see if there are changes.  This information is cached by
    the compiler.  The standard memoization features in clojure will
    again simplify the implementation and allow such caching for other
    similar tasks.
  * Pan is declarative and data-oriented.  Clojure more closely
    matches these aspects than pure java.  This will also allow a
    second DSL syntax directly in clojure.
  * Possibly more extensible by users because of dynamic nature of
    clojure.  Could allow for more contributions from other
    developers. 

Worries with the Transition
---------------------------

  * Slow to load and slow to run.  (AOT)
  * Larger executable.
  * Inclusion of external libraries.

Current Status
--------------

What has been implemented: scripts and new features.  Configuration
infrastructure next candidate for changes. 
