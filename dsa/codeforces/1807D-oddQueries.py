
def oddQuery(array, c):
    l = c[0] - 1
    r = c[1] - 1
    k = c[2]
    range_n = []
    for i in range(l, r+1):
        range_n.append(i)

    sm = 0
    for i in range(len(array)):
        if i in range_n:
            sm += k
        else:
            sm += array[i]
    if sm % 2 == 0:
        print('NO')
    else:
        print('YES')

tests = int(input())

for i in range(tests):
    size, queries = map(int, input().split())
    Query = []
    array = list(map(int, input().split()))

    que = []
    for i in range(queries):
        q = tuple(map(int, input().split()))
        que.append(q)

    Query.append(array)
    Query.append(que)
for i in range(1,len(Query) - 1):
    for j in range(len(Query[i])):
        current = Query[1]
        oddQuery(array, current[j])
    # for i in range(queries):
    #     l, r, k = map(int, input().split())
    #     oddQuery(array, l-1, r-1, k)
