class MyHashMap:

    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def get_hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hsh = self.get_hash(key)
        self.table[hsh] = value

    def get(self, key: int) -> int:
        hsh = self.get_hash(key)
        if not self.table[hsh]:
            return self.table[hsh]
        return -1

    def remove(self, key: int) -> None:
        hsh = self.get_hash(key)
        if self.table[hsh]:
            self.table[hsh] = None
    
    def __str__(self) -> str:
        print(self.table)
        return ''

# Your MyHashMap object will be instantiated and called as such:
# [[],[2],[3,11],[4,13],[15,6],[6,15],[8,8],[11,0],[11],[1,10],[12,14]]
obj = MyHashMap()
obj.remove(2)
obj.put(3, 11)
print(obj)
obj.get(3)
obj.put(4, 13)
obj.put(15, 6)
obj.put(6, 15)
obj.put(8, 8)
obj.put(11, 0)
print(obj.get(11))
obj.put(1, 10)
obj.put(12, 14)
# obj.put()


print(obj)
param_2 = obj.get(11)

obj.remove(1)