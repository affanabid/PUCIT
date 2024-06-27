# def calculateGCD(n1, n2, i=0):
#     if n1%i == 0 and n2 % i == 0:
#         print(i)
#         return i
    
#     if n1>n2:
#         calculateGCD()
#     else:
#         pass

#     high = max(n1, n2)
#     low = min(n1, n2)    
#     calculateGCD(n1, n2, low-1)

# calculateGCD(12, 18)

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        remainder = a%b
        return gcd_recursive(b, remainder)

num1 = 40
num2 = 60

result = gcd_recursive(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")

examples = [[12, 18], [25, 15], [40, 60]]
for e in examples:
    A, B = e
    gcd = gcd_recursive(A, B)
    print("GCD of", A, "and", B, "is:", gcd)
