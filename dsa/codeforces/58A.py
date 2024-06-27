s = input()

stack = []

found = False

for char in s:
    if len(stack) == 0:
        if char == 'h':
            stack.append('h')
    elif stack[-1] == 'h':
        if char == 'e':
            stack.append('e')
    elif stack[-1] == 'e':
        if char == 'l':
            stack.append('l')
    elif stack[-1] == 'l' and stack[-2] == 'e':
        if char == 'l':
            stack.append('l')
    elif stack[-1] == 'l' and stack[-2] == 'l':
        if char == 'o':
            stack.append('o')
            found = True
            break
if found:
    print('YES')
else:
    print('NO')        
