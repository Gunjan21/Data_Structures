# define class Node
class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self, data):
    self.data = data

  def setNext(self, next):
    self.next = next

# define class Linked List (we consider it unordered list.i.e. not sorted)
# The code is partial
class LinkedList:
  def __init__(self):
    self.head = None


  def add_at_begin(self, data):
    n = Node(data)
    n.setNext(self.head)
    self.head = n

  def add_at_end(self, data):
    #Create the new node
    n = Node(data)

    #situate a pointer 'curr' at the last node
    curr = self.head
    while (curr != None) and (curr.getNext() != None):
      curr = curr.getNext()

    #either curr is None or at the end. None if the list is empty
    if (curr == None):
      self.head = n #so we make the new node the head
    else:
      curr.setNext(n)

  def print(self):
    curr = self.head
    print("List is :", end = " ")
    while (curr != None):
      print(curr.getData(), end = " -> ") 
      curr = curr.getNext()
    print("None")

  def is_empty(self):
    return (self.head == None)

  def pop_from_begin(self):
    curr = self.head
    if (curr != None):
      self.head = self.head.getNext()
      return curr.getData()
    raise RuntimeError("Popping from an empty list")

  # Remove an element at position index (index starts at 0)
  def pop(self, index):
    n = self.head
    prev = None
    count = 0
    while (count != index) :
      prev = n
      n = n.getNext()
      count += 1
  
    if (n != None):
      prev.setNext(n.next)
      n.setData(None)
    else:
      self.head = None
      
    return n.getData()

         
  # Remove the last element
  def pop_from_end(self):
    curr = self.head
    prev = None

    if (curr == None):
      raise RuntimeError("pop_from_end : pop attempted from Empty list")

    # Move current to last element
    while (curr.getNext() != None):
      prev = curr
      curr = curr.getNext()

    if (prev != None):
      prev.setNext(None)
    else:
      self.head = None 
    return curr.getData()

  def get_length(self):
    length = 0
    curr = self.head
    while (curr != None):
      curr = curr.getNext()
      length = length + 1
    return length
  
  def search(self, data):
     found = False
     curr = self.head
     while (curr != None):
       if (curr.getData() == data):
         found = True
         break
       curr = curr.getNext()
     return found
         
  def remove_elem(self, data):
    curr = self.head
    prev = None
    found = False
    while not found:
      if curr.getData() == data:
        found = True
      else:
        prev = curr
        curr = curr.getNext()
    if prev == None:
      self.head = curr.getNext()
    else:
      prev.setNext(curr.getNext())
    
  def insert_at(self, index, data):
    n = Node(data)
    curr = self.head
    count = 0
    while (count != (index)):
      curr = curr.getNext()
      count = count + 1

    if (n != None):
      n.setNext(curr.getNext())
      curr.setNext(n)


l = LinkedList()
l.add_at_begin(4)
l.add_at_end(5)
l.add_at_begin(6)
l.print()

