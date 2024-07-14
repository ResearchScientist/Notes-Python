# Data Structures

A sequence or collection that holds multiple values within one variable. Lists, arrays, and tuples are types of data structures.
- **string** holds a list, or a sequence of characters
- **list** holds multiple individual values within one variable
similar to arrays, and tuples
- **dictionary** holds key value pairs, entering the key retrieves its value
similar to maps, associative arrays, hash maps, and hash tables

**Passing by Value**

Variables are not used for the computation only their values are used.
Since only the value is known and not its location in memory, then it cannot be accessed and changes cannot be made to the variable.

**Passing by Reference**

Variables are accessed during computation and can be written to directly.
The reference is the location in memory. Since the location is known the variable can be accessed and its value can be changed.

**Immutable Data Types**

Data types which cannot be changed.

Primitives such as integers, floats, strings are immutable. 
Lists are mutable.

In reality for Python all data types are immutable. What Python does it assigns a new memory location for each reassignment.
The memory location can be retrieved with `id()`. It returns the memory address. 

But for practicality consider primitives immutable. Checking their address after a change shows different addresses for the original variable and the changed variable.
```
int1 = 1
int2 = 2
print(id(int1))
print(id(int2))
# the two memory addresses are the same
```
Consider non primitives mutable. Checking the address of a variable before and after a change in its content shows the same memory location before and after the change.
```
list1 = ["1","2","3"]
list2 = ["1","2","3"]
print(id(list1))
print(id(list2))
# the two memory addresses are different
```

# Methods

Function contained within a data structure.
Methods are called with the following syntax `someVar.someFunction()`.

`someString.find(string)` returns index of first occurrence of string within someString
`someString.count(string)` returns number of occurrences of string within someString
`someString.split()` splits a string up into a list of strings
`someString.capitalize()` capitalizes first character in a string
`someString.lower()` returns all characters as lower case
`someString.upper()` returns all characters as upper case
`someString.title()` capitalizes first character after each space
`someString.strip()` removes whitespace before and after the string, if an argument is passed it strips that character
`someString.replace("s1","s2")` replaces all occurrences of s1 with s2
`print("and".join(someString))` joins each character or item in a list with the given value

Boolean Methods that return True or False

`someString.startswith("someValue")` True when string begins with value given
`someString.endswith("someValue")` True when string ends with value given
`someString.isalpha()` True when string is all letters
`someString.isalnum()` True when string is all letters and numbers
`someString.isdigit()` True when string is all numbers
`someString.isnumeric()` True when string is all numbers including fractions
`someString.isdecimal()` True when string is a decimal or integer number
`someString.islower()` True when string is all lower case
`someString.isupper()` True when string is all upper case
`someString.istitle()` True when each word in the string is capitalized
