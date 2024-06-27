def decimalToBinary(n):
    if n == 0:
        return 
    decimalToBinary(n//2)
    print(n%2, end='')

def decimalToOctal(n):
    if n == 0:
        return
    decimalToOctal(n//8)
    print(n%8, end='')

decimalToBinary(20)
print()
decimalToOctal(20)
