#!/usr/local/bin/python3

class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()
        
    # other helper functions
    def peek(self):
        return self.items[self.size()-1]
        
    def size(self):
        return len(self.items)
        
    def isEmpty(self):
        return self.items == []
        
    def __str__(self):
        return ','.join(self.items)
        
s = Stack()
s.push('a')
s.push('b')
print(s)