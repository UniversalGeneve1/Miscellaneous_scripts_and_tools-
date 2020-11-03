#tiny script i use to test boolean logic functions

def tester(f):
  a = True
  b = True
  print('running as a-t b-t')
  print("the result is: ", f(a, b))

  a = False
  b = False
  print('running as a-f b-f')
  print("the result is: ", f(a, b))

  a = True
  b = False
  print('running as a-t b-f')
  print("the result is: ", f(a, b))

  a = False
  b = True
  print('running as af b-t')
  print("the result is: ", f(a, b))


#example functions for testing: 

def de_morgans1(a, b):
  return (not(a and b)) == (not(a) or not(b))

def de_morgans2(a, b):
  return (not(a or b)) == (not(a) and not(b))

