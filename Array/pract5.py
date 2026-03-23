# numpy array
# create numpy array 
import numpy as np 

arr1 = np.array([1,2,3,4,5])
print(arr1)

# zeros array
arr2 = np.zeros((2,2))

# one's array
arr3 = np.ones((2,2))

# constant values
arr4 = np.full((2,2),5)

# identity matrix 
arr5 = np.eye(2)

# creating an array with radom values 
rndom = np.random.random((2,2))

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(rndom)


# 0-D,1-D,2-D,3-D array 
# 0-D 
zero = np.array(1)
print(zero)
# 1-D 
ones = np.array([1,1])
print(ones)
# 2-D 
twod = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(twod)
#3-D 
threed = np.array([[[1,2,3],[3,4,5]],[[5,6,7],[7,8,9]]])
print(threed)

# multidimensional array 
mult = np.array([1,2,3,4,5], ndmin=5)
print(mult)


# CRUD Operations in array
sample = np.array([i for i in range(0,10)])
for i in range(0,len(sample)):
    print(sample[i],end=" ")
print("\n")

# updating elements
sample[9] = 100
print(sample)
print("\n")

# delting elements 
sample = np.delete(sample,3)
print(sample)


# searching elements
x = list(range(0,20000,5))
sample2 = np.array(x)
sort2 = np.sort(sample2)[::-1]
print(sort2)
