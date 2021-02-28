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
        
    def after_node(self, value, num):
        curr = self.head 
        while curr is not None:
            if num == curr.value:
                break 
            curr = curr.next 
        if curr is None:
            print("cannot find this node")
        else:
            new_node = Node(value)
            new_node.next = curr.next 
            curr.next = new_node


ll = LinkedList()
ll.add(5)
ll.add(7)
ll.add(9)
ll.add(10)
# add value 8 after value 9
ll.after_node(8, 9)

ll.print_list()