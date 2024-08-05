Strings are immutable.

Any operation on a string returns a new string.

# Methods

## Boolean

Returns `True` if all elements satisfy the condition.

If empty returns `False`.

`s.isalnum()` alpha numeric

`s.isalpha()` alpha

`s.isdigit()` numeric

`s.islower()` lowercase letters

`s.isupper()` uppercase letters

`s.isspace()` only whitespace

`s.istitle()` first letter uppecase, rest lowercase

## Transformation

`s.lower()` to lowercase

`s.upper()` to uppercase

`s.capitalize()` first letter to uppercase, rest to lowercase

`s.title()` each word is capitalized

`s.swapcase()` all lower to upper, all upper to lower

## Search

`s.startswith('')` returns `True` if string starts with given letter

`s.endswith('')` returns `True` if string ends with given letter

`s.count('')` counts occurrences of given string

`s.find('')` returns index of first occurrence of given string or -1

`s.rfind('')` returns index of last occurrence of given string or -1

`s.replace('','')` new string where 1st parameter is replaced with 2nd parameter

## Trim

`s.strip()` removes leading and trailing white space

`s.lstrip()` removes leading white space

`s.rstrip()` removes trailing white space

## Justify

`s.center(n)` centers string among n length

`s.ljust(n)` left justifies string among n length

`s.rjust(n)` right justifies string among n length

**Example**

```python
balls = [1,3,5]

for ball in balls:
  b = "*" * ball
  print(f"{b.center(5)}")

#   *
#  ***
# *****
```

## Join

`'someDelimiter'.join(s)` joins characters in a string or items in a list by given delimiter

**Example**

```python
s = "kat"

print('-'.join(s))

# k-a-t
```

```python
s = ["kit","kat"]

print('-'.join(s))

# kit-kat
```

```python
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

# 1 + 2 = 3
```

## Split

`s.split('someDelimiter')` splits string by given delimiter and returns a list , if delimiter blank then splits on white space

**Example**

```python
s = "kit-kat"

print(s.split('-'))

# ['kit', 'kat']
```
