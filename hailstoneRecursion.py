def hailstone(n):
  if n <=0:
    print("Input must be a positive integer!")
    return
  else:
    if n == 1:
      print(1)
      return
    else:
      print(int(n))
      if n % 2 == 0:
        n = n/2
      elif n % 2 != 0:
        n = 3*n + 1
      hailstone(n)

