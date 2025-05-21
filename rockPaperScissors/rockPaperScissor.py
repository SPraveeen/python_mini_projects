import random
user_choice=int(input("Enter your choice : 0 for Rock, 1 for paper, 2 for Scissors."))
if user_choice>2 or user_choice<0:
    print("You entered invalid input")
else:
    computer_choice=random.randint(0,2)
    print("Computer Choice", computer_choice)
    if computer_choice == user_choice:
        print("It's a draw")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif user_choice==0 and computer_choice== 2:
        print("you win")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("you win")
