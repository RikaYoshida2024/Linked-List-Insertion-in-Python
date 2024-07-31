class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
if __name__ == "__main__":
    l1=LinkedList()
    l1.insert_at_end(1)
    l1.insert_at_end(2)
    l1.insert_at_end(3)
    l1.insert_at_end(4)
    l1.print_list()


