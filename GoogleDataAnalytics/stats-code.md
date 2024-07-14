# Descriptive

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = {'cat': ['suki','nero','hello kitty','pusheen'],
'size': ['small','small','med','big'],
'age': [2,5,10,15]}

df = pd.DataFrame(data=df).sort_values('age').reindex(['cat','size','age'],axis=1)


df = df['age'].describe()

print(df)
# returns
count     8.000000
mean      7.214435
std       4.245286
min       2.000000
25%       4.187500
50%       6.607738
75%       8.812500
max      15.000000
Name: age, dtype: float64

df = df.describe(include='all')

print(df)
# returns
         cat   size        age
count      4      4   4.000000
unique     4      3        NaN
top     nero  small        NaN
freq       1      2        NaN
mean     NaN    NaN   8.000000
std      NaN    NaN   5.715476
min      NaN    NaN   2.000000
25%      NaN    NaN   4.250000
50%      NaN    NaN   7.500000
75%      NaN    NaN  11.250000
max      NaN    NaN  15.000000
```

# Probability

```python
import numpy as np
import pandas as pd

df = {'grades': [100,90,39,48,78,89,79,48,85,79,56,97,92,82,71,69,90,91,67,78,81,93,56,98,99,34,67,88,69,78,87,93,94]}
df = pd.DataFrame(data=df)

mean = df['grades'].mean()
stddev  = df['grades'].std()
print(mean)
print(stddev)
print(df.describe())
# returns
77.72727272727273
17.764558690115145
           grades
count   33.000000
mean    77.727273
std     17.764559
min     34.000000
25%     69.000000
50%     81.000000
75%     91.000000
max    100.000000

num_of_dev = 2

one_bel = mean - (num_of_dev*stddev)
one_abo = mean + (num_of_dev*stddev)
one_bel = round(one_bel,2)
one_abo = round(one_abo,2)

percent_of_data = ((df['grades'] >= one_bel) & (df['grades'] <= one_abo)).mean()*100
percent_of_data = round(percent_of_data,1)

print('for ' + str(num_of_dev) + ' std dev ' + str(percent_of_data) + '% of the data is between ' + str(one_bel) + ' and ' + str(one_abo))
# returns
for 2 std dev 93.9% of the data is between 42.2 and 113.26
# clearly there's an issue here since the range returned is outside the max of 100
# this is due to the dev just being added and subtracted

dfZ = df['zScores'] = stats.zscore(df['grades'])

zScore = 2

dfZscores = df[(dfZ > zScore)|(dfZ < -zScore)]

print(dfZscores)
# returns
    grades   zScores
2       39 -2.213831
25      34 -2.499654
# adds a column of z scores and shows grades that are 2 std deviations from mean
```

# Pull Random Samples

`.sample(n,replace,random_state)` n=sample size , replace = T or F , random_state = seed 

```python
df = {'grades': [100,90,39,48,78,89,79,48,85,79,56,97,92,82,71,69,90,91,67,78,81,93,56,98,99,34,67,88,69,78,87,93,94]}
df = pd.DataFrame(data=df)

sampleDF = df.sample(n=5,replace=True,random_state=200)

print(sampleDF)
# returns
    grades
26      67
16      90
4       78
12      92
15      69
```

# Confidence Interval

`stats.norm.interval(alpha,loc,scale)` builds a C, alpha is % margin of error , loc is sample mean , scale is estimate of standard error

```python
import numpy as np
import pandas as pd
from scipy import stats

df = {'grades': [100,90,39,48,78,89,79,48,85,79,56,97,92,82,71,69,90,91,67,78,81,93,56,98,99,34,67,88,69,78,87,93,94]}
df = pd.DataFrame(data=df)

sampleDF = df.sample(n=5,replace=True,random_state=200)

sampleMean = sampleDF['grades'].mean()

estimateSE = sampleDF['grades'].std()/np.sqrt(sampleDF.shape[0])

confintDF = stats.norm.interval(alpha=0.95,loc=sampleMean,scale=estimateSE)

print(confintDF)
# returns
(69.0648823950898, 89.33511760491021)
```

# T Test

Are the mean grades from 2 groups statistically different.
For a confidence level of 5% the returned p value of 1.4% indicates a statistical difference in mean grades between the two groups.

```python
import pandas as pd
from scipy import stats

df1 = {'grades': [100,90,39,48,78,89,79,48,85,79,56,97,92,82,71,69,90,91,67,78,81,93,56,98,99,34,67,88,69,78,87,93,94,80,34,49,67,89,99,97,78,86,89,83,73,91,82,89,79,76,88,93,92,79,70,84,92,82,71,91,79,80,84,75,88,89,93,94,97,88,86,81,79,79,86]}
df1 = pd.DataFrame(data=df1)

df2 = {'grades': [98,67,83,80,86,81,67,78,75,72,89,90,81,60,67,65,56,60,50,72,67,76,78,80,84,88,85,76,74,78,89,67,56,83,81,80,79,74,77,76,71,67,68,62,54,89,45,54,89,75,72,69,65,78,72,67,89,82,61,73,75,85,82,81,89,78,67,78,71,67,82,80,91,89,90]}
df2 = pd.DataFrame(data=df2)

pval = stats.ttest_ind(a=df1['grades'],b=df2['grades'],equal_var=False)

print(df1.describe())
print(df2.describe())
print(pval)
# returns
           grades
count   75.000000
mean    80.346667
std     14.915522
min     34.000000
25%     77.000000
50%     83.000000
75%     90.500000
max    100.000000
          grades
count  75.000000
mean   75.093333
std    10.813122
min    45.000000
25%    67.000000
50%    76.000000
75%    82.000000
max    98.000000
Ttest_indResult(statistic=2.46951675300867, pvalue=0.014777935459853436)
```
