# CSV

**Split**

`someString.split(",")` splits given file based on given parameter , returns list

```python
someString = "suki,5,calico"

someString.split(",")

# returns ["suki","5","calico"]
```

```python
someString = "suki,5,calico"

name,age,breed = someString.split(",")

name
# suki
age
# 5
breed
# calico
```

**Join**

```python
some_list = ['this','is','a','comma','seperated','list']

": ".join(some_list)

# returns string 'this: is: a: comma: seperated: string'
```

```python
some_list = ['this','is','a','comma','seperated','list']

" ".join(some_list)

# returns string 'this is a comma seperated string'
```

# Type Casting

`str()` or `" "` casts as string
`int()` casts as integer
`float()` casts as float

# List Comprehension

`[someAction for item in items]` shorthand for loop with append to a new list

Returns ordered list.
```python
{num * num for num in range(11)}
# [0,1,4,9,16]
```

```python
names = ["cat","bird","dinosaur"]
[name.upper() for name in names]

# returns `["CAT","BIRD","DINOSAUR"]`
```

```python
names = ["cat","bird","dinosaur"]
", ".join([f"pet is {name}" for name in names])

# returns `'pet is cat, pet is bird, pet is dinosaur'`
```

```python
[num * num for num in range(6) if num % 2 == 0]
# returns [0,4,16]
```

```python
even_squares = [num * num for num in range(6) if num % 2 == 0]
", ".join([str(even_square) for even_square in even_squares])
# returns '0,4,16'
```

# Set Comprehension

Returns randomly unordered set.
```python
{num * num for num in range(11)}
# {0,16,4,9}
```

# Dictionary Comprehension

Returns ordered dictionary.
```python
{num: num * num for num in range(5)}
# {0:0,1:1,2:4,3:9,4:16}
```

# Maths

`sum()`
`min()`
`max()`
`sorted()`

```python
import random
random randint(0,10)
```

# Generators

Memory efficient way of calculating values.

`(someComprehension)` wrapping any comprehension with `( )` makes a generator

`sum(someComprehension)` can use maths on generators

# Zip

Combines two lists into a dictionary.

`zip(list1,list2)`

```python
players = ["cat","bird","teridactl"]
scores = [10,15,200]

# makes dictionary
zip(players,scores)

# displays dictionary items
for item in zip(players,scores):
    print(item)

# displays name and score for each player on separate lines
for name,score in zip(players,scores):
    print(f"{name} score is {score}")
```

```python
players = ["cat","bird","teridactl"]
scores = [10,15,200]

# shorthand for all of above
[f"{name} score is {score}" for name, score in zip(players,scores)]
```

# Exception Errors

Unhandled exceptions halt the execution and exit the running program.

`CTRL + c` stops currently running program

```python
try:
    num = int(user_input)
    print("yay you entered a num")
except ValueError:
    print("you did not enter a num")
```

```python
def division(num):
    try:
        result = 3.14 / num
    except ArithmeticError:
        print("math error")
    except ZeroDivisionError:
        print("divide by zero error")
```

**Custom Exception**

```python
class GitHubError(Exception):
    def __init__(sefl,status_code):
        if status_code == 403:
            message = "rate limit reached"
        else:
            message = f"status code is: {status_code}"
        super().__init__(message)
```

# Standard Library

Included libraries.

- math
- json

# Modules

`from somefile import somefunction`
`from print import pprint as pp`

`pip install someModule`

# Terminal User Input

**Display Input**

```pyton
import sys

arguments = sys.argv[1:]
print(f"you typed: {arguments}")
```

**Interactive Input**

```python
name = input("what is your name? ")

print(f"hi {name}")
```

# Testing

Tests are usually kept in a separate file called test.py.

**Assertion**

For simple debugging.
Not for production.

`assert a > 0` returns true or false
`assert a < 0` returns true or false

`assertEqual(a,b)`
`assertNotEqual(a,b)`
`assertTrue(x)`
`assertFalse(x)`
`assertIs(a,b)`
`assertIsNot(a,b)`
`assertIn(a,b)`
`assertNotIn(a,b)`

**Unit**

somefile.py
```python
def multiply(x,y):
    return x * y
```

test.py
```python
import unittest

class TestMultiply(unittest.TestCase):
    
    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x,test_y),50,"result should be 50") # displays string if result not 50
        
if __name__ == "__main__":
    unittest.main()
```

*Basic Results*

terminal
```bash
python3 test.py
# returns ran 1 test ok
```

*Verbose Results*

Must remove from test.py
```python
if __name__ == "__main__":
    unittest.main()
```

terminal
```bash
python3 -m test.py mult -v
# returns detailed explanation of each test and its result
```

# Frameworks

- flask , lightweight for webapps and APIs
