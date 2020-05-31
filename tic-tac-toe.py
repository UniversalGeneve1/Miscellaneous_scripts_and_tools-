#tic-tac-toe:

#step 1: make the square board given a length:

def board_maker(n):
  for i in range(n):
    print(" ---"*(n))
    print("|   "*n + "|")
  print(" ---"*(n))

#step 2:  