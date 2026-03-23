import array as myarray
# accessing elements from an array using index values
x = list(range(1,100,2))
new_array = myarray.array('i',x)

for i in range(0,len(new_array)):
    print(new_array[i], end=" ")
print("\n")

# accessing elements at index 20
print(new_array[20])


# adding elements in array
arr1 = myarray.array('i',[3,4,5,6,7,8,9,10])
for i in range(0,len(arr1)):
    print(arr1[i],end=" ")
print("\n")

# adding 
arr1.insert(0,2)
arr1.insert(0,1)
arr1.insert(0,0)

# printing new array 

for i in range(0,len(arr1)):
    print(arr1[i],end=" ")
print("\n")

# using append
arr1.append(20)
arr1.append(100)
for i in range(0,len(arr1)):
    print(arr1[i],end=" ")
print("\n")


# updating elemnts in an array
arr2 = myarray.array('i',[1,2,2,4,5])

for i in range(0,len(arr2)):
    print(arr2[i],end=" ")
print("\n")

arr2[2] = 20
for i in range(0,len(arr2)):
    print(arr2[i],end=" ")
print("\n")


# deleting element in array
print(arr2[len(arr2) - 2])
arr2.pop(len(arr2) - 2)
for i in range(0,len(arr2)):
    print(arr2[i],end=" ")
print("\n")


# using the remove() method

arr2.remove(5)
for i in range(0,len(arr2)):
    print(arr2[i],end=" ")
print("\n")



