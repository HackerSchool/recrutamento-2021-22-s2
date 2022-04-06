import sys
from copy import deepcopy
import mysql.connector

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from tictactoe_ui import Ui_MainWindow

class tictactoe(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        global board
        global jogador_ctr, computador_ctr
        jogador_ctr = 0
        computador_ctr = 0
        board = [
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ]
        ]
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.actionQuit.triggered.connect(self.close)
        self.start_button.clicked.connect(self.start_game)
        self.b1.clicked.connect(lambda: self.make_player_move(0, 0))
        self.b2.clicked.connect(lambda: self.make_player_move(0, 1))
        self.b3.clicked.connect(lambda: self.make_player_move(0, 2))
        self.b4.clicked.connect(lambda: self.make_player_move(1, 0))
        self.b5.clicked.connect(lambda: self.make_player_move(1, 1))
        self.b6.clicked.connect(lambda: self.make_player_move(1, 2))
        self.b7.clicked.connect(lambda: self.make_player_move(2, 0))
        self.b8.clicked.connect(lambda: self.make_player_move(2, 1))
        self.b9.clicked.connect(lambda: self.make_player_move(2, 2))
    
    def start_game(self):
        global board
        board = [
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ]
        ]
        self.sq1.setText(board[0][0])
        self.sq2.setText(board[0][1])
        self.sq3.setText(board[0][2])
        self.sq4.setText(board[1][0])
        self.sq5.setText(board[1][1])
        self.sq6.setText(board[1][2])
        self.sq7.setText(board[2][0])
        self.sq8.setText(board[2][1])
        self.sq9.setText(board[2][2])
        self.jogador_ctr.setText("Jogador: " + str(jogador_ctr))
        self.computador_ctr.setText("Computador: " + str(computador_ctr))

    def make_player_move(self, row, col):
        global board

        if self.is_tied():
            self.error("Game is tied")
            self.start_game()
            return 0

        if board[row][col] == '_':
            board[row][col] =  'X'
            self.update_board()
            if self.is_winning_move("X", row, col):
                self.error("Player wins")
                global jogador_ctr
                jogador_ctr = jogador_ctr + 1
                self.start_game()
                return
            self.next_move()
        else:
            self.error("Square already taken")

    def make_computer_move(self, row, col):
        global board
        if board[row][col] == '_':
            board[row][col] = 'O'
            self.update_board()

        else:
            self.error("Square already taken")

    def update_board(self):
        global board
        self.sq1.setText(board[0][0])
        self.sq2.setText(board[0][1])
        self.sq3.setText(board[0][2])
        self.sq4.setText(board[1][0])
        self.sq5.setText(board[1][1])
        self.sq6.setText(board[1][2])
        self.sq7.setText(board[2][0])
        self.sq8.setText(board[2][1])
        self.sq9.setText(board[2][2])

    def next_move(self):
        global board

        if self.is_tied():
            self.error("Game is tied")
            self.start_game()
            return 0

        # First we check if any move will result instant win.
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    if self.is_winning_move('O', row, col):
                        self.make_computer_move(row, col)
                        self.update_board()
                        self.error("Computer wins")
                        global computador_ctr
                        computador_ctr = computador_ctr + 1
                        self.start_game()
                        return 1
        
        # If no winning move, we check if any move will result in instant loss.
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    if self.is_winning_move('X', row, col):
                        self.make_computer_move(row, col)
                        return 0

        # If possible, we move to a corner.
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    if row == 0 and col == 0:
                        self.make_computer_move(row, col)
                        return 0
                    elif row == 0 and col == 2:
                        self.make_computer_move(row, col)
                        return 0
                    elif row == 2 and col == 0:
                        self.make_computer_move(row, col)
                        return 0
                    elif row == 2 and col == 2:
                        self.make_computer_move(row, col)
                        return 0

        # If possible, we move to the center.
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    if row == 1 and col == 1:
                        self.make_computer_move(row, col)
                        return 0

        # If possible, we move to a side.
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    if row == 0 and col == 1:
                        self.make_computer_move(row, col)
                        return 0
                    elif row == 1 and col == 0:
                        self.make_computer_move(row, col)
                        return 0
                    elif row == 1 and col == 2:
                        self.make_computer_move(row, col)
                        return 0
                    elif row == 2 and col == 1:
                        self.make_computer_move(row, col)
                        return 0

    def is_tied(self):
        # Check if the board is full.
        global board
        full = True
        for row in range(3):
            for col in range(3):
                if board[row][col] != 'X' and board[row][col] != 'O':
                    full = False
        return full

    def is_winning_move(self, player, row, col):
        if player == "X":
            opponent = "O"
        else:
            opponent = "X"

        global board

        board_copy = deepcopy(board)
        board_copy[row][col] = player

        for row in range(3):
            if board_copy[row][0] == board_copy[row][1] == board_copy[row][2] == player:
                return 1
            elif board_copy[row][0] == board_copy[row][1] == board_copy[row][2] == opponent:
                return 0
        for col in range(3):
            if board_copy[0][col] == board_copy[1][col] == board_copy[2][col] == player:
                return 1
            elif board_copy[0][col] == board_copy[1][col] == board_copy[2][col] == opponent:
                return 0
        if board_copy[0][0] == board_copy[1][1] == board_copy[2][2] == player:
            return 1
        elif board_copy[0][0] == board_copy[1][1] == board_copy[2][2] == opponent:
            return 0
        if board_copy[0][2] == board_copy[1][1] == board_copy[2][0] == player:
            return 1
        elif board_copy[0][2] == board_copy[1][1] == board_copy[2][0] == opponent:
            return 0
        else:
            return 0

    def error(self, message):
        QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = tictactoe()
    win.show()
    sys.exit(app.exec())