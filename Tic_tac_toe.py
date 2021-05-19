

board = ["  " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
# | is given for splitting of the row data and {} refers to place holder and once this has data, it gets filled

    print("\n"+row1)
    print(row2)
    print(row3)

def  player_move(icon):
    if icon == 'X':
        number = 1
    else:
        number = 2
    print("Your turn player {}".format(number))
# here strip function tells us that if any spaces or character is typed along with the number, consider only no
# choice - 1 because user is giving input from 1-9 and we are taking from 0-8

    choice = int(input("Enter your move [1-9]: ").strip())
    if board[choice-1] == "  ":
        board[choice - 1] = icon
    else:
        print("That space is already chosen, please select other one")

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if "  " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("x"):
        print("Player1 has won the game !!! congrats")
        break
    elif is_draw():
        print("It is a draw")
        break
    player_move("O")
    if is_victory("O"):
        print("Player2 has won the game !!! Congrats")
        break





