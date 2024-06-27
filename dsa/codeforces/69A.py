n = int(input())
res_x = res_y = res_z = 0
for i in range(n):
    x, y, z = map(int, input().split())
    res_x += x
    res_y += y
    res_z += z

if res_x == 0 and res_y == 0 and res_z == 0:
    print('YES')
else:
    print("NO")