def recursiveBinarySearch(array, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right ) // 2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return recursiveBinarySearch(array, target, left, mid-1)
    
    else:
        return recursiveBinarySearch(array, target, mid+1, right)


array = [5,2,7,1,9]
target = 9
print(recursiveBinarySearch(array, target, 0, len(array)))

def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

arr = [1,3,5,7,9]
target = 5
result = binarySearch(arr, target)
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print("Target not found.")