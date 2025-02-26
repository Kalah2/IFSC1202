import random 

player_name = input("Enter Name: ")
player_score = 0
computer_score = 0

while player_score < 30 and computer_score < 30:
    print("Press Enter To Roll.")
    input()

    player_roll = random.randint(1, 6)
    print(f"{player_name} rolled a {player_roll}")

    computer_roll = random.randint(1, 6)
    print(f"A computer rolled a {computer_roll}")

    if player_roll == 1:
        player_score = 0
        print("Oops")
    else: 
        player_score += player_roll

    if computer_roll == 1:
        computer_score = 0
        print("Oops")
    else:
        computer_score += computer_roll

print(f"{player_name}: {player_score}, computer: {computer_score}")

if player_score > computer_score:
    print(f"{player_name} wins")
else: 
    print ("computer wins")
