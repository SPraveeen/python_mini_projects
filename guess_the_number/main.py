import random
import logo
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
    
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your Guess is too low")
        return attempts-1
    elif guessed_number > answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"your guess was right... The answer was {answer}")



def game():
    print(logo.logo)
    print("Let me think of a number betwee 1 to 50.")
    answer=random.randint(1,50)
    # print(answer)
    level=input("Choose level of difficulty...Type 'easy' or 'hard': ")
    attempts=set_difficulty(level)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts !=HARD_LEVEL_ATTEMPTS:
        print("You have etered wrong difficulty level..play again!")
        return

    guessed_number=0
    while guessed_number != answer:
        print(f"you have {attempts} remaining to guess the number: ")
        guessed_number=int(input("Guess a number: "))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print(f"You are out of guesses... you lose!,answer is {answer}")
            return
        elif guessed_number != answer:
            print("Guess again")

game()