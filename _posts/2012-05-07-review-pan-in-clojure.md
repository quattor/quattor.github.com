---
layout: article
title: Migrating to Clojure for Pan Language Implementation
author: Charles Loomis
category: review
---

Abstract
--------

Migrating the pan compiler implementation from java to clojure offers
potential benefits by reducing the size and complexity of the code base. This
article describes clojure features that are interesting for use within the pan
compiler and a roadmap for implementation. It also provides concrete
benchmarks that will allow quantitative comparisions between pan compiler
versions as the migration to clojure takes place. Future articles will track
the incremental migration and benchmarks.

Introduction
------------

The Quattor Toolkit facilitates the complete machine lifecycle management for
sites with tens to tens of thousands of machines. The pan compiler plays a
central role in the toolkit, transforming the site's configuration, written in
the pan configuration language (see the "Pan Book" for a complete description
of the language), into individual machine profiles for consumption by agents
(Quattor configuration modules) that effect the necessary configuration
changes on the machines.

Because of the potentially large numbers of machines being managed, the pan
compiler must perform well, with maximum speed and minimum memory footprint.
The pan compiler already has a number of optimizations to enhance the
performance. It is multithreaded, uses a copy-on-write scheme to minimize
duplicate machine information, and caches heavily used information (for
example, pan configuration file status). These optimizations, however, do
increase the size and complexity of the code base.

Clojure, a LISP that runs on the JVM and interoperates well with Java,
provides standard features that would make many of these optimizations
redundant. These include clojure's software transactional memory (STM),
persistent data structures, and lock-free concurrency, among others,
potentially leading to a smaller and more robust code base. Moreover,
clojure's direct compilation to java bytecode offers the potential for faster
generation of machine profiles.

This article describes the expected benefits of migrating the current Java
implementation to clojure. It provides a set of benchmarks to allow
quantitative comparisions as chunks of the compiler are re-implemented in
clojure. This article will be followed by others as concrete changes are made.

Code Base Statistics
--------------------

Provide information about the size of the implementation. Lines of code and
number of classes/namespaces. Also describe the number of tests and test
coverage (if possible).

Performance Benchmarks
----------------------

Describe the LAL site configuration--numbers of machines, pan language files,
etc. Give the performance characteristics in terms of CPU time, wall clock
time, and memory footprint (perhaps broken down by cluster).

Current Issues
--------------

Current issues: developer maintenence time; performance; random errors
(probably from concurrency); non-optimal memory sharing. Must maintain a
working, optimal compiler.

Clojure Features
----------------

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

Conclusions
-----------

What has been implemented: scripts and new features.  Configuration
infrastructure next candidate for changes. 
