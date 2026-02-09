class GeneralTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = '  ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_eccomerce_chart():
    root = GeneralTree("Electronics")

    laptop = GeneralTree("Laptop")
    laptop.add_child(GeneralTree("Mac"))
    laptop.add_child(GeneralTree("Surface"))
    laptop.add_child(GeneralTree("Thinkpad"))

    cellphone = GeneralTree("Cell Phone")
    cellphone.add_child(GeneralTree("iPhone"))
    cellphone.add_child(GeneralTree("Google Pixel"))
    cellphone.add_child(GeneralTree("Vivo"))

    tv = GeneralTree("TV")
    tv.add_child(GeneralTree("Samsung"))
    tv.add_child(GeneralTree("LG"))
    tv.add_child(GeneralTree("Sony"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ =="__main__":
    build_eccomerce_chart()



