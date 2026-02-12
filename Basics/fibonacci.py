class Fibonacci:
    def __init__(self):
        self.series = [0, 1]

    def generate_series(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n ==2:
            return self.series
        else:
            while len(self.series) < n:
                next_value = self.series[-1] + self.series[-2]
                self.series.append(next_value)
            return  self.series

if __name__ == "__main__":
    fib = Fibonacci()
    print(fib.generate_series(10))