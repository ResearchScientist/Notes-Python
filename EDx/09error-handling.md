# Errors

- **compilation error** before running code : missing files etc
- **runtime error** during code execution : type errors etc
- **name error** undefined var or object
- **attribute error** attribution queried is not part of object
- **syntax error** formatting issue : missing parenthesis etc

# Debugging

## Tracing
Using print statements after each line of code to visualize outputs

## Scope
Using print statements after each code block to visualize outputs

## Rubber Ducking
Explaining the problem in detail out loud to someone else (a duck, a cat). The act of figuring out how to explain can reveal the solution.

## Step by Step Execution
Stepping over into by lines of code

## Variable Visualization
Viewing the value of variables as they change

## In Line Debugging
Real time flagging of errors

# Error Handling

- **Exception** an anticipated error
- **Exception Handling** code that gracefully responds to an exception error
- **Error Catching** preventing a program from crashing when an error is encountered
- **Uncaught Error** error not handled by error handling code

## Exception Handling

Makes use of three main structural statements.

- **Try** marks a block of code as potentially containing an error
- **Catch** names the anticipated errors and indicates what code to run in response to those errors
- **Finally** marks a block of code to run after the Try code and Catch code regardless if they ran
```
try:
    code block that includes a line of code that may cause an error
except:
    code block that runs when error encountered within try block of code above
else:
    code block that runs when no errors are encountered
finally:
    code block that runs regardless if errors were encountered or not
    additionaly if any uncaught errors occur, the code within the finally block will still run
```
**All Errors**
Catches any error regardless of type.
```
try:
    var = 1/0
    print(var)
except:
    print("error encountered")
print("complete")
```
**Specific Errors**
Catches specific error types. The specific error type is given after the `except` statement.
```
try:
    print(1/var)
except ZeroDivisionError:
    print("no zero divison allowed")
except NameError:
    print("a name error occurred")
```
**Structured Approach**
Catches various error types both in user input and in computation. The `else` is used to display the actual result, which would only display if none of the errors listed occurred.
```
try:
    dividend = int(input("Enter dividend: "))
    divisior = int(input("Enter divisor: "))
    quotient = dividend/divisor
except ZeroDivisionError:
    print("no zero division allowed")
except ValueError:
    print("enter only integers")
else:
    print("the result is",quotient)
```
**File Input**
Good practice. When reading in a file always use error handling.
```
try:
    someFile = open("someFile.txt",mode = "r")
    for line in someFile:
        print(line)
except IOError as error:
    print("check the file name")
except ValueError as error:
    print("check the file data type")
else:
    print("file read successfully")
finally:
    someFile.close()
```
**Nested Error Handling**
This allows for compartmentalizing error handling. Especially useful when dealing with loops.
```
try:
    someFile = open("someFile.txt",mode = "r")
    try:
        for line in someFile:
            print(line)
    except ValueError as error:
        print("check the file data type")
    else:
        print("file converted successfully")
    finally:
        someFile.close()
except IOError as error:
    print("error reading file, check the file name")

```
# Looping Tip

To check if a condition is met iterate through the item and use `return True` the moment the condition is met.
If the loop ends without the condition being met then use `return False`.
Useful for the following criteria:
- **checking if a file is a valid format** use `return False` when something invalid is found, use `return True` when nothing invalid is found
- **searching for an item in a list** use `return True` or its index when it's found, use `return False` if the loop ends without it being found
- **checking if two lists are equal** use `return False` when a difference is found, use `return True` when no difference is found

**Finding a Vowel**
Finds the first instance of a vowel and exits.
```
def has_vowel(string)
    for letter in string:
        if letter in "aeiou":
            return True
    return False

print(has_vowel("abba")) # returns True
print(has_vowel("cdfg")) # returns False
```
**Opening a File**
Always use exception handling.

```
def open_file(file_name):
    try:
        file = open(file_name)
    except:
        return "error opening file"
    file_text = file.read()
    return file_text
```
**More Nested Error Handling**

In the following code the `for` loop is nested inside the `try` statement. 
It reads the file integers but if it encounters a non integer it moves to the `except` code block.
```
try:
    inputFile = open("someFile.txt",mode = "r")
    try:
        for line in inputFile:
            print(int(line))
    except ValueError as error:
        print("value error")
    else:
        print("no errors")
    finally:
        inputFile.close()
except IOError as error:
    print("error reading file")
```

In the following code the `try` block is nested inside the `for` loop.
It reads the file integers  but if it encounters a non integer it attempts to read the next line instead of exiting.
Note that the `except` block is inside the `for` loop. That makes it so that if one iteration causes an error the `for` loop continues with the next `line` in `inputFile`.
```
try:
    inputFile = open("someFile.txt",mode = "r")
    for line in inputFile:
        try:
            print(int(line))
        except ValueError as error:
            print("value error")
        else:
            print("no errors")
    #finally:
    inputFile.close()
except IOError as error:
    print("error reading file")
```
A function with exception handling `try` and `except`.
```
def get_integer(my_var):
    try:
        conversion = int(my_var)
        return conversion
    except Exception as error:
        error_msg = "Cannot convert!"
        return error_msg

print(get_integer("1"))
print(get_integer("hi"))
```
A function with exception handling `try` and `except` and `finally`.
```
def get_integer(my_var):
    try:
        conversion = int(my_var)
    except Exception as error:
        conversion = "Cannot convert!"
    finally:
        return conversion

print(get_integer("1"))
print(get_integer("hi"))
```
