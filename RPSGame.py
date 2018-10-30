from random import randint

choices=['Rock','Paper','Scissor']
player = False
player_lives = 5
computer_lives = 5
computer = choices[randint(0,2)]

#define win or lose function
def winorlose(status):
	print("Called win or lose function")
	print("**************************************")
	print("You", status,"! Would you like to play again?")
	choice = input("Y/N?")

	#reset the lives
	if (choice == "Y" or choice == "y"):
		#change global variables
		global computer_lives
		global player_lives
		global player
		global computer

		player = False
		player_lives = 5
		computer_lives = 5
		computer = choices[randint(0,2)]

	elif (choice == "N" or choice == "n"):
		print("You chose to quit!")
		print("**************************************")
		exit()

while player is False:
	print("============================================")
	print("Player lives:", player_lives, "/5")
	print("Computer lives:", computer_lives, "/5")
	print ("Choose your weapon!\n")
	player = str(input("Rock, Paper or Scissor?\n"))
	print("Player chooses", player)

	if (player == computer):
		print("Tie! You live to shoot another day")

	elif (player == "Rock"):
		if (computer == "Paper"):
			player_lives = player_lives - 1
			print("You lose!", computer, "covers", player)
		else:
			computer_lives = computer_lives - 1
			print("You win!", player, "smashes", computer)

	elif (player == "Paper"):
		if (computer == "Scissor"):
			player_lives = player_lives - 1
			print("You lose!", computer, "cuts", player)
		else:
			computer_lives = computer_lives - 1
			print("You win!", player, "covers", computer)
			
	elif (player == "Scissor"):
		if (computer == "Rock"):
			player_lives = player_lives - 1
			print("You lose!", computer, "smashes", player)
		else:
			computer_lives = computer_lives - 1
			print("You win!", player, "cuts", computer)

	elif (player == "Quit"):
		exit()
	else:
			print("Invalid option")
	
	#check for win or lose
	if player_lives is 0:
		winorlose("lose")
	if computer_lives is 0:
		winorlose("lose")

	player = False
	computer = choices[randint(0,2)]