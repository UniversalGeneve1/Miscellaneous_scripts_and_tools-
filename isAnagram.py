#anagram checker

def isAnagram(s1, s2):
  if len(s1) != len(s2):
    print(False)
  else:
    s1_dict = {}
    s2_dict = {}
    ones = [1 for i in range(0,len(s1)) if True]

    for i in range(0, len(s1)):
      if s1[i] in s1_dict:
        s1_dict[s1[i]] += 1
      else:
        s1_dict[s1[i]] = 1 
      if s2[i] in s2_dict:
        s2_dict[s2[i]] += 1
      else:
        s2_dict[s2[i]] = 1
    if s1_dict == s2_dict:
      print(True)
    else:
      print(False) 