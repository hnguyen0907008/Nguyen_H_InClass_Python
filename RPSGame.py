from random import randint
choices=['Rock','Paper','Scissor']
player = False
computer_choice = choices[randint(0,2)]

while player is False:
	print ("Choose your weapon!")
	player = str(input("Rock, Paper or Scissor?"))
	print("Computer chooses", computer_choice)
	print("Player chooses", player)
	if (player == computer_choice):
		print("Tie! You live to shoot another day")
	elif (player == "Rock"):
		if (computer_choice == "Rock"):
			print("Tie! You live to shoot another day")
		elif (computer_choice == "Paper"):
			print("You lose!")
		elif (computer_choice == "Scissor"):
			print("You win!")
	elif (player == "Paper"):
		if (computer_choice == "Paper"):
			print("Tie! You live to shoot another day")
		elif (computer_choice == "Scissor"):
			print("You lose!")
		elif (computer_choice == "Rock"):
			print("You win!")
	elif (player == "Scissor"):
		if (computer_choice == "Scissor"):
			print("Tie! You live to shoot another day")
		elif (computer_choice == "Rock"):
			print("You lose!")
		elif (computer_choice == "Paper"):
			print("You win!")
	else:
			print("Invalid")
	player = False
	computer_choice = choices[randint(0,2)]