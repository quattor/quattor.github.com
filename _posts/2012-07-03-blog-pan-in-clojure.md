---
layout: article
title: Migrating to Clojure for Pan Language Implementation
author: Charles Loomis
category: review
---

The pan configuration language compiler provides the link between
human-readable machine configurations for system administrators and back-end
tools that affect the necessary changes on real systems. Migrating the pan
compiler from Java to Clojure may make the compiler faster, less resource
intensive, and easier to maintain.

Introduction
------------

The Quattor Toolkit facilitates the complete machine lifecycle management for
sites with tens to tens of thousands of machines. The pan compiler plays a
central role in the toolkit, transforming the site's configuration, written in
the pan configuration language (see the ["Pan Book"][sf-panc-files] for a
complete description of the language), into individual machine profiles for
consumption by agents (Quattor configuration modules) that affect the
necessary configuration changes on the machines.

Because of the potentially large numbers of machines being managed, the pan
compiler must perform well, with maximum speed and minimum memory footprint.
The pan compiler already has a number of optimizations to enhance the
performance. It is multithreaded, uses a copy-on-write scheme to minimize
duplicate machine information, and caches heavily used information (for
example, pan configuration file status). These optimizations, however, do
increase the size and complexity of the code base.

There are some issues with the current pan compiler: complexity of the current
implementation makes suboptimal use of the available development time,
there are rare transient errors in the compilation of machine profiles likely
due to locking problems, the copy-on-write scheme reduces memory utilization
but not at the same level that fine-grained sharing would, and as always,
there is a need for the fastest compilations possible. Clojure may help with
all of these.

Clojure
-------

[Clojure][clojure], a LISP that runs on the JVM and interoperates well with Java,
provides standard features that would make many of these optimizations
redundant. These include clojure's software transactional memory (STM),
persistent data structures, and lock-free concurrency, potentially leading to
a smaller and more robust code base. Moreover, clojure's direct compilation to
java bytecode offers the potential for faster generation of machine profiles.

Migration
---------

A re-implementation of the pan compiler in Clojure would not be the first
migration of the compiler between languages. The initial prototype was written
in Perl and the first production-level version, in C. The current
implementation in Java was undertaken to take advantage of the transparent and
efficient memory managment of the JVM.

However because of the good interoperability between Clojure and Java, it is
the first migration that can happen incrementally. This is important as the
limited development effort can be applied to a single code base and the
compiler will remain compatible with other Quattor tools that use, to a
certain extent, Java-based tooling.

Specific Changes
----------------

There are a large number of areas where the move to Clojure may help, either
by reducing the code complexity or by improving performance. Some specific
areas where Clojure features may help are below.

* STM and immutable objects allow for cleaner multithreading.
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
    compiler.  It will certainly simplify the implementation by
    removing the interpretation code.
* The pan templates are read from disk.  The large number of such
    templates means that a lot of time is spent "statting" the file
    system to see if there are changes.  This information is cached by
    the compiler.  The standard memoization features in clojure will
    again simplify the implementation and allow such caching for other
    similar tasks.
    
Towards the Future
------------------

As the migration towards Clojure takes place, the size of the code base will
be measured along with the performance against a standard benchmark. These
will help to judge whether the changes actually improve the compiler itself.
Future articles will describe the changes and report on the code and
performance benchmarks.

[sf-panc-files]: http://sourceforge.net/projects/quattor/files/panc/
[clojure]: http://clojure.org 
