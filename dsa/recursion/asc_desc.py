def descending(n):
    if n == 0:
        return
    print(n)
    descending(n-1)

def ascending(n):
    if n == 0:
        return
    ascending(n-1)
    print(n)
    
ascending(5)