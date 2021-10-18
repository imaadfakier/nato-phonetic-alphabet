import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet_df = pd.read_csv(filepath_or_buffer='./nato_phonetic_alphabet.csv')
# print(nato_phonetic_alphabet_df)
# print(nato_phonetic_alphabet_df.to_dict())
# for index, series_obj_ins in nato_phonetic_alphabet_df.iterrows():
#     # print(index)
#     # print(series_obj_ins)
#     # print(series_obj_ins['letter'])
#     # print(series_obj_ins['code'])
#     # pass
nato_dict = {series_object_instance.letter: series_object_instance.code for (index, series_object_instance)
             in nato_phonetic_alphabet_df.iterrows()}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input('Enter word: ').strip()
# print([nato_dict[char] for char in user_input.upper()])
print([nato_dict[char] for char in input('Enter word: ').upper().strip()])
