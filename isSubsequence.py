def isSubsequence(s1, s2):
  indexContainer = []
  trigger = 0

  for char in s1:
    if s2.find(char) == -1:
      trigger += 1
      print(False)
      break
    else:
      indexContainer.append(s2.find(char))


  if trigger == 0:
    for i in range(1,len(indexContainer)):
      if indexContainer[i-1] > indexContainer[i]:
        trigger += 1
        print(False)
        break


  if trigger == 0:
    print(True)
