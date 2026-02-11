class BubbleSort:
    def __init__(self, array):
        self.array = array

    def  bubble_sort(self):
        size = len(self.array)

        for i in range(size - 1):
            swapped = False
            for j in range(size - 1 - i):
                if self.array[j] > self.array[j + 1]:
                    tmp = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = tmp
                    swapped = True

            if not swapped:
                break

if __name__ == "__main__":
    arr = [1, 34, 465,657 ,353, 345, 35, 345, 23, 45, 345, 34, 5, 345, 34, 5, 345, 34, 5, 345, 34, 5]
    print(arr)
    sort = BubbleSort(arr)
    sort.bubble_sort()
    print(arr)
