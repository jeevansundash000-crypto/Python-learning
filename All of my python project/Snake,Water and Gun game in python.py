print("Welcome to Snake,Water and Gun game in python")
print(
    "Rules are:-\n1)Snake drinks the water\n2)Water damage the gun\n3)Gun kills the snake"
)
while True:
    player_1 = input("Player_1-Choose any snake or water or gun: ")
    player_2 = input("Player_2-Choose any snake or water or gun: ")
    if player_1 == "snake" and player_2 == "gun":
        print("player_2 got 1")
    elif player_1 == "gun" and player_2 == "water":
        print("player_2 got 1 point")
    elif player_1 == "water" and player_2 == "snake":
        print("player_2 got 1")
    elif player_1 == player_2:
        print("Draw")
        print("None of you got any point")
        print("Retry")
    else:
        print("player_1 got 1 point")
