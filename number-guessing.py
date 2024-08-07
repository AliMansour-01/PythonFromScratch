
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# checking user guess
def check_answer(user_guess, num, turns):
    """ Checks answer against guess, returns the number of turns remaining """
    if user_guess > num:
        print("Too high, guess again")
        return turns - 1
    elif user_guess < num:
       print("Too low, guess again")
       return turns - 1
    else:
        print(f"you got it! the answer was {num}.")

#function to set difficulty
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    #chosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()

    #repeat guessing function if user gets it wrong
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        #let the user guess a number
        guess = int(input("Make a guess: "))
        check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()



