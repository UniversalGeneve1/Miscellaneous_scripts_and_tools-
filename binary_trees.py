class Node():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self, val=None):
    self.root = val

  def insert(self, insert_val):
    if self.root == None:
      self.root = Node(insert_val)
      return self

    curr_node = self.root
    while True:
      if insert_val == curr_node.val:
        print("node is already in the tree")
        return self

      if insert_val > curr_node.val:
        if curr_node.right == None:
          curr_node.right = Node(insert_val)
          return self
        curr_node = curr_node.right

      if insert_val < curr_node.val:
        if curr_node.left == None:
          curr_node.left = Node(insert_val)
          return self
        curr_node = curr_node.left 

  def search(self, search_val):
    if self.root == None:
      print("Empty tree, no values to return")
      return False

    curr_node = self.root
    while True:
      if search_val == curr_node.val:
        return True
      
      if search_val > curr_node.val:
        if not curr_node.right:
          return False
        curr_node = curr_node.right

      if search_val < curr_node.val:
        if not curr_node.left:
          return False
        curr_node = curr_node.left

  def BFS(self):
    queue = []
    req= []
    node = self.root
    queue.append(node)
    while len(queue) != 0:
      node = queue.pop(0) #shift
      req.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    return req
  def DFSPre(self):
    req = []

    def traverse(node):
      req.append(node.val)
      if node.left:
        traverse(node.left)
      if node.right:
        traverse(node.right)

    traverse(self.root)
    return req
#-------------------------------
  def DFSIn(self):
  req = []

    def traverse(node):
      if node.left:
        traverse(node.left)
      req.append(node.val)
      if node.right:
        traverse(node.right)

    traverse(self.root)
    return req
#-------------------------------
  def DFSPost(self): 
    req = []

    def traverse(node):
      if node.left:
        traverse(node.left)
      if node.right:
        traverse(node.right)
      req.append(node.val)

    traverse(self.root)
    return req

bt = BinaryTree()
bt.insert(5)
print(bt.root.val)
bt.insert(3)
bt.insert(7)
insvals = [1, 2, 4, 6, 8]
for i in insvals:
  bt.insert(i)

print(bt.BFS())