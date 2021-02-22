'''
prev_node -> None
    
        1 -> 2 -> 3 -> 4 -> None
        cn   nn
       head
The original setup
- The current or cn node will be the head of the list.  In this case, 1.
- The prev_node is pointing to None. We'll use it in the while loop
- The next_node or nn will be used in the while loop

First while loop pass
- next_node = current_node.next severs the link between 1 & 2
- So now 1 is pointing to the previous_node, which is none.
- previous_node = current_node sets 1 as the previous_node
- current_node = next_node sets 2 as the current node

prev_node
       \
        1    2 -> 3 -> 4 -> None
             cn   nn
'''
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None

    while current_node is not None:
        # set the next node
        next_node = current_node.next
        #  make current node point to prev node
        current_node.next = previous_node
        # shift current & prev pointers to right
        previous_node = current_node
        current_node = next_node

    return previous_node

def print_list(head_of_list):

    current_node = head_of_list
    return_str = ''

    while current_node:
        return_str += f'({current_node.value})-> '
        current_node = current_node.next

    print(return_str)



head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)

print_list(head)
new_head = reverse(head)
print_list(new_head)