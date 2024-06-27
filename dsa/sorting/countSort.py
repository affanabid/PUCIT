import time

def countingSort(a):
    max_a = max(a)

    b = [0] * (max_a + 1)
    c = [0] * len(a)

    for i in range(len(a)):
        b[a[i]] += 1

    for i in range(1, max_a+1):
        b[i] += b[i-1]

    for i in range(len(a)):
        c[b[a[i]] - 1] = a[i]
        b[a[i]] -= 1

    return c

array = [3,6,1,4,2,5]
countingSort(array)