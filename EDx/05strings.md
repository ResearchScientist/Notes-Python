# String

- **character** a single letter, number, symbol
- **unicode** standard hexadecimal codes for characters
- **hexadecimal** 16 characters comprised from 0 to 9 and A to F

`ord()` returns unicode for given character
`chr()` returns character for given unicode

Declaring a string. `" "`
```
string1 = "123" # 123
string2 = '123' # 123
string3 = "Hi" # Hi
string4 = 'Hi' # Hi
string5 = "'Hi'" # 'Hi'
string6 = '"Hi"' # "Hi"
string7 = '''"'Hi'"''' # "'Hi'"
string8 = ''''"Hi"'''' # error
```

**Escape Characters**
`\n` line break
`\t` tab spaces
`\'` displays '
`\"` displays "
`\\` displays \

**String Concatenation**
Joining two or more strings to form one new string.
```
string1 = "abc"
string2 = "def"
string3 = string1 + string2

print(string3) # "abcdef"
print(string1 + string2) # "abcdef"
```

**String Slicing**
Obtaining a substring from a string.
```
string = "Hi cutie"

string[0] # H
string[0:2] # Hi
string[3:] # cutie
string[:2] # Hi

string = "123456789"

string[1:9] # 2345678
string[0:10:2] # 2468
string[::2] # 2468
string[::3] # 369
string[-1] # 9
string[-10] # IndexError: string index out of range
string[-3:] # 789
string[:-3] # 123456
```
Possible to use slicing in a loop.
```
for i in "0123456789"[::4]:
    print(i) # 0 4 8
```
Even possible to slice a slice in a loop.
```
for i in "0123456789"[6:][:2]:
    print(i) # 67
    
# first slice [6:] gives 6789
# second slice [:2] slices 6789 and gives 67
```

**IN**
Boolean that checks if a string is within another string.
```
def has_string(search,key):
    if search not in key:
        return search + " not found"
    else:
        return search + " found"
    
print(has_string("hi","hiya")) # hi found
```

**FIND**
Method that returns first index of string within another string, returns -1 if string not found within the other string. `.find(text,[start],[end])` start and end are optional index parameters to narrow the search.
```
string = "abcd"
print(string.find("cd")) # 2
```
Find multiple instances of a string.
```
string = "abc123abc123abc123"
find_this = "abc"
current_index = string.find(find_this)

while current_index >= 0:
    print(find_this, "found at", current_index)
    current_index = string.find(find_this, current_index + 1)
    
# abc found at 0
# abc found at 6
# abc found at 12
```

**COUNT**
Method that returns number of instances one string is inside another.
`.count(string)`
```
string = "abc123abc123abc123"
find_this = "abc"

print("There are a total of", string.count(find_this), find_this, "in", string)

# There are a total of 3 abc in abc123abc123abc123
```

**SPLIT**
Method that takes a string and splits it based on a value given. Returns a list of strings. If no value given then split is made on spaces. `.split(someSeperator)`
```
string = "Hi there"
print(string.split(" ")) # ['Hi', 'there']
```

**JOIN**
Method that joins individual items in a string or list with the given character or string.
`"someValue".join(someStringOrList)
```
nums = "123"
print("and".join(nums)) # 1and2and3

nums = "1 2 3"
print("and".join(nums)) # 1and and2and and3

word = "hi"
print("and".join(word)) # handi

words = ["Hi","there"]
print("-".join(words)) # Hi-there
```
