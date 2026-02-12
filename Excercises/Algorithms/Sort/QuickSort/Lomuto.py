class Lomuto:
    def __init__(self, arr):
        self.arr = arr

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = len(arr) // 2

        left = [x for x in arr if x < arr[pivot]]
        middle = [x for x in arr if x == arr[pivot]]
        right = [x for x in arr if x > arr[pivot]]

        return self.quick_sort(left) + middle + self.quick_sort(right)

if __name__  == "__main__":
    arr = [3, 1, 4, 2, 5, 9, 8, 7, 6]
    print(arr)
    sort = Lomuto(arr)
    sorted_arr = sort.quick_sort(arr)
    print(sorted_arr)


