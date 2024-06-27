def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def even(n):
    if n % 2 == 0:
        return True
    return False

def goodDigit(array, n, i):
    if i == n:
        return "Good"
    if (even(i) == True and even(array[i]) == False) or (even(i) == False and prime(array[i]) == False):
        return "Not good"
    return goodDigit(array, n, i+1)

# array = [2,2,4,3,6,5]
array = [3,2,7,8]

n = len(array)
print(goodDigit(array, n, 0))
# print(even(18))