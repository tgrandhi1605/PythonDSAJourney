class Location:
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

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = '  ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_world_chart():
    world = Location("Global")

    india = Location("India")

    gujarat = Location("Gujarat")
    gujarat.add_child(Location("Ahmedabad"))
    gujarat.add_child(Location("Baroda"))

    karnataka = Location("Karnataka")
    karnataka.add_child(Location("Bangalore"))
    karnataka.add_child(Location("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = Location("USA")

    california = Location("California")
    california.add_child(Location("San Francisco"))
    california.add_child(Location("Palo Alto"))
    california.add_child(Location("Mountain View"))

    new_jersey = Location("New Jersey")
    new_jersey.add_child(Location("Princeton"))
    new_jersey.add_child(Location("Trenton"))

    usa.add_child(new_jersey)
    usa.add_child(california)

    world.add_child(india)
    world.add_child(usa)

    world.print_tree(3)

if __name__ =="__main__":
    build_world_chart()



