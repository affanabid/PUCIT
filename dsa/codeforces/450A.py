def last_child(n, m, line):
    new_line = []
    for i in range(len(line)):
        data = (i+1, line[i])
        new_line.append(data)

    i = 0
    while i < len(new_line):
        current = new_line[i]
        candies = current[1]
        new_candies = candies - m
        if new_candies > 0:
            new_data = (current[0], new_candies)
            new_line.append(new_data)
        i += 1
    result = new_line[-1][0]
    return result

n, m = map(int, input().split())
array = list(map(int, input().split()))
print(last_child(n, m, array))
