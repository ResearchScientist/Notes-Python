- set
- frozen set

`.format(var1,var2)` substitutes vars into template denoted by `{}`.
to format numbers within `{}`
`{:2f}` limits decimal to 2 places
`{:>3}` aligns output 3 spaces to right

```python
cat = 'Suki'
size = 'small'

print("I'm {name} and I'm {size}.".format(name=cat,size=size))
```

# Numbers

```python
def shortNum(x):
    if x >= 1e6:
        s = '{:1.1f}M'.format(x*1e-6)
    else:
        s = '{:1.0}K'.format(x*1e-3)
    return s

df['easyCookieCount'] = df['cookies'].apply(shortNum)

# returns
# numbers abbreviated as 2.5K or 1.1M instead of 2500 or 1100000
```

