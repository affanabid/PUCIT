n, m = map(int, input().split())
array = input().split()
a = input().split()
b = input().split()
STDOUT = 0
for i in range(len(array)):
    if array[i] in a:
        STDOUT += 1
    elif array[i] in b:
        STDOUT -= 1
print(STDOUT)
