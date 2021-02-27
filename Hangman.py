import random
from words import words
import string

def valid_word(words):
	word = random.choice(words)

	while '-' in word or ' ' in word:
		word = random.choice(words)

	return word

def hangman():
	word = valid_word(words)
	lives = len(word)
	letters = set(word)
	#alphabet = set(string.ascii_lowercase)
	used_letters = set()

	print(f'You have {lives} lives') 
	while(len(letters) > 0 and lives > 0):
		print(f"Current used letters: {' '.join(used_letters)}")

		word_list = [letter if letter in used_letters else '-' for letter in word]
		print(f"Current word: {' '.join(word_list)}")


		user_letter = input('Guess letter: ').lower()
		if user_letter not in used_letters:
			used_letters.add(user_letter)

			if user_letter in letters:
				letters.remove(user_letter)
			else:
				lives -= 1
				print(f'Lives: {lives}')
		else:
			print('Already guessed')
	

	if lives == 0:
		print(f'\nYou LOST! The word is: {word}')
	else:
		print(f'You WON! The word is: {word}')


hangman()


