# Map

**Syntax**

`map(someFunction,someList)`

- Takes 2 parameters : a function and a list.
- Parameter function operates on each element of the list.
- Parameter function receives one value an returns one value.
- Map function returns a map object.
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
