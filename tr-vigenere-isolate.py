import re

alphabet = list("abcdefghijklmnopqrstuvwxyz")
alpha_dict = dict(zip(alphabet, list(range(26)))) 

def cleaner(s):
    return re.sub(r'[^A-Za-z0-9]+', '', s)

def tabula_recta(c, r):
    '''col = key char, row = phrase char, return character '''
    return alphabet[(int(alpha_dict[c]) + int(alpha_dict[r])) % 26]

def vigenere(phrase, key):
    
    phrase = cleaner(phrase).lower()
    key = cleaner(key).lower()
    keystr = ''

    while True:
        keystr += key
        if len(keystr) > len(phrase):
            break

    keystr = keystr[:len(phrase)]
    ciphered = ''

    for i in range(len(phrase)):
        ciphered += tabula_recta(keystr[i], phrase[i])

    return ciphered

if __name__ == "__main__":
    phrase = input("Enter phrase >>> ")
    key = input("Enter cipher key >>> ")
    ciphered = vigenere(phrase, key)
    print(ciphered, len(ciphered))

