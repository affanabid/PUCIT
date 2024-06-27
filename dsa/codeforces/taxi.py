
array = [2,3,4,4,2,1,3,1]

for i in range(len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
        array[j+1] = array[j]
        j-=1
    array[j+1] = key

taxis = 0
count = 0
i = 0
while i < len(array):
    current = array[i]
    if current != -1:
        count += current
    # current = array[i]
    # count += current
    # if count == 4:
    #     count = 0
    #     taxis += 1
    #     i += 1
    # elif count > 4:
    #     count = 0
    #     taxis += 1
    # elif count < 4:
        
    #     i += 1

print(taxis)
