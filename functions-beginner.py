#Hangman

import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

empty_list = []
game_over = False

for i in range(len(word)):
    empty_list += "_"


while not game_over:
    guess = input("Guess a word: ").lower()
    for position in range(len(word)):
        if guess == word[position]:
            empty_list[position] = guess
    print(empty_list)

    if '_' not in empty_list:
        game_over = True
        print("You win!")




