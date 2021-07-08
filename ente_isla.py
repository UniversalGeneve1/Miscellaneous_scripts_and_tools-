def ei_cipher(phrase):
  alphabet = list("abcdefghijklmnopqrstuvwxyz")
  forward_dict = dict(zip(alphabet, list(range(26)))) 
  
  ente_isla = list("azyxewvtisrlpnomqkjhugfdcb")
  reverse_dict = dict(zip(list(range(26)), ente_isla))
  
  phrase = list(phrase.lower())
  for i in range(len(phrase)):
    if phrase[i].isalpha() == False:
      continue
    else:
      phrase[i] = reverse_dict[forward_dict[phrase[i]]]
    
  phrase = "".join(phrase)
  return phrase

