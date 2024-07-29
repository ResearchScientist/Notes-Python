# kittens = {"suky":1,"pusheen":2,"nero":3}

L = [1,2,3]

def adds(l):
  s=0
  for n in l:
    s = s+n
  return s

print(adds(L))

from functools import reduce

reduced = reduce(lambda a,b:a+b,L,0)

print(reduced)