import re

def cleaner(s):
    return re.sub(r'[^A-Za-z0-9]+', '', s)

def ei_cipher(phrase):
  alphabet = list("abcdefghijklmnopqrstuvwxyz")
  forward_dict = dict(zip(alphabet, list(range(26)))) 
  
  ente_isla = list("azyxewvtisrlpnomqkjhugfdcb")
  reverse_dict = dict(zip(list(range(26)), ente_isla))
  
  phrase = list(cleaner(phrase.lower()))
  for i in range(len(phrase)):
    phrase[i] = reverse_dict[forward_dict[phrase[i]]]
    
  phrase = "".join(phrase)
  return phrase

if __name__ == "__main__":
  phrase = input("Enter phrase to translate: >>> ")
  coded = ei_cipher(phrase)
  print(coded, len(coded))