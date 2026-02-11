class LinearSearch:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def linear_search(self):
        for index, element in enumerate(self.arr):
            if element == self.target:
                return index
        return -1

if __name__ == "__main__":
    arr = [1, 34, 465,657 ,353, 345, 35, 345, 23, 45, 345, 34, 5, 345, 34, 5, 345, 34, 5, 345, 34, 5]
    target = 6575

    search = LinearSearch(arr, target)
    print(search.linear_search())
