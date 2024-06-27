def maxSubarray(array, n):
    maxSum = 0
    sum = array[0]
    for i in range(1,n):
        currSum = sum + array[i]

        if ((array[i] % 2) == (array[i-1] % 2)) or currSum <= 0:
            sum = 0
        else:
            sum = currSum
        maxSum = max(sum, maxSum)

    return maxSum
        

print(maxSubarray([9, 9, 8, 8], 4)) 