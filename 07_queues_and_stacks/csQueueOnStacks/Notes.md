Two operations:     
Enqueue (put something in line) - enqueue always goes in at the end of the line    
Dequeue (take something out of line) - always takes from the front of the line    

```
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, n):
        self.queue.append(n) # puts n at the end of the queue
                             # time complexity 0(1)

    def dequeue(self):
        self.queue.pop(0)  # grab the item of the front
                           # time complexity 0(n)

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())

q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
```

# Linked List
```
class ListNode:
    def __init__(self, value)
    self.value = value
    self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, n): # 0(1)
        # special case: enqueu on an empty queue
        if self.head is None:
            self.head = n
            self.tail = n
            return
        
        # general case
        self.tail.next = n
        self.tail = n

    def dequeue(self): # 0(1)

        # special case: dequeue the last item
        if self.head == self.tail:
            prev_head = self.head
            self.head = self.tail = None
            return prev_head


        # general case
        prev_head = self.head # keeps track of the head so we can return it
        self.head = self.head.next
        prev_head.next = None # disconnects it from list

        return prev_head # returns head that we popped off the front


q = Queue()

q.enqueue(ListNode(1)) # a new node
q.enqueue(ListNode(2))
q.enqueue(ListNode(3))

print(q.dequeue())

q.enqueue(ListNode(4))
q.enqueue(ListNode(5))

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
```
# Stacks

Push: add an item to the top of the stack    
Pop: remove an item from the top of the stack    

The last item you push is the first item you pop

```
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    <!-- def __repr__(self):
        return f"ListNode({repr(self.value)}) -->



class Stack:
    def __init__(self):
        self.head = None

    def push(self, n): # 0(1)
        n.next = self.head
        self.head = n

    def pop(self): # 0(1)
        if self.head is None:
            return None
        
        prev_head = self.head
        self.head = self.head.next
        prev_head.next = None

        return prev_head


s = Stack()

s.push(ListNode(1))
s.push(ListNode(2))
s.push(ListNode(3))
s.push(ListNode(4))

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
```