class TreeNode:
    def __init__(self,loc):
        self.loc = loc
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

        return child

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level    

    def print_tree(self,l):
              # 1st Method 
        # if self.get_level() > l:
        #     return

        spaces = ' ' * self.get_level() * 3 
        prefix = spaces + "|__" if self.parent else ""
           # second method 
        if self.get_level() <= l:
            print(prefix + self.loc)
            if self.children:
                for child in self.children:
                    child.print_tree(l)
            

def build_loc_tree():
    Global = TreeNode("Global")

    India = Global.add_child(TreeNode("India"))
    state = India.add_child(TreeNode("Gujrat"))
    state.add_child(TreeNode("Ahamdabad"))
    state.add_child(TreeNode("Barodra"))

    Karnatka = India.add_child(TreeNode("Karnatka"))
    Karnatka.add_child(TreeNode("Banluru"))
    Karnatka.add_child(TreeNode("Mysore"))


    USA = Global.add_child(TreeNode("USA"))
    newjersy = USA.add_child(TreeNode("New Jersy"))
    newjersy.add_child(TreeNode("Priceton"))
    newjersy.add_child(TreeNode("Trenton"))

    california = USA.add_child(TreeNode("California"))
    california.add_child(TreeNode("San Fransisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))
    
    return Global

if __name__== '__main__':
    root_node = build_loc_tree()
    root_node.print_tree()
    # print("Level of root node:", root_node.children[0].get_level())