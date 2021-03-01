class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Linked:
    def __init__(self):
        self.start = None

    def display(self):
        #Prints the list.
        print("[", end="")
        if self.start:
            print(self.start.value, end="")
            current = self.start.next
            while current:
                print(", ", end="")
                print(current.value, end="")
                current = current.next
        print("]")
    def sum(self):
      i = self.start
      if i==None:
        return 0
      sum_link = 0
      while i.next!=None:
        sum_link += i.value
        i = i.next
      return sum_link+i.value
    def count(self, search_for):
      i = self.start
      if i==None:
        return 0
      count_link = 0
      while i.next!=None:
        if i.value==search_for:
          count_link += 1
        i = i.next
      if i.value==search_for:
          count_link += 1
      return count_link

    def getValue(self, index):
        #Returns the value at the given index (or None if too high).
        curr = self.start
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.value

    def append(self, value):
        #Adds a node with the given value to the end of the list.
        if self.start == None:
            self.start = Node(value)
        else:
            current = self.start
            while current.next != None:
                current = current.next
            current.next = Node(value)

    def isEmpty(self):
        #Returns True if the list is empty, False otherwise.
        return (self.start == None)

    def length(self):
        #Returns the length of the list.
        if self.start == None:
            return 0
        else:
            curr = self.start
            count = 1
            while curr.next != None:
                curr = curr.next
                count += 1
            return count

    def insert(self, index, value):
        #Inserts a node with the given value at the given index.
        if index == 0:
            self.start = Node(value, self.start)
        else:
            curr = self.start
            count = 1
            while count < index:
                curr = curr.next
                count += 1
            curr.next = Node(value, curr.next)

    def delete(self, index):
        #Deletes the node at the given index.
        if index == 0:
            self.start = self.start.next
        else:
            prev = self.start
            curr = self.start.next
            count = 1
            while count < index:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = curr.next