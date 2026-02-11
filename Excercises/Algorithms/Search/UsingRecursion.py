class SearchUsingRecursion:
    def __init__(self, array, target):
        self.array = array
        self.target = target

    def search(self, left = 0, right = None):
        if right is None:
            right = len(self.array) -1
        if left > right:
            return -1

        mid = (left + right) // 2

        if self.array[mid] == self.target:
            return mid
        elif self.array[mid] > self.target:
            return self.search(left, mid -1)
        else:
            return self.search(mid + 1, right)

if __name__ == "__main__":
    arr = [23, 22, 45, 65, 89, 99, 87, 45]
    target = 65
    arr.sort()
    print(arr)
    search = SearchUsingRecursion(arr, target)
    print(search.search())