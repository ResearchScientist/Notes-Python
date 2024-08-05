# kittens = {"suky":1,"pusheen":2,"nero":3}

S = "the cats are here"

# L = 
# [1,5,7]
L = [1,2]

def sum_equation(l):
  total = 0
  for item in l:
    total = total + item
  stringed = [str(i) for i in l]
  joined = ' + '.join(stringed)
  if (l == []):
    joined = '0'
  print(f"{joined} = {total}")
sum_equation(L)