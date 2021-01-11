class Node:
  def __init__(self, data = None):
   dataval = data
   nextval = None
   
# 1). Node class for linked list
class LinkedList:
  def __init__(self):
    head = None
   
# 2). Node class for Doubly linked list
class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None 
    
# 3). Node class for Circular linked list 
class CircularLinkedList:
  def __init__(self):
        self.head = None
  def push(self, data):
        ptr1 = Node(data)
        temp = self.head
        ptr1.nextval = self.head
        
# 4). Create class for stack
class Stack: 
    def __init__(self): 
        self.head = None
      
    # Checks if stack is empty 
    def isempty(self): 
        if self.head == None: 
            return True
        else: 
            return False
            
# 5). Create class for Queues
class Queue: 
    # Function to initialize head  
    def __init__(self): 
        self.head = None
        self.last = None
    # Function to add an element data in the Queue 
    def enqueue(self, data): 
        if self.last is None: 
            self.head =Node(data) 
            self.last =self.head 
        else: 
            self.last.next = Node(data) 
            self.last.next.prev=self.last 
            self.last = self.last.next
 
# 6). Create class for De-Queue
    def dequeue(self): 
   
        if self.head is None: 
            return None
        else: 
            temp= self.head.data 
            self.head = self.head.nextval
            self.head.prev = None
            return temp 
