// Author: Beatriz Gavilan - 102463 - LEIC
// Login prompt and TicTacToe game - HackerSchool C++ project

// File with Tic Tac Toe functions

#include "myfunctions.h"


/*  function that draws print_board with players' marks */

void print_board(int number_players, vector<char> square)
{

	int i=1, e=0;
	if (number_players==2)
		cout << PRINT_TWO_PLAYERS << endl << endl;
	else
		cout << PRINT_ONE_PLAYER << endl << endl;
	cout << endl;

	cout << "     |     |     " << endl;

	while (i < 10){
		cout << "  " << square[i] << "  |  " << square[i+1] << "  |  " << square[i+2] << endl;
		if (i < 7){
			cout << ++e << "____|" << ++e <<"____|" << ++e << "____" << endl;
			cout << "     |     |     " << endl;
		}
		i+=3;
	}
	cout << ++e << "    |" << ++e << "    |" << ++e << "    " << endl << endl;
}



/* function that checks if the game is over. Returns 1 if someone won,
 * 0 if it's a tie and -1 if the game is still in progress. */

int checkwin(vector<char> square)
{
	int tie = 0;

	// see if there's a win in diagonals
	if (square[1] == square[5] && square[5] == square[9])
		return 1;

	if (square[3] == square[5] && square[5] == square[7])
		return 1;

	for (int i=1; i <= 9; i++){
		// if there's a win in a column
		if (i < 4 && square[i] == square[i+3] && square[i+3] == square[i+6]) {
			return 1;
		}
		// if there's a win in a line
		if ((i == 1 || i == 4 || i == 7) && square[i] == square[i+1] && square[i+1] == square[i+2]) {
			return 1;
		}
		if (square[i] == 'X' || square[i] == 'O')
			++tie;
	}
	// if there's a tie
	if (tie == 9)
		return 0;
		// if the game is still in progress
	else
		return -1;
}


int find_in_available_squares(int move, vector<int> available_squares){
	int len = available_squares.size();
	for (int i=0; i < len; i++){
		if (available_squares[i] == move){
			return i;   // returns move's index to be removed from available_squares
		}
	}
	return -1;   // if move isn't available
}


int easy_computer_move(vector<int> available_squares, char computer_mark, vector<char> square){

	int move=0, len = available_squares.size(), i = 1;
	while ( i < 9 ){
		// with index within limit, see if anyone almost has a full line
		// (to either win or stop them from winning)
		if (i != 3 && i != 6 && i != 9 && square[i] == square[i+1]){
			if (i == 1 || i == 4 || i == 7){
				move = i+2;
			}
			else {
				move = i-1;
			}
		}
			// a player has 2 marks in a line, separated by an empty square
		else if ((i == 1|| i == 4 || i == 7) && square[i] == square[i+2]){
			move = i+1;
		}
		// with index within limit, see if anyone almost has a full column
		// (to either win or stop them from winning)
		if (i < 7 && square[i] == square[i+3]){
			if (i < 4){
				move = i+6;
			}
			else{
				move = i-3;
			}
		}
			// a player has 2 marks in a column, separated by an empty square
		else if ((i == 1 || i == 2 || i == 3) && square[i] == square[i+6]){
			move = i+3;

		}
		// check right diagonal
		if (i == 1 && square[i] == square[i+4])
			move = i+8;
		else if (i == 1 && square[i] == square[i+8])
			move = i+4;
		else if (i == 5 && square[i] == square[i+4])
			move = i-4;

		// check left diagonal
		if (i == 3 && square[i] == square[i+2])
			move = i+4;
		else if (i == 3 && square[i] == square[i+4])
			move = i+2;
		else if (i == 5 && square[i] == square[i+2])
			move = i-2;

		// immediate win for computer: (move != 0 means 2 equal squares were found in a row)
		// no need to keep searching for possible moves
		if (move && square[i] == computer_mark && find_in_available_squares(move, available_squares) != -1){
			return move;
		}

		i++;
	}
	if (move && find_in_available_squares(move, available_squares) != -1){
		return move;    // if computer has a move (to stop human player's win), return it
	}
	// providing seed value for diff random numbers
	srand((unsigned) time(NULL));

	// when there's no immediate win for the computer nor an immediate block for the human
	move = rand() % len;
	move = available_squares[move];
	return move;
}


bool checkMove(int move, vector<char> square){
	// check if input is a valid number and square isn't occupied
	if ( 0 < move && move < 10 && square[move] != 'O' && square[move] != 'X') {
		return true;
	}
	cout << INVALID_INPUT;
	// same player will be next
	cin.ignore();
	return false;
}


int new_move(int number_players, int player, vector<int>* available_squares,
			 char mark, char first_player, vector<char>* square){
	int move, index;

	// player 1 is by default human, when playing against a computer
	if (NOT_FIRST_PLAYER && PLAYER_1){
		player=2;
	}
	else if(NOT_FIRST_PLAYER && PLAYER_2){
		player=1;
	}

	if (TWO_PLAYERS){
		do {
			cout << PLAYER_MOVE;
			cin >> move;
		} while(!checkMove(move, *square));

	}
	else {
		if (PLAYER_1){   //human
			do {
				cout << HUMAN_MOVE;
				cin >> move;
			} while(!checkMove(move, *square));

		}
			// computer's turn to play
		else{
			cout << PC_MOVE << endl;
			move = easy_computer_move(*available_squares, mark, *square);
		}

	}

	// update available_squares
	if (ONE_PLAYER){

		index = find_in_available_squares(move, *available_squares);
		(*available_squares).erase((*available_squares).begin() + index);
	}

	return move;
}




void tictactoe(int number_players, char first_player){
	int player = 1, i, move;
	// the 'o' is to make the code more readable (instead of 1 being in index 0, 2 being in index 1, etc)
	vector<char> square{'o','1','2','3','4','5','6','7','8','9'};
	vector<char> square_to_print{'o',' ',' ',' ',' ',' ',' ',' ',' ',' '};

	vector<int> available_squares {1,2, 3, 4, 5, 6, 7, 8, 9};
	char mark;

	cout << TICTACTOE;
	print_board(number_players, square_to_print);

	do {
		mark = UPDATE_MARK;
		move = new_move(number_players, player, &available_squares, mark, first_player, &square);

		square[move] = mark;
		square_to_print[move] = mark;

		player++;
		PLAYER_UPDATE;
		i=checkwin(square);
		print_board(number_players, square_to_print);

	} while(i==-1);


	--player;
	PLAYER_UPDATE;

	if (NOT_FIRST_PLAYER){
		player = (player == 1) ? 2:1;
	}

	if(i==1)
		if (number_players == 1 && player == 1)
			cout << YOU_WIN << endl;

		else if (number_players == 1) // player == 2 (computer)
			cout << PC_WIN << endl;

		else
			cout<<PLAYER_WIN <<endl;

	else
		cout << TIE;


}


int main(){
	int choice;
	cout << HELLO << endl;
	do {

		cout << EXIT_PROGRAM << endl;
		cout << OTHER_OPTIONS;
		cin >> choice;

		switch (choice) {
			case 1: {
				register_user();
				break;
			}

			case 2: {
				string username = log_in();
				if (username != " ")
					logged_in(username);
				break;
			}
		}

	} while (choice);

	cout << BYE << endl;
	return 0;

}

