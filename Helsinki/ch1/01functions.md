
# Functions

- [Map](#map)
- [Lambda](#lambda)
- [Filter](#filter)
- [Reduce](#reduce)

# Map

**Syntax**

`map(someFunction,someList)`

- Takes 2 parameters : a function and a list.
- Parameter function operates on each element of the list.
- Parameter function receives one value an returns one value.
- Map function returns an iterable map object.
- To view the map object convert it to a list.

```python
numbers = [1,2,3]

def doubleThem(someNumbersList):
  return 2*someNumbersList

mappedDoubleThem = map(doubleThem,numbers)
print(mappedDoubleThem)
# <map object at>

listMappedDoubleThem = list(mappedDoubleThem)
print(listMappedDoubleThem)
# [2, 4, 6]
```

**String To Int**

In order to perform mathematical operations, convert any strings to integers or floats.
This is useful when reading files such as `.csv` where numbers are usually read as strings and thus need to be converted to integers.

Traditional method.
```python
string = "1 2 3"
print(type(string))
# <class 'str'>

list = string.split()
print(type(string))
# <class 'list'>

def adds(something):
  total = 0
  for some in something:
    some = int(some)
    total = total + some
  print(total)

adds(list)
# 6
```

Map method.
```python
string = "1 2 3"
print(type(string))
# <class 'str'>

list = string.split()
print(type(list))
# <class 'list'>

adds = sum(map(int,list))

print(adds)
# 6
```

# Lambda

An anonymous function. Useful when the function will only be used once and not needed anywhere else in the program.

**Syntax**

`lambda parameter1,parameter2 : someExpression`

- takes any number of parameters, and an expression that uses those parameters

**Example**

Within A Map Function

```python
L = [1,2,3]
square = map(lambda x : x**2,L)
squareList = list(square)

print(squareList)
# [1, 4, 9]
```

# Filter

- takes 2 parameters : a function and a list
- function takes only one parameter
- function returns `True` or `False`
- returns new list with elements matching `True` condition

**Example**

Return Only Even Integers
```python
L = [1,2,3,4,5]

def is_it_even(n):
  return n % 2 == 0 # even
  # return n % 2 == 1 # odd

filter_even = filter(is_it_even,L)
list_even = list(filter_even)

print(filter_even)
# <filter object>

print(list_even)
# [2, 4]
```

# Reduce

Takes 3 parameters

- a function
- an iterable
- a starting value (if none given then 1st item in iterable is used)

The function `reduce` is a python core function but must be imported prior to use.

```python
from functools import reduce
```

**Example**

Traditional sum function.

```python
L = [1,2,3]

def adds(l):
  s=0
  for n in l:
    s = s+n
  return s

print(adds(L))
# 6
```

Using reduce function.

```python
from functools import reduce

L = [1,2,3]

reduced = reduce(lambda a,b:a+b,L,0)

print(reduced)
# 6
```

