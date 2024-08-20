import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dic = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ").upper()

letters_list = [data_dic[letter] for letter in word]
print(letters_list)