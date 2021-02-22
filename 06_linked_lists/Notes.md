### Core operations
- access 0(n)
- search 0(n)
- insert 0(1)
- delete 0(1)

```
   head      node       node      tail
     0  ref->  1  ref->  2   ref->  3  ref-> None
```

#### Example 1
```
Given only a ref to a specific node in a linked list, delete that node from
a singly-linked list.

We are passing 'y' to the del func(), so the pointer is on 'y'.  Knowing that    
we can set the current_node.value = curuent_node.next.value.  This essentially    
removes 'y' from the picture and makes it 'z'.  
Then set current_node.next = current_node.next.next.  This is basically pointing
to what the original 'z' was pointing to.
```

```
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_node(delete_this_node):
    #  The next value to y is z.  So it's saying z = y.next
    next_node = delete_this_node.next
    if next_node is not None:
        # y.value = z.value.  it's a copy. so it's really z.value = z.value
        delete_this_node.value = next_node.value
        # now z is pointing to the next node after the original z.  basically removes y.
        delete_this_node.next = next_node.next
    else:
        print('this method doesn't work')


# the individual nodes
x = LinkedListNode('x')
y = LinkedListNode('y')
z = LinkedListNode('z')

# this code links the nodes
x.next = y
y.next = z

delete_node(y)

```

#### Example 2

```
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head_of_list):
    current_node = head_of_list
    prev_node = None
    next_node = None

    while current_node:
        # set the next node
        next_node = current_node.next
        #  make current node point to prev node
        current_node.next = prev_node
        # shift current & prev pointers to right
        prev_node = current_node
        current_node = next_node

    return prev_node

def print_list(head_of_list):
    current_node = head_of_list
    return_str = ""

    while current_node:
        return_str += f'({current_node.value})->'
        current_node = current_node.next

    print(return_str)



head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)

print_list(head)
new_head = reverse(head)
print(new_head)
```