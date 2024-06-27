def totalCharges(n, m, a, b):
    charges = 0
    while n > 0:
        if n == 1:
            charges += a
            n -= 1
        else:
            charges += b
            n -= m
    print(charges)

# n, m, a, b = map(int, input().split())
n, m, a, b = 10,3,5,1


        
totalCharges(n, m, a, b)


