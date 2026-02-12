class FibonacciIteator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0 , 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count +=1
            return 0
        elif self.count == 1:
            self.count +=1
            return 1
        else:
            next_value = self.a + self.b
            self.a = self.b
            self.b = next_value
            self.count +=1
            return next_value

if __name__ == "__main__":
    n = 10
    fib = FibonacciIteator(10)
    for num in fib:
        print(num)