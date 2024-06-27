# def merge(array, p, q, r):
#     n1 = q-p+1
#     n2 = r-q
#     left = [0] * (n1+1)
#     right = [0] * (n2+1)
#     for i in range(len(left)):
#         left[i] = p + i - 1
#     for j in range(len(left)):
#         right[j] = q + j
#     i = 1
#     j = 1
#     for k in range(p, r+1):
#         if left[i] <= right[j]:
#             array[k] = left[i]
#             i += 1
#         else:
#             array[k] = array[j]
#             j += 1

# def mergeSort(array, p, r):
#     if p < r:
#         q = (p+r)/2
#         mergeSort(array, p, q)
#         mergeSort(array, q+1, r)
#         merge(array, p, q, r)

# array = [7,5,3,1]
# mergeSort(array, 0, len(array)-1)

def merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = array[p:q+1]  # Copy the left subarray
    right = array[q+1:r+1]  # Copy the right subarray
    left.append(float('inf'))  # Add a sentinel value to mark the end of left array
    right.append(float('inf'))  # Add a sentinel value to mark the end of right array
    i = j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

def mergeSort(array, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(array, p, q)
        mergeSort(array, q + 1, r)
        merge(array, p, q, r)

array = [7, 5, 3, 1]
mergeSort(array, 0, len(array) - 1)
print(array)
