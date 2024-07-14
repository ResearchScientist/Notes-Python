# Control Structures
Statements that control the flow of the program. They control when other lines of code run. These are **Conditionals**, **Loops**, **Functions**, and **Error Handling**.

- **scope** the reach of a program's execution , that is what variables and functions can it access
- **global var** created before functions , available to all functions in the program
- **local var** created within a function , available to only that function

True for most programming languages. But specifically to Python the scope of a variable or function begins once the variable or function has been created and is available to all functions appearing afterwards.

Caveat, if a variable is declared within a loop then its value will be reset to its declared value at the beginning of each iteration. In order to have the variable update and not reset itself then it must be declared outside of the loop.

# Conditionals
Execute code based on certain conditions. The conditions can combine relational and mathematical expressions but the result must evaluate to a boolean `True` or `False`. The logical expression or condition can be enclosed in `()` but not necessary. Ending the condition with `:` is required.
```
if/elseif/else logical expression :
    code block
```

## if
Executes code when `if` condition is `True`. 
Multiple `if` statements can follow each other. Each will run when the preceding one is `True`.
```
if(logical expression == True):
    run this code block
```

## else
Executes code when `if` condition is `False`.
```
if(logical expression == False):
    skip this code block
else:
    run this code block
```

## elif
Executes code when `if` condition is `False` and `elseif` condition is `True`. 
Can have multiple `elif` between one `if` and one `else`.
```
if(logical expression == False):
    skip this code block
elif(logical expression == False):
    skip this code block
elif(logical expression == True):
    run this code block
else:
    skip this code block
```
## Nested Conditional
A conditional statement within another conditional statement. A nested conditional tests its condition only if its parent condition is `True`.
```
if(logical expression 1 == True):
    if(logical expression 2 == True):
        if(logical expression 3 == True):
            print("all 3 True")
        else:
            print("logical expression 3 not true")
    else:
        print("logical expression 2 not true")
else:
    print("logical expression 1 not true")
```
Similarly
```
if(logical expression 1 == True):
    print("logical expression 1 true")
else:
    if(logical expression 2 == True):
        print("logical expression 2 true")
    else:
        if(logical expression 3 == True):
            print("logical expression 3 true")
        else:
            print("logical expressions 1,2,3 not true")
```

# Loops
Execute code multiple times.

- **iteration** one execution of a repeated block of code

## for
Runs a block of code for a predetermined number of iterations.
- **loop control variable** variable that tracks how many times a loop has ran (i j k)
- `range()` function that returns a list to iteriate through. First parameter is starting number, second parameter is ending number - 1, optional third parameter is number to count by. Use neg to count backwards.

```
for i in range(1,11):
    print(i)
    
for i in range(10,0,-1):
    print(i)
```
Can be used to iterate through a string or list.
```
astring = "hiya"
for i in range(0,len(astring)):
    print(i,astring[i])  // displays every character and its index

alist = ["I","like","you"]
for i in range(0,len(alist)):
    print(i,alist[i])  // displays every word and its index
```

## for each
A `for` loop in which the length of a list determines the number of iterations and the items within the list are loaded into a variable for use by the block of code within the function. 
Python makes working with lists and strings easier by iterating through the list that is given after `in` and passing each value into the variable given before `in`. The code below gives the exact same result as the code above. Notice the count variable begins with -1 in order to return a beginning index of 0.
```
alist = ["I","like","you"]
count = -1
for i in alist:
    count += 1
    print(i,count)
```
A `for` loop can also be nested so that the second `for` loop iterates through itself completely for every single item belonging to the outer `for` loop.
```
# a simple multiplication table
for i in range(1,11):
    for j in range(1,11):
        print(i,"times",j,"equals",i*j)
```

**to Range or not to Range**

Iterates through the length of the string and returns the index for each iteration.
```
string = "abc"
for i in range(len(string)):
    code block
    print(i) # 0 1 2
```
Iterates through the length of the string and returns the value at the index for each iteration.
```
string = "abc"
for i in string:
    code block
    print(i) # a b c
```

## while
Runs a block of code while the logical expression is `True`. It is not known ahead of time how many iterations will occur.
```
while (logical expression == True):
    run this code block
```
A simple `while` count down.
```
number = 10
while number >= 0:
    print(number)
    number -= 1
```
A simple `for` count down.
```
number = 10
for i in range(number,-1,-1):
    print(i)
```
- **infinite loop** a block of code that runs indefinitely, mostly due to a condition never able to change. That is the condition is always `True` or always `False` based on the parameters given.
```
while 1 > 0:
    print("1")
```
## Loop Keywords
- `continue` skips the rest of the current iteration & continues with next iteration
- `break` skips the rest of the current iteration & exits the loop completely
- `pass` allows an empty block of code to be skipped over, useful when a function hasn't been written yet, but you know where it will appear.

`continue` skips 3 and continues iterating through rest of range.
```
for i in range(1,11):
    if i == 3:
        continue
```
`break` skips 3 and exits loop, does not continue to iterate through range.
```
for i in range(1,11):
    if i == 3:
        break
```
`pass` acts as placeholder, skips the area where code or functions would appear.
```
for i in range(1,11):
    pass
```
