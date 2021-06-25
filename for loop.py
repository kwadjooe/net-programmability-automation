# Prompt the user to enter a word
user_word = input("Please input your word: \n")
# and assign it to the user_word variable.
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    v = ["A", "E", "I", "O", "U"]

    if letter not in v:
        letter = []
        print(letter)

        continue
        
