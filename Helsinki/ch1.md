f strings `print(f"{var} is a var)`

escape characters with `\`
`'I can\'t wait to see ya'`

`\n` new line
`\t` tab

```python
multiplelines = '''a
b
c'''
```

# decimals

```python
print(f'(1.5:.1f)(1.5:.2f)(1.5:.3f)')
# 1.5 1.50 1.500
```

# while

function runs while condition returns true

```python
i = 1
while i*i < 100:
  print(f'square of {i} is {i*i}')
  i += 1
print('all done')
```

# for

function runs once for each element in list

```python
n = 0
for i in [1,2,3]:
  print(f'{n} + {i} is {n + i}')
  n += i
  # print(f'{n}')
print(f'total is {n}')
```

# matrix

multiplication table
```python
for i in range(1,11):
  for j in range(1,11):
    print(f"{i*j:>4}",end="")
  print()
```
