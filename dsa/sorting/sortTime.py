import time
import random


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

def mergeSort(A, p, r):
    if p < r:
        q = (p+r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1+1)
    R = [0] * (n2+1)
    for i in range(n1):
        L[i] = A[p + i]
    for i in range(n2):
        R[i] = A[q + i + 1]

    L[n1] = float('inf')
    R[n2] = float('inf')

    i = j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def main():
    array_size = 5000
    min_value = 1  
    max_value = 10000
    generated_array = [random.randint(min_value, max_value) for _ in range(array_size)]
    mergeSort(generated_array, 0, len(generated_array) - 1)
    countingSort(generated_array)

start_time = time.time()

main()

end_time = time.time()

final_time = round(end_time - start_time, 5)
print('Execution Time (s):  ', final_time)

final_time_ms = round(final_time * 1000, 2)  
print('Execution Time (ms): ', final_time_ms)
