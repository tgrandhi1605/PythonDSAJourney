class FibonacciRecursion:
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)


if __name__ == "__main__":
    fib = FibonacciRecursion()
    n = 10
    print(f"Fibonacci number at position {n} is: {fib.fibonacci(n)}")
    for i in range(n):
        print(f"Fibonacci number at position {i}: is {fib.fibonacci(i)}")
