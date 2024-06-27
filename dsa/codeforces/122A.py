num = int(input())

lucky = True
for n in str(num):
    if n != '4' and n != '7':
        lucky = False
        break

if lucky:
    print('YES')
else:
    if num % 4 == 0 or num % 7 == 0:
        print('YES')
    else:
        print('NO')
