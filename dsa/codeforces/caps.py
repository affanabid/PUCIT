string = input()

accid = True
for i in range(1, len(string)):
    if ord(string[i]) >= 97:
        accid = False

new_string = ''

if accid:
    for i in range(len(string)):
        if i == 0 and ord(string[i]) >= 97:
            new_string += chr(ord(string[i]) - 32)
        elif i == 0 and ord(string[i]) <= 90:
            new_string += chr(ord(string[i]) + 32)
        elif i > 0 and ord(string[i]) <= 90:
            new_string += chr(ord(string[i]) + 32)
        else:
            new_string += string[i]
    string = new_string

print(string)
