name = "hello kitty"
print(name)

try:
    int("a")
except ValueError as e:
    print("oops",e)
    
print("program finished")