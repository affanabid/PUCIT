def decToOct(n):
    if n == 0:
        return 0
    decToOct(n//8)
    print(n%8, end='')

decToOct(16)