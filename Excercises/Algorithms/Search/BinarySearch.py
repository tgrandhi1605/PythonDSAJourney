class BinarySearch:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def binary_search(self):
        left_index = 0
        right_index = len(self.arr) - 1
        mid_index = 0

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if self.arr[mid_index] < self.target:
                left_index = mid_index + 1
            elif self.arr[mid_index] > self.target:
                right_index = mid_index - 1
            else:
                return mid_index

        return  -1

if __name__ == "__main__":
    arr = [1, 34, 465,657 ,353, 345, 35, 345, 23, 45, 345, 34, 5, 345, 34, 5, 345, 34, 5, 345, 34, 5]
    target = 34

    arr.sort()
    print(arr)
    search = BinarySearch(arr, target)
    print(search.binary_search())

