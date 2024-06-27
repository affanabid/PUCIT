def count(s):
    return len(set(s))

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    
    seen = []
    i = 0
    while i < n:
        if s[i] in seen:
            break
        else:
            seen.append(s[i])
        i += 1
    s1 = s[:i]
    s2 = s[i:]
    ans = count(s1) + count(s2)
    print(ans)
