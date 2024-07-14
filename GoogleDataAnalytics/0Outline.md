# Set

`set()` 
`intersection()` `&` elements common to both
`union()` `|` all elements from both
`difference()` `-` elements from one set and not the other , order matters
`symmetric_difference()` elements not found in both sets

```python
set1 = {1,2,3,4}
set2 = {3,4,5,6}

inters = set1.intersection(set2)
uni = set1.union(set2)
dif = set1.difference(set2)
dif = set2.difference(set1)
sym = set1.symmetric_difference(set2)

print(inters)
print(uni)
print(dif)
print(dif)
print(sym)

# returns
set([3, 4])
set([1, 2, 3, 4, 5, 6])
set([1, 2])
set([5, 6])
set([1, 2, 5, 6])

inters = set1 & set2
uni = set1 | set2
dif = set1 - set2
dif = set2 - set1
sym = set1 ^ set2

print(inters)
print(uni)
print(dif)
print(dif)
print(sym)

# returns
set([3, 4])
set([1, 2, 3, 4, 5, 6])
set([1, 2])
set([5, 6])
set([1, 2, 5, 6])
```

