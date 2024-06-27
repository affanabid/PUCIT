def containsDuplicates(array):
    return len(array) != len(set(array))

array = [1,2,2,4,4]
print(containsDuplicates(array))
