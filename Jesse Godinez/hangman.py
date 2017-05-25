import random #brings in the random and time modules
import time
HANGMAN_PICS = ['''     
			
			
			|
		________|__''',
		'''
		        |
			|
			|
			|
			|
		________|__''',
		'''
		  ________
			|
			|
			|
			|
			|
		________|__''',
		'''
		  ________
	            |	|
	            	|
			|
			|
			|
		________|__''',
		'''
		  ________
	            |	|
	            O	|
			|
			|
			|
		________|__''',
		'''
		  ________
		    |	|
		    O	|
		   /|\	|
			|
			|
		________|__''',
		'''
		  _________
		    |	|
		    O	|
		   /|\  |
		   / \  |
			|
		________|___'''] #creates the graphics for the game
word_list=["apple","cat","ball","dog","elephant","fish","girl","hat","ink","jug","king","lion","man" ,"net","owl","pink","queen","rat","sun", "tits", "umbrella", "van", "wood", "xmas", "yummy" , "zebra"] #creates a list of available words

def clear_board(): #clears the board 
	for i in range(50):
		print ("\n")

def get_random_word(words): #generates a random word from the word list
	secret_word = word_list[random.randint(0, len(word_list)-1)]
	return (secret_word)

def display_board(HANGMAN_PICS,missed_letter, correct_letter, secret_word): #displays the play board
	print(HANGMAN_PICS[len(missed_letter)])
	print "missed letters"
	for letter in missed_letter:
		print letter,
	print "\n"	
	blank = '_' * len(secret_word)
	for i in range (len(secret_word)):
		if secret_word[i] in correct_letter:
			blank = blank[:i] + secret_word[i] + blank[i+1:]
	for letter in blank:
		print letter,
	print "\n"
def get_guess(already_guessed): #adds the input for the player to guess the word
	while True:
		print ("Guess a letter")
		guess =raw_input() #the actual player input
	
		if(len(guess)) != 1: #lets the player know that they inputed a character that isn't a letter
			print ("Please input a letter")
		elif guess in already_guessed: #lets the player know that they've already guessed a letter
			print("You have already guessed that letter. Choose another one")
		elif guess not in "abcdefghijklmnopqrstuvwxyz": #also informs the player that they've inputed a character that isn't a letter. Restricts options to a list of the 26 letters
			print ("Plese enter a valid letter")
		else:
			return (guess.lower())
			

def play_again(): #asks the player if they want to play again
	print ("Game is over")
	time.sleep(3)
	print ("Do you want to play again?, yes/no")
	return (raw_input().lower().startswith('y')) #raw input for the player choice

print "H A N G M A N" #prints the title of the game
missed_letter = ''
correct_letter = ''
secret_word = get_random_word(word_list) #lines 99-103 are the make up of the ui
game_is_over = False
while True: #if game_is_over is true, then the following code will procede to wipe the board
	clear_board()
	display_board(HANGMAN_PICS,missed_letter, correct_letter, secret_word)
	guess = get_guess(missed_letter + correct_letter)

	if guess in secret_word: 
		correct_letter = correct_letter + guess

		found_all_letter = True #determines if the word is in the list of words
		for i in range (len(secret_word)):
			if secret_word[i] not in correct_letter:
				found_all_letter = False
				break #if not true, then the game "breaks" and keeps going until it's over
		if found_all_letter: #determines if the word is the correct word
			clear_board()
			print ("Yes! The secret word is' " + secret_word +  "'! You have won!")
			game_is_over = True #attaches the word to the phrase, and sets game_is_over to true
	else:
		missed_letter = missed_letter + guess #informs the player that they have ran out of guesses and that the game is over
		if len(missed_letter) == len(HANGMAN_PICS) - 1:
			clear_board()
			print ("You have ran out of guesses")
			time.sleep(1)
			print ("You lost")
			print (HANGMAN_PICS[len(missed_letter)])
			time.sleep(1)
			print ("The secret word is'" + secret_word +"'")
			game_is_over = True
	if game_is_over: #resets the board for further play
		if play_again():
			missed_letter = ''
			correct_letter = ''
			game_is_over = False
			secret_word = get_random_word(word_list)
		else:
			break
	
