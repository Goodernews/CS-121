class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, value):
        if self.first == None:
          self.first = Node(value)
          self.last = Node(value)
        elif self.first.next==None:
          self.last = Node(value)
          self.first.next = self.last
        else:
          self.last.next = Node(value)
          self.last= self.last.next


    def head(self):
        #Your code should replace 'pass'
        if self.first==None:
          return None
        return self.first.value

    def dequeue(self):
        #Your code should replace 'pass'
        if self.first==None:
          return None
        return_val = self.first.value
        if self.first.next ==None:
          self.first=None
          self.last = None
          return return_val
        else:
          self.first = self.first.next
          return return_val
