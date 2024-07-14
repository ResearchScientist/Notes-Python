# Read File

```python
df = pd.read_csv('file url')
df.head(10)
```

```python
import json
pd.read_json()
pd.df.to_json()
```

# Basic DF Info non pandas

`df.info()` returns # of col, col names, data types, # of values
`.describe(include='all')` counts,min,max,stats,quartiles
`.sample()`
`.size()`
`.shape`
`df.dtypes` data type for each column
`df.isnull().sum()` total missing values

# Stat Methods

`df.['colName'].sum()`
`df['colName'].mean()`
`df['colName'].min()`
`df['colName'].max()`
`df['colName'].std()`
`df['colName'].value_counts()` number of rows per col
`df['colName'].describe()` summary stats count,mean,std,min,max,quartiles

# Subset

`df[(df['age'] == 20) & (df['hgt'] > 120)]` filters df

# New Column

`df['newColName'] = df['someCol'] * 2` adds new column whose values are twice some col

# Aggregate

```python
CookiesBought = df.groupby(['sex','year']).agg({'CookiesBought': ['count','sum']})
CookiesBought['ave'] = CookiesBought['cookies']['sum']/CookiesBought['cookies']['count']
CookiesBought

# returns

            cookies         ave
            count   sum
sex year    
f   1       10      100     10
    2       13      130     10
    3       9       90      10
m   1       20      200     10
    2       30      300     10
    3       34      340     10
```

# Data Frame

Using pandas only
```python
import pandas as pd

data = {'col1': [1,2], 'col2': [3,4]}
df = pd.DataFrame(data=data)
print(df)

# returns
   col1  col2
0     1     3
1     2     4
```

Using pandas and numpy
```python
import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),
columns=['a','b','c'], index=['x','y','z'])

print(df)

# returns
   a  b  c
x  1  2  3
y  4  5  6
z  7  8  9
```

# Series

A one dimensional labeled array.

# Row and Column Methods

`df.columns` returns column names
`df.shape` returns shape
`df.info()` counts, nan, and data type 
`df['colname']` returns a series object
`df[['col1','col2']]` returns new df object
`df.iloc[n]` n is index location (can pass range n1:n2), returns row(s) at given index
`df.iloc[0:3,[3,4]]` returns rows 0,1,2 from columns 3,4
`df.iloc[:,[2]]` returns all rows from column 2
`df.iloc[1,2]` returns value at row 1 column 2
`df.loc[1:3,['colname']]` returns rows 1 to 3 since they are named 1,2,3 for the given column
`df['newcolname'] = df['somecol'] + 100` returns new df with new column called newcolname with new calculated values

# Boolean Masking

Overlays boolean grid over DF and filters through only T values.

```python
import pandas as pd

df = {'cat': ['suki','nero','hello kitty','pusheen'],
'size': ['small','small','small','big'],
'age': [2,5,10,10]}

cats = pd.DataFrame(df)

print(cats)

# returns
   age          cat   size
0    2         suki  small
1    5         nero  small
2   10  hello kitty  small
3   10      pusheen    big

mask = cats['age'] < 5
print(mask)

kittens = cats[mask]

print(kittens)

# returns
   age   cat   size
0    2  suki  small
```

# Logical Operators

`&` and
`|` or
`~` not

# Methods

`groupby()` groups rows based on given columns

```python
import pandas as pd

df = {'cat': ['suki','nero','hello kitty','pusheen'],
'size': ['small','small','med','big'],
'age': [2,5,10,15]}

cats = pd.DataFrame(df)

print(cats)

# returns
   age          cat   size
0    2         suki  small
1    5         nero  small
2   10  hello kitty    med
3   15      pusheen    big

res = cats.groupby(['size','age']).sum()

print(res)

# returns
size  age             
big   15       pusheen
med   10   hello kitty
small 2           suki
      5           nero
```

```python
import pandas as pd

df = {'cat': ['suki','nero','hello kitty','pusheen'],
'size': ['small','small','med','big'],
'age': [2,5,10,15]}

cats = pd.DataFrame(df)

print(cats)
   age          cat   size
0    2         suki  small
1    5         nero  small
2   10  hello kitty    med
3   15      pusheen    big

res = cats.groupby('size').mean()

print(res)

# returns
size    age   
big    15.0
med    10.0
small   3.5
```

`agg()` 

```python
import pandas as pd

df = {'cat': ['suki','nero','hello kitty','pusheen'],
'size': ['small','small','med','big'],
'age': [2,5,10,15]}

cats = pd.DataFrame(df)

print(cats)

# returns
   age          cat   size
0    2         suki  small
1    5         nero  small
2   10  hello kitty    med
3   15      pusheen    big

res = cats.groupby('size').agg(['mean','max'])

print(res)

# returns
        age    
       mean max
size           
big    15.0  15
med    10.0  10
small   3.5   5
```

# Functions

`concat([df1,df2])` concatenates DFs vertically or horizontally
`merge()` only merges DFs horizontally

axis 0 runs function vertically along a column
axis 1 runs function horizontally along a row

## concat

```python
import pandas as pd

df1 = {'cat': ['suki','nero'],
'size': ['small','small'],
'age': [2,5]}

df2 = {'cat': ['hello kitty','pusheen'],
'size': ['med','big'],
'age': [10,15]}

smallCats = pd.DataFrame(df1)
bigCats = pd.DataFrame(df2)

print(smallCats)
print(bigCats)

# returns
   age   cat   size
0    2  suki  small
1    5  nero  small
   age          cat size
0   10  hello kitty  med
1   15      pusheen  big

df3 = pd.concat([smallCats,bigCats],axis=0)

print(df3)

# returns
   age          cat   size
0    2         suki  small
1    5         nero  small
0   10  hello kitty    med
1   15      pusheen    big

df3 = df3.reset_index(drop=True)

# returns
   age          cat   size
0    2         suki  small
1    5         nero  small
2   10  hello kitty    med
3   15      pusheen    big
```

## merge

`inner = pd.merge(df1,df2,on='someKey',how='inner')` inner join , only elements common to both
`outer = pd.merge(df1,df2,on='someKey',how='inner')` outer join , all elements from each
`left = pd.merge(df1,df2,on='someKey',how='left')` left join , all from left
`right = pd.merge(df1,df2,on='someKey',how='right')` right join , all from right

# Date

`df['month'] = df['date'].dt.month` makes new col called month where month is indicated by number
`df['month_name'] = df['date'].dt.month_name().str.slice(stop=3)` new col with month as string with only first 3 letters

`df['week'] = df['date'].dt.strftime('%Y-W%V')`                         2020-W5
`df['month'] = df['date'].dt.strftime('%Y-%m')`                         2020-02
`df['quarter'] = df['date'].dt.to_period('Q').dt.strftime('%Y-Q%q')`    2020-Q1
`df['year'] = df['date'].dt.strftime('%Y')`                             2020

# Missing Values

```python
df[pd.isnull(df.someCol)]
df.shape  # returns total number of NaNs
df.info() # returns non null count per column
```

# Transform

New column named levels with 4 labels.
```python
df['levels'] = pd.qcut(df['cookies'],4,labels=['few','some','lots','way too much'])
df
```

Assigns numerical code to categorical levels as a new column.
```python
df['levelcodes'] = df['levels'].cat.codes
df
```

Assigns 1 to cells with values and 0 to empty cells.
```python
pd.get_dummies(df['levelcodes'])
```

Pivot Table
```python
dfMonthly = df.pivot('year','month','cookies')
dfMonthly()

# returns
# month jan feb mar apr may jun jul aug sep oct nov dec
# year
# 2020  0   0   1   0   1   0   1   1   0   1   0   1
# 2021  1   1   1   0   1   1   1   0   0   1   0   0
```
