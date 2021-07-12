'''
Deep crypt quadruple encryption:
phrase -> ente isla -> tr-polyviginere -> morse -> charblurring
'''
import re

def cleaner(s):
    return re.sub(r'[^A-Za-z0-9]+', '', s)

#pieces needed:
alphabet = list("abcdefghijklmnopqrstuvwxyz")
alpha_dict = dict(zip(alphabet, list(range(26)))) 

ente_isla = list("azyxewvtisrlpnomqkjhugfdcb")
ei_dict = dict(zip(list(range(26)), ente_isla))

def tabula_recta(c, r):
  '''
  row = phrase char, col = key char, return character 
  '''
  comp = int(alpha_dict[c]) + int(alpha_dict[r])
  if comp >= 26:
    return alphabet[comp - 26]
  return alphabet[comp]

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
                    'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
                    'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
                    '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def DeepCrypt(phrase, key):
    if not phrase or not key:
        print('missing either phrase or key')
        return
    
    phrase = list(cleaner(phrase.lower()))
    key = cleaner(key.lower())

    #ente_isla
    ei_return = ''
    for c in phrase:
      ei_return += ei_dict[alpha_dict[c]]
 
    #tr-polyviginere
    keystr = ''
    while True:
      keystr += key
      if len(keystr) > len(ei_return):
        break

    keystr = keystr[:len(ei_return)]

    pv_return = ''
    for i in range(len(phrase)):
      pv_return += tabula_recta(ei_return[i], keystr[i])

    #morse:
    mo_return = ''
    for c in list(pv_return):
      mo_return += MORSE_CODE_DICT[c.upper()]

    #charblur:
    cb_return = mo_return.replace("-", "l").replace(".", "I")
    return cb_return

if __name__ == "__main__":
  phrase = input("Phrase to Encrypt >>> ")
  key = input("Encrypting key >>> ")
  print(DeepCrypt(phrase, key))