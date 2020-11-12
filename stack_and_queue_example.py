#make a stack object:
class Stack:
  def __init__(self):
    self.stack = []
  
  def current_state(self):
    print(self.stack)

  def stack_push(self, val):
    self.stack.append(val)

  def stack_pop(self):
    val = self.stack[-1]
    self.stack.pop()
    return val

#test stack:
"""
stacc = Stack()
stacc.current_state()
stacc.stack_push(1)
stacc.current_state()
val = stacc.stack_pop()
print(val)
"""
#make a queue:
class Queue:
  def __init__(self):
    self.queue = []
  
  def current_state(self):
    print(self.queue)

  def enqueue(self, val):
    self.queue.append(val)

  def dequeue(self):
    val = self.queue[0]
    self.queue.pop(0)
    return val

"""
#test queue:
q = Queue()

for i in range(4):
  q.enqueue(i)
  q.current_state()

for _ in range(4):
  q.dequeue()
  q.current_state()
"""


