class HashTable:
    def __init__(self, size):
        self.table = [None] * size # Dynamic array of strings to store
  
        self.S = size # Total number of slots in the table
        self.n = 0 # Current number of elements present in the table
    def __del__(self):
        del self.table

    def isEmpty(self):
        return self.n == 0

    def isFull(self):
        return self.n == self.S

    def loadFactor(self):
        return self.n / self.S

    def getHashValue(self, name):
        temp = 0
        for char in name:
            temp += ord(char)
        return temp
    
    def insert(self, name):
        n = self.getHashValue(name)
        hsh = n % self.S
    
        if not self.table[hsh]:
            self.table[hsh] = name
            self.n += 1

        else:
            print('Traversing:', end=' ')
            while hsh < self.S and self.table[hsh] is not None:
                print(self.table[hsh], end=' ')
                hsh += 1
            print()
            if hsh < self.S:
                self.table[hsh] = name
                self.n += 1
            else:
                return False
        return True
        
    def display(self):
        for element in self.table:
            if element is None:
                print('empty', end=' ')
            else:
                print(element, end=' ')
        print()

    def search(self, name):
        n = self.getHashValue(name)
        hsh = n % self.S
        if self.table[hsh] == name:
            print('Found')
            return True
        else:
            print('Traversing: ', end='')
            while hsh < self.S:
                if self.table[hsh] == name:
                    print('Found')
                    return True
                print(self.table[hsh], end=' ')
                hsh += 1
            
        print('\nNot Found')
        return False

    def remove(self, name):
        n = self.getHashValue(name)
        hsh = n % self.S
        if self.table[hsh] == name:
            self.table[hsh] = None
            return True
        else:
            print('Traversing: ', end='')
            while hsh < self.S:
                if self.table[hsh] == name:
                    self.table[hsh] = None
                    return True
                print(self.table[hsh], end=' ')
                hsh += 1
            
        print('\nNot Found')
        return False

def main():
    size = int(input('Enter the size of the table: '))
    h = HashTable(size)
    while True:
        choice = int(input('1. Insert a name \n 2. Search for a name \n 3. Remove a name \n 4. Display the Hash Table \n 5. Display Load Factor of the table \n6. Exit\n\nEnter your choice: '))
        if choice == 1:
            name = input('Enter name: ')
            h.insert(name)
        elif choice == 2:
            name = input('Enter name: ')
            h.search(name)
        elif choice == 3:
            name = input('Enter name: ')
            h.remove(name)
        elif choice == 4:
            h.display()
        elif choice == 5:
            print(h.loadFactor())
        elif choice == 6:
            break
main()
# h = HashTable(5)
# h.insert('affan')
# h.insert('abid')
# # print(h.insert('abid'))
# # print(h.insert('abid'))
# # print(h.insert('affan'))
# # print(h.insert('affan'))

# h.remove('abid')
# h.display()


    

