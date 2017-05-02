#!/usr/local/bin/python3

class Queue:
    
    def __init__(self):
        self.items = []
        
    def push(self, data):
        self.items.insert(0, data)
        
    def pop(self):
        return self.items.pop()
        
    # other helper functions
    def peek(self):
        return self.items[0]
        
    def size(self):
        return len(self.items)
        
    def isEmpty(self):
        return self.items == []
        
    def __str__(self):
        return ','.join(self.items)
        
q = Queue()
q.push('a')
q.push('b')
print(q)