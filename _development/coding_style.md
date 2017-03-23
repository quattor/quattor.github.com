---
layout: article
title: Quattor Coding Style
author: Luis Fernando MuÃos Mejias
menu: Coding Style
---

[quattor_rtd_documentation]: http://quattor-documentation.readthedocs.io/en/latest/

Introduction
------------

All major software projects have a set of guidelines for their code. It helps 
people to understand each other's code, 
and even your own code a few months (or days!) after you wrote it for the first time.

There are lots of documents motivating this, feel free to review them. 
[This one](http://www.kroah.com/linux/talks/ols_2002_kernel_codingstyle_paper/codingstyle.ps) 
is a good starting point but in short:

-   I want to read your code.
-   I want you to read my code.
-   I want to fix your bugs.
-   I want you to fix my bugs.

### Further reading

-   [Perl coding style guide](http://perldoc.perl.org/perlstyle.html)
-   [Documentation/CodingStyle and beyond](http://www.kroah.com/linux/talks/ols_2002_kernel_codingstyle_paper/codingstyle.ps), 
by Greg Kroah-Hartman

The basics
----------

### Indentation

Use 4 white spaces. No tabs, no 8 white spaces, no funny things. Fix your editor's configuration, 
or use a decent one. There are plenty of them.

### Capitalisation

Use lowercase for local variables, uppercase for constants.

We have no consistent convention for function names enforced in the existing code but 
the recommandation is function\_names\_like\_this\_one rather than functionNameLikeThis.

### Use meaningful names for globals, short names for locals

`i` is a perfectly valid identifier for a loop variable. However, you deserve nasty punishment 
if you use it as a function name.

On the opposite, `this_is_a_temporary_counter` is plain bad for a loop variable.

So, some good examples:

```
sub write_user_credentials
{
    # ...
}
```

```
foreach my $i (0..10) {
    # ...
}
```


And very bad examples:

```
sub wuc
{
    # WTH???
}
```

```
foreach my $counter_from_0_to_10_included (0..10) {
    # Excuse me???
}
```

### Be modular

Really, it **matters**. Have you ever tried to understand a module which is 700 lines long? 
Did you ever try to understand what's the purpose 
of a variable that was defined 5 screens ago? Or the meaning of the 30th variable on this block? 
Or the purpose of that line that starts and finishes beyond the screen?

Here are the classic metrics for modularity:

* No lines longer than 80 columns.
  * Split or rearrange longer strings
  * Split longer statements
* If you have more than 3 levels of indentation, split your block
* If your function goes beyond the screen, split it
  * And don't try to reduce the font. ;)
* If you have more than 7 local variables, split your function.
  * Sometimes it's OK to have 10, but if you have 15 your code is a problem.

### Don't use magic numbers

The `constant` pragma will give you meaningful names for any values other than 0 and 1 you need. 
They'll help you to understand why you chose such values on the past.

A good example:

```
use constant PI => 3.141592;
my $circle_area = $radio * PI * PI;
```

And the bad example:

```
# Oops! I missed a decimal somewhere!
 my $circle_area = $radio * 3.14159 * 3.141592;
```

### Module header

A Perl module **must** start with a line like:

```
#${PMpre} NCM::Component::mycomp${PMpost}
```

Update `NCM::Component::mycomp` to reflect the namespace of your module.

This ensures that the module starts with the proper information about license, authors... 
and this adds the `use strict`, `use warnings` and other things that are required in 
every Quattor module. **Never had them manually**.

### Comments

When in doubt, don't use them.

Comment all Pan data structures, or at least provide a link to their full description. Try 
to use the new annotation syntax which can be processed to produce the documentation.

Comment the purpose of each file, probably using POD syntax. Write a comment before the 
beginning of each function, telling
what it does and how to use it. But don't annoy the reader with the internals.

Don't comment function bodies. If your code is so complex that it needs further explanations, 
you should probably split it in several functions and comment those functions. Of course, sometimes 
you have to work around some broken API, or some corner case. In such case, please comment 
**why** you are doing it, but not **how**. And don't comment the obvious.

Bad examples:

```
#!perl
 ############################################################
 #
 # Increment by 1
 #
 ############################################################
 $i++;
```

```
#!perl
 sub do_something
 {
    my @args = @_;
 
    # I do foo and bar here
    ...
    ...
    ...
    # And now, let's do bar again, but with a small difference
    ...
    ...
 }
```

These are best done like this:

```
#!perl
 $i++;
```

```
#!perl
 # Performs task foo...
 sub foo {...}
 # Performs task bar...
 sub bar {...}
 # Performs task baz, which is quite similar to bar
 sub baz {...}

 # Performs a set of tasks, returning blah blah with arguments
 # $arg1:
 # $arg2:
 sub do_something
 {
     my @args = @_;
     foo (@args);
     bar (@args);
     baz (@args);
 }
```

### Don't use `vars`

This pragma has been deprecated since Perl 5.6, and that's a long time ago. Instead, 
use the `our` declaration for package-wide variables:

Good:

```
#!perl
 our @EXPORT = ...;
```

Bad:

```
#!perl
 use vars qw (@EXPORT);
 @EXPORT = ...;
```

### Curly bracket position

Follow Kernighan-Ritchie's convention: open curly brackets on the same line as the sentence 
they belong to and close them on a line for their own, excepting when it's an else or a do-while block:

```
#!perl
 if ($foo) {
     ...
 }
```

```
#!perl
 while ($bar) {
     ...
 }
```

```
#!perl
 if ($foo) {
     ...
 } else {
     ...
 }
```

```
#!perl
 do {
     ...
 } while ($bar);    
```


This way it is perfectly clear where each block starts, finishes and continues.

The only exception to this are the curly brackets that open a function. They should be on a 
different line, and have nothing else on the same line:

```
#!perl
 sub foo
 {
     my @args = @_;
 }
```

The reason for this is that decent editors (f.i, Emacs) are aware that such curly braces mean 
something special, and allow you to move to the beginning and the end of a function with a 
single key stroke. This is a great help for navigating code.

### Parenthesis

Use them a lot. When in doubt, use them. Especially:

-   Always use parenthesis on function calls
-   Always use them on function calls even when there are no arguments

The reason is that:

```
#!perl
 foo();
```

Is easier to understand than:

```
#!perl
 foo;
```

### Prefer methods over plain functions

Especially when writing components, you want to log unexpected things. It's free to have a 
`$self` object, and let it log.

Only use plain functions if you want them exported to some other module.


## The Quattor library (aka CAF)

`CAF` is a set of modules that provide an interface to system calls (or their Perl equivalent) 
allowing to execute commands, 
manipulate files... It is mandatory to use them rather than the system calls for the following reasons:

- If they generate exceptions, this is properly handled to avoid crashing the configuration module.
- They log what they are doing  on the terminal and in log files with a verbosity controlled by command 
options or the daemon configuration.
- For file manipulations, a lot of checks are done to avoid doing weird things like silently following 
symlinks and overwriting files.
- They are mocked by the Quattor unit test framework, allowing to run unit tests without root access or 
without installing the underlying services.

`CAF` documentation is part of the online [Quattor documentation][quattor_rtd_documentation].

### Running commands

Do not use backticks or `system`, nor use `open` for pipes. The `CAF::Process` module has all you need, 
and it won't spawn new subshells, which is much safer.

As the `CAF::Process` module logs the command line that you are executing at verbose and debug levels, 
you don't need to handle the logging yourself. Do not do:

```
#!perl
 $self->debug (5, "Going to run ls -l");
 system ("ls", "-l");
```

Instead, do: 

```
#!perl
 # Or any reporter object.
 my $proc = CAF::Proces->new (["ls", "-l"], log => $self);
 $proc->run();
 # One-line version:
 CAF::Process->new (["ls", "-l"], log => $self)->run();
```

The log option is any CAF::Logger object, for instance the component you are writing (`$self`).

Sometimes you pass confidential data to your commands. For instance, an encrypted password to usermod. 
In this cases, you don't want your command logged. Just don't pass any log argument to CAF::Process::new:

See [Quattor documentation][quattor_rtd_documentation] for examples covering 
the most common use cases.


### File handling

Writing to files is not as simple as one could think: there are risks that you should be aware of. For 
instance, the following code seems harmless but is an example of what shouldn't be done:

```
#!perl
 open (FH, ">/tmp/foo");
```

If `/tmp/foo` already exists and is a symbolic link to `/etc/shadow`, you just lost all accounts on your system.

For this reason, `CAF` provides several modules related to file manipulation:

* `CAF::FileWriter`: allow to create a new file
* `CAF::FileEditor`: allow to update an existing file or create a new one if it doesn't exist yet
* `CAF::FileReader`: allow to read an existing file but not to modify it

`CAF::FileWriter` and `CAF::FileEditor` update a file when the CAF object is closed. The update is done only 
if the contents was changed. They allow you to specify the file owner, permissions, a backup file name to save 
the existing file if it is modified...

See [Quattor documentation][quattor_rtd_documentation] for examples covering the 
most common use cases.

#### Temporary files

Don't use them. If you don't use `File::Temp`, you'll use predictable filenames, and that's just bad. Then, 
most implementations make temporary files
world readable, and you usually don't want that. If you need temporary storage for some text, use an array, 
IO::String, in-memory files, a CAF::FileWriter or anything like that.

So you want to run a command which needs a file name as an argument, right? Easy. Just pipe to that command, 
as shown above. And pass /dev/fd/0 as the file name.

Finally, if really all these options are not good enough, use `File::Temp::tmpfile`, which will provide you an 
anonymous file handle. But please, use this only if you are convinced there is no other way to keep your temporary data.


### Other file operations: CAF::Path

`CAF::Path` is a module related to path operations (rather than file contents). Its main features are:

* Test if a path exists, is a file, a symlink, a hardlink or a directory
* Symlink and hardlink management
* Management of file permissions and owner

See [Quattor documentation][quattor_rtd_documentation] for more details on the 
available methods and for examples covering the most common use cases.

## Input handling

Make sure that your code can run in *tainted mode*: this is a requirement for Quattor configuration modules 
and most of the other Quattor components.

The basic thing is that no input should be trusted, even when coming from the host profile. 
Sanitise everything just after reading it else Perl will complain that your input is tainted.

Also, when you create files that will be sourced by shell scripts, be sure to print all values between single quotes. 
This is true for almost every file you have under `/etc/sysconfig`.

## Quality of messages

The main principle is to find the balance between a totally silent execution and an excessive verbosity that doesn't 
allow to identify the important things. Use `info` and `ok` methods only for the important messages, use `verbose` 
or `debug` for others. `debug` implies `verbose`.

Provide a detailed trace of any task you perform with `verbose` messages. Trace DNS queries, URLs being retrieved, 
services you have to enable or disable... but avoid to log (detailed) output of the actions. You don't need to log 
the files that you open or the commands that you run. 
The CAF objects will do so for you.

### Debugging output

`debug` is for information only relevant to developers. A normal user should never be required to ask for debug 
message to get the information
he needs. This should be used only for developer-relevant stuff, such as tracking temporary contents or so. 

There are 5 levels of debug information. We don't have a precise convention about what must be logget at which 
level. Generally it is enough to use the first 2 levels.

### Use `error` only for fatal errors

Use the `error` method only if this error will make the entire configuration module to fail. 
If you can handle it, or the failure is not really important for
the component's results, use `warn` instead. If failing to download a file is OK because you can work around it, 
or you know you may have 
no rights to write on AFS, but that's OK, use a `warn` message. `warn` events don't cause the component to fail.

After an error has been logged, the configuration module will be re-run each time a new profile arrives until 
it succeeds. And the other configuration modules that depend on it will not be run.

Conclusions
-----------

Code quality matters. It will reduce bugs, and will make everybody's life easier.

All these conventions can be improved, so feedback will be appreciated. Especially, the CAF library can be extended 
with whatever task we repeat over and over.
