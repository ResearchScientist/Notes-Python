# for i in range(3):
#   print('hey')
# print('you')

# print("what's your favourite food?")

# favourite_food = input()

# print("wow, I also like",favourite_food)

# print(f'{1.5:.1f} {1.5:.2f} {1.5:.3f}')

# i = 1
# while i*i < 100:
#   print(f'square of {i} is {i*i}')
#   i += 1
# print('all done')

# n = 0
# for i in [1,2,3]:
#   print(f'{n} + {i} is {n + i}')
#   n += i
#   # print(f'{n}')
# print(f'total is {n}')

for i in range(1,11):
  for j in range(1,11):
    print(f"{i*j:>4}",end="")
  print()