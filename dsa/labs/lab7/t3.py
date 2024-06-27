import random

def getRandomNumber(start, end):
    return random.randint(start, end)

def getHashValue(n, table):
    size = len(table)
    return n % size

def insert(num, table):
    hsh = getHashValue(num, table)
    
    if table[hsh] is None:
        table[hsh] = num
        return True

    else:
        return False

insertions = []
j = 0
i = 0
while i < 50:
    count = 0
    size = 100000

    hashtable = [None] * size

    while True:


        rand = getRandomNumber(0, 100)
        if insert(rand, hashtable):
            count += 1
        else:
            break
    # insertions.append(count)
    j += count
    print(f'Exp#{i+1}: {count}')
    i += 1

average = j / 50
print('---------------------------')
print('Average', round(average))
