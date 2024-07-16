# Var Assignements

Use `=` to declare a variable and its content.

Variable on left of `=` and content on right

`salutation = "hiya"`

Delete a variable while not deleting the content.

`del salutation`

Delete an item via its index.
```python
salutation = ["hi","hiya","hello"]

print(salutation)
# ['hi', 'hiya', 'hello']

del salutation[0]

print(salutation)
# ['hiya', 'hello']
```

# Strings

f strings `print(f"{var} is a var)`

# Strings

escape characters with `\`
`'I can\'t wait to see ya'`

`\n` new line
`\t` tab

```python
multiplelines = '''a
b
c'''
```

# User Input

```python
print("what's your favourite food?")

favourite_food = input()

print("wow, I also like",favourite_food)
```

# Numbers

`int()` integer
`float()` decimal

# Decimals

```python
print(f'{1.5:.1f} {1.5:.2f} {1.5:.3f}')
# 1.5 1.50 1.500
```

# While

function runs while condition returns true

```python
i = 1
while i*i < 100:
  print(f'square of {i} is {i*i}')
  i += 1
print('all done')
```

# For

function runs once for each element in list

```python
n = 0
for i in [1,2,3]:
  print(f'{n} + {i} is {n + i}')
  n += i
  # print(f'{n}')
print(f'total is {n}')
```

```python
for i in range(3):
  print('oi')
print('you')
```

# Matrix

multiplication table
```python
for i in range(1,11):
  for j in range(1,11):
    print(f"{i*j:>4}",end="")
  print()
```

returns
```
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100
```

# If

```python
user_input = input("enter a number ")
n=float(user_input)
if n > 0:
  print("your number is positive")
elif n < 0:
  print("your number is negative")
else:
  print("you entered 0")
```

# Break

```python
l = [3,2,1,0,-1,-2,-3]
for n in l:
  if n < 0:
    break
print(f"I broke out at {n}")

#  3 2 1
# I broke out at -1
```

# Continue

```python
l = [3,2,1,0,-1,-2,-3]
for n in l:
  if n < 0:
    print(f"{n}")
    continue
print(f"I stopped at {n}")

# -1 -2 -3
# I stopped at -3
```

# Combinations

All combinations of 2 dice adding to 5.

```python
for i in range(1,7):
  for j in range(1,7):
    if (i + j) == 5:
      print(f"{i},{j}")

# 1,4 2,3 3,2 4,1
```

# Functions

```python
def doubleUp(x):
  """
  This function doubles x.
  """
  return x*2

print(doubleUp(10))
print(doubleUp('hi'))

# 20
# hihi
```

# Docstring

The triple quoted comment inside a function.
Used for example to explain what the function does or any gotchas to watch out for.

`help(doubleUp)` displays the given function's docstring
`print(doubleUp.__doc__)` displays the given function's docstring

use `help()` to display docstrins for any of Python's built in functions

# Parameters & Arguments

Parameters appear in the function definition.
Arguments appear in the function call.

```python
def sumUp(alist): # alist is the paramater
  """
  the alist is passed as a parameter into the function
  the elements of the alist are used as arguments by the function
  """
  total = 0
  for i in alist:
    total = total + i;
  return total

print(sumUp([1])) # value 1 is the argument
print(sumUp([1,2,3])) # values 1 2 3 are the arguments

# 1
# 6
```

# Scope

Variables defined inside functions are not accessible outside the function.

Variables defined inside functions where a global variable with that name already exists do not alter the global variable.

To bind or rebind a global variable from within a function use `global varname`.

**Global**

Unbound to global.
```python
i = 10
def someFunction():
  i = 0
  print(i)

print(i)       # 10
someFunction() # 0
print(i)       # 10
```

Bound to global.
```python
i = 10
def someFunction():
  global i
  i = 0
  print(i)

print(i)       # 10
someFunction() # 0
print(i)       # 0
```

**Local**

Nested functions also scope their variables. To bind a local variable to the immediate outer scope function use `nonlocal`.

Unbound to outer.
```python
def outerFunction():
  i = 10
  def innerFunction():
    i = 0
    print(i)
  innerFunction()
  print(i)
outerFunction()
# 0
# 10
```

Bound to outer.
```python
def outerFunction():
  i = 10
  def innerFunction():
    nonlocal i
    i = 0
    print(i)
  innerFunction()
  print(i)
outerFunction()
# 0
# 0
```

# Sort

`someList.sort()` mutates list , optional parameter `reverse=True`
`sorted(someList)` does not mutate list , optional parameter `reverse=True`

```python
l1 = [2,6,1,2,9,3,7,5]

sortl1 = l1.sort()
print(f"l1 sort {sortl1}")
print(f"li {l1}")

l2 = [2,6,1,2,9,3,7,5]
sortl2 = sorted(l2)
print(f"l2 sorted {sortl2}")
print(f"l2 {l2}")

# l1 sort None                 displays None because sort() does not return anything, it mutates the original
# li [1, 2, 2, 3, 5, 6, 7, 9]  original list is sorted
# l2 sorted [1, 2, 2, 3, 5, 6, 7, 9]  displays sorted copy of original
# l2 [2, 6, 1, 2, 9, 3, 7, 5]         original list is unchanged
```

# Combine Sequences

Merge sequences onto a tuple.

```python
l1 = ['a','b','c']
l2 = [1,2,3]

zipped = zip(l1,l2)   # returns a zipped object
listed = list(zipped) # returns the zipped object as a list
print(listed)

# [('a', 1), ('b', 2), ('c', 3)]
```

```python
days = "mo tu we th fr sa su".split()
climates = "sunny windy sunny cold warm nice sunny".split()
temps = [11,9,11,8,10,9,10]

for day,climate,temp in zip(days,climates,temps):
  print(f"On {day} it was {climate} and {temp} celsius.")

# On mo it was sunny and 11 celsius.
# On tu it was windy and 9 celsius.
# On we it was sunny and 11 celsius.
# On th it was cold and 8 celsius.
# On fr it was warm and 10 celsius.
# On sa it was nice and 9 celsius.
# On su it was sunny and 10 celsius.
```

# Dictionaries

```python
d = dict(one=1,two=2,three=3)
print(d.keys())
print(d.values())
```

# Sets

A set is dynamic and unordered. The elements must be hashable. Each unique element is counted once.

**Create Set**

`s = set([1,2,3,'a','b','c',3,2,1])`

**Example**

```python
word = "stippsi"
wordLength = len(word)
uniqueLetters = len(set(word))
print(f"{word} has {wordLength} letters and {uniqueLetters} are unique")
# stippsi has 7 letters and 4 are unique
```

**Set Operators**

`|` or

`&` and

`-` difference

`^` symmetric difference

**Methods Non Mutating**

where `s1 = set([1,2,3])` and `s2 = set([2,3,4])`

`s1.copy()`

`s1.issubset(s2)`

`s1.issuperset(s2)`

`s1.union(s2)` or `s1|s2`

`s1.intersection(s2)` or `s1&s2`

`s1.difference(s2)` or `s1-s2`

`s1.symmetric_difference(s2)` or `s1^s2`

Examples
```python
s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1.union(s2))
print(s1|s2)
# {1, 2, 3, 4}
# {1, 2, 3, 4}

print(s1.intersection(s2))
print(s1&s2)
# {2, 3}
# {2, 3}

print(s1.difference(s2))
print(s1-s2)
# {1}
# {1}

print(s2.difference(s1))
print(s2-s1)
# {4}
# {4}

print(s1.symmetric_difference(s2))
print(s1^s2)
# {1, 4}
# {1, 4}
```

**Methods Mutating**

`s.add()`

`s.clear()`

`s.discard()`

`s.pop()`

`s.remove()`

# In

Checks if an iterable contains the passed element and returns boolean `True` or `False`.

```python
print(1 in [1,2])
print("cat" in "cats")
print("kat" in "cats")
# True
# True
# False
```

```python
words = ["house","boat","puppy","kitten"]

def dist_chars(wordlist):
  wordDict = {}
  for word in wordlist:
    wordDict[word] = len(set(word))
  print(wordDict)

dist_chars(words)
# {'house': 5, 'boat': 4, 'puppy': 3, 'kitten': 5}
```

# Unpack

By declaring multiple variables on the left of `=` the elements within an iterable on the right are assigned to each variable on the left.

Unpack a list.
```python
one,two = [1,2]
print(one,two)
# 1 2
```

Unpack a string.
```python
one,two,three = "cat"
print(two)
# a
```

Unpack a dictionary.
```python
d=dict(a=1,b=2)
key1,key2 = d

print(d)
print(key1,key2)
print(d[key1])

# {'a': 1, 'b': 2}
# a b
# 1
```

```python
d=dict(a=1,b=2)

for i,j in d.items():
  print(f"the key is {i} and it's value is {j}")

# the key is a and it's value is 1
# the key is b and it's value is 2
```

# Reverse Dictionary Order

```python
d = {"caldo":"hot in italian","caliente":"hot in spanish","chaud":"hot in french","cold":"cold in english"}

def switchOrder(someDic):
  newd = {}
  for i,j in someDic.items():
    newd[j] = i
  print(newd)

switchOrder(d)

# {'hot in italian': 'caldo', 'hot in spanish': 'caliente', 'hot in french': 'chaud', 'cold in english': 'cold'}
```

# List Comprehension

A one line manner of writing a 

Via for loop.
```python
l = []
for i in range(1,11):
  l.append(i**2)

print(l)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Via list comprehension.
```python
l = [i**2 for i in range(1,11)]
print(l)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
