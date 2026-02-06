class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


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
    del ht["March 7"]
    print(ht.arr)
