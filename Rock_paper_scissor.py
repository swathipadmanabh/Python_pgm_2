import random

def play():
    user_input = input("Hi User, Please enter your choice, "
                       "Enter r for rock, "
                       "Enter p for paper, "
                       "Enter s for scissor\n ").lower()
    computer_input = random.choice(['r','p','s'])
    print(f"You have selected {user_input} and computer has selected {computer_input}")

    if user_input == computer_input:
        return "Match is a tie"

    if who_is_the_winner(user_input,computer_input):
        return "Hurray, You won"

    return "Sorry, you lost"

def who_is_the_winner(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

