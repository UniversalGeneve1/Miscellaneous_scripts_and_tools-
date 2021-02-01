"""
A BASIC TRIE IMPLEMENTATION.
"""

class Trie_Node:
  def __init__(self, char):
    self.char = char
    self.isEndWord = False
    self.children = {}

class Trie:
  def __init__(self):
    self.root = Trie_Node("*")

  def add_word(self, word):
    curr_node = self.root
    for char in word:
      if char in curr_node.children:
         curr_node = curr_node.children[char]
         continue
      else:
        curr_node.children[char] = Trie_Node(char)
        curr_node = curr_node.children[char]
        continue
    curr_node.children['*'] = '*'
    curr_node.isEndWord = True

  def does_word_exist(self, word):
    #edge case:
    if word == "":
      return True
    curr_node = self.root
    for char in word:
      if char in curr_node.children:
         curr_node = curr_node.children[char]
         continue
      else:
        return False
    return curr_node.isEndWord

test_trie = Trie()
test_trie.add_word("wait")
#print(test_trie.root.children['w'].children['a'].children['i'].children['t'].children)
print(test_trie.does_word_exist('waits'))
