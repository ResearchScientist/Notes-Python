`.array()` mutable elements , but to change length then need to assign to new array
Elements in arrays are auto type cohersed to be the same type.

`arrayName.dtype` returns element type
`arrayName.shape` returns # of col, # of rows in array
`arrayName.ndim` returns # of dimensions

`arrayName.reshape(#rows,#cols)` changes arrays dimensions to those given 

`np.mean()`
`np.median(df['colname'])`
`np.log()`
`np.floor()`
`np.ceil()`

Lists cannot be multiplied together directly.
To do so use numpy to turn the lists into arrays and then multiply them together.

```python
import numpy as np

listA = [1,2,3]
listB = [2,4,6]

arrayA = np.array(listA)
arrayB = np.array(listB)

listC = arrayA * arrayB

print(listC)

# returns
[ 2  8 18]
```
