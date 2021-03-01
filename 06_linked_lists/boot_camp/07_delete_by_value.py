class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 

    def print_list(self):
        if self.head is None:
            print("There is no list")
        
        else:
            curr = self.head
            while curr is not None:
                print(curr.value)
                curr = curr.next

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            curr = self.head 
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)

    def delete_value(self, v):
        if self.head is None:
            print("There is nothing in the list to delete")
            return
        
        if v == self.head.value:
            self.head = self.head.next 
            return 

        curr = self.head 
        while curr.next is not None:
            if v == curr.next.value:
                break
            curr = curr.next 
        if curr.next is None:
            print("No node by that value")
        else:
            curr.next = curr.next.next


ll = LinkedList()
ll.add(5)
ll.add(7)
ll.add(9)
ll.add(10)
ll.print_list()
print("----")
ll.delete_value(9)
ll.print_list()