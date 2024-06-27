def similar(n1, n2):
    if abs(n1-n2) == 1  or remainder(n1) == remainder(n2):
        return True
    return False

def remainder(n):
    return n % 2

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
