# Algorithms

A collection of a complex set of steps that transform input into output.
Data compression and random number generators are two examples of algorithms.

**Complexity**
Rate at which the number of operations required to run an algorithm grows based on the value of the input on which it operates

- **big o notation** worst case efficiency `O(n^2/2)` or simply `O(n^2)`
- **big omega notation** best case efficiency
- **big theta notation** typical case efficiency

|Type|O|# of Operations|Example|
|--|--|--|--|
|constant|O(1)|constant regardless of data size|does 1st name start with A|
|linear|O(n)|1 less than total data size|duplicates in a sorted list|
|quadratic|O(n^2)|increases square with increase in data size|duplicates in an unsorted list|
|polynomial|O(n^3)|increases cubic with increase in data size|triplicates in a list|
|exponential|O(2^n)|exponential increase with increase in data size|brute force password hacking|
|logarithmic|O(log(n))|slowly increases with square root size of data|binary search|
|loglinear|O(nlog(n))|slowly increases with square root size of data times size of data (most optimal)|merge sort|
|factorial|O(n!)|increases with factorial size of data|shortest possible route|

## Recursion

Function that calls additional copies of itself. Useful for breaking down a problem into smaller instances in order to solve them independently. Then combine the solutions to solve the original problem.

- **head recursion** recursive call occurs near beginning of function
- **tail recursion** recursive call occurs near end of function

Countdown using tail recursion.
```Python
def count_down1(start):
    if start <= 0:
        print(start)            # prints 0 when start is 0 or less
    else:
        print(start)            # displays current count
        count_down1(start - 1)  # calls itself again but decreases current count by 1

count_down1(5)                  # 5 4 3 2 1
```

Countdown using head recursion.
```Python
def count_down1(start):
    if start <= 0:
        print(start)            # prints 0 when start is 0 or less
    else:
        count_down1(start - 1)  # calls itself again but decreases current count by 1
        print(start)            # displays current count

count_down1(5)                  # 0 1 2 3 4 5
```

A Fibonacci sequence.
This implementation is very inefficient due to the multiple function calls through each iteration.
```Python
def Fibonacci(n):
    if n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2) # function called twice here
    else:
        return 1

print(Fibonacci(5)) # returns the sum of the last 2 Fibonacci numbers , 3 + 2 = 5
```

A simple exponent calculator.
```Python
def exponent_calc(base,expo):
    if expo == 0:
        return 1
    else:
        return base * exponent_calc(base,expo - 1)

print(exponent_calc(5,3))  # 125
```

## Sorting

**Bubble Sort**
Iterates through list one pair at a time. If a pair is in the wrong order it switches the pair. When done iterating through the list if any pairs were switched then it iterates again from the new sorted list. Continues to reiterate through each new sorted list until an iteration results in no pairs being switched. The result is a fully sorted list. Number of iterations is n - 1.
```Python
def sort_with_bubbles(lst):
    swap_occurred = True               # allows first iteration to happen
    while swap_occurred:               # if swap happened then run code
        swap_occurred = False
        for i in range(len(lst) - 1):  # ignore the last number in the list
            if lst[i] > lst[i + 1]:    # first number > second number
                temp = lst[i]          # assign first number to temp var
                lst[i] = lst[i + 1]    # reassign first number as second number
                lst[i + 1] = temp      # reassign second number as first number which is temp
                swap_occurred = True
        #print(lst)                    # displays the list after each iteration
    return lst

print(sort_with_bubbles([5,3,1,2,4]))   # 1 2 3 4 5
```

**Selection Sort**
Iterates through the list one item at a time. Finds the lowest item and moves it to the beginning of the list. Repeats the search with a new iteration beginning with the number next to the one it just moved. Number of iterations is n - 1.
```Python
def sort_with_select(a_list):
    for i in range(len(a_list)):
        minIndex = i                          # first item assumed to be lowest
        for j in range(i + 1,len(a_list)):
            if a_list[j] < a_list[minIndex]:  # checks value of current index j against value of minIndex
                minIndex = j                  # if current j is lower then it becomes the new minIndex
        minValue = a_list[minIndex]           # save current minimun value as minValue
        del a_list[minIndex]                  # delete min value from its current index
        a_list.insert(i,minValue)             # insert min value at the new index
    return a_list

print(sort_with_select([5,3,1,2,4]))          # 1 2 3 4 5
```

**Insertion Sort**
Iterates through the list one item at a time. Compares current item with items previous to it. If current item is lower than previous item or set of items it moves item to the beginning. If current item is more than previous item or set of items it leaves item where it is. If current item is between previous set of items it places item between them. Iterations run until the last item is reached and placed in the correct location. Number of iterations is n - 1.

**Merge Sort**
Splits a list into individual lists containing one item. Then merges 2 lists by comparing the first item in each list and removing the smaller item. This item is placed in a new list and the other item is placed after it. This process is recursive and continues until all the lists are empty. Resulting in one sorted list. Number of iterations is n log n.
```Python
def merge_sort(a_list):
    if len(a_list) <= 1:                        # when the list consists of only 1 item return that list
        return a_list
    else:                                       # while the list has more than 1 item
        midpoint = len(a_list) // 2             # gives index of the middle value in the list
        left = merge_sort(a_list[:midpoint])    # returns the left half of the original list
        right = merge_sort(a_list[midpoint:])   # returns the right half of the original list
        new_list = []                           # list where the smaller values will be added
        while len(left) and len(right) > 0:     # while both lists contain more than 1 item , compare the first item of each list
            if left[0] < right[0]:              # if left first item smaller than right first item
                new_list.append(left[0])        # add value of left first item to new list
                del left[0]                     # delete left first item from original list
            else:                               # if right first item smaller than left first item
                new_list.append(right[0])       # add value of right first item to new list
                del right[0]                    # delete right first item from original list
                                                # while loop ends when one of the lists is empty
        new_list.extend(left)                   # adds remainder of items in left list to new list, since already sorted
        new_list.extend(right)                  # adds remainder of items in right list to new list, since already sorted
        return new_list

print(merge_sort([2,5,3,8,6,9,1,4,7]))          # [1,2,3,4,5,6,7,8,9]
```

## Searching

Given a list and a search value as inputs search algorithms return the index of the value.

**Linear Search**
Each item in the list is checked for a match and its index is returned if found. Works on sorted and unsorted lists. Number of iterations is n.

**Binary Search**
Selects middle item in the list or one lower or higher if no middle. Compares that item with the search value and returns one of three results the item is higher,the item is lower, the item is found. If found returns current item index. If current item is higher then returns first half of list. If current item is lower then returns second half of list. Selects middle item of new list and repeats process until item is found. Items can be integers,strings,dates. Number of iterations is log n.
```Python
def binary_search(searchList,searchTerm):
    searchList.sort()
    minimum = 0
    maximum = len(searchList) - 1
    while minimum <= maximum:                         # while items are in list search for item
        currentMiddle = (minimum + maximum) // 2
        if searchList[currentMiddle] == searchTerm:   # middle term is the search term , returns True
            return True
        elif searchTerm < searchList[currentMiddle]:  # if search term less than middle term , search first half of list
            maximum = currentMiddle - 1
        else:
            minimum = currentMiddle + 1               # if search term more than middle term , search second half of list
    return False                                      # search term not found , returns False

integers = [10,11,5,9,30,2]
names = ["Cat","Hello Kitty","Kittens","Suki"]

print("9 is in integers",binary_search(integers,9))
print("Hello Kitty is in names",binary_search(names,"Hello Kitty"))
```
