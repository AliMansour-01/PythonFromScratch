#Hangman

import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)

empty_list = []

for e in range(len(word)):
    empty_list += "_"
game_over = False
lives = 6

while game_over == False:
    guess = input("Guess a letter: ").lower()
    for position in range(len(word)):
        if guess == word[position]:
            empty_list[position] = guess
    if guess not in word:
        lives -= 1
    if '_' not in empty_list:
        game_over = True
        if game_over == True:
            print("You Win!")
    elif lives == 0:
        print("You Lose!")
        game_over = True
    print(stages[lives])
    print(f"{' '.join(empty_list)}")





