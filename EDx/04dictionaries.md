# Dictionary

A dictionary is a data structure comprised of key value pairs.
Easy to retrieve items within a dictionary since the user defines the keys. In contrast to lists which use indexes to access the items. 
Although indexes can be used ot access dictionary items , the order is not always maintained.
Keys must be immutable objects such as strings, integers, floats, and tuples.
But not mutable objects such as lists or dictionaries.

- **key** passed into a dictionary in order to retrieve a value
- **value** returned that corresponds to the key passed in

Declaring a dictionary `{ }`
```python
aDictionary = {"kittens":10,"kitties":4,"cats":2}
print(aDictionary)         # {'cats': 2, 'kittens': 10, 'kitties': 4}
```

Accessing Values

```python
print(aDictionary["cats"]) # 2
aDictionary["cats"] = 9    # changes value of key cats from 2 to 9
print(aDictionary["cats"]) # 9

myKittens = aDictionary["kittens"] # assigns value of key to variable
print(myKittens)                   # 10
```

Making a dictionary from a list

```python
aList = [("kittens",10),("kitties",4),("cats",2)]

aDict = {}
for catTuple in aList:
    aDict[catTuple[0]] = catTuple[1]  # assigns key value pair
```

Adding new key value pairs to a dictionary

```python
aDict = {"kittens":10,"kitties":4,"cats":2}
aDict["mews"] = 100  # adds key to dictionary and assigns its value
print(aDict)  # {'mews': 100, 'kittens': 10, 'kitties': 4, 'cats': 2}
```

Removing key value pairs from a dictionary

```python
aDict = {'mews': 100, 'kittens': 10, 'kitties': 4, 'cats': 2}
del aDict["mews"]  # removes key value pair
print(aDict)  # {"kittens":10,"kitties":4,"cats":2}
```

Incrementing key value counts

```python
# looks up key inside dictionary if found increments it by 1
# when not found creates new key and sets it equal to 1
if myKey in myDict:
    myDict[myKey] += 1
else:
    myDict[myKey] = 1

# same as above
if not myKey in myDict:
    myDict[myKey] = 0  # makes new key
myDict[myKey] += 1     # always increments the key
```

**Methods**

`someDict.keys()` returns list of keys from given dictionary
`someDict.values()` returns list of values from given dictionary
`someDict.items()` returns list of tuples where first item is the key and second item is the value

Use `.keys()` to iterate through keys and return the value for that key

```python
myDict = {"kittens":10,"kitties":4,"cats":2}

for key in myDict.keys():
    value = myDict[key]
    if value < 3:
print("We have",value,key)  # We have 2 cats
```

Use `.items()` to iterate either through keys or through values

```python
# itrate through keys
for (key,value) in myDict.items():
    if key == "kitties":
print("We have",value,key)  # We have 4 kitties

# iterate through values
for (key,value) in myDict.items():
    if value < 3:
print("We have",value,key)  # We have 2 cats
```

How to count words in a string

```python
myString = "This is just a random string made to fill up some space. It means nothing. Just a bunch of words. Wait, a long time ago in a galaxy far far away. There lived some space kittens. Who traveled in pirate ships. That's right they were space pirates. And did you know that in space there are sharks with lasers. If you scream in space they can hear you. It's just that no one cares."

# data cleaning
myString = myString.replace(".","") # removes periods
myString = myString.replace(",","") # removes comas
myString = myString.replace("'","") # removes apostrophes
myString = myString.lower()         # makes everything lowercase
splitString = myString.split()      # returns a list where each word is a separate item, words in string were separated by a space

# new dictionary
wordDict = {}
for word in splitString:    # for each word in the list of strings
    if word in wordDict:    # if word exists in wordDict
        wordDict[word] += 1 # overwrite the key and add 1 to its value
    else:                   # if word does not exist in wordDict
        wordDict[word] = 1  # make a key and set its value to 1
        
print(wordDict)             # result is a dictionary where the key is the word and the value is its count
```

Dictionary with a string key and a list value

```python
classes = {"Math":["Alice","Betty"],
          "Physics":["Chery","Debbie"],
          "CS":["Val","Julie"]}

# access one classroom
print(classes["Math"])  # ['Alice','Betty']

# add to one of the classrooms
classes["Math"].append("Chewy")
print(classes["Math"])  # ['Alice','Betty','Chewy']
```

Dictionary with a string key and a tuple value

```python
addressBook = {"Alice":("12 ave","1234567899","alice@gmail"),
              "Betty":("34 ave","9987654321","betty@gmail"),
              "Julie":("56 way","1231231234","julie@gmail")}

# all values for one key
print(addressBook["Julie"])     # ('56 way', '1231231234', 'julie@gmail')

# one particular value for one key
print(addressBook["Julie"][2])  # julie@gmail
```

Dictionary with a string key and a dictionary value

```python
addressBook = {"Alice":{"address":"12 ave","phone":"1234567899","email":"alice@gmail"},
              "Betty":{"address":"34 ave","phone":"9987654321","email":"betty@gmail"},
              "Julie":{"address":"56 way","phone":"1231231234","email":"julie@gmail"}}

# all values for one key
print(addressBook["Julie"])           # ('56 way', '1231231234', 'julie@gmail')

# one particular value for one key
print(addressBook["Julie"]["email"])  # julie@gmail
```

# Make a dictionary from a tuple.

```python
# list of tuples
cats = [('suki','small',5),
('pusheen','big',10),
('nero','med',8),
('dr. tana','med',12),
('sylvester','med',10),
('neko','small',4)]

cats_by_sizes = {}

for name, size, age in cats:
    if size in cats_by_sizes:
        cats_by_sizes[size].append((name,age))
    else:
        cats_by_sizes[size] = [(name,age)]

print(cats_by_sizes)

# returns dictionary where key is size and value is tuple name and age
{'small': [('suki', 5), ('neko', 4)], 'big': [('pusheen', 10)], 'med': [('nero', 8), ('dr. tana', 12), ('sylvester', 10)]}
```
