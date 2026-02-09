class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if self.data < data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)

        if self.data > data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def search(self, value):
        if self.data == value:
            return True

        if self.data < value:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if self.data > value:
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