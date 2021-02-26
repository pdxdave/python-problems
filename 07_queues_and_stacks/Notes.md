### Stacks
Last-In First-Out (LIFO)    
Think of a stack of plates.  The last plate on the stack    
is typicall the first plate out to be used.    
- push(val) to pot a value on top of the stack    
- pop() to return the top value

### How to implement a stack using a list
- push(value) appends to the end of the list
- pop() remove and returns from the end of the list    
``` [a, b, c] ``` add d ```[a, b, c, d]```
#### Example
```
class Stack:
    def __init__(self):
        self.myList = []

    def push(self, val)
        self.myList.append(val)

    def pop(self):
        return self.myList.pop()

myStack = Stack()
myStack.push(1)
myStack.push(2)
print(myStack.pop())
```


