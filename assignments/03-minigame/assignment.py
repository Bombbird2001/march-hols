from random import randint

number = randint(1, 100)
guessNo = 0
guess = 0
print("I'm thinking of a number from 1-100. You have 7 guesses.")
guessed = []
while True:
	while True:
		try:
			guess = int(input("Guess #" + str(guessNo + 1) + ": "))
			repeat = False
			for no in guessed:
				if no == guess:
					repeat = True
					print("You guessed that already! Guess again!")
					break
			if not repeat:
				guessed.append(guess)
				break
		except:
			print("Please enter a valid integer!")
	if guess >= 1 and guess <= 100:
		guessNo += 1
		if guess == number:
			print("You guessed it! What are the odds?? (Quite high actually)")
			break
		elif guess > number:
			print("Too high!")
		elif guess < number:
			print("Too low!")
	else:
		print("That's not between 1-100! Guess again!")
	if guessNo >= 7:
		print("Sorry, you didn't guess it in 7 tries! You lose.")
		print("The answer was", number)
		break