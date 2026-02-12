class InsertionSort:
    def __init__(self, array):
        self.array = array

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]

            j = i - 1
            # [1, 2, 3, 4]
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1

            self.array[j + 1] =  key

        return  self.array

if __name__ == "__main__":
    arr = [1, 4, 8, 2, 5, 7, 9, 0]
    print(arr)
    sort = InsertionSort(arr)
    sorted_arr = sort.insertion_sort()
    print(sorted_arr)


