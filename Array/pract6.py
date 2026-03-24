def insert(arr, n, key, capacity):
    if (n >= capacity):
        return n
    i = n - 1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = key
    return (n + 1)


def binarySearch(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if key == arr[mid]:
        return mid
    elif key > arr[mid]:
        return binarySearch(arr, mid + 1, high, key)
    else:
        return binarySearch(arr, low, mid - 1, key)


def delete(arr, n, key):
    pos = binarySearch(arr, 0, n - 1, key)

    if pos == -1:
        print("Element not found")
        return n

    for i in range(int(pos), n - 1):
        arr[i] = arr[i + 1]
    return n - 1


arr = [10, 20, 30, 40, 50, 0]
n = 5
capacity = len(arr)
key = 25

print("Before Insert : ", arr[:n])
n = insert(arr, n, key, capacity)
print("After Insert  : ", arr[:n])

print("Before Deletion : ", arr[:n])
n = delete(arr, n, key)
print("After Deletion  : ", arr[:n])
