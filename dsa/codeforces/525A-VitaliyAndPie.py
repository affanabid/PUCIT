n = int(input())
string = input()
len_string = 2*n - 2

keys = set()
count = 0

i = 0
while i < len_string:
    
    current_key = string[i]
    next_door = string[i+1]
    
    if chr(ord(current_key) - 32) != next_door:
        keys.add(current_key)
        next_door_key = chr(ord(next_door) + 32)

        if next_door_key in keys:
            keys.remove(next_door_key)

        else:
            count += 1

    i += 2
print(count)