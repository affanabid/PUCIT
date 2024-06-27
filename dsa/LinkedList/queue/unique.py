def getUniqueElement(string):
    l = len(string)
    seen = []
    q = []
    for i in range(l):
        current = string[i]
        if current == q[0]:
            pop(q)
            seen.append(current)
        else:
            q.append(current)
    while len(q) != 0:
        if q[0] not in seen:
            return q[0]
        else:
            pop(q)
    return -1


def pop(list):
    element = list[0]
    list.pop(0)
    return element
q = [5, 4, 3, 2, 1]
s = 'leetcode'
getUniqueElement(s)
# print(q)
# print(pop(q))
# print(q)

# q.append(2)
# print(q.pop())