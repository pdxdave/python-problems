'''
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    
    newList = ListNode(0)
    cur = newList 
    while l1 and l2:
        if l1.value < l2.value:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        else:
            cur.next = l2
            l2 = l2.next
            cur = cur.next # this updates the cur.next. it will for either list we're working with
        
    # if there's a remaining portion of a list, this will insert it into the end. Either will work
    
    cur.next = l1 or l2 
    
    if l1:
        cur.next = l1
    elif l2:
        cur.next = l2
    return newList.next
        
    '''
    l1 = [1,2,4]
    l2 = [1,3,4]
    
    Create a new list starting at 0.  Even though l1 and l2 start with 1, we'll still consider l1 to be less than l2.
    The first loop compares l1 to l2 ( 1 to 1 ). We'll say l1 is less, so l1 will become the current next. [0 , 1], then
    the l1 pointer moves to the right which is l1.next.
    The second loop, we compare l1.value of 2, to l2.value of 1.  The l2.value is less. Now l2 is the cur.next [0, 1, 1],
    then the l2 pointer moves to the right and becomes l2.next
    '''