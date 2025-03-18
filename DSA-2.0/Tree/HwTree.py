class TreeNode:
    def __init__(self, name,des):
        self.name = name
        self.des = des
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    
    def print_tree(self,property_name):
        if property_name == "both":
            value = self.name + '(' + self.des + ')'
        elif property_name == "name":
            value = self.name
        else:
            value = self.des

        spaces = " "   * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)

    # def print_tree(self):
    #     spaces = ' ' * self.get_level() * 3
    #     prefix = spaces + "|__" if self.parent else ""
    #     print(prefix + self.data)
    #     if self.children:
    #         for child in self.children:
    #             child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_managment_tree():
    CEO = TreeNode("Nipul Tiwari","CEO")
    
    CTO = TreeNode("Chinmay", "CTO")
    CEO.add_child(CTO)

    infra_head = TreeNode("Vishwa", "Inrastructure Head")
    CTO.add_child(infra_head)
    infra_head.add_child(TreeNode("Dhawal","cloud manager"))
    infra_head.add_child(TreeNode("Abhijeet ","App Manager"))
    
    application_head = TreeNode("Amir","Application Head")
    CTO.add_child(application_head)

    hr_head = TreeNode("Gells", " HR Head")
    CEO.add_child(hr_head)
    hr_head.add_child(TreeNode("Peter","Recuireter Manager"))
    hr_head.add_child(TreeNode("Waqas","Policy Manager"))

    return CEO

if __name__ == '__main__':
    root_node = build_managment_tree()
    root_node.print_tree("bot")