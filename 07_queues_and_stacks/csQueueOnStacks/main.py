'''
You are given an array of requests, where requests[i] can be "push <x>" or "pop". Return an array composed of the results of each "pop" operation that is performed.

Example

For requests = ["push 1", "push 2", "pop", "push 3", "pop"], the output should be
queueOnStacks(requests) = [1, 2].

After the first request, the queue is {1}; after the second it is {1, 2}. Then we do the third request, "pop", and add the first element of the queue 1 to the answer array. The queue becomes {2}. After the fourth request, the queue is {2, 3}. Then we perform "pop" again and add 2 to the answer array, and the queue becomes {3}.
'''
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    # 1st solution
    def insert(x):
        # insert code here
        left.push(x)

    def remove():
        # insert code here
        if len(right.items) == 0:
            while len(left.items) > 0:
                right.push(left.pop())
            if len(right.items) == 0:
                return None 
        return right.pop()

    # second solution
    def insert(x):
        left.push(x)

    def remove():
        # isEmpty refers to class Stack
        while not left.isEmpty():
            popped = left.pop() 
            right.push(popped)
        ls = right.pop() 
        
        while not right.isEmpty():
            popped = right.pop() 
            left.push(popped)
        return ls

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans