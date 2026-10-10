while True:

	player1 = input("Rock, Paper, Scissor:")
	player2 = input("Rock, Paper, Scissor: ")
	if player1 == player2:
		print("Draw")
	elif player1 == "Rock" and player2 == "Paper":
		print("player2 win")
	elif player1 == "Paper" and player2 == "Scissor":
		print("player2 win")
	elif player1 == "Scissor" and player2 == "Rock":
		print("player2 win")
	else:
		print("player1 win")
	print("Again,play ")

	

													