import random

selections = ["Rock", "Paper", "Scissors"]
while True: 
    y = random.choice(selections)



    x = input("")

    if x == "Rock" and y == selections[1]:
        print(f"Computer chose {y}: Paper Beats Rock: You Lost!")

    elif x == "Paper" and y == selections[2]:
        print(f"Computer Chose {y}: Scirrors Beats Paper: You Lost!")

    elif x == "Scissors" and y == selections[0]:
        print(f"Computer Chose {y}: Rock Beats Scissors: You lost!")

    elif x == "Rock" and y == selections[2]:
        print(f"Computer Chose {y}: Rock Beats Scissors: You Win!")

    elif x == "Paper" and y == selections[0]:
        print(f"Computer Chose {y}:Paper Beats Rock: You Win!")

    elif x == "Scissors" and y == selections[1]:
       print(f"Computer Chose {y}:Scissors Beaats Paper: You Win!")

    elif x == y:
        print(f"Computer Chose {y}:It's a tie!")

    elif x is not selections:
        print("Invalid Input")