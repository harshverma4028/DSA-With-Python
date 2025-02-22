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
    
    def remove_at(self,index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index : ")
        
        if index ==0:
            self.head = self.head.next
            return
        
        count =0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count +=1
    
    def insert_at(self,index,data):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index : ")

        if index ==0:
            self.insert_at_begning(data)
            return        
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

    def insert_after_value(self,value,data):
        if self.head is None:
            print("Empty linked list: ")
            return

        itr = self.head

        while itr:
            if itr.data == value:
                itr.next = Node(data,itr.next)
                return
            itr = itr.next
        print("value not found ")
    

    def remove_by_value(self,value):
        if self.head is None:
            # print("No vlaue in the list :")
            return
        itr = self.head
        if itr.data == value:
            itr = self.head.next
            print(f" head deleted {value}")
            return

        if self.head.data == None:
            self.head = self.head.next
            print("Only one value was present in the list")
            return
        

        prev = self.head
        cur = self.head.next
        while cur:
            if cur.data == value :
                prev.next = cur.next
                print(f"Removed node with value {value}")
                return
            prev = cur
            cur = cur.next
        print(f"value not found in the list {value} ")    




if __name__ =='__main__':
    ll = Linke_list() 
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    # ll.insert_values(["apple","cherry","grapes","coconut"])
    # ll.print()
    # print("the length of ll is :", ll.get_length())
    # # ll.remove_at(1)
    # ll.insert_at(0,"fizz")
    # ll.print()
    # ll.insert_at(2,"banana")
    # ll.print()
    # ll.remove_at(2)
    # ll.print()

