import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dic = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():

    word = input("Enter a word: ").upper()
    try:
        letters_list = [data_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(letters_list)

generate_phonetic()