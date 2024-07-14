# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from scipy import stats
# import statsmodels.api as sm

# df = {'cat': ['suki','nero','hello kitty','pusheen'],
# 'size': ['small','small','med','big'],
# 'age': [2,5,10,15]}

# df = pd.DataFrame(data=df).sort_values('age').reindex(['cat','size','age'],axis=1)

# df = df.describe(include='all')
# df = df['age'].describe()

df1 = {'grades': [100,90,39,48,78,89,79,48,85,79,56,97,92,82,71,69,90,91,67,78,81,93,56,98,99,34,67,88,69,78,87,93,94,80,34,49,67,89,99,97,78,86,89,83,73,91,82,89,79,76,88,93,92,79,70,84,92,82,71,91,79,80,84,75,88,89,93,94,97,88,86,81,79,79,86]}
df1 = pd.DataFrame(data=df1)

df2 = {'grades': [98,67,83,80,86,81,67,78,75,72,89,90,81,60,67,65,56,60,50,72,67,76,78,80,84,88,85,76,74,78,89,67,56,83,81,80,79,74,77,76,71,67,68,62,54,89,45,54,89,75,72,69,65,78,72,67,89,82,61,73,75,85,82,81,89,78,67,78,71,67,82,80,91,89,90]}
df2 = pd.DataFrame(data=df2)

print(df1.describe())
print(df2.describe())

pval = stats.ttest_ind(a=df1['grades'],b=df2['grades'],equal_var=False)

print(pval)