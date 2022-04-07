//
// Created by Eduardo Nazário.
//

#include "game.h"


class TicTacToe {

public:
	char board[3][3];

	TicTacToe() {

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				board[i][j] = ' ';
			}
		}

	};

	// Display the board
	void printBoard() {

		for (int i = 0; i < 3; i++) {

			cout << board[i][0] << " || " << board[i][1] << " || " << board[i][2] << endl;
			if (i != 2) {
				cout << "——||———||——";
			}
			cout << endl;
		}

	};

	bool play(int x, int y, char player) {
		if (board[x][y] == ' ') {             //Checks if space is empty
			this->board[x][y] = player;            //Places player's symbol in the space
			return true;
		}
		return false;
	};

	// Checks if the game is over and returns the winner if there is one
	char checkWin() {

		// Verifies rows
		for (int i = 0; i < 3; i++) {
			if (board[i][0] != ' ' && board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
				return board[i][0];
			}
		}

		// Verifies columns
		for (int i = 0; i < 3; i++) {
			if (board[0][i] != ' ' && board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
				return board[0][i];
			}
		}

		// Verifies Positive Diagonal
		if (board[0][0] != ' ' && board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
			return board[0][0];
		}

		// Verifies Negative Diagonal
		if (board[0][2] != ' ' && board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
			return board[0][2];
		}

		return NOTFINISHED;
	};

	vector<vector<int> > getAvailableMoves() {
		vector<vector<int> > availableMoves;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				vector<int> move;
				if (board[i][j] == ' ') {
					move.push_back(i);
					move.push_back(j);
					availableMoves.push_back(move);
				}
			}
		}
		return availableMoves;
	};

	char isOver() {
		char isWin = checkWin();
		if (isWin != NOTFINISHED) {
			return isWin;
		} else {
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					if (board[i][j] == ' ') {
						return KEEPPLAYING;
					}
				}
			}
		}
		return DRAW;
	};


};


class Player {
public:
	TicTacToe *game;
	char letter;
	string name;

	Player(TicTacToe *currentGame, string playerName, char letter) {
		game = currentGame;
		this->letter = letter;
		this->name = playerName;
	}

};

class HumanPlayer : public Player {
public:
	HumanPlayer(TicTacToe *game, string player, char letter) : Player(game, player, letter) {};

	void play() {
		int r, c;
		while (true) {
			cout << name << ", choose your move: " << endl;
			cout << "Row:\t";
			cin >> r;
			cout << "Column:\t";
			cin >> c;
			cout << endl;
			for (auto &&avMove: game->getAvailableMoves()) {
				if (avMove[0] == r-1 && avMove[1] == c-1) {
					game->play(r-1, c-1, letter);
					return;
				}
			}
			cout << "Invalid move, try again." << endl;
		}

	};
};

class DumbCPU : public Player {
public:
	DumbCPU(TicTacToe *game, string player, char letter) : Player(game, player, letter) {};

	void play() {
		srand(time(0));
		int numAvailableMoves, size, r, c;
		vector<vector<int> > availableMoves;
		vector<int> nextMove;

		availableMoves = game->getAvailableMoves();
		numAvailableMoves = availableMoves.size();
		nextMove = availableMoves[rand() % (numAvailableMoves + 1)];

		game->play(nextMove[0], nextMove[1], letter);
	}
};

class StartDaGAIM {
	TicTacToe *game;
	string winnerName;
	char winner;
public:
	StartDaGAIM(HumanPlayer *player1, HumanPlayer *player2) {
		game = player1->game;
		bool p1 = whoStarts(player1->name); // p1 is used to keep track of who's playing next
		do {

			(*game).printBoard();
			if (p1) {
				(*player1).play();
				p1 = false;
			} else {
				(*player2).play();
				p1 = true;
			}

			winner = (*game).isOver();
		} while (winner == KEEPPLAYING);

		if (winner == DRAW) {
			cout << "It bool p1 = whoStarts(player1->name);\n"
					"\t\tdo {\n"
					"\n"
					"\t\t\t(*game).printBoard();\n"
					"\t\t\tif (p1) {\n"
					"\t\t\t\t(*player1).play();\n"
					"\t\t\t\tp1 = false;\n"
					"\t\t\t} else {\n"
					"\t\t\t\t(*player2).play();\n"
					"\t\t\t\tp1 = true;\n"
					"\t\t\t}looks like it is a tie!" << endl;
		} else {
			if (winner == (*player1).letter) {
				winnerName = (*player1).name;
			} else {
				winnerName = (*player2).name;
			}

			(*game).printBoard();

			cout << "And the winner isssssss...." << endl << "Not me!" << endl << "Fine:\t";
			cout << winnerName << "!!! YAYYYY" << endl;
		}
	}

	StartDaGAIM(HumanPlayer *player1, DumbCPU *player2) {
		game = player1->game;
		bool p1 = whoStarts(player1->name);
		do {

			(*game).printBoard();
			if (p1) {
				(*player1).play();
				p1 = false;
			} else {
				(*player2).play();
				p1 = true;
			}

			winner = (*game).isOver();
		} while (winner == KEEPPLAYING);

		if (winner == DRAW) {
			cout << "It looks like it is a tie!" << endl;
		} else {
			if (winner == (*player1).letter) {
				winnerName = (*player1).name;
			} else {
				winnerName = (*player2).name;
			}

			(*game).printBoard();

			cout << "And the winner isssssss...." << endl << "Not shy not me! ITZZYYYY" << endl << "Fine:\t";
			cout << winnerName << "!!! YAYYYY" << endl;
		}
	}

	bool whoStarts(string playerName) {
		char answer;
		cout << "Hey " << playerName << ", Would you like to go first? (y/n)";
		cin >> answer;
		if (answer== 'y'|| answer == 'Y') {
			return true;
		}
		return false;
	}

};


void TicTacToe_App() {
	char answer;

	cout << "Welcome to Tic Tac Toe!" << endl;
	cout << "Do you have Friends??? (y/n)" << endl;
	cin >> answer;
	if (answer == 'y' || answer == 'Y') {
		cout << "X to doubt?" << endl;
		cout << "I'll let you play against yourself, maybe you can win that way." << endl;

		startMultiplayer();

	} else {
		cout << "I knew it!" << endl;
		startDumbCPU();
	}

}

void startMultiplayer() {
	TicTacToe game;
	string player1Name, player2Name;
	char player1Letter, player2Letter;
	cout << "Player 1, please enter your name:\t";
	cin >> player1Name;
	cout << player1Name << ", please choose your letter:\t";
	cin >> player1Letter;
	cout << endl << endl;
	cout << "Now it's time for Player 2!" << endl;
	cout << "Player 2, please enter your name:\t";
	cin >> player2Name;
	cout << player2Name << ", please choose your letter:\t";
	cin >> player2Letter;


	HumanPlayer player1 = {&game, player1Name, player1Letter};
	HumanPlayer player2 = {&game, player2Name, player2Letter};

	StartDaGAIM(&player1, &player2);
}

void startDumbCPU() {
	TicTacToe game;
	string player1Name;
	char player1Letter, dumbLetter;


	cout << "Player, please enter your name:\t";
	cin >> player1Name;
	cout << player1Name << ", please choose your letter:\t";
	cin >> player1Letter;
	cout << "Choose CPU's Letter";
	cin >> dumbLetter;
	cout << endl;

	HumanPlayer player1 = {&game, player1Name, player1Letter};
	DumbCPU player2 = {&game, "Dumb CPU", dumbLetter};

	StartDaGAIM(&player1, &player2);


}
