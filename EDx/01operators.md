# Programming

- **Functional** Code segmented into functions
- **Object Oriented** Code segmented into classes objects and functions
- **Event Driven** Code that waits for specifed events in order to trigger its execution

# Operators

## Logical Operators
Evaluate and return True or False for given conditions.

### Rational
`==` `>` `<` `>=` `<=` `!=`

### Set
`in`
```
list = [1,2,3]
print(1 in list) # returns True
```

### Boolean
- `not` acts on one boolean value and returns the opposite
- `and` requires both boolean values to be True in order to return True , otherwise returns False
- `or` either boolean value can be True in order to return True , requires both boolean values to be False in order to return False

Expressions within parentheses are evaluated first. Expressions are evaluated left to right. 
`not` is always evaluated before `and` and `and` is always evaluated before `or` regardless of the order they are written in.
1st `not`
2nd `and`
3rd `or`
Make sure to use parentheses to organize expressions. Keep your end goal in mind, that is what do you want the whole expression to ultimately evaluate to True or False.

### Truth Tables
Visualize the results of Boolean logic according to the results of individual variables.

|var a | var b | a and b | a and !b | !a or !b | !(a or b)|
|--|--|--|--|--|--|
|True | True | True | False | False | False|
|True | False | False | True | True | False|
|False | True | False | False | True | False|
|False | False | False | False | True | True|

`a and (b or c)` is the same as `(a and b) or (a and c)`

#### Demorgans Law
`!(a and b)` same as `!a or !b`
`!(a or b)` same as `!a and !b`

## Mathematical Operators

- `=` assignment operator , assigns a value from right to var on left
- `%` modulo , gives remainder of a division , use to check if a value is even 
if `value % 2` is 0 then value is even , `4 % 2` is 0 so even , when result is 1 it is odd
- `//` floor division , rounds down to whole number , `7//2` is 3 , notice no decimal
- `**` exponentiation , n1 raised to n2 , `8**2` is 64
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division

## Logical and Mathematical Operators
Both logical and mathematical operators can be combined in statements.
```
result = (a + b) > c
print(result)
```

If you use booleans with math operators they are treated as a 0 for `False` and a 1 for `True`.
```
2 * (True) # returns 2
2 * (False) # returns 0
```
## Relational Operators on Strings
`<` used for sorting strings alphabetically
`>` used for sorting in reverse alphabetical order
Capital letters are sorted before lowercase letters.

# Self Assignment
A variable appears on both sides of an assignment and the result from the right is assigned to the variable on the left.

## Increasing a Counter

```
count = 0
count = count + 1
```

This works because first the right side is assigned the values by replacing the var with the value and once completed its result is assigned to the left side.

Shortcut notation `count += 1`.

# Data Types

## Primitive
- **boolean**
- **integer** whole number
- **float** contains decimal
- **string**
- **complex**
- **NoneType**

Booleans such as `True` and `False` are interpreted as `1` and `0` and can have math operations acted on them.

`NoneType` describes a variable that has a value of none. This is different than a variable with no value assigned to it.

## Conversions
`type(var)` returns the data type of the var
`str(var)` changes the var type to a str type
`int(var)` changes a str comprised of digits with or without neg sign and changes it to int, returns `ValueError` if unsuccessful.
`bool(var)` changes a str to boolean and returns `False` if `var = 0` or empty returns `True` if var is any other value, returns `ValueError` if unsuccessful.
`float(var)` changes a str of pos or neg digits and with or without decimal to a float, returns `ValueError` if unsuccessful.

# Reserved Keywords
The following keywords are already used by Python so they are not to be used as variables.
`{and as assert break class continue def del elif else except False finally for from global if import in is lambda None nonlocal not or pass raise return True try While with yield}`

To see the list from python use
```
import keyword
print(keyword.kwlist)
```

If reserved keywords are used as variable names or function names then Python will return an error. 
Sometimes a reserved keyword can be assigned as a variable name, but then the original function for the keyword will no longer work.

# Tip
Multiple strings and outputs can be organized as follows.
```
print("some text {0}, more text {1}, more text {2}".format(var1 + var2 + var3))
```
In the code above the variables replace the indexes within the braces. This makes it easier to read the code.

# Dot Notation
Name to the right of the dot is a method belonging to the object on the left of the dot.
