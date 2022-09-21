#A Tic_Tac_Toe Game, a 3 X 3 grid where the player predicts the other player move and blocks it, and also tries to win in the process, 
# in which you could play against computer or Play against a fellow human being
#Built using a Dictionary and Functions




import random
import time

x_dict = {
    'top_l': ' ', "top_m": " ", "top_r": " ",
    "mid_l": " ", "mid_m": " ", "mid_r": " ",
    "bottom_l": " ", "bottom_m": " ", "bottom_r": " "
}

checker = []
comp_moves = ["top_l", "top_m", "top_r", "mid_l", "mid_m", "mid_r", "bottom_l", "bottom_m", "bottom_r"]


def print_board(board: dict):
    print(f' {board["top_l"]} | {board["top_m"]} | {board["top_r"]}  ')
    print("-----------")
    print(f' {board["mid_l"]} | {board["mid_m"]} | {board["mid_r"]}  ')
    print("-----------")
    print(f' {board["bottom_l"]} | {board["bottom_m"]} | {board["bottom_r"]}  ')
    return "Tic-Tac-Toe"


def tic_tac_toe_for_human():
    global x_dict
    print("""
        for this game , the use of certain keywords would be used, the board takes the format
        top_l  |   top_m  | top_r
        ---------------------
        mid_l  |   mid_m  | mid_r
        ---------------------
      bottom_l | bottom_m | bottom_r
        """)

    time.sleep(5)
    turn = "X"
    for i in range(9):
        print(print_board(x_dict))
        choice = validate_choice(turn)
        x_dict[choice] = turn
        confirmation()
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"

    print("This is a tie")
    time.sleep(3)
    return "TIC TAC TOE"


def tic_tac_toe_vs_comp():
    global comp_moves
    global x_dict
    print("""
        for this game , the use of certain keywords would be used, the board takes the format
        top_l  |   top_m  | top_r
        ---------------------
        mid_l  |   mid_m  | mid_r
        ---------------------
      bottom_l | bottom_m | bottom_r
        """)

    time.sleep(5)
   
    turn = "X"
    for i in range(9):
        if turn == "X":
            print(print_board(x_dict))
            choice = validate_choice_computer(turn)
            comp_moves.remove(choice)
            x_dict[choice] = turn
            confirmation()
        elif turn == "O":
            print(print_board(x_dict))
            comp_choice = random.choice(comp_moves)
            comp_moves.remove(comp_choice)
            x_dict[comp_choice] = turn
            confirmation()

        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"

    print("This is a tie")
    time.sleep(3)
    return intro()


def validate_choice(turn):
    global checker
    test = turn
    choice = input(f" {turn}, make your move by inputting the empty spaces code ,as said earlier \n ")
    if choice in checker:
        print("invalid input")
        return validate_choice(test)
    elif choice == "bottom_m" or choice == "bottom_l" or choice == "bottom_r":
        checker.append(choice)
        return choice
    elif choice == "mid_m" or choice == "mid_l" or choice == "mid_r":
        checker.append(choice)
        return choice
    elif choice == "top_m" or choice == "top_l" or choice == "top_r":
        checker.append(choice)
        return choice
    print("invalid input")
    return validate_choice(test)

def validate_choice_computer(turn):
    global comp_moves
    global checker
    test = turn
    choice = input(f" {turn}, make your move by inputting the empty spaces code ,as said earlier \n ")
    if choice not in comp_moves:
        print("invalid input, computer already played it")
        return validate_choice_computer(test)
    elif choice in checker:
        print("invalid input")
        return validate_choice(test)
    elif choice == "bottom_m" or choice == "bottom_l" or choice == "bottom_r":
        checker.append(choice)
        return choice
    elif choice == "mid_m" or choice == "mid_l" or choice == "mid_r":
        checker.append(choice)
        return choice
    elif choice == "top_m" or choice == "top_l" or choice == "top_r":
        checker.append(choice)
        return choice
    


def confirmation():
    global x_dict
    if x_dict["bottom_l"] == "X" and x_dict["bottom_m"] == "X" and x_dict["bottom_r"] == "X":
        print("X wins via horizontal alignment of the bottom row")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_l"] == "O" and x_dict["bottom_m"] == "O" and x_dict["bottom_r"] == "0":
        print("O wins via horizontal alignment of the bottom row")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_l"] == "X" and x_dict["mid_l"] == "X" and x_dict["top_l"] == "X":
        print("X wins via vertical alignment of the left column")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_l"] == "O" and x_dict["mid_l"] == "O" and x_dict["top_l"] == "O":
        print("O wins via vertical alignment of the left column")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["top_l"] == "X" and x_dict["top_m"] == "X" and x_dict["top_r"] == "X":
        print("X wins via horizontal alignment of the top row")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["top_l"] == "O" and x_dict["top_m"] == "O" and x_dict["top_r"] == "O":
        print("O wins via horizontal alignment of the top row")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_r"] == "X" and x_dict["top_r"] == "X" and x_dict["mid_r"] == "X":
        print("X wins via vertical alignment of the right column")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_r"] == "O" and x_dict["top_r"] == "O" and x_dict["mid_r"] == "O":
        print("O wins via vertical alignment of the right column")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_r"] == "X" and x_dict["mid_m"] == "X" and x_dict["top_l"] == "X":
        print("X wins via left - right diagonal alignment ")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_r"] == "O" and x_dict["mid_m"] == "O" and x_dict["top_l"] == "O":
        print("O wins via left -right diagonal alignment")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()

    elif x_dict["bottom_l"] == "X" and x_dict["mid_m"] == "X" and x_dict["top_r"] == "X":
        print("x wins via right - left diagonal alignment ")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_l"] == "O" and x_dict["mid_m"] == "O" and x_dict["top_r"] == "O":
        print("O wins via right -left diagonal alignment")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()

    elif x_dict["bottom_m"] == "X" and x_dict["top_m"] == "X" and x_dict["mid_m"] == "X":
        print("X wins via vertical alignment of the middle column")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["bottom_m"] == "O" and x_dict["top_m"] == "O" and x_dict["mid_m"] == "O":
        print("O wins via vertical alignment of the middle column")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()

    elif x_dict["mid_l"] == "X" and x_dict["mid_m"] == "X" and x_dict["mid_r"] == "X":
        print("X wins via horizontal alignment of the middle row")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()
    elif x_dict["mid_l"] == "O" and x_dict["mid_m"] == "O" and x_dict["mid_r"] == "O":
        print("O wins via horizontal alignment of the middle row")
        print("Thank you for gaming with us !")
        time.sleep(3)
        return intro()



def intro():
    choice = input(
        "Welcome to Tic-Tac-Toe, If you will like to play with computer, enter (1)... if you will like to play with human, enter(2) \n").lower()
    if choice == "1":
        return tic_tac_toe_vs_comp()
    elif choice == "2":
        return tic_tac_toe_for_human()
    return intro()


print(intro())
