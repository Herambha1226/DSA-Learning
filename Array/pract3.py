# Slicing 
import array as arr

x = list(range(0,100,3))
arr1 = arr.array('i',x)

# slicing Operation
arr2 = arr1[10:20]
for i in range(0,len(arr2)):
    print(arr2[i],end=" ")
print("\n")

# negative indxing
arr3 = arr1[10:-20]
for i in range(0,len(arr3)):
    print(arr3[i],end=" ")
print('\n')

# Reversing the oreder using slicing
arr4 = arr1[::-1]
for i in range(0,len(arr4)):
    print(arr4[i],end=" ")
print("\n")


