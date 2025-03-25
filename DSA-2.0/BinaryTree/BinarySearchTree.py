class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return

        if data < self.data:
            # Adding in the lef side
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)            
    

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node 
        elements.append(self.data)

        # visit right
        if self.right:
            elements += self.right.in_order_traversal()

        return elements        
    
    def pre_order_traversal(self):
        elements = []
        
        # Append the current Node 
        elements.append(self.data)

        # checking for the left
        if self.left:
            elements += self.left.pre_order_traversal()


        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
    
    def post_tree_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_tree_traversal()

        # might be in the right
        if self.right:
            elements += self.right.post_tree_traversal()

        elements.append(self.data)    
 
        return elements

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False    
        
        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False    
    
    def find_min(self):
        if self.left:
            return self.left.find_min()       
        return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data
    
    def calculate_sum(self):
        right_sum  = self.right.calculate_sum() if self.right else 0
        left_sum  =  self.left.calculate_sum() if self.left else 0
        return self.data + left_sum + right_sum
      
        
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
            
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right     
            if self.right is None:
                return self.left
            
                         # By using the right min element delete method
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
                         
                         # Used the left max delete element method 
            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.delete(max_value)

        return self  

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root  

if __name__ == '__main__':
    numbers = [17,4,10,20,9,23,18,34]
    number_tree = build_tree(numbers)
    # print(number_tree.search(20))
    # print("The min number is the ",number_tree.find_min())
    # print("The max element is the ",number_tree.find_max())
    # print("the sum of the all element is ",number_tree.calculate_sum())
    # print("The in order traversal is ",number_tree.in_order_traversal())
    # print("the pre order traversal is ",number_tree.pre_order_traversal())
    # print(" Just for checkin :",number_tree.post_tree_traversal())
    print(("th tree befor deleting is ",number_tree.in_order_traversal()))
    number_tree.delete(10)
    print("the tree after deleting is ", number_tree.in_order_traversal())