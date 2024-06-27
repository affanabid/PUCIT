s = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
res = ''

for char in s:
    if char in vowels or char.lower() in vowels:
        pass
    else:
        res += '.'
        res += char.lower()

print(res)