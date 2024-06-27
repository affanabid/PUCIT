def case1(a, b, c):
    return a + b * c

def case2(a, b, c):
    return a * (b + c)

def case3(a, b, c):
    return a * b * c

def case4(a, b, c):
    return (a+b) * c

def case5(a, b, c):
    return a + b + c

def case6(a, b, c):
    return a * b + c

a = int(input())
b = int(input())
c = int(input())

mxVal = max(case1(a, b, c), case2(a, b, c), case3(a, b, c), case4(a, b, c), case5(a, b ,c), case6(a, b, c))

print(mxVal)
