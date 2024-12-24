# PEP 8 Style

## Why should I use this?
1. Using a consistent style makes your code **more apporoachable and easier to read.**
2. It becomes easier to collaborate.
3. It makes easier to change your code later.
4. It can help to avoid common error

## Pulbic guide link
[PEP-0008](https://peps.python.org/pep-0008/)

## Contents
### Whitespace (refer to example_code1.py)
- In Python, Whitespace is **syntactically significant**
    - Because
        1. It **determines code blocks**
        2. **Mandatory** (unlike other language)
            - In other language, Indentation is optional and for readability
- So Python programmers are especially sensitive to the effects of whitespace
- Guidelines
    1. **Use 4 spaces** instead of tabs
    2. **lines should be 79 characters** in length or less
    3. **Additional 4 indentations** in new lines if you are using **a long expression to make a new line**
    4. In a file, **Functions and classes** should be **separated by two blank lines**
    5. In a class, methods should be separated by one blank lines
    6. In dictionary, Don't put space between each key and colon, and put a single space before the corresponding value 
    7. Put one space and one space before and after the = operator(assignment)
    8. For type annotations, ensure that there is no separation between the variable name and the colon, and use a space before the type information

### Naming (refer to example_code2.py)
- PEP 8 recommends unique styles of naming
    - These conventions make it easy to distinguish to each name when reading code
- Conventions
    1. `lowercase_underscore format` : Functions, Varialbes, Attributes
    2. `_leading_underscore format` : protected instance attributes
    3. `__double_leading_underscore format` : private instance attributes
    4 . `CapitalizedWord format` : Classes(including Exception)
    5. `ALL_CAPITALS` : Module-level constants
        - Class-level constants should use `ALL_CAPS`
        - function-level constants should use `lowercase_underscore`
    6. Instance methods in classes `should use self`, as `the name of the first parameter`
    7. Class methods `should use cls`, which refers to the class as `the name of the first parameter`
        - Class methods can be accessed without creating an instance of the class (similar to static methods in other languages).

### Expressions and Statements (refer to example_code3.py)
- Guidelines
    1. `Use inline negation` instead of negation of positive
    2. `Don't check` for `empty containers or sequences`. Let empty values `be implicitly evaluated to false`
        - The same thing goes for non-empty values
    3. `Avoid single-line` if statement, for and while loops, and except compound statements. `Spread these over multiple lines` for clarity
    4. If the expression gets too long, `use parantheses` instead of \
