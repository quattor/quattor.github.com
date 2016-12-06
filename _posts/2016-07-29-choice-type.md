---
layout: article
title: Implementing the choice type
author: Isaura Claeys
category: documentation
---

# Implementing the choice type
Related to this [pull request](https://github.com/quattor/pan/pull/121).

## Implementation

In the `PanParser.jjt` file, another `OR` option was added to `baseTypeSpec()`:

```
t=<CHOICE> <LPAREN> stringLiteral() (<COMMA> stringLiteral())` e=<RPAREN>
```

This will specifically match the `Choice`-type.

`ChoiceType` extends `AdvancedType`, a very simple super class used to define more advanced types.
The `AdvancedType` class inherits from the `BaseType` class. This is required because all types are
wrapped in a `FullType` and a `FullType` contains a `BaseType`. Since the actual identifier is
`choice`, and not a primitive type, we use the identifier to make the difference between a normal
`AliasType` and a `ChoiceType` in `PanParserAstUtils.astToType()`. The validation phase checks if the
value of an element is one of the possible choices.

This type requires that the input arguments are strings, thus no variables referencing strings, since
the arguments of a type can't be executed during the build phase.

## Tests

* Added a `ChoiceTypeTest` to `test/java/org/quattor/pan/type/`.
* Added pan test files to `test/pan/Functionality/types/choice`.
