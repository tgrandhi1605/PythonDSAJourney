class LinearProbing:
    def __init__(self):
        self.arr = [None for i in range(10)]
        self.TOMBSTONE = "DELETED"

    def get_hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % 10

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        for i in range(len(self.arr)):
            probing_index = (h + i) % len(self.arr)

            if self.arr[probing_index] is None:
                self.arr[probing_index] = (key, value)
                return
            elif self.arr[probing_index][0] == key:
                self.arr[probing_index] = (key, value)
                return

        raise Exception("HashTable  is full")

    def __getitem__(self, key):
        h = self.get_hash(key)
        for i in range(len(self.arr)):
            probing_index = (h + i) % len(self.arr)
            if self.arr[probing_index] is None:
                return None
            if self.arr[probing_index] == self.TOMBSTONE:
                continue
            if self.arr[probing_index][0] == key:
                return self.arr[probing_index][1]
        return None

    def __delitem__(self, key):
        h = self.get_hash(key)
        for i in range(len(self.arr)):
            probing_index = (h + i) % len(self.arr)

            if self.arr[probing_index] is None:
                return

            if self.arr[probing_index] != self.TOMBSTONE and self.arr[probing_index][0] == key:
                self.arr[probing_index] = self.TOMBSTONE
                return

if __name__ == "__main__":
    ht = LinearProbing()
    ht["name"] = "Alice"
    ht["age"] = 30
    ht["name"] = "Tharun"
    ht["age"] = 33
    print(ht.arr)  # Output: Tharun
    print(ht["name"])  # Output: Alice
    print(ht["age"])   # Output: 30
    del ht["name"]
    print(ht.arr)  #
    print(ht["name"])  # Output: None





