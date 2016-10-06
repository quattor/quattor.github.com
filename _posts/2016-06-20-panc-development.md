---
layout: article
title: Overview of pan compiler development
author: Isaura Claeys
category: documentation
---

# Overview
The clojure file *pan_compiler.clj* is the main entry point of the program. It takes care of the
command line arguments, creates a new instance of the *Compiler* class and starts the compilation
process. The program consists of different stages: *Compile*, *Build*, *Valid1*, *Valid2* and
*WriteOutput*. All stages, except the output stage, make use of a *cache*. For every stage a single
*ThreadPoolExecutor* is created to which the different tasks are submitted. Submitting a task to a
certain threadpool is done via the compiler.

## Phases
### Compile phase
The actual compilation is started by executing a *CompileTask* for every file.

#### AST
First of all, an AST (Abstract Syntax Tree) is created from the source file using JJTree and JavaCC.
The source files are parsed corresponding to the grammar defined in *PanParser.jjt*. This builds a
JJTree and passes the output to JavaCC in order to finally generate a parser with parse tree actions.
The output can be found in *src/main/target/generated-sources*. To generate an AST, the parser also
uses some files in the *src/main/java/org/quattor/pan/parser* directory.

#### Template
After that, the AST nodes are converted into *Statements* and a *Template* object is created. All
methods needed to convert the nodes into statements can be found in
*src/main/java/org/quattor/pan/parser/PanParserAstUtils.java*. Statements contain operations,
elements, strings or type definitions. Elements are also operations. All statements can
be executed. For elements this means that the element itself is returned. During the conversion, all
the statements are sequentially saved in a *LinkedList*. During the creation of a new *Template*, a
*SourceFile* is created and all statements in the LinkedList are divided into two groups: static and
normal statements.

After generating this template, the *PostCompileProcessor* is called. This will send the template
through the build, valid1 and valid2 phases and will eventually create the output files in the
requested formats. Going through all these remaining phases is implemented with nested function
calls: the *PostCompileProcessor* will ask the result of a *WriteOutputTask* for the template it is
currrently processing. The *WriteOutputTask* will then ask the result from the *Valid2Cache*. When
the result is available in the cache it will return it to the write task, otherwise it will request
the result from the *Valid1Cache* and process it before returning it. This goes on until the
*BuildTask* requests the result from the *CompileTask*.

+ CompileTimeContext: only used for executing dml statements?

### Build phase
All the statements created during the previous phase are executed while maintaining a *BuildContext*.
This context contains all defined functions, types, global and local variables, dependencies, etc.
After executing the statements, defaults are inserted where there might be missing elements.

Template dependencies discovered during this phase by using the *IfExists* function or dependencies
already discovered during the compilation phase (these will be wrapped in an *IncludeStatement*) will
be included in the current template during execution of the *IncludeStatement* or the *Create*
function.

At the end of the build phase, the result will be a *HashResource* (which is implemented as a tree).
This tree is kept in the build context and will be passed on to the next phases.

### Valid1 phase
Checks if there are undefined elements and checks the type bindings. The compiler loops over all bind statements and checks if the value associated with a certain path is of the correct type. For some types extra checks, such as range checks, may be performed as well.

### Valid2 phase
Checks the object dependencies and compiles them.

### Output
The actual output is generated for every format that is passed as an argument. Every format has a
corresponding *Formatter* class. You can find all the formatters in the *org/quattor/pan/output*
package.

## SELF
*SELF* is initially parsed as a variable and is then converted into the corresponding operator
depending on what type SELF is (*SelfSimpleVariable*, *SelfSimpleListVariable*...). This is done in
*PanParserAstUtils.astToVariable()*. Suppose we have the following statement

<p align="center"> `'/x' = list(1); '/x' = prepend(SELF, 2)`. </p>

During execution of a statement where a *SELF* reference might be used, a placeholder will be created
for the variable, which in this case will be a *PathSelfHolder*, and will be saved in the build
context. If a reference to *SELF* should be used somewhere in the statement, we can retrieve this
value from the build context. The placeholder will only be used in the second statement in our
example.

## Types
All types are wrapped in a *FullType* object, used to completely define a type. All types, built-in
and user-defined, are saved in a *TypeMap* in the *BuildContext*. The *TypeMap* gets the primitive
built-in types from the *BaseType* class. This map is used to check whether a type that is used is
actually defined.

### Built-in types
All implementations of data types are located in *src/main/java/org/quattor/pan/dml/data/*. These are
primitive types, which are types that don't have default values or validation blocks, and are thus
wrapped in a *ConcretePrimitiveType*.

### User-defined types
User-defined types can be built up from the primitive types. All pan language types used to create
user-defined types are defined in *src/main/java/org/quattor/pan/type*.

#### AliasType
An *AliasType* associates a new name with an existing type, plus some restrictions.
For example: `type mylong = long with SELF >= 5`.

#### RecordType
A *RecordType* is a hash that explicitly names and types its children.
For example:
```
type mytype = {
    'entry1': string
    'entry2': double(1..)
}
```

#### CompositeType
The *CompositeType* enables us to create user-defined lists, hashes or links. These types will contain an *AliasType* referring to the type of the elements contained in the composite type.

##### ListType
Defines a user-defined list. For example `type mylist = string[]` defines a list containing strings.

##### HashType
Defines a user-defined hash. For example `type myhash = string{}` defines a hash with strings as
values.

##### LinkType
A *LinkType* specifies the type of the link it refers to.
For example: `type mylink = string*`. The value of this link will be a path that refers to a
value, which needs to be a string.

#### Processing user-defined types
Let's look again at the example for *RecordType*. The pan compiler will first create a *FullType* of
`string`, to map `entry1` to this type. It does not use the built-in *StringProperty* type. Later,
when the compiler will need to check whether the actual values assigned to this entry are strings,
the mapping of `string` to *StringProperty* in the *BaseType* class will be used. It will do the same
for `entry1`. It will then create a new *FullType*, which will be a *RecordType*, that contains
these two entries.

## Term
The *Term* class is used to index the different pan data types. For example, a *HashResource* can be
indexed through a string and a *ListResource* can be indexed with a number. Since in the pan language
*Resources* are indexed by a *String-* or *LongProperty*, these classes inherit from *Term*.

## Repository
These classes are used to keep track of all the directories that were passed as an argument to the
`--include-path` option and are responsible to locate files.

# Adding functionality
## Adding a new built-in function
### Implementation
#### /src/main/java/org/quattor/pan/parser/PanParserAstUtils.java
Add the function constructor of the new function to the hashmap. This is used to check whether a
function is user-defined or built-in during translation of the AST to a template.

#### /src/main/java/org/quattor/pan/dml/functions
The implementation of the new built-in should be placed in this package. The class needs to extend
the *BuiltInFunction* class and should be final. A new object of the built-in function is always
created via the *getInstance* method, which should perform the actual creation of a new object after
doing some checks on the input of the function.

### Testing
Tests for the built-in functions are located in the */src/test/java/org/quattor/pan/dml/functions*
folder and use JUnit. The test class should extend the *BuiltInFunctionTestUtils* class, which
performs some checks. To perform these checks, you should create a test-method called
*checkGetInstance* that calls *checkClassRequirements*. The test should have separate tests for every
Exception that can be thrown, as well as separate tests for every possible use of the function. There
are two ways to test the execution of the function: using *runDml*, which is a test method, or
creating a *CompileTimeContext* and executing the function via the context.

All functions also have test files written in pan itself. To add such a test for a new function, add
the test files to *src/test/pan/Functionality/*. The filenames should have the name of the
function with a number attached to it. At the beginning of such a file, you can specify some
settings. These are normally placed at the beginning of the file and should be inserted as comments.
It is mandatory to define the expected outcome. These settings are parsed in
*panc/src/test/java/org/quattor/pan/utils/TestUtils.java*.

#### Expected outcome
You can declare whether the expected result will be an exception or a value in the tree.
If you expect a *SyntaxException* to be thrown, you would place the following line in the
file: <p align="center">`@expect=org.quattor.pan.exception.SyntaxException regex`, </p>
where regex is optional. If you expect a specific result, you should use an XPath. For example:  
<p align="center">`@expect="/profile/result=1"`.</p>

#### Expected dependencies
You can declare what dependencies you expect from the source file. This should be declared as
follows: <p align="center">`dep: template_name`. </p>

#### Formatter
You can specify a specific formatter to use for the compilation. For example: `@format=pan`. The
default formatter is the pan formatter.

### Documentation
The javadoc is automatically generated by maven when building the project. The online documentation
of the built-in functions is kept separate. All online documentation is located in the
*pan/panc-docs/* folder. To add information about a new function, add it to the
*panc-docs/source/standard-functions/standard-functions.rst* file and to the *Functions*
section in *panc-docs/source/pan-book/pan-book.rst*. This documentation is written in
reStructuredText. Mind that all functions are sorted alphabetically.

# Commands
## Complete build of the whole project
#### Including tests
`mvn clean package`

#### Without tests   
`mvn -Dmaven.test.skip=true clean package`

## Building panc
#### Including tests
`mvn -pl panc clean package`

#### Without tests
`mvn -pl panc -Dmaven.test.skip=true clean package`

#### Without tests and javadoc
`mvn -pl panc -Dmaven.test.skip=true -Dmaven.javadoc.skip=true clean package`

## Running tests in panc

#### Run all tests, including the clojure tests
`mvn -pl panc test`

#### Run a single test class
`mvn -pl panc -Dtest=Test test` where Test is the name of the test you want to run.

#### Run multiple test classes
`mvn -pl panc -Dtest=Test1,Test2 test`

#### Run a single method in a specific class
`mvn -pl panc -Dtest=Test#method test`

#### Run multiple methods in a specific class
`mvn -pl panc -Dtest=Test#method1+method2 test`

#### Running all clojure tests
`mvn -pl panc clojure:test`

## Running the project
After building the project, all created files will be located in the *panc/target/* folder. The
built project can be executed on the command line as follows:

`java -cp path_to/panc/target/panc-10.3-SNAPSHOT-jar-with-dependencies.jar org.quattor.pan.pan_compiler [OPTIONS]`
