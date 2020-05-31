def averagePair(numlist, targavg):
  FP = 0
  EP = len(numlist)-1
  trigger = 0


  while FP < EP:
    pairavg = (numlist[FP] + numlist[EP])/2

    if pairavg > targavg:
      EP -= 1
    elif pairavg < targavg:
      FP += 1
    else:
      trigger += 1
      print(True)
      break
  if trigger == 0:
    print(False)