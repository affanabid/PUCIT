def pairSum(array, n, key):
    if n == 0:
        return False
    
    if array[0] + array[n-1] == key:
        return True
    
    elif array[0] + array[n-1] > key:
        return pairSum(array[:-1], n-1, key)
    
    else:
        return pairSum(array[1:], n-1, key)

def sumR(array, n, key, i, j):
    if i == j:
        return False
    
    if array[i] + array[j] == key:
        return True
    
    elif array[i] + array[j] > key:
        return sumR(array, n, key, i, j-1)

    else:
        return sumR(array, n, key, i+1,  j)

def recursivePairSum(array, n, key):
    if array[0] >= key or array[n-1] * 2 <= key:
        return False
    return sumR(array, n, key, 0, n-1)
    
array = [1,3,5,7,9]
key = 16

print(pairSum(array, len(array), key))
print(recursivePairSum(array, len(array), key))