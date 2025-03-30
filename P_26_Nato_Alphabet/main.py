import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
phonetics = { row.letter: row.code for (index, row) in df.iterrows()}
# print(phonetics)

# Create a list of the phonetic code words from a word that the user inputs.
def generate_pheonetic():

        user_input = input("Enter your name : ").upper()
        
        try:
                output_list = [phonetic_dict[letter] for letter in word]
        except KeyError:
                print("ERROR! Enter letters only from alphabets please!")
                generate_pheonetic()
        else:
                print(output_list)
