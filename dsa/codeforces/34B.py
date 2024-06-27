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

n, m = input().split()
n = int(n)
m = int(m)

tvs = list(map(int, input().split()))

mergeSort(tvs, 0, n-1)

i = 0
total = 0
while i < m:
    if tvs[i] >= 0:
        break

    total += abs(tvs[i])
    i += 1

print(total)
