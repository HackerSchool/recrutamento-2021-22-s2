#ifndef TicTacToe_h
#define TicTacToe_h

#include <fstream>
#include <cstring>
#include <iostream>
#include <string.h>

using namespace std;

class TicTacToe {
    private:
        int positions[9]; 
        char board[9] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
        char bot = 'X'; char player = 'O';
        string name;
        
        bool emptySpace(int position);
        bool verifyDraw();
        bool verifyWin();
        bool verifyWinner(char player);
    
    public:
        TicTacToe(string newName){
            name = newName;
        };
        

        void printBoard();
        void inicializeGame();

        bool playTurn(char player, int position);
        bool playerMove();
        bool botMove();
        int minMax(int depth , bool isMaximizing);

        void playGame();
};

#endif