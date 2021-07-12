def main():    # Here I have made a Function

    # Importing the random module here
    import random
    # defining a class here
    class game:
        # here trying the code 
        try:
            RandNo = random.randint(1, 3)
            if RandNo == 1:
                computer = "Stone"
            elif RandNo == 2:
                computer = "Paper"
            elif RandNo == 3:
                computer = "Scissor"
            
            print("1. Stone")
            print("2. Paper")
            print("3. Scissor")
            
            Player = int(input("Enter your choice here (1, 2 or 3 ?)\n"))

            if Player == 1:
                player = "Stone"
            elif Player == 2:
                player = "Paper"
            elif Player == 3:
                player = "Scissor"

            # Here checking all the possiblities
            if computer == player:
                print(f"You have choosed {player}")
                print(f"The computer had choosed {computer}")
                print(f"The game has tied")

            # Here checking all the possibilites if the computer has choosen Stone
            elif computer == "Stone" and player == "Paper":
                print(f"The compuer has choosen {computer} and you have choosed {player}")
                print("Congratulations! You Won..")
            elif computer == "Stone" and player == "Scissor":
                print(f"The computer has choosen {computer} and you have choosed {player}")
                print("Sorry! You lose..")

            # Here checking all the possibilites when the computer has choosen Paper 
            elif computer == "Paper" and player == "Stone":
                print(f"The computer has choosen {computer} and you have choosed {player}")
                print("Sorry! You lose..")
            elif computer == "Paper" and player == "Scissor":
                print(f"The computer has choosen {computer} and you have choosed {player}")
                print("Congratulations! You Won..")

            # Here checking all the possibilities when the computer has choosen Scissor
            elif computer == "Scissor" and player == "Stone":
                print(f"The computer has choosen {computer} and you have choosed {player}")
                print("Congratulations! You Won..")
            elif computer == "Scissor" and player == "Paper":
                print(f"The computer has choosen {computer} and you have choosed {player}")
                print("Sorry! You lose..")
        
        except Exception as e:
            print(f"Your input resulted in an error.({e})")

        # Here checking weather the user wants to exit the code or not 

        restart = input("Do you want to restart the game(y/n): ")
        if restart == "y":
            main()
        else:
            exit()
        # And now all the possibilities have been defined 

# From here the code will starts
main()