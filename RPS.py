#Pretty Code, UwU :>
import random
print("Lets play Rock Paper Scissor, shoot")

play_status = 1
while play_status == 1:
    ran_num = random.randint(1,3)
    comp_guess = str
    comp_points = 0
    player_points = 0
    points = {'Player Points': 0, 'Computer Points': 0}
    if ran_num == 1:
        comp_guess = 'r'
    elif ran_num == 2:
        comp_guess = 'p'
    else:
        comp_guess = 's'
    player_guess = input("Please provide your input:(r for rock, p for paper, s for scissor) ").lower()
    if comp_guess == 'r' and player_guess == 'r':
        print("Its a draw!!!")
    elif comp_guess == 'r' and player_guess == 'p':
        print("You Win!!!")
        points['Player Points'] += 1
    elif comp_guess == 'r' and player_guess == 's':
        print("You Lose!!!")
        points['Computer Points'] += 1
    elif comp_guess == 'p' and player_guess == 'r':
        print("You Lose!!!")
        points['Computer Points'] += 1
    elif comp_guess == 'p' and player_guess == 'p':
        print("Its a draw!!!")
    elif comp_guess == 'p' and player_guess == 's':
        print("You Win!!!")
        points['Player Points'] = 1
    elif comp_guess == 's' and player_guess == 'r':
        print("You Win!!!")
        points['Player Points'] += 1
    elif comp_guess == 's' and player_guess == 'p':
        print("You Lose!!!")
        points['Computer Points'] += 1
    elif comp_guess == 's' and player_guess == 's':
        print("Its a draw!!!")
    print(points)
    play_status = int(input("do you wanna play again(press 1 for yes, and 0 for no): "))

#Effecient Code, Zooooom!!!!
import random
print("Lets play Rock Paper Scissor, shoot")
play_status = 1
while play_status == 1:
    ran_num = random.randint(1,3)
    comp_guess = str
    comp_points = 0
    player_points = 0
    points = {'Player Points': 0, 'Computer Points': 0}
    if ran_num == 1: comp_guess = 'r'
    elif ran_num == 2: comp_guess = 'p'
    else: comp_guess = 's'
    player_guess = input("Please provide your input:(r for rock, p for paper, s for scissor) ").lower()
    if player_guess == comp_guess:
        print("Its a draw!!!")
    #Player Win cases
    elif (player_guess == 'r' and comp_guess == 's') or (player_guess == 's' and comp_guess == 'p') or (player_guess == 'p' and comp_guess == 'r'):
        print("You Won!!!")
        points['Player Points'] += 1
    else:
        print("You Lose!!!")
        points['Computer Points'] += 1
    print(points)
    play_status = int(input("do you wanna play again(press 1 for yes, and 0 for no): "))