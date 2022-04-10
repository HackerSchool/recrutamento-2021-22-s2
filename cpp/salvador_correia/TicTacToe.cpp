#include "TicTacToe.h"

void drawBoard(char board[9]){

    cout << "\n    " <<  board[0] << " | " << board[1] <<  " | " << board[2] <<"\n";
    cout << "   -----------\n";
    cout << "    " <<  board[3] << " | " << board[4] <<  " | " << board[5] <<"\n";
    cout << "   -----------\n";
    cout << "    " <<  board[6] << " | " << board[7] <<  " | " << board[8] <<"\n\n";

}



bool Won(char board[9]){

    //horizontal verifications
    if (board[0] == board[1] && board[1] == board[2] && board[1] != ' ') 
        return true;
    if (board[3] == board[4] && board[4] == board[5] && board[4] != ' ') 
        return true;
    if (board[6] == board[7] && board[7] == board[8] && board[7] != ' ') 
        return true;
    
    //vertical
    if (board[0] == board[3] && board[3] == board[6] && board[3] != ' ') 
        return true;
    if (board[1] == board[4] && board[4] == board[7] && board[4] != ' ') 
        return true;
    if (board[2] == board[5] && board[5] == board[8] && board[5] != ' ') 
        return true;

    //diagonal
    if (board[0] == board[4] && board[4] == board[8] && board[4] != ' ') 
        return true;
    if (board[2] == board[4] && board[4] == board[6] && board[4] != ' ') 
        return true;

    return false;
}

int game(){
    //init variable
    char board[9] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
    int play_index = 5;
    int moves = 0;
    char dummy = 'a';
    int random = rand() % 8;

    cout << "\033[2J\033[1;1H";

    while (true){

        cout << "\nIt's your time to play :D";
        drawBoard(board);

        cout << "Choose a number between 1 and 9: ";
        cin >> play_index;
        while ((play_index < 1 || play_index > 9) || board[play_index-1] != ' '){
            cout << "Please choose a possible move\n";
            cout << "Choose a number between 1 and 9:";
            cin >> play_index;
        }

        //play
        board[play_index-1] = 'X';

        //keep count of moves
        moves++;

        while (((random < 1 || random > 9) || board[random] != ' ') && moves < 9){
            random = rand() % 8;
        }

        //play
        board[random] = 'O';

        //keep count of moves
        moves++;

        //check end conditions
        if (Won(board)){    
            cout << "\033[2J\033[1;1H";
            drawBoard(board);
            cout << "\n Game finished\n";
            cout << " Enter 0 to exit!\n";
            cout << " Or any other chr to restart!\n";
            cin >> dummy;
            if (dummy == '0')
                return 0;
            
            cout << "\033[2J\033[1;1H";

            //reset board
            int i;
            moves = 0;
            for (i=0; i<9; i++){
                board[i] = ' ';
            }

            
        }
        else if (moves == 10){
            cout << "\033[2J\033[1;1H";
            drawBoard(board);
            cout << "\n Draw \n";
            cout << "Enter 0 to exit!\n";
            cout << "Or any other chr to restart!\n";
            cin >> dummy;
            if (dummy == '0')
                return 0;
            
            cout << "\033[2J\033[1;1H";

            //reset board
            int i;
            moves = 0;
            for (i=0; i<9; i++){
                board[i] = ' ';
            }
        }

        else 
            cout << "\033[2J\033[1;1H";
    }   

    return 0;

}