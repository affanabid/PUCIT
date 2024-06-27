s, n = map(int, input().split())

success = True
for i in range(n):
    x, y = map(int, input().split())

    if s < x:
        success = False
        break
    else:
        s += y

if success:
    print('YES')
else:
    print('NO')
    