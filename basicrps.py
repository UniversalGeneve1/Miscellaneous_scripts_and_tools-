valid = ['rock', 'paper', 'scissors']
switch = True
wins = [['rock', 'scissors'], ['paper', 'rock'], ['scissors', 'paper']]
loses = [['rock', 'paper'], ['paper', 'scissors'], ['scissors', 'rock']]

while switch == True:
  p1 = None
  p2 = None

  while p1 == None:
    p1 = input("rock, paper or scissors?: ")
    p1.lower()
    if p1 not in valid:
      p1 = None
      print("invalid choice. rock, paper or scissors?: ")

  while p2 == None:
    p2 = input("rock, paper or scissors?: ")
    p2.lower()
    if p2 not in valid:
      p2 = None
      print("invalid choice. rock, paper or scissors?: ")

  check = [p1, p2]
  if check in wins:
    print(p1 + ' beats ' + p2 + '. p1 wins!')
    choice = input('go again? y/n: ')
    choice.lower()

  elif check in loses:
    print(p2 + ' beats ' + p1 + '. p2 wins!')
    choice = input('go again? y/n: ')
    choice.lower()

  else:
    print("It's a tie! Go again!")

  if choice == 'n':
        switch = False 