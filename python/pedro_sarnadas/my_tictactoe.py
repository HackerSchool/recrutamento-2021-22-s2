from os import system, name
import random
# from random import choice
import re
# from re import split, match


class AI:
    def __init__(self):
        self.ai_positions = [" ", " ", " ", " ", " "]
        self.pp_positions = [" ", " ", " ", " ", " "]
        self.possible_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.count = 0

    def reset(self):
        self.ai_positions = [" ", " ", " ", " ", " "]
        self.pp_positions = [" ", " ", " ", " ", " "]
        self.possible_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.count = 0


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def reset_board3x3():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


def reset_coord_board3x3():
    return [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]


def print_board(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if j == 2:
                print("" + board[i][j], end =" ")
            else:
                print("" + board[i][j] + " |", end =" ")
        if i < 2:
            print("\n-----------")


def print_boards(board, aux_board):
    for i in range(0, 3):
        for j in range(0, 3):
            if j == 2:
                print("" + board[i][j], end =" ")
            else:
                print("" + board[i][j] + " |", end =" ")
        print("\t \t \t", end =" ")
        for j in range(0, 3):
            if j == 2:
                print("" + aux_board[i][j], end =" ")
            else:
                print("" + aux_board[i][j] + " |", end =" ")
        if i < 2:
            print("\n-----------\t\t\t-----------")


def set_dictionary_row():
    return {"1": "0", "2": "0", "3": "0",
            "4": "1", "5": "1", "6": "1",
            "7": "2", "8": "2", "9": "2"}


def set_dictionary_col():
    return {"1": "0", "2": "1", "3": "2",
            "4": "0", "5": "1", "6": "2",
            "7": "0", "8": "1", "9": "2"}


def valid_move(move, board, row_scheme, col_scheme):
    if move.isdigit():
        if bool(int(move) > 0) and bool(int(move) < 10):
            i = int(row_scheme[move])
            j = int(col_scheme[move])
            if board[i][j] == " ":
                return True
        else:
            return False
    else:
        return False


def add_move(move, board, row_scheme, col_scheme, current_player):
    i = int(row_scheme[move])
    j = int(col_scheme[move])
    board[i][j] = current_player
    return board


def victory_condition(board, mode):
    #Lines
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == mode:
        return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == mode:
        return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == mode:
        return True
    elif board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == mode:
        return True
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == mode:
        return True
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == mode:
        return True
    #Diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == mode:
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == mode:
        return True
    else:
        return False


def end_round(board, current_player, not_ai):
    clear()
    if victory_condition(board, current_player):
        if not_ai:
            print("\nVictory! Player " + current_player + " won!")
        else:
            print("\nVictory! AI " + current_player + " won!")
    elif stalemate(board):
        print("\nStalemate!")
    print_board(board)
    print("\nContinue playing? (y/n)")
    decision = input()
    clear()
    return decision


def play_menu(board, aux_board, current_player, not_ai):
    clear()
    if not_ai:
        print("PvP Game:")
        print("Current Player: " + current_player + "\n")
    else:
        print("PvE Game:")
        print("CPU Player: " + current_player + "\n")
    print_boards(board, aux_board)

    if not_ai:
        print("\nYour move:")
        move = input()
        return move


def continue_menu(board, current_player, not_ai):
    ret = 0
    if victory_condition(board, current_player) or stalemate(board):
        decision = end_round(board, current_player, not_ai)
        if re.match("y", decision):
            ret = 1
        elif re.match("n", decision):
            ret = 2
        else:
            print("Invalid option... Leaving game")
            ret = 2
    return ret


def pvp_ttt(board, aux_board, row_scheme, col_scheme):
    while True:
        while True:
            current_player = "X"
            move = play_menu(board, aux_board, current_player, True)
            if valid_move(move, board, row_scheme, col_scheme):
                board = add_move(move, board, row_scheme, col_scheme, current_player)
                break
            else:
                continue
        cont = continue_menu(board, current_player, True)
        if cont == 1:
            board = reset_board3x3()
        elif cont == 2:
            break

        #Next Player
        while True:
            current_player = "O"
            move = play_menu(board, aux_board, current_player, True)
            if valid_move(move.strip("\n"), board, row_scheme, col_scheme):
                board = add_move(move.strip("\n"), board, row_scheme, col_scheme, current_player)
                break
            else:
                continue

        cont = continue_menu(board, current_player, True)
        if cont == 1:
            board = reset_board3x3()
        elif cont == 2:
            break


def occupied_positions(board, aux_board, mode):
    count = 0
    lista = ["", "", "", "", "", "", "", "", ""]
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == mode:
                lista[count] = aux_board[i][j]
                count += 1
    return lista


def try_draw_win(board, aux_board, row_scheme, col_scheme, mode):
    move = " "
    if ((board[0][0] == mode and board[1][0] == mode) or (board[2][1] == mode and board[2][2] == mode)
            or (board[0][2] == mode and board[1][1] == mode)) and board[2][0] == " ":
        move = aux_board[2][0]
    elif ((board[1][0] == mode and board[2][0] == mode) or (board[0][1] == mode and board[0][2] == mode)
            or (board[1][1] == mode and board[2][2] == mode)) and board[0][0] == " ":
        move = aux_board[0][0]
    elif ((board[0][1] == mode and board[1][1] == mode) or (board[2][0] == mode and board[2][2] == mode))\
            and board[2][1] == " ":
        move = aux_board[2][1]
    elif ((board[1][1] == mode and board[2][1] == mode) or (board[0][0] == mode and board[0][2] == mode))\
            and board[0][1] == " ":
        move = aux_board[0][1]
    elif ((board[0][2] == mode and board[1][2] == mode) or (board[2][0] == mode and board[2][1] == mode)
            or (board[0][0] == mode and board[1][1] == mode)) and board[2][2] == " ":
        move = aux_board[2][2]
    elif ((board[1][2] == mode and board[2][2] == mode) or (board[0][0] == mode and board[0][1] == mode) \
            or (board[1][1] == mode and board[2][0] == mode)) and board[0][2] == " ":
        move = aux_board[0][2]
    elif ((board[1][0] == mode and board[1][1] == mode) or (board[0][2] == mode and board[2][2] == mode))\
            and board[1][2] == " ":
        move = aux_board[1][2]
    elif ((board[1][1] == mode and board[1][2] == mode) or (board[0][0] == mode and board[2][0] == mode))\
            and board[1][0] == " ":
        move = aux_board[1][0]
    if move != " ":
        if valid_move(move, board, row_scheme, col_scheme):
            return move
    return " "


def county(lista):
    count = 0
    for i in range(len(lista)):
        if lista[i].isdigit():
            count += 1
    return count


def stalemate(board):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == " ":
                count +=1
    if count == 0:
        return True
    else:
        return False


def ai_first_second_move(myAI, board):
    move = " "
    if myAI.count == 7 and board[1][1] == "O":  # Second move
        if myAI.ai_positions[0] == "1":
            move = "9"
        elif myAI.ai_positions[0] == "3":
            move = "7"
        elif myAI.ai_positions[0] == "7":
            move = "3"
        elif myAI.ai_positions[0] == "9":
            move = "1"
    else:
        move = second_vantage_point(myAI, board)
    return move


def second_vantage_point(myAI, board):
    lista = [" ", " "]

    if (myAI.ai_positions[0] == "1") and (myAI.pp_positions[0] == "2" or myAI.pp_positions[0] == "3"):
        lista = ["7", "9"]
    elif (myAI.ai_positions[0] == "1") and (myAI.pp_positions[0] == "4" or myAI.pp_positions[0] == "7"):
        lista = ["3", "9"]
    elif (myAI.ai_positions[0] == "3") and (myAI.pp_positions[0] == "2" or myAI.pp_positions[0] == "1"):
        lista = ["7", "9"]
    elif (myAI.ai_positions[0] == "3") and (myAI.pp_positions[0] == "6" or myAI.pp_positions[0] == "9"):
        lista = ["1", "7"]
    elif (myAI.ai_positions[0] == "7") and (myAI.pp_positions[0] == "1" or myAI.pp_positions[0] == "4"):
        lista = ["3", "9"]
    elif (myAI.ai_positions[0] == "7") and (myAI.pp_positions[0] == "8" or myAI.pp_positions[0] == "9"):
        lista = ["1", "3"]
    elif (myAI.ai_positions[0] == "9") and (myAI.pp_positions[0] == "7" or myAI.pp_positions[0] == "8"):
        lista = ["1", "3"]
    elif (myAI.ai_positions[0] == "9") and (myAI.pp_positions[0] == "3" or myAI.pp_positions[0] == "6"):
        lista = ["1", "7"]
    else:
        move = "5"
        return move
    move = random.choice(lista)
    return move


def open_vantage_point(board, aux_board, move, opponent):
    if board[1][1] == " ":  # Just in case middle is unoccupied
        move = "5"
    if move == " ":         # Control Corners Accordingly (probably not needed...)
        if board[0][0] == " " and ((board[0][1] != opponent and board[0][2] != opponent) \
                                   or (board[1][0] != opponent and board[2][0] != opponent)):
            move = aux_board[0][0]
        elif board[0][2] == " " and ((board[0][1] != opponent and board[0][0] != opponent) \
                                     or (board[1][2] != opponent and board[2][2] != opponent)):
            move = aux_board[0][2]
        elif board[2][0] == " " and ((board[1][0] != opponent and board[0][0] != opponent) \
                                     or (board[2][1] != opponent and board[2][2] != opponent)):
            move = aux_board[2][0]
        elif board[2][2] == " " and ((board[1][2] != opponent and board[0][2] != opponent) \
                                     or (board[2][0] != opponent and board[2][1] != opponent)):
            move = aux_board[2][2]
    return move


def mild_vantage_corner(board, aux_board, opponent):
    move = " "
    # Control Corners
    if board[0][0] == " " and board[0][1] != opponent and board[1][0] != opponent:
        move = aux_board[0][0]
    elif board[0][2] == " " and board[0][1] != opponent and board[1][2] != opponent:
        move = aux_board[0][2]
    elif board[2][0] == " " and board[1][0] != opponent and board[2][1] != opponent:
        move = aux_board[2][0]
    elif board[2][2] == " " and board[1][2] != opponent and board[2][0] != opponent:
        move = aux_board[2][2]
    return move


def ai_first_strat(myAI, board, aux_board, row_scheme, col_scheme):
    myAI.possible_list = occupied_positions(board, aux_board, " ")
    myAI.ai_positions = occupied_positions(board, aux_board, "X")
    myAI.pp_positions = occupied_positions(board, aux_board, "O")
    myAI.count = county(myAI.possible_list)

    #First Moves
    if myAI.count == 9: #Opening
        lista = ["1", "3", "7", "9"]
        move = random.choice(lista)
        return move
    if myAI.count == 7:
        move = ai_first_second_move(myAI, board)
        return move
    #Late Game
    if myAI.count <= 5:
        move = try_draw_win(board, aux_board, row_scheme, col_scheme, "X")
        if move == " ":
            move = try_draw_win(board, aux_board, row_scheme, col_scheme, "O")
            if move == " ":
                move = open_vantage_point(board, aux_board, move, "O")
                if move == " ":
                    move = mild_vantage_corner(board, aux_board, "O")
        if move == " ":
            move = myAI.possible_list[0]
    return move


def ai_second_controls_middle(myAI, board, aux_board, row_scheme, col_scheme):
    if myAI.count == 6:
        move = try_draw_win(board, aux_board, row_scheme, col_scheme, "X")
        if move == " ":
            lista = ["2", "4", "6", "8"]
            move = random.choice(lista)
    else:
        move = try_draw_win(board, aux_board, row_scheme, col_scheme, "O")
        if move == " ":
            move = try_draw_win(board, aux_board, row_scheme, col_scheme, "X")
        if move == " ":
            move = myAI.possible_list[0]
    return move


def ai_second_no_middle_ctrl(myAI, board, aux_board, row_scheme, col_scheme):
    move = try_draw_win(board, aux_board, row_scheme, col_scheme, "X")
    if move == " ":
        move = try_draw_win(board, aux_board, row_scheme, col_scheme, "O")
    if move == " ":
        move = open_vantage_point(board, aux_board, move, "X")
        if move == " ":
            move = mild_vantage_corner(board, aux_board, "X")
        else:
            move = myAI.possible_list[0]
    return move


def ai_second_strat(myAI, board, aux_board, row_scheme, col_scheme):
    myAI.possible_list = occupied_positions(board, aux_board, " ")
    myAI.ai_positions = occupied_positions(board, aux_board, "O")
    myAI.pp_positions = occupied_positions(board, aux_board, "X")
    myAI.count = county(myAI.possible_list)

    if board[1][1] == " " and myAI.count == 8:
        move = "5"
    if board[1][1] == "O":
        move = ai_second_controls_middle(myAI, board, aux_board, row_scheme, col_scheme)

    if board[1][1] == "X" and myAI.count == 8:
        lista = ["1", "3", "7", "9"]
        move = random.choice(lista)
    elif board[1][1] == "X":
        move = ai_second_no_middle_ctrl(myAI, board, aux_board, row_scheme, col_scheme)
    return move


def pve_ttt(board, aux_board, row_scheme, col_scheme):
    myAI = AI()
    player = "O"
    ai = "X"
    while True:
        while True:
            play_menu(board, aux_board, ai, False)
            if ai == "X":
                move = ai_first_strat(myAI, board, aux_board, row_scheme, col_scheme)
            elif ai == "O":
                move = ai_second_strat(myAI, board, aux_board, row_scheme, col_scheme)
            else:
                exit()
            input("\n")
            if valid_move(move, board, row_scheme, col_scheme):
                board = add_move(move, board, row_scheme, col_scheme, ai)
                break
            else:
                continue
        cont = continue_menu(board, ai, False)
        if cont == 1:
            ai = "O"
            player = "X"
            myAI.reset()
            board = reset_board3x3()
        elif cont == 2:
            break

        while True:
            move = play_menu(board, aux_board, player, True)
            if valid_move(move.strip("\n"), board, row_scheme, col_scheme):
                board = add_move(move.strip("\n"), board, row_scheme, col_scheme, player)
                break
            else:
                continue
        cont = continue_menu(board, player, True)
        if cont == 1:
            ai = "X"
            player = "O"
            myAI.reset()
            board = reset_board3x3()
        elif cont == 2:
            break

def main_2players():
    col_scheme = set_dictionary_col()
    row_scheme = set_dictionary_row()

    aux_board = reset_coord_board3x3()
    board = reset_board3x3()

    pvp_ttt(board, aux_board, row_scheme, col_scheme)
    return


def main_ai_player():
    col_scheme = set_dictionary_col()
    row_scheme = set_dictionary_row()

    aux_board = reset_coord_board3x3()
    board = reset_board3x3()

    pve_ttt(board, aux_board, row_scheme, col_scheme)
    return

if __name__ == "__main__":
    col_scheme = set_dictionary_col()
    row_scheme = set_dictionary_row()

    aux_board = reset_coord_board3x3()
    board = reset_board3x3()

    #pve_ttt(board, aux_board, row_scheme, col_scheme)
    main_ai_player()
    input()
    exit()