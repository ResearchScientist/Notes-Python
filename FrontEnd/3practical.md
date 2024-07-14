# Virtual Environment

`python3 -m venv env` starts python in a virtual environment , for keeping all libraries in the same version

# VS Code Packages

- pylance

# REPL

Python in terminal.

- `python3` starts editor
- `help()` docs on given function or given function.somemethod , `space` continue , `q` exits
- `type()` returns type
- `dir()` returns methods available to given function

# Nums

`x = 0` int
`x = 0.` float
`x = 0a` complex

**Type Conversion**

`int()`
`float()`

**Maths**

`25 / 5` returns 5.0 , float
`25 // 5` returns 5 , integer

`round()`

# Strings

mystring = "string"

`f"hi {name}"`

Replace string
```python
name = "pusheen"
name.replace("p","q")
# returns 'qusheen'
name
returns 'pusheen'
```

# List

`len()`
`someList[0]` returns first index
`sorted(someList)` returns sorted list, does not change original list
`someList.sort()` sorts given list

`10 in someList` returns True if 10 in list False if not in list

`someList.pop()` removes last item

# Hash

Only immutable items can have a hash.

- `hash()` returns hash for given item

# Empty List

If making an empty list, put it inside the function and give the argument a type of None.
```python
def thing(my_list=None):
    if my_list == None:
        my_list = []
    my_list.append('stuff')
    return my_list
    
```

# Boolean

Use `is` for comparisons.
`a is True` true
`a == True` false , not pythonic

- `and`
- `or`
- `not`

# Function

```python
def addnums(x,y,operation="add"):
    if operation == "add":
        return x + y
    else:
        return x - y

addnums(1,2)
# returns 3
addnums(1,2,operation="nah")
# returns -1
```

```python
colours = {'r':'red','g':'green','b':'blue'}
for colour in colours:
    print(colour)

# r , g , b
colours.items()
# returns items([('r':'red'),('g':'green'),('b':'blue')])

for key,value in colours.items():
    print(key)
    print(---)
    print(value)
    
# returns
# r
# ---
# red
# g
# ---
# green
# b
# ---
# blue
```

# For

```python
def return_target(target="cat"):
    for name in names:
        if name == target:
            return name
            
return_target()
# cat

return_target(target="bird")
# bird
```

# Files

**Open**

`somefile = open("somefile.txt")` opens as read and saves to var given
`somefile = open("somefile.txt","w")` opens as write and saves to var given , replaces existing file
`somefile = open("somefile.txt","a")` opens as write and saves to var given , appends to end of existing file

**Close**

Closes open file when finished.
```python
with open("somefile.txt") as somefile:
    contents = somefile.read()
```

# Exceptions

Use one exception for each error.

```python
try:
    x = something
except ValueError:
    print('a value error')
except KeyError:
    print('a key error')
```

# Main

Encapsulates code so that when code is shared only the prototype is exported.

`__main__`

# Import

**Included Libraries**

- random
- unittest

`import random` gets full library
`from random import randint` gets only given item from library

**External Libraries**

`pip install requests` installs requests library

# Modules

Custom functions.

`import myFunction`
`from myFunctions import addNums`

# Frameworks

- django
- flask
