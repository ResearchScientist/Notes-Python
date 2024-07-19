# kittens = {"suky":1,"pusheen":2,"nero":3}

string = "1 2 3"
print(type(string))
# <class 'str'>

list = string.split()
print(type(string))
# <class 'list'>

def adds(something):
  total = 0
  for some in something:
    some = int(some)
    total = total + some
  print(total)

adds(list)
