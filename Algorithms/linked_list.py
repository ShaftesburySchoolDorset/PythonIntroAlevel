#!/usr/local/bin/python3

class Node(object):
    
    def __init__(self, cargo, next=None):
        self.cargo = cargo
        self.next = next
        
    def __str__(self):
        return str(self.cargo)
        
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        
    def add(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
        else:
            n.next = self.head
            self.head = n
    
    def sort(self):
        pass 
      
    def remove(self, p):
        pass
        
    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.cargo
                p = p.next
            s += p.cargo
        return s
        
# Example code:

l = LinkedList()
l.add('A')
l.add('P')
l.add('Z')

print(l)