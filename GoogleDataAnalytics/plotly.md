# Import

express is used for helping run large data sets faster

```python
import plotly.express as px
```

# Scatter Overlaid on Geo Map

```python
scatter = px.scatter_geo(df[df.colName >= 50],
h="heigth", w="weight",size="colName")

scatter.show()
```

