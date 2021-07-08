"""
caesar cipher generator
given a key, create a cipher function
pass a phrase on the returned function to receive key-encrypted phrase
"""

def cipher(key):
  alphabet = list("abcdefghijklmnopqrstuvwxyz")
  #generate index dictionary
  forward_dict = dict(zip(alphabet, list(range(26))))

  #clean key — no spaces, no duplicates, all alphabet, but keep order
  tmp = []
  for c in list(key.lower()):
    if c not in tmp and c.isalpha():
      tmp.append(c)
  key = tmp

  #generate the cyphered alphabet:
  cypherbet = key + [c for c in alphabet if c not in key]
  #generate encoding reverse dictionary
  reverse_dict = dict(zip(list(range(26)),cypherbet))

  #debugging:
  #print("".join(alphabet))
  #print("".join(cypherbet))

  def cipher_tool(phrase):
    phrase = list(phrase.lower())
    for i in range(len(phrase)):
      if phrase[i].isalpha() == False:
        continue
      else:
        phrase[i] = reverse_dict[forward_dict[phrase[i]]]
      
    phrase = "".join(phrase)
    #debugging:
    #print(phrase)
    return phrase

  return cipher_tool


cyphtool = cipher("")
print(cyphtool("")) 