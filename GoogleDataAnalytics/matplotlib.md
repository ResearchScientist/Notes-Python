# Import

```python
from matplotlib import pyplot as plt
```

# Bar

## DF

```python
df['month'] = df['date'].dt.month
df['month_name'] = df['date'].dt.month_name().str.slice(stop=3)
dfMonths = df.groupby(['month','month_name']).sum().sort_values('month',ascending=True).head(12)
```

##Plot

```python
plt.bar(x=dfMonths['month_name'],height=dfMonths['cookies'],label="Cookies Eaten")
plt.plot()
plt.xlabel('months')
plt.ylabel('cookies')
plt.title('How many cookies are eaten per month.')
plt.legend()
plt.show()
```

## DF

```python
df2020Weeks = df[df['year']=='2020'].groupby(['week']).sum().reset_index()
```

## Plot

```python
plt.bar(x=df2020Weeks['week'],height=df2020Weeks['cookies'],label="Cookies Eaten")
plt.plot()
plt.xlabel('weeks')
plt.ylabel('cookies')
plt.xticks(rotation=90,fontsize=8)
plt.title('How many cookies are eaten per week.')
plt.show()
```

# Boxplot

```python
box = sns.boxplot(x=df['colName'])
```

# Heatmap

```python
axis = sns.heatmap(df,cmap='Blues')
colorbar = ax.collections[0].colorbar
colorbar.set_ticks([0,1,2])
colorbar.set_ticklabels(['low','med','high'])
plt.show()
```

