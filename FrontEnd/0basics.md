# Resources

- learnpython.dev
- twitter @nnja
- practical.learnpython.dev

# Terminal

`python3` starts python
`quit()` exits
`CTRL + d` exits
`CTRL + l` clears screen

`help(somefunction)` lists info on how to use given function

# Variables

`somevar = None` declares an empty variable

# Functions

`def someFunction():` defines function

Format
- indent 4 spaces
- blank line after function end

```python
def somefunction():
    print("hiya")
    
somefunction()
```

# Arguments

**Default Argument**

```python
def someFunction(firstName,lastName=" last name not given"):
    print(firstName,lastName)
    
someFunction("pusheen")
```

# Data Structures

- `len()` length

# List

Lists can contain different data types.
Mutable.
Sorted.

`[]` empty list
`list()` empty list

`somelist = ["a","c","b",]` makes a list

`sorted(somelist)` sorts list ascending a,b,c
`sorted(somelist, reverse=True)` sorts list descending c,b,a

`somelist.sort()` sorts ascending , call function to view list
`somelist.reverse()` sorts descending , call function to view list

`somelist.append("muffin")` adds to end of list
`somelist.insert(0,"muffin")` adds to given index position
`list1.extends(list2)` appends list2 to list1

**Find**

`"pusheen" in somelist` returns true if found in list
`somelist.index("pusheen")` returns index position of first match
`somelist.count("pusheen")` returns total number of instances of given item in list

**ReAssign**

`somelist[0] = "hello kitty"` reassigns existing item at position 0 to hello kitty

Find and Replace
```python
pos = somelist.index("pusheen") // returns index position of pusheen
somelist[pos] = "hello kitty"   // replaces given position item with hello kitty
```

**Delete**

`somelist.remove("pusheen")` deletes first instance
`somelist.pop("pusheen")` deletes and returns last item
`somelist.pop(n)` deletes and returns item at given index

# Tuples

Tuples are immutable lists.
Ordered

- no reassignment
- no append
- no delete

Good for using as keys in a dictionary.

`sometuple = (1,2,3)` makes a tuple
`sometuple = (1,)` makes a tuple
`sometuple = 1,2,3` makes a tuple


**Unpacking*

`pet = ("suki","5","calico")` makes tuple called pet

`name,age,breed = pet` assigns given variables to items in pet , order matters
`name` returns suki
`age` returns 5
`breed` returns calico

# Sets

Collection of items.
Mutable.
Unsorted.

- only unique items , no duplicates

`set()` makes an empty set
`someSet = {"pusheen","hello kitty","pusheen"}` makes a set
`someset` returns `{"pusheen","hello kitty"}` since sets only contain unique items
`set(someList)` returns set of unique items found in given list

`someset.add("neko")` adds neko to set
`someset.discard("neko")` removes neko from set whether or not neko is in the set or not
`someset.remove("neko")` removes neko from set only if neko is in set , if not in set then returns error

`set1.update(set2)` appends set2 to set1 , always expects sets to be a sequence

example
```python
set1 = (1,2,3)
set2 = ("cat")
set1.update(set2)
```
Returns `(1,2,c,3,a,t)` since it separates the one string into a sequence of characters , order is random.

**Operations**

- `s1.union(s2)` - s1 | s2 , new set contains all items from each s1 & s2
- `s1.intersection(s2)` - s1 & s2 , new set contains items found only in both s1 & s2
- `s1.difference(s2)` - s1 ^ s2 , new set contains items from s1 but not from s2

# Dictionaries

Key Value pairs.
Dictionary is mutable.
Keys are immutable.
Not ordered.
Not indexible.

`{}` makes empty dictionary
`dict()` makes empty dictionary

`someDict = {"one":1,"two":2,"three":3}`

`someDict["one"}` returns value of given key only if key found , 1 , if not found returns error
`someDict.get["one","not found"}` returns value of given key if key found , if key not found returns not found

`someDict["four"] = 4` adds key value pair to dictionary
`someDict["one"] = "won"` replaces value of given key

`d1.update(d2)` appends d2 to d1

`someDict.keys()` returns keys
`someDict.values()` returns values
`someDict.items()` returns list of tuples comprising the key value pairs

**Example**

Add items to a list which is the value of a key.
```python
food = {"green":["asparagus"]}
food["green"].append("peas")
food
```
Returns `{"green":["asparagus","peas"]}`

# Strings

`myList = ["h","i","y","a"]`

**Slice**
`myList[0:2]` returns `["h","i"]`
`[:]` everything
`[:10]` from first to 10
`[10:]` from 10 to last

**Copy**
`newlist = myList[:]` copies all of my list and assigns it to given var newlist

**Reverse**
`myList[::-1]` returns list in reverse order

`myList.insert(4,"s")` returns `["h","i","y","a","s"]`

`"Cat".lower()` cat
`"Cat".upper()` CAT


# For Loops

`for item in items:` automatically loops through all elements of the given list

**Range**

`range(1,11)` list of numbers from 1 to 10
`range(1,11,2)` list of odd numbers from 1 to 10

**List**

```python
cats = ["suki","pusheen","cat"]
for cat in cats:
    print(cat)
```
Returns suki pusheen cat

**Dictionary**

Returns key value pairs.
```python
colours = {"r":"red","g":"green","b":"blue"}

for label,colour in colours.items():
    print(label,colour);
```
Needs `label` & `.items` in order to return both key value pairs.

Returns index and key as a tuple.
```python
colours = {"r":"red","g":"green","b":"blue"}

for i,colour in enumerate(colours):
    print(i,colour);
```

# Conditions

```python
a = False
b = True

if a:
    print("1")
elif b:
    print("2")
else:
    print("3")
```
**While**

Runs as long as condition is true.

```python
counter = 0
max = 5

while counter < max:
    print(counter)
    counter = counter + 1
```

# Control Statements

`break` exits loop , if multiple loops then breaks out of nested loop
`continue` returns to top of loop

Returns pusheen.
```python
names = ["suki","pusheen","hello kitty"]

for name in names:
    if name != "pusheen":
        continue
    print(name)
```

Continues through each name that does not match pusheen.

Returns hi cat , hi dog
```python
names = ["teridactyl","cat","dog","bird","cow"]

for name in names:
    if len(name) != 3:
        continue
    print("hi ",name)
    if name == "dog":
        break

print("finished")
```

# Files

`python3 somefile.py` runs given file

**Modules**

`import file1.py` imports code from given file into current file
`__main__` encapsulate code to keep variables from leaking out


file1.py
```py
if __name__ == "__main__":
    // some code
```

# Errors

Entering `int("a")` returns an error and hangs the program.
Look at the error log and copy the error type and place it in an except.
Place the code to run in a try.
Now the code will run to completion even when that specific error is caught.

```py
try:
    int("a")
except ValueError as e:
    print("oops",e)

print("program finished")
```

# External Modules

`python -m pip install someModule` installs module

`import someModule` add to file to import module

# Libraries

- requests , for making http requests easier

`python -m pip install requests`

somefile.py
```py
import requests

def create_query(languages,min_stars=50000):
    query = f"stars:>{min_stars} "
    
    for language in languages:
        query += f"language:{language} "
    return query

def repos_with_most_stars(languages):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    
    query = create_query(languages)
    parameters = {"q": query, "sort": "stars","order": "desc"}
    response = requests.get(gh_api_repo_search_url, params=parameters)
    
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError("oops",status_code)
    
    // print(response.text)
    else:
        response_json = response.json()["items"]
        return response_json
    
    //print(response_json.keys())
    
if __name__ == "__main__":
    languages = ["Python","Javascript"]
    results = repos_with_most_stars(languages)
    
    
    print("query is ",query)
    
    //print(len(results))
    //first_result = results[0]
    
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        
        print(name," is an ",language," repo with ",stars," stars")     
```

# Booleans

`any()` are any True
`all()` are all True

```python
any([True,False,True])
# returns True
```

```python
all([True,False,True])
# returns False
```