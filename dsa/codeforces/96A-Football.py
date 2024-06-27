s = input()
n = len(s)

i = 1
current = int(s[0])
current_count = 1
dangerous = False
while i < n:
    num = int(s[i])
    if num == current:
        current_count += 1
        if current_count == 7:
            dangerous = True
            break
        i += 1
    else:
        current = num
        current_count = 1
        i += 1

if dangerous:
    print('YES')
else:
    print('NO')
