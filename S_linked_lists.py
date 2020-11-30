##linked lists
#node functionality: this is the basis of
#all ll nodes

class Node:
  def __init__(self, val):
    self.val = val
    self.nextval = None

#singly linked list:
class SLinkedList:
  def __init__(self):
    self.headval = None
    self.tailval = None
    self.length = 0
  
  #push
  def push(self, val):
    push_node = Node(val)
    if self.headval == None: #empty list
      self.headval = push_node
      self.tailval = push_node
    else:
      self.tailval.nextval = push_node
      self.tailval = push_node
    self.length +=1
    return True
  
  #pop
  def pop(self):
    if self.headval == None:
      print("No values to return")
      return False
    elif self.length == 1:
      pop_node = self.headval
      self.headval = None
      self.tailval = None
      return pop_node
    else:
      pop_node = self.headval #we want this at the end 
      new_tail = self.headval #end-1
      while pop_node.nextval:
        new_tail = pop_node
        pop_node = pop_node.nextval
      self.tailval = new_tail
      self.length -= 1
      return pop_node

  def reverse(self):
    curr_node = self.headval
    next_node = None
    prev_node = None

    while curr_node.nextval:
      next_node = curr_node.nextval
      curr_node.nextval = prev_node
      prev_node = curr_node
      curr_node = next_node

    self.headval, self.tailval = self.tailval, self.headval


      


  



  

