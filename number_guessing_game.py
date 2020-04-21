import random

def GuessName():
	print("Enter the Level you want to play")
	print("Enter\n e for easy\n m for medium\n h for hard\n")
	
	while True:
		try:
			level = str(input(":::"))
		except ValueError:
			print("Invalid input type...Use format stated above")
			continue
		else:
			break
		
	if level == "e":
		randomNumber = random.randint(0,10)
		count = 0
		chances = 6
		while True:
			while count < chances :
				print("Guess a number: [NB: you have {} guesses]" .format(int(chances)-int(count)))
				while True:
					try:
						myGuess = int(input(":::"))
					except ValueError:
						print("Please Enter a Number")
						continue
					else:
						break
	
				if myGuess == randomNumber:
					print("You got it right in {} guesses" .format(count + 1))
					break
				if myGuess != randomNumber:
					print("You got it wrong")
					count = count + 1
			print("Secret Number was {}" .format(randomNumber))
			c = input("Do you want to play this level again? Y/N\n :::")
			if c == "y":
				count = 0
				randomNumber = random.randint(0,10)
				continue
			if c == "n":
				break
				exit(0)
			
	if level == "m":
		randomNumber = random.randint(0,20)
		count = 0
		chances = 4
		while True:
			while count < chances:
				print("Guess a number: [NB: you have {} guesses]" .format(int(chances)-int(count)))
				while True:
					try:
						myGuess = int(input(":::"))
					except ValueError:
						print("Please Enter a Number")
						continue
					else:
						break
				if myGuess == randomNumber:
					print("You got it right in {} guesses" .format(count + 1))
					break
				if myGuess != randomNumber:
					print("You got it wrong")
					count =  count + 1
			print("Secret Number was {}" .format(randomNumber))
			c = input("Do you want to play this level again? Y/N\n :::")
			if c == "y":
				count = 0
				randomNumber = random.randint(0,20)
				continue
			if c == "n":
				break
				exit(0)
			
	if level == "h":
		randomNumber = random.randint(0,50)
		count = 0
		chances = 3
		while True:
			while count < chances :
				print("Guess a number: [NB: you have {} guesses]" .format(int(chances)-int(count)))
				while True:
					try:
						myGuess = int(input(":::"))
					except ValueError:
						print("Please Enter a Number")
						continue
					else:
						break
						
				if myGuess == randomNumber:
					print("You got it right in {} guesses" .format(count + 1))
					break
				if myGuess != randomNumber:
					print("You got it wrong")
					count += 1
			print("Secret Number was {}" .format(randomNumber))
			c = input("Do you want to play this level again? Y/N\n :::")
			if c == "y":
				count = 0
				randomNumber = random.randint(0,50)
				continue
			if c == "n":
				break
				exit(0)
			


print("***********~~~~~~~~************")
print("Welcome to the Modified number guessing game")
print("***********~~~~~~~~************")

		
while True:
	GuessName()
	c = input("Do you want to Restart the game? Y/N\n :::")
	if c == "y":
		continue
	if c == "n":
		print("We hope you will come back to Play. Goodbye")
		break
	exit(0)


