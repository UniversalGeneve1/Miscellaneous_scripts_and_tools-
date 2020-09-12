#hangman in python
#ADD MORE / REPLACE WORDS INSIDE THE BRACKETS BELOW, SEPARATED BY COMMAS
words = ["apple", "banana", "carrot"]
## IMPORTS:
#import pandas as pd 
import sys
import random
from time import sleep
## HELPER:
def slow_printer(s,t):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(t)
## SETUP:
image_1= """ 
                    ____________
                    |          :
                    |          :
                    |          
                    |         
                    |		   
                    |         
                    |________________________
                   /|                       /|
                  / |                      //
                 /                        //
                /_______________________ //
                |_______________________|/ """
image_2 = """ 
                    ____________
                    |          :
                    |          :
                    |          @
                    |         
                    |		   
                    |         
                    |________________________
                   /|                       /|
                  / |                      //
                 /                        //
                /_______________________ //
                |_______________________|/"""
image_3 = """ 
                    ____________
                    |          :
                    |          :
                    |          @
                    |          |
                    |		   
                    |         
                    |________________________
                   /|                       /|
                  / |                      //
                 /                        //
                /_______________________ //
                |_______________________|/"""
image_4 = """ 
                    ____________
                    |          :
                    |          :
                    |          @
                    |         /|
                    |		   
                    |         
                    |________________________
                   /|                       /|
                  / |                      //
                 /                        //
                /_______________________ //
                |_______________________|/"""
image_5 = """ 
                    ____________
                    |          :
                    |          :
                    |          @
                    |         /|\\
                    |		   
                    |         
                    |________________________
                   /|                       /|
                  / |                      //
                 /                        //
                /_______________________ //
                |_______________________|/"""
image_6 = """ 
                    ____________
                    |          :
                    |          :
                    |          @
                    |         /|\\
                    |          |
                    |         
                    |________________________
                   /|                       /|
                  / |                      //
                 /                        //
                /_______________________ //
                |_______________________|/"""
image_7 = """ 
                    ____________
                    |          :
                    |          :
                    |          @
                    |         /|\\
                    |          |
                    |         /
                    |________________________
                   /|                       /|
                  / |                      //
                 /                        //
                /_______________________ //
                |_______________________|/"""
image_final = """ 
                    ____________
                    |          :
                    |          :
                    |          @
                    |         /|\\
                    |          |
                    |         / \\
                    |________________________
                   /|                       /|
                  / |                      //
                 /                        //
                /_______________________ //
                |_______________________|/"""
image_generator = iter([image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_final])
#words = [word.lower() for word in pd.read_csv(words, header = None, encoding = 'utf-8')[0].tolist()]
words = [word.lower() for word in words]
##########
## MAIN ##
##########
word = random.choice(words)
curr_game_word = list(word)
curr_img_state = image_generator.__next__()
letterboard = "_ " * len(curr_game_word)
prev_guesses = []

slow_printer("W E L C O M E   T O\n", 0.05)
slow_printer("   H A N G M A N   \n", 0.05)
sleep(1)

print(curr_img_state)
print(letterboard)

while True:
	guess = str(input("What's your guess? ")).lower()
	if len(guess) != 1 or not guess.isalpha():
		print("please enter a single letter, try again!")
		continue

	print("previous guesses: ", prev_guesses)
	if guess not in prev_guesses:
		prev_guesses.append(guess)
	else:
		print("You guessed that letter before, try again")
		continue

	if guess in curr_game_word:
		intermed_index = []
		for idx, let in enumerate(curr_game_word):
			if let == guess:
				intermed_index.append(idx)

		letterboard = list(letterboard)
		for swap_idx in intermed_index:
			letterboard[swap_idx*2] = guess

		letterboard = "".join(letterboard)

		if "_" in letterboard:
			print(curr_img_state)
			print("Good guess!")
			sleep(0.2)
			print(letterboard)
			continue
		else:
			print()
			slow_printer("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n", 0.03)
			slow_printer("*C O N G R A T U L A T I O N S*\n", 0.03)
			slow_printer("*-------Y O U---W I N!--------*\n", 0.03)
			slow_printer("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n", 0.03)
			break
	else:
		curr_img_state = image_generator.__next__()
		if curr_img_state == image_final:
			print(image_final)
			print()
			print("It seems that your luck has run dry...\n")
			sleep(0.5)
			print(f"The correct answer was: {word.upper()}\n")
			sleep(1.2)
			slow_printer("(X.X) (X.X) (X.X) (X.X) (X.X)\n", 0.03)
			slow_printer("(X.X) G A M E   O V E R (X.X)\n", 0.03)
			slow_printer("(X.X) (X.X) (X.X) (X.X) (X.X)\n", 0.03)
			break
		else:
			print("not quite! try again")
			print(curr_img_state)
			print(letterboard)
			continue
