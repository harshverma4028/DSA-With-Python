         ## Hw problem doubley linked list

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node


    def print_forward(self):
        if self.head == None:
            print("the doubly linked list is empty ")
            return
        
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '--->'
            itr = itr.next
        print(listr[:-4])  # Remove the last arrow

    def print_backward(self):
        if self.head == None:
            print("the DLL is empty : ")
            return
        last_nod = self.get_last_nod()
        itr = last_nod
        
        listr = ''
        while itr:
            listr += str(itr.data) + '--->'
            itr = itr.prev
        print("the linked list in reverse: " + listr[:-4])  # Remove the last arrow



    def get_last_nod(self):
        itr = self.head
        while itr and itr.next:
            itr = itr.next
        return itr

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None,itr)    

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data , itr.next , itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count +=1


    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



if __name__  =='__main__' :
    ll = DoubleyLinkedList()  
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()