# searching Operations on array using index()
import array as arr_

x = list(range(0,10000,2))
arr = arr_.array('i',x)

# print first 10 elements of the array
for i in range(0,len(arr[0:10])):
    print(arr[i],end=" ")
print("\n")

# Search 
index = arr.index(3928)
res = arr[index]
print(index,res)


# Sorting array 
srt_arr = arr_.array('i',[5,3,4,1,6,7,10,9,8])
sorted_arr = srt_arr.tolist()

# ascending order
sorted_arr.sort()
print(sorted_arr)

#desending order
sorted_arr.sort(reverse=True)
print(sorted_arr)

