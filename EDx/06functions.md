# Functions
A segment of code that performs a specific task. Useful for organizing code and making sections reusable.

- **function call** the location in which a saved function is used
- **function definition** the function name, parameters, and code
- **header** the name and list of parameters
- **parameters** variables expecting values when function is called
- **body** code to be ran when function is called
- **return statement** code defining what output to return
- **arguments** the values passed into the parameters

```
def functionName(parameters):
    some code
    return a var

functionName(values)
```
**RETURN Debugging**
If a `return` is not explicitly requested from a function then the function implicitly returns a `return` of type `None`. This is useful in debugging code were certain conditionals may not be running.

**Keyword Parameters**
Optional parameters that override default behaviours. They must be entered after all other required parameters.

For `print()` they are:
- `sep = ""` separator between strings , default is a space
- `end = ""` no end of line character but can be anything, so displays on same line , default is a new line

Custom keyword parameters can be defined for functions.
- **First** set a parameter name equal to a default value within the function definition.
- **Second** within the function define some behaviour for that default value.

```
def weather(temp,measure="celsius"):
    if measure == "celsius":
        print(temp,"celsius")
    elif measure == "kelvin":
        print(temp,"kelvin")
    else:
        print("why are you using a weird measure")
weather(80,"farenheit")
```
