class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

        return None

    def inorder_traversal(self):
        elements = []

        # Left Tree
        if self.left:
            elements += self.left.inorder_traversal()

        # Root Node
        elements.append(self.data)

        # Right Tree
        if self.right:
            elements += self.right.inorder_traversal()

        return  elements

    def pre_order_traversal(self):
        elements = []

        # Root Node
        elements.append(self.data)

        # Left Tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Right Node
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        # Left Tree
        if self.left:
            elements += self.left.post_order_traversal()

        # Right Node
        if self.right:
            elements += self.right.post_order_traversal()

        # Root Node
        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()


    def find_sum(self):
        total = self.data

        if self.left:
            total += self.left.find_sum()

        if  self.right:
            total += self.right.find_sum()

        return  total

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:", numbers_tree.inorder_traversal())
    print("Post order traversal gives this sorted list:", numbers_tree.pre_order_traversal())
    print("Pre order traversal gives this sorted list:", numbers_tree.post_order_traversal())

    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.find_sum())

    deleted_tree = numbers_tree.delete(1)
    print("After deleting 20, in order traversal gives this sorted list:", deleted_tree.inorder_traversal())
