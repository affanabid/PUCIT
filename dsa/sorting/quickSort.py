def partition(array, p, r):
    pivot = array[r]
    i = p-1
    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1

def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)
    return array

array = [1,3,5,0,2,4,7,6]
print(quickSort(array, 0, len(array)-1))