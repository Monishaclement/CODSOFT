import random

options =("rock","paper","scissors")

game = True

while game:
    player=None

    computer=random.choice(options)

    while player not in options:
        player =input("enter a choice:(rock,paper,scissors)")

        print(f"Player:{player}")

        print(f"Computer:{computer}")


        if player==computer:

            print(" its a tie")

        elif player == "rock" and computer == "scissors":

            print("you win!")

        elif player == "paper" and computer =="rock" :

            print("you win!")

        elif player == "scissors" and computer =="paper" :

            print("you win!")
        else:

            print("you loose")

        if not input("play again?(yes/no)").lower()=="yes":

            game=False
            
print("thanks for playing! hope you loved it")