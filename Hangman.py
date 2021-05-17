# This is basically guess the word where we have already defined an array of words in this game
# Computer will generate a random word from that array and user will guess the word by giving one by one letters

import random
import string

def hangman():
    word_array = ['ABD', 'Kohli', 'Bumrah', 'Dhoni', 'Rohit', 'Dhawan', 'Rahul', 'Mayank', 'Boult', 'Kane' ]
    word = random.choice(word_array).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)

    lives = 5
    used_letters = set()

    while len(word_letters) > 0 and lives > 0:
        print("hey, you have ", lives,"lives and the letters you have guessed is : ",' '.join(used_letters))
# here using Join for used_letters will give a string of letters user has guessed till now
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current letter is : ", ' '.join(word_list))
        user_guess = input("Guess a letter: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
            else:
                lives = lives - 1
                print(f"Your letter {user_guess} is not there in the word selected")

        elif user_guess in used_letters:
            print("You have already guessed this letter", user_guess,"try some other letter")

        else:
            print("Invalid character, enter a valid character")

    if lives == 0:
        print("Sorry, you have lost the game, the word is ",word)
    else:
        print(f"Hurray, You have guessed the word and the word is {word}")




hangman()
