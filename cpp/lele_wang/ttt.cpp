#include <iostream>
#include <cstdlib>

#include "ttt.hpp"

using namespace std;

class Board {
public:
    Board() {
        char a = '1';

        for (int x = 0; x < 3; x++) {
            for (int y = 0; y < 3; y++) {
                board[x][y] = a++;
            }
        }
    }

    void print() {
        cout << "╭─────┬─────┬─────╮\n";

        for (int x = 0; x < 3; x++) {
            cout << "│     │     │     │\n";

            for (int y = 0; y < 3; y++) {
                cout << "│  " << board[x][y] << "  ";
            }

            cout << "│\n";
            cout << "│     │     │     │\n";

            if (x == 0 || x == 1) {
                cout << "├─────┼─────┼─────┤\n";
            } else {
                cout << "╰─────┴─────┴─────╯\n";
            }
        }
    }

    bool place(char player, char slot) {
        for (int x = 0; x < 3; x++) {
            for (int y = 0; y < 3; y++) {
                if (board[x][y] == slot) {
                    board[x][y] = player;
                    return true;
                }
            }
        }

        return false;
    }

    bool isOver() {
        if (win('X') || win('O')) {
            return true;
        }

        for (int x = 0; x < 3; x++) {
            for (int y = 0; y < 3; y++) {
                if ((board[x][y] != 'X') && (board[x][y] != 'O')) {
                    return false;
                }
            }
        }
        
        return true;
    }

    bool win(char player) {
        for (int x = 0; x < 3; x++) {
            if (board[x][0] == board[x][1] && board[x][1] == board[x][2] && board[x][2] == player) {
                return true;
            }
        }

        for (int y = 0; y < 3; y++) {
            if (board[0][y] == board[1][y] && board[1][y] == board[2][y] && board[2][y] == player) {
                return true;
            }
        }

        if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] == player) {
            return true;
        }

        if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[2][0] == player) {
            return true;
        }

        return false;
    }

    char result() {

        if (win('X') == true) {
            cout << "And we have a winner!\n";
            cout << "Player X has won :D\n";
            return 'X';
        } else if (win('O') == true) {
            cout << "And we have a winner!\n";
            cout << "Player O has won :D\n";
            return 'O';
        } else {
            cout << "TIE\n";
            return 'T';
        }
    }

    void dumbBot() {
        char r = '1' + rand() % 9;

        while (!place('O', r)) {
            r = '1' + rand() % 9;
        }
    }

private:
    char board[3][3];
};

void runTTT() {
    srand(time(NULL));

    bool quit = false; 

    while (!quit) {
        cout << "─╥─ ╶╥╴ ╓─╴    ─╥─ ╓─╖ ╓─╴    ─╥─ ╓─╖ ╓─╴\n";
        cout << " ║   ║  ║   ──  ║  ╟─╢ ║   ──  ║  ║ ║ ╟─\n";
        cout << " ╨  ╶╨╴ ╙─╴     ╨  ╨ ╨ ╙─╴     ╨  ╙─╜ ╙─╴\n\n";
        cout << "Choose a mode: (1) 2 players; (2) Dumb bot\n";
        int m;
        cin >> m;
        cout << "Enter the number of the slot where you want to play.\n";

        Board b;
        char n;
        char p;
        b.print();

        p = 'X';

        while (!b.isOver()) {
            cin >> n;

            if (!b.place(p, n)) {
                cout << "Invalid play :(\n";
            } else {
                if (m == 1) {
                    b.print();

                    if (p == 'X') {
                        p = 'O';
                    } else if (p == 'O') {
                        p = 'X';
                    }
                } else if (m == 2) {
                    b.print();
                    if (!b.isOver()) {
                        b.dumbBot();
                        b.print();
                    }
                } else {
                    cout << "Unknown option " << m << " :(\n";
                }
            }
        }

        b.result();
        cout << "END!\n";
        cout << "Enter (r) to restart the game or (q) to quit: ";
        char w;
        cin >> w;

        if (w == 'q') {
            quit = true;
        } else if (w != 'r') {
            cout << "Unknown option " << w << " :(\n";
        }
    }
}