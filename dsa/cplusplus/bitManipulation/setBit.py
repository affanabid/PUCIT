def setBit(n, pos):
    return (n | (1<<pos))

print(setBit(5, 1))