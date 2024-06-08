import ipdb

class Stack:

 def __init__(self, items = [], limit = 100):
   self.items = items[0:limit]
   self.limit = limit

def isEmpty(self):
           return self.size() == 0

def push(self, item):
              self.items.insert(0, item)

def pop(self):
    return self.items.pop(0) 

def peek(self):
               return self.items[len(self.items)]
    
def size(self):
      return len(self.items)  

def full(self):
          return self.size() >= self.limit

def search(self, target):
          for idx, value in enumerate(self.items):
            if target == value:
                return idx

          return -1