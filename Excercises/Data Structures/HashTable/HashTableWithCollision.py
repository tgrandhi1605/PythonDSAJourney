class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

if __name__ == '__main__':
    ht = HashTable()
    ht["March 6"] = 3100
    ht["March 7"] = 3200
    ht["March 17"] = 3300
    ht["March 27"] = 3400
    print(ht.arr)
    print(ht["March 6"])
    print(ht["March 7"])
    print(ht["March 27"])