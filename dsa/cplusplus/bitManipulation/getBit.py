def getBit(n, pos):
    return (n & (1<<pos)) != 0

def setBit(n, pos):
    return (n | (1<<pos))

def clearBit(n, pos):
    mask = ~(1<<pos)
    return mask & n

def main():
    # print(setBit(5, 1))
    # print(getBit(5, 5))
    print(clearBit(7, 2))

main()