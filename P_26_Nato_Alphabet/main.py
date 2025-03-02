import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
phonetics = { row.letter: row.code for (index, row) in df.iterrows()}
# print(phonetics)

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name : ").upper()
output_list = [ phonetics[letter] for letter in user_input]
print(output_list)