# File Input Output

File Types `.txt` `.csv` `.pdf` `.md` `.html`

-**reading** viewing file content
-**writing** overwriting file content
-**appending** adding to the end of the file content

`open()` opens the file given the filename within the working directory, a full path can also be passed in. An optional second parameter `r`,`w`,`a` opens the file in read, write, or append mode.
`close()` closes the given file

Methods

`someFile.write()` input is a string, all arguments are concatenated with `+`
`someFile.writelines()` input is a list of strings, strings are written to file without spaces

**Write**
Writing variable values to a file.
```
leta = "a"
letb = "b"
letc = "c"
nums = 123

newFile = open("someFile.txt","w")
newFile.write(leta + "\n")
newFile.write(letb + "\n")
newFile.write(letc + "\n")
newFile.write(str(nums))
newFile.close()

```

Writing a list to a file.
```
someList = ["I","like","you"]

newFile = open("newfile.txt","w")
for word in someList:
    newFile.write(word + "\n")
newFile.close()
```

Writing a list to a file using `join` method.
This is the best way to write from lists. It allows separating characters by `" "` or `\n` or any other character.
```
someList = ["I","like","you"]

newFile = open("newfile.txt","w")
newFile.write(" ".join(someList))
newFile.close()
```

Alternative to `.write()` method.
`print(someVar,file = newFile)` 
Passing the keyword `file` and the file name writes to the file instead of displaying on the console.

Writing a list of tuples to a file.
```
# movielist will be written onto a file
movieList = [('Rogue One',530,2017),('Finding Dory',486,2017),('Captain America',408,2017)]

outputFile = open("movies.txt","w") # creates a txt file called movies and assigns a variable
for movie in movieList: # iterates through each tuple
    print(movie, file = outputFile) # writes each tuple on its own line into the variable wich points to the movies.txt
outputFile.close()

# ('Rogue One', 530, 2017)
# ('Finding Dory', 486, 2017)
# ('Captain America', 408, 2017)
```

Since a tuple will be read in as a string, use `import ast` and `ast.literal_eval()` to turn the string into a tuple.
```
import ast

myString = "('Rogue One', 530, 2017)"
print(myString,type(myString))

myTuple = ast.literal_eval(myString)
print(myTuple,type(myTuple))
```

Making a list of tuples.
```
import ast

newMovieList = []
inputFile = open("movies.txt","r")
for line in inputFile:
    lineAsTuple = ast.literal_eval(line)
    newMovieList.append(lineAsTuple)
inputFile.close()

print(newMovieList)
```

**Append**
```
def append_to_file(file,data):
    newFile = open(file,"a")
    data = str(data)
    newFile.write(data + "\n")
    newFile.close()
    
append_to_file("somefile.txt",2018)
```

**Read**
`newFile.readline()` reads file one line at a time
`newFile.read()` reads the whole file
```
print(newFile.readline(), end="") # removes new line character at then end
print(newFile.readline().strip()) # removes \n or spaces form beggining and end of the line
```

Assign read data to a variable
```
newFile = open("somefile.txt","r")
someVar = int(newFile.read())
print(someVar)
newFile.close()
```

Assign read data to a list
```
newList = []
newFile = open("someFile.txt","r")
for words in newFile:
    newList.append(words.strip())
print(newList)
```

A function `save` that opens a file and writes the contents from a list to that file.
A function `load` that opens the file creates a list and appends the content of the file to the list then returns the list.

```
def save(filename,inList):
    outputFile = open(filename,"w")
    for item in inList:
        print(item, file = outputFile)
    outputFile.close()
    
def load(filename):
    inputFile = open(filename,"r")
    inList = []
    for line in inputFile:
        inList.append(line.strip())
    inputFile.close()
    return inList

myList = ["a","b","c"]

save("outputfile.txt", myList)
newList = load("outputfile.txt")

print(newList)
```
**Final Tips on Reading a File**

Read `somefile.read()`
```
file = open("filename.txt","r") # opens file
readfile = file.read().strip() # reads all lines of file and takes out end space
splitfile = readfile.split(" ") # splits file on white space , creating a long list of strings
```

Read `for line in file`
```
file = open("filename.txt","r") # opens file
myList = []
for line in file:
    myList.append(line.strip()) # removes white space at ends of line and adds each line as an element in to myList
```
