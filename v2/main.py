# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# while True:
#     word = input("Enter a word: ").upper()
#     try:
#         # word = input("Enter a word: ").upper()
#
#         # NOTE: only put code statement(s) that is/are prone to error inside try
#         #       block
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print('Sorry, only letters in the alphabet please.')
#     else:
#         print(output_list)
#         break


def generate_phonetic_equivalent():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic_equivalent()  # recursion - very helpful at times!
    else:
        print(output_list)


generate_phonetic_equivalent()
