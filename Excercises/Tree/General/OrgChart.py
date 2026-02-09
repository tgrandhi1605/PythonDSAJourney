class OrgChart:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, filter):
        if filter == "name":
            value = self.name
        if filter  == "designation":
            value = self.designation
        if filter  == "both":
            value =  self.name + " (" + self.designation + ")"

        spaces = '  ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(filter)

def build_org_chart():
    ceo = OrgChart("CEO", "Alice")

    cto = OrgChart("CTO", "Chinmay")
    infra_head = OrgChart("Infrastructure Head", "Vishwa")
    infra_head.add_child(OrgChart("Cloud Manager", "Dhaval"))
    infra_head.add_child(OrgChart("App Manager", "Abhijith"))

    hr_head = OrgChart("HR Head", "Gels")
    hr_head.add_child(OrgChart("Recruitment Manager", "Peter"))
    hr_head.add_child(OrgChart("Policy Manager", "Waqas"))

    cto.add_child(hr_head)
    cto.add_child(infra_head)

    ceo.add_child(cto)

    ceo.print_tree(filter="both")

if __name__ == "__main__":
    build_org_chart()