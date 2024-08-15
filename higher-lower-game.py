import random
from higher_lower_art import logo, VS
from higher_lower_data import data


# Display Art
print(logo)

score = 0

def format_data(account):
    """Format account data and make it printable"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return (f"{account_name}, a {account_description}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """Take user's guess and the follower counts and return if they got it right or wrong"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

account_b = random.choice(data)

#make game repeatable by adding a while loop
game_continues = True
while game_continues:
    #make account b become the next account a
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(VS)
    print(f"Compare B: {format_data(account_b)}.")

    #ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear screen
    print("\n" * 20 )
    print(logo)
    # check if the user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    correct_answer = check_answer(guess, a_follower_count, b_follower_count)

    # score keeping
    if correct_answer:
        score += 1
        print(f"Your answer is right! score: {score}")
    else:
        print(f"You got the wrong answer. Final {score}")
        game_continues = False



