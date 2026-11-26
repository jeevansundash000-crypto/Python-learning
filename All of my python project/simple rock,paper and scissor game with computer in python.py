import random as r
choices = ["rock","paper","scissor"]
print("*********Welcome to rock,paper and scissor game in python*********")
print(" *****In this game you should should fight with computer*********")
print("  **************Can you defect python computer****************** ")
score_1 = 0
score_2 = 0
while True:
    
    player_1 = input("Player_1 enter any one rock,paper or scissor: ").lower()
    computer = r.choice(choices)
    print("Computer:",computer)

    if player_1 == computer:
        print("Draw")
    elif player_1=="rock" and computer =="paper":
        print("Computer win")
        score_2 +=1
        print("Computer got:",score_2,"point.")
        
    elif player_1=="scissor" and computer =="rock":
        print("Computer win")
        score_2 +=1
        print("Computer got:",score_2,"point.")
    
    elif player_1=="paper" and computer =="scissor":
        print("Computer win")
        score_2 +=1
        print("Computer got",score_2,"point.")
    else:
        print("Player_1 win")
        score_1 +=1
        print("Player_1 got",score_1,"point.")
    print(score_1)
    print(score_2)
    print("************************************************************************")
     
    if score_1 == 3:
        print("Player_1 win this game")
        break

    elif score_2 ==3:
        print("Computer win this game")
        break
    
    print("Noone win this game")
        
    
