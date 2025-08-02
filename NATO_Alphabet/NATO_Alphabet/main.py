import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_code = {row.letter : row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

output_list = [phonetic_code[letter] for letter in word]

print(output_list)
