PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()   # Converting names into a list

with open("./Input/Letters/starting_letter.txt") as body:
    content = body.read()
    for name in names:
        stripped_name = name.strip()    # Removing extra spaces and new llines
        personalized_letter = content.replace(PLACEHOLDER, stripped_name) # Replacing certaing words
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode = "w") as letter:
            letter.write(personalized_letter)