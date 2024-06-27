k = int(input())

for i in range(k):
    n = int(input())
    a = list(map(int, input().split()))

    i = 0
    j = n - 1
    while i != j:
        if a[i] != a[i+1] and a[j] != a[j-1]:
            i += 1
            j -= 1
            break
        if a[i] == a[i+1]:
            i += 1
        if a[j] == a[j-1]:
            j -= 1
    if i == j:
        print(0)
    else:
        print(a[j] - a[i] + 1)
