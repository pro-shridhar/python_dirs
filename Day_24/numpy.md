# NUMPY
  it is a array like datatype used to handel similer type of data
  numpy used in scientific computing
  --> Fixed size of creation
  --> Faster then list
  --> 
# 1st 
  import numpy as <name as we want{np}>

  arr = np.array([1,2,3,4])

  for homogeneus data 

  arr = np.array([1,2,3,4],dtype = <name of dataType>)
  in multi dimension array element should be equal en evry sub arrya

# 2nd arange
  arr = np.arange(<this work same as range function in pyhton>)

  --> for reshape array we use reshape function
  arr = np.arange(1,11).reshape(2,5)
  this reshape give you 2D arrya of 2 by 5 dimension 
  we can reshape array only in factors a of total element in it \

  exapmle -> if array have 20 element in in then array can we re shape in
             (2,10),(5,4)

# 3rd ones and zeros
  arr = np.ones((3,4))
  it will give us 3/4 matrix of ones

  arr = np.zeros((2,4))
  it will give us 2/4 matrix of zeros

# 4th random
  arr = np.random.random((3,14))
  it will create array of random value of range you pass

# 5th linspace
  arr = np.linspace(start,end,number of element)
  arr = np.linspace(-10,10,10)
  this mean array strat with -10 have 10 element of equal differenc till 10

# 6th identity
  arr = np.identity(number)
  it create identity matrix


# ndim, shape, size, itemsize, dtype, astype
  ndin -> used to now the dimensions of arr
  shape -> used to now the attributes of arr
  size -> used to now the total of all the element of arr
  itemsize -> used to now the size of element of arr
  dtype -> used to now the data type of arr
  astype -> used to change data type of arr

# Operation on array 
  scaler function -> simple operation on every element
  example => arr1*2 (any arthmetic operation)
  vecter function -> array level operation 
  example => arr1 + arr2 or np.max(arr2)

# for itration
use np.ndilter(arr)

# Transpose
  np.transpose(arr)
  or 
  arr.t
  both give as transpode matrix

# Ravel
  to convert any array into 1D use arr.ravel()

# Stacking
  if we want to join array then it is neccessary to have compatable dimension
 
  for horizontal stacking
  np.hstack(all arrays)

  for vertical stacking
  np.vstack(all arrays)

# Splitiing
  if we want to split any dimension array then you can cut it only in equal part of there fector

  for horizontal spliting 
  np.hsplit(arr,<number of part you wnat>)

  for vertical spliting 
  np.vsplit(arr,<number of part you wnat>)