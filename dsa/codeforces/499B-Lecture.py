n, m = map(int, input().split())
data = {}
for i in range(m):
    a, b = map(str, input().split())
    if len(a) <= len(b):
        data[a] = a
        data[b] = a
    elif len(b) < len(a):
        data[a] = b
        data[b] = b

s = list(map(str, input().split()))
for word in s:
    print(data[word], end=' ')
    