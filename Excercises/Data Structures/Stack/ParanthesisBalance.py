from Excercises.Stack.Stack import Stack

class ParanthesisBalance:
    def __init__(self):
        self.expression = {
    ")": "(",
    "]": "[",
    "}": "{"
}
    def is_balanced(self, string):
         stack = Stack()
         for char in string:
             if char in self.expression.values(): # ')'
                 stack.push(char)
             if char in self.expression.keys():
                 if stack.is_empty():
                    return False

                 if stack.peek() == self.expression[char]:
                     stack.pop()
                 else:
                     return False

         return  stack.is_empty()


if __name__ == "__main__":
    # stack ( (
    pb = ParanthesisBalance()
    print(pb.is_balanced("()"))  # Output: True
    print(pb.is_balanced("()[]{}"))  # Output: True
    print(pb.is_balanced("(]"))  # Output: False
    print(pb.is_balanced("([)]"))  # Output: False
    print(pb.is_balanced("{[]}"))  # Output: True