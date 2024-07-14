# List

Data structure that contains multiple values accessed via an ordered numerical index.

-**list** mutable list like structure
-**tuple** immutable list like structure

**Tuple**
Although tuples can contain heterogeneous data types, any actions performed on those types must be valid for each data type.

Declaring a tuple. `( )`

Packing a tuple.
```python
tuple1 = (1,2,3)

var1 = 1
var2 = 2
var3 = 3
tuple2 = (var1,var2,var3)

tuple3 = ("hi","there")

var1 = "hi"
var2 = "there"
tuple4 = (var1,var2)
```

Unpacking a tuple. Allows for assigning new variables to point to the values stored in the tuple.
```python
(newvar1,newvar2,newvar3) = tuple2

(newvar1,newvar2) = tuple4
```

Tuple Example
```python
# cat team where a list contains 3 tuples, one tuple per member
teamcat = [('suki','small',5),
('pusheen','big',10),
('nero','med',15)]

for name, size, age in teamcat:
    print('name ' + name + '\n size ' + size + '\n age ' + str(age))

# Returns
name suki
 size small
 age 5
name pusheen
 size big
 age 10
name nero
 size med
 age 15
```

**List**

All operations described above for strings and tuples can also be applied to lists. Lists are similar to tuples with the addition that lists are mutable.

Furthermore lists can contain combinations of lists and tuples and tuples can contain combinations of lists and tuples.

Declaring a list. `[ ]`
```
list1 = [1,2,3]

var1 = "a"
var2 = "b"
var3 = "c"
list2 = [var1,var2,var3]
```

Methods (list specific)

`someList.sort()` sorts integers from smallest to largest and letters into alphabetical order
`someList.append(someItem)` adds item given to the end of the list
`someList.extend(someOtherList)` adds values from someOtherList and adds them to the end of the list
`someList.insert(index,value)` adds given value to the given index
`someList.remove(value)` removes value given from the list
`someList.reverse()` reverses the current order of the list
`someList.pop()` removes last item from the list and returns it
`someList.index(value)` returns index of given value
`someList.copy()` returns a copy of the list
`someList.clear()` removes all items from the list

`sorted(someList, key=itemgetter(index))` unlike sort which only sorts according to the first index in a tuple, sorted sorts a tuple based on any index given, before using this function `from operator import itemgetter, attrgetter` must be imported

`del someList[:]` not a method, but similar to slicing

Adding to a list
When setting `newlist = oldlist` both lists point to the same values in memory. They reference the same list.
```
list = [1,2,3]
def combo(oldlist):
    oldlist.append(4)
    newlist = oldlist
    print(newlist) # [1,2,3,4]
    newlist.append(5)
    print(newlist) # [1,2,3,4,5]
    return newlist
    
print(combo(list)) # [1,2,3,4,5]
print(list)        # [1,2,3,4,5]
```

When setting `newlist = oldlist + (something)` both lists point to different values in memory. They reference different lists.
```
list = [1,2,3]
def combo(oldlist):
    newlist = oldlist + [4]
    print(newlist) # [1,2,3,4]
    newlist.append(5)
    print(newlist) # [1,2,3,4,5]
    return newlist

print(combo(list)) # [1,2,3,4,5]
print(list)        # [1,2,3]
```

When making changes to a nested list, those changes persist outside the function.
```
list = [1,2,3,["a","b","c"]]
def combo(oldlist):
    newlist = oldlist + [4]
    print(newlist) # [1,2,3,['a','b','c'],4]
    newlist[3][0] = 0
    print(newlist) # [1,2,3,[0,'b','c'],4]
    return newlist

print(combo(list)) # [1,2,3,[0,'b','c'],4]
print(list)        # [1,2,3,[0,'b','c']]

```

**Multi Dimensional Lists** are lists within lists

**2 Dimensional List**

The following code returns a list of average grades per student. The input is a list of students that contains lists of each students grades.
```
def student_grades_averages(student_grades):
    result = []
    for student in student_grades:
        sums = 0
        for grade in student:
            sums += grade
        result.append(sums/len(student))
    return result

allStudentGrades = [[91,95,89,92,85],
                   [85,87,91,81,82],
                   [79,75,85,83,89],
                   [81,89,91,91,90],
                   [99,91,95,89,90]]

print("averages:",student_grades_averages(allStudentGrades))
# averages: [90.4, 85.2, 82.2, 88.4, 92.8]
```

**Stack**
A list like structure. Items are not able to be inserted anywhere inside the stack. Nor accessed from inside the stack.
Items can only be added to the top. And can only be removed from the top. Once removed then an item can be accessed.
The last item added is the first item removed.

**Queue**
A list like structure. An item cannot be accessed until it is removed.
The first item added is the first item removed.

**Linked List**
A list in which only the first item is allocated an index. Within that location it points to the next items location. The next item points to the following items location and so on. Useful for improving performance in older programming languages. Not really an issue for modern programming languages.
