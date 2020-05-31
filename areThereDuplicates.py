def areThereDuplicates(*args):
  args = args
  argValDict = {}
  FL = 0
  EL = len(args)-1
  trigger = 0

  while FL < EL:
    if (args[FL] not in argValDict) and (args[EL] not in argValDict):
      argValDict[args[FL]] = 1
      argValDict[args[EL]] = 1
      FL += 1
      EL -= 1
    else:
      trigger += 1
      print(True)
      break

  if trigger == 0:
    print(False)
    
