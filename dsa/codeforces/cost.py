x = int(input())

for i in range(x):
    # elements = list(map(int, input().split()))
    elements = []
    string = input()
    for char in string:
        elements.append(int(char))
    n = len(elements)
    i = 0
    cost = 0
    while i < n:
        if i+1 < n:
            if elements[i] == elements[i+1]:
                i += 1
                cost += 1
            else:
                i += 2
        else:
            cost += 1
            i += 1

    print(cost)
