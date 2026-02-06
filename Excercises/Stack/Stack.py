from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def reverse_string(self, string):
        for char in string:
            self.push(char)

        reverse_string = ""
        while not self.is_empty():
            reverse_string += self.pop()
        return reverse_string


if __name__ == "__main__":
    stack = Stack()
    input_string = "Tharun is great!"
    reversed_string = stack.reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")