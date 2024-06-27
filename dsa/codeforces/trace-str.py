x = int(input())
for i in range(x):
    n = int(input())
    trace = list(map(str, input().split()))
    s = ''
    seen = [0] * n
    for i in range(n):
        for j in range(len(seen)):
            if int(trace[i]) == seen[j]:
                s += chr(j+97)
                seen[j] = seen[j] + 1
                
                break
    print(s)


