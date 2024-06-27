def selectionSort(array):
    length = len(array)

    for i in range(length-1):
        min_index = i

        for j in range(i+1, length):

            if array[j] < array[min_index]:
                min_index = j
        
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            
    return array

array = [3,5,2,1]
print(selectionSort(array))