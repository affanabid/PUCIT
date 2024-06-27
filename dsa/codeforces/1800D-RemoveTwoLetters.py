t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    # hashmap = {}
    unique_substrings = set()
    for i in range(n-1):
        new_s = s[:i] + s[i+2:]
        unique_substrings.add(new_s)
        
    key_count = len(unique_substrings)
    print(key_count)


