class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linke_list:
    def __init__(self):
        self.head= None 

    def insert_at_begning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        

    
    def print(self):
        if self.head is None :
            print("the linked list is empty")
            return
        
        itr = self.head
        listr = ''

        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)    
    
    def get_length(self):
        count = 0
        itr =self.head
        while itr:
            count +=1
            itr = itr.next
        return count


if __name__ =='__main__':
    ll = Linke_list() 
    ll.insert_values(["apple","cherry","grapes","coconut"])
    print("the length of ll is :", ll.get_length())
    ll.print()