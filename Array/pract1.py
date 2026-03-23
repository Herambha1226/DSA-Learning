import array as myarray

# here document of the array
# https://docs.python.org/3/library/array.html

# creating array 
arr = myarray.array('i',[1,2,3])
arr1 = myarray.array('d',[1.0,2.1,2.4,2.5,2.6])
arr2 = myarray.array('u',['a','b','c','d'])

# type codes
print(arr.typecode)
print(arr1.typecode)
print(arr2.typecode)

# first look ar array
print(arr)
print(arr1)
print(arr2)

# printing the length of an array
print(len(arr))
print(len(arr1))
print(len(arr2))


for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\n")


for i in range(0,len(arr1)):
    print(arr[i],end=" ")
print("\n")


for i in range(0,len(arr2)):
    print(arr[i],end=" ")
print("\n")


