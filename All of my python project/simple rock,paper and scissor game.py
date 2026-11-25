player_1 = 0
player_2 = 0
while True:
 		
	player1 = input("Player_1 enter any one of them Rock, Paper, Scissor: ").lower()
	player2 = input("Player_2 enter any one of them Rock, Paper, Scissor: ").lower()
	if player1 == player2:
		print("Draw")
		print("Play again ")
		
	
	elif player1 == "rock" and player2 == "paper":
		print("player2 win")
		player_2 +=1
	elif player1 == "paper" and player2 == "scissor":
		print("player2 win")
		player_2 +=1
	elif player1 == "scissor" and player2 == "rock":
		print("player2 win")
		player_2 += 1
	else:
		print("player1 win")
		player_1 +=1
	

	print(player_1)
	print(player_2)
	if player_1 ==3: 
		print("Congrulation player_1 you won this game")
		break
	if player_2 ==3:
		print("Congrulation player_2 you won this game")
		break
	print("Noone win this game so play again")
	
			   

	

													