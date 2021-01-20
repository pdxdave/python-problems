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
