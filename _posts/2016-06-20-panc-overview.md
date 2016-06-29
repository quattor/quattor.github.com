
## Overview
The clojure file *pan_compiler.clj* is the main entry point of the program. It takes care of the command line arguments, creates a new instance of the Compiler class and starts the compilation process. The program consists of different stages: compile, build, valid1, valid2 and output. All stages, except output, make use of a cache. For every stage a single threadPoolExecutor is created to which the different tasks are submitted. Submitting a task to a certain threadpool is done via the compiler.

### Phases
#### Compile phase
The actual compilation is started by executing a CompileTask for every file passed as an argument.

##### AST (Abstract Syntax Tree)
First of all, an AST is created from the source file using JJTree and JavaCC. The source files are parsed corresponding to the grammar defined in *PanParser.jjt*. This builds a JJTree and passes the output to JavaCC in order to finally generate a parser with parse tree actions. The output can be found in src/main/target/generated-sources. To generate an AST, the parser also uses some files in the *src/main/java/org/quattor/pan/parser* directory.

##### Template
After that, the AST nodes are converted to statements and a Template object is created. All this is done in *src/main/java/org/quattor/pan/parser/PanParserAstUtils.java*. Statements contain operations, elements, strings or type definitions. Elements are also operations. All statements can be executed. For elements this means that the element itself is returned. All the statements are sequentially saved in a LinkedList. During the creation of a new Template, a SourceFile is made and all statements in the LinkedList are divided in two groups: static and normal statements.

After generating this template, the PostCompileProcessor is called. This will send the template through the build, valid1 and valid2 phases and will eventually create the output files in the requested formats. Going through all these remaining phases is implemented with nested function calls: the postCompileProcessor will ask the result of a WriteOutputTask for the template it is processing. The WriteOutputTask will then ask the result from the Valid2Cache. When the result is available in the cache it will return it to the write task, otherwise is will request the result from the Valid1Cache and process it before returning it. This goes on until the BuildTask will request the result from the CompileTask, which will be available.

+ CompileTimeContext: only used for executing dml statements?

#### Build phase
All the statements created during the previous phase are executed while maintaining a BuildContext. This context contains all defined functions, types, global vars, local vars, dependencies, etc. After executing the statements, defaults are inserted where there might be missing elements.

Template dependencies discovered during this phase by using the IfExists function or dependencies already discovered during the compilation phase (these will be wrapped in an IncludeStatement) will be included in the current template during execution of the IncludeStatement or the Create function.

At the end of the build phase, the result will be a HashResource (which is implemented as a tree). This tree is kept in the build context and will be passed on to the next phases.

#### Valid1 phase
Checks if there are undefined elements and if the type bindings are correct.

#### Valid2 phase
Checks the object dependencies and compiles them.

#### Output
The actual output is generated for every format that is passed as an argument. Every format has a corresponding **Formatter** class.

#### SELF
SELF is initially parsed as a variable and is then converted into the corresponding operator depending on what type SELF is (SelfSimpleVariable, SelfSimpleListVariable...). This is done in **PanParserAstUtils.astToVariable()**. Suppose we have the following statement

<center> `'/x' = list(1); '/x' = prepend(SELF, 2)`.

During execution of a statement where a SELF reference might be used, a placeholder will be created for the variable, which in this case will be a PathSelfHolder, and will be saved in the build context. If a reference to SELF should be used somewhere in the statement, we can retrieve this value from the build context. The placeholder will only be used in the second statement in our example.

### Built-in types


## Adding functionality

### Adding a new built-in function
#### /src/main/java/org/quattor/pan/parser/PanParserAstUtils.java
Add the function constructor of the new function to the hashmap. This is used to check whether a function is user-defined or built-in during translation of the AST to a template.

#### /src/main/java/org/quattor/pan/dml/functions
The implementation of the new built-in should be placed in this package. The class needs to extend the **BuiltInFunction** class. A new object of the built-in function is always created via the **getInstance** method, which should perform the actual creation of a new object after doing some checks on the input of the function.

### Adding a new built-in data type
#### /src/main/java/org/quattor/pan/dml/data
The implementation of the new type should be placed in this folder. Depending on what type your going to add, you should inherit from the right class.

#### /src/main/java/org/quattor/pan/type/BaseType.java
THe type should be added to the hashmap.

## Commands
### Complete build of the whole project
##### Including tests
`mvn clean package`

##### Without tests
`mvn -Dmaven.test.skip=true clean package`

### Building panc
##### Including tests
`mvn -pl panc clean package`

##### Without tests
`mvn -pl panc -Dmaven.test.skip=true clean package`

### Running tests in panc

##### Run all tests, including the clojure tests
`mvn -pl panc test`

##### Run a single test class
`mvn -pl panc -Dtest=Test test` where Test is the name of the test you want to run.

##### Run multiple test classes
`mvn -pl panc -Dtest=Test1,Test2 test`

##### Run a single method in a specific class
`mvn -pl panc -Dtest=Test#method test`

##### Run multiple methods in a specific class
`mvn -pl panc -Dtest=Test#method1+method2 test`

##### Running all clojure tests
`mvn -pl panc clojure:test`

### Running the project
After building the project, al created files will be located in the *panc/target/* folder. The built project can be executed on the command line as follows:

`java -cp path_to/panc/target/panc-10.3-SNAPSHOT-jar-with-dependencies.jar org.quattor.pan.pan_compiler [OPTIONS]`
