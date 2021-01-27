'''
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since this is what you will be asked to accomplish in an interview.

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [1, 3, 4, 6] and value = 5, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];
For l = [1, 3, 4, 6] and value = 10, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];
For l = [1, 3, 4, 6] and value = 0, the output should be
insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].

'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    
    x = ListNode(value)
    currentNode = l
    
    
    if l is None:
        return x
        
        
    if value < l.value:
        x.next = l
        return x
        
    next_node = currentNode.next   
    
    if next_node == None:
        l.next = x
        return l

    while currentNode.value <= value and next_node.value <= value:
        
        currentNode = currentNode.next 
        next_node = next_node.next
        
        if next_node is None:
            
            currentNode.next = x
            return l
    currentNode.next = x
    x.next = next_node
    return l

    # Or Kim's solution 

    def insertValueIntoSortedLinkedList(l, value):
    # printing to see what I'm working with
    print(value, l)
    # create a new_node with the value
    new_node = ListNode(value)
    # if there is no list return ListNode
    if l == None: 
        return ListNode(value)
    previous_node = None 
    next_node = l
    # looping through where we want to insert the new node
    while next_node is not None and value > next_node.value: 
        previous_node = next_node
        # this will point to the next node in the linked list
        next_node = next_node.next 
        
    # setting the new node.next to the next node
    new_node.next = next_node 
    # set the previous_node.next to the new_node 
    if previous_node is not None: 
        previous_node.next = new_node
    else: 
        l = new_node
    return l
        
 
