Object Oriented Programming uses objects and classes.

- class , is a prototype or template or model
- instance , is an object based on the class

`class someName:` defines a class
`someName = someClass()` defines an instance
`def __init__(self,someArgument)` allows for passing of arguments into class

# Class

Makes a class.
```python
class Car:
    runs = True
    def start(self,name):
        self.name = name
        if self.runs:
            print(f"{self.name} car fast")
        else:
            print(f"{self.name} car slow")
```

# Instance

Makes an instance
```python
my_subaru = Car()
```

Execute instance.
```python
my_subaru.start("Subaru")
# returns Subaru car is fast
```

Modify instance.
```python
my_subaru.runs = False

my_subaru.start("Subaru")
# returns Subaru car is slow
```

# Init

Make class with init.
```python
class Car:
    runs = True
    
    def __init__(self,name): # always include self
        print("new car")
        self.name = name
    
    def start(self,name):
        if self.runs:
            print(f"{self.name} car fast")
        else:
            print(f"{self.name} car slow")
```

Makes an instance with init
```python
my_subaru = Car("Subaru") # requires argument name since name was written in parameter for init
```

# Class Methods

```python
class Car:
    runs = True
    number_of_wheels = 4
    
    def __init__(self,name): # always include self
        print("new car")
        self.name = name
    
    def start(self,name):
        if self.runs:
            print(f"{self.name} car fast")
        else:
            print(f"{self.name} car slow")
            
    @classmethod
    def get_number_of_wheels(cls): # cls used by convention , can be anything
        return cls.number_of_wheels
```

```python
my_subaru = Car("Subaru")
```

```python
my_subaru.get_number_of_wheels()
```

# Magic Methods

`__str__` makes class readable and DRY

```python
def __str__(self):
    return f"the {self.name} is {self.runs}"
```

```python
class Car:
    runs = True
    number_of_wheels = 4
    
    def __init__(self,name): # always include self
        print("new car")
        self.name = name
        
    def __str__(self):
        return f"the {self.name} is {self.runs}"
    
    def start(self,name):
        if self.runs:
            print(f"{self.name} car fast")
        else:
            print(f"{self.name} car slow")
            
    @classmethod
    def get_number_of_wheels(cls): # cls used by convention , can be anything
        return cls.number_of_wheels
```

# Inheritance

```python
class Vehicle:
    def __init__(self,make,model,fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel
        
class Car(Vehicle):
    def __init__(self,make,model,fuel="gas",num_wheels=4):
        super().__init__(make,model,fuel)
        self.num_wheels = num_wheels
```

```python
four_by_four = Vehicle("mac","truck",fuel="oil")
four_by_four.make
# returns mac
```

```python
my_subaru = Car("subaru","sports",fuel="diesel")
my_subaru.make
# returns subaru
```
