import random

CHOICE = ['R','P','S']
CHANCE = 3
human_score,Com_score = 0,0

while CHANCE>=1:
    Com_choice = random.choice(CHOICE)
    Hum_choice = input("Enter Choice\n1.ROCk\n2.PAPER\n3.SCISSOR\n")
    CHANCE-=1
    if Com_choice == Hum_choice:
        print("DRAW")
        CHANCE+=1
    elif Com_choice == 'R' and Hum_choice == 'P':
        print("HUMAN WINS")
        human_score+=1
    elif Com_choice == 'R' and Hum_choice == 'S':
        print("COMPUTER WINS")
        Com_score+=1
    elif Com_choice == 'P' and Hum_choice == 'R':
        print("COMPUTER WINS")
        Com_score+=1
    elif Com_choice == 'P' and Hum_choice == 'S':
        print("HUMAN WINS")
        human_score+=1
    elif Com_choice == 'S' and Hum_choice == 'R':
        print("HUMAN WINS")
        human_score+=1
    elif Com_choice == 'S' and Hum_choice == 'P':
        print("COMPUTER WINS")
        Com_score+=1

if Com_score > human_score:
    print("COMPUTER WINS IN ALL MATCHES")
else:
    print("HUMAN WINS ALL MATCHES")