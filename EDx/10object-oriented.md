**Object**
Custom data structure that organizes and encapsulates variables and methods into a single data type.

**Class**
Template for a prototypical custom data type comprised of multiple variables and methods.
Instances or objects are created based on the template given by the class.

**Instance**
The realization of an entity in terms of a unique set of values that are mapped to the class variables.

**Attributes**
The variables that constitute an instance of a class.

Declaring a class.
```Python
class Cat:                     # declaration
    def __init__(self):        # constructor method
        self.name = ""         # attribute string
        self.age = 0           # attribute integer
        self.friendly = True   # attribute boolean
        self.toys = []         # attribute list
```

Declaring an instance.
```Python
myCat = Cat()     # declaration
print(myCat.age)  # 0  returns default values

myCat.age = 1     # attribute assigned new value
print(myCat.age)  # 1  returns new value
```

Nested classes.
```Python
class Name:
    def __init__(self):
        self.firstname = "first"
        self.lastname = "last"

class Owner:
    def __init__(self):
        self.name = Name()        # points to the class called Name
        self.otherpets = False

myOwner = Owner()
print(myOwner.name.firstname)     # first  accesses class name then attribute firstname

myOwner.name.firstname = "wonder"
print(myOwner.name.firstname)     # Wonder  accesses class name then attribute firstname

```

Declaring a class with parameters.
```Python
class Name:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last

ww = Name("wonder","woman")
print(ww.firstname)                  # Wonder
```

Declaring nested classes with parameters.
```Python
class Name:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last

class Owner:
    def __init__(self,name,age):
        self.name = name
        self.age = age

myOwner = Owner(Name("wonder","woman"),200)  # instance constructed
print(myOwner.name.firstname)                # firstname inside name which is inside owner
print(myOwner.name.lastname)                 # lastname inside name which is inside owner
print(myOwner.age)                           # age inside owner
```

Nested instances.
```Python
class Cat:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother
        
mrCat = Cat("Mr. Cat",20)
mrsCat = Cat("Mrs. Cat",20)
babyCat = Cat("little kitty",5,mrCat,mrsCat)  # intsances of mrCat and mrs Cat are inside instance of baby cat

print(babyCat.father.name)                    # Mr. Cat
print(babyCat.mother.name)                    # Mrs. Cat
print(babyCat.name)                           # little kitty
```

Instance as an argument. Instance of name serves as an argument for the function capitalizeName.
```Python
class Owner:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Name:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
        
def capitalizeName(name):
    name.firstname = name.firstname.capitalize()
    name.lastname = name.lastname.capitalize()
        
myOwner = Owner(Name("wonder","woman"),200)  # instance constructed

print(myOwner.name.firstname)                # wonder
print(myOwner.name.lastname)                 # woman

capitalizeName(myOwner.name)                 # definition called

print(myOwner.name.firstname)                # Wonder
print(myOwner.name.lastname)                 # Woman
```

Copies of instances. The following makes actual copies of the values not just makes a pointer to the same memory location. Changes to one instance do not affect the other instance.
```Python
class Owner:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Name:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last

myOwner1 = Owner(Name("wonder","woman"),200)

# all values are copied from myOwner1 to myOwner2
myOwner2 = Owner(Name(myOwner1.name.firstname,myOwner1.name.lastname),myOwner1.age)

# both myOwner1 and myOwner2 display the same values
print(myOwner1.name.firstname)  # wonder
print(myOwner2.name.firstname)  # wonder

# value is changed in myOwner2
myOwner2.name.firstname = "wander"  

print(myOwner1.name.firstname)  # wonder
print(myOwner2.name.firstname)  # wander
```

# Method Types

**Constructor**
Method that runs when a new instance of a class is created. Can contain parameters that provide values to initialize the variables defined by the class.
The `__` around the `__init__` method are used to indicate that code within that function should not be accessed by other functions but they can be.

**Destructor**
Method that specifies how the instance of the data should be destroyed. Useful for memory management.

**Getter**
Method that returns the value of a variable. Allows for custom access to those variables. Useful for privacy and security and making logs.

**Setter**
Method that changes the value of a variable. Allows for custom access to those variables. Useful for privacy and security and making logs.

- **abstraction** only essential information is made available to outside programs
- **polymorphism** ability for methods to access different objects similarly
- **inheritance** the ability for a class to obtain all the variables and methods from another class while having its own unique variables and methods

Methods always begin with a `self` parameter.
```Python
class Pokemon:
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def would_defeat(self,a_different_pokemon):     # method declaration
        if self.power > a_different_pokemon.power:  # selfpower refers to pokemon 1 , adifferentpokemon refers to pokemon 2 or 3
            return True
        else:
            return False
    
new_pokemon_1 = Pokemon("Pikachu", 500)
new_pokemon_2 = Pokemon("Charizard", 2412)
new_pokemon_3 = Pokemon("Squirtle", 312)
print(new_pokemon_1.name)
print(new_pokemon_1.power)
print(new_pokemon_1.would_defeat(new_pokemon_2))
print(new_pokemon_1.would_defeat(new_pokemon_3))
```
