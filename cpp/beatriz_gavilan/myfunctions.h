
// Author: Beatriz Gavilan - 102463 - LEIC
// Header file for HackerSchool C++ project, with function prototypes, output messages and a few defined commands.


#ifndef MYFUNCTIONS_H
#define MYFUNCTIONS_H


#include <iostream>
#include <fstream>
#include <vector>


// list of cout messages
#define TICTACTOE "\n\n\tTic Tac Toe\n\n"
#define TIE "==> There's a tie!"
#define PLAYER_WIN "==> Player "<< player <<" won "
#define PC_WIN "==> The computer won :P "
#define YOU_WIN "You win!"

#define PLAYER_MOVE "Player " << player << ", enter a number:  "
#define PC_MOVE "It's my turn, I'm thinking..."
#define HUMAN_MOVE "It's your turn, enter a number:  "
#define PRINT_TWO_PLAYERS "Player 1 (X)  -  Player 2 (O)"
#define PRINT_ONE_PLAYER "You (X)  -  Computer (O)"

#define BACK_TO_APP_MENU "Returning to app menu..."
#define INVALID_INPUT "Invalid move, try again. "
#define BACK_TO_MAIN_PAGE "Returning to the main page..."
#define LOGGING_OUT "Logging out..."

#define SURE_TO_LOG_OUT "Are you sure you want to logout? (y/n) "
#define WANNA_PLAY_AGAIN "Do you want to play Tic Tac Toe again? (y/n) "
#define WANNA_PLAY "Do you want to play Tic Tac Toe? (y/n) "
#define WHICH_APP "Which app do you want to use? (Currently, there's only 1 available, apologies...)"

#define BYE "Aww :( Okay, goodbye!"
#define HELLO "Hello, welcome!"
#define EXIT_PROGRAM "If you want to exit the program, write the number 0."
#define OTHER_OPTIONS "If you want to create an account, write 1.\nIf you already have one, write the number 2 to login: "

#define WHAT_TO_DO "What do you want to do?"
#define LOG_OUT "0. Log out"
#define SEE_APPS "1. See apps"
#define CHANGE_PASS "2. Change password"
#define TICTACTOE_APP "1. Tic-Tac-Toe"
#define LEAVE_APP_MENU "0. Leave app menu."

#define WRONG_PASS "Incorrect password."
#define INVALID_BACK_TO_MAIN "Invalid input. You'll be directed to the main page."
#define CANCEL_CHANGE "Password change cancelled."
#define SUCCESSFUL_CHANGE "Password changed successfully."
#define CHANGING_PASS "Changing password..."
#define SURE_TO_CHANGE_PASS "Are you sure you want to change your password? (y/n) "
#define NEW_PASS_CONFIRMED "New password confirmed."

#define PASSES_DONT_MATCH "Passwords do not match, please try again."
#define REPEAT_NEW_PASS "Enter your new password again: "
#define CHOOSE_NEW_PASS "Enter your new password: "
#define CURRENT_PASS "What's your current password?"

#define PRINT_ONE_PLAYER "1-player game"
#define PRINT_TWO_PLAYERS "2-players game"
#define WANNA_PLAY_FIRST "Do you want to play first? (y/n): "
#define WELCOME_TO_GAME "Welcome to the game!"
#define LEAVE_OR_PLAY "To leave the game menu, write 0. Otherwise, choose the number of players.  "
#define PC_OR_HUMAN "Write 1 to play against the computer, or 2 to play against another player: "

#define REGISTERED "Registered successfully!"
#define CANCEL_REGISTRATION "Registration cancelled."
#define SURE_TO_REGISTER "Are you sure you want to register? (y/n)"
#define PASS_CONFIRMED "Password confirmed."
#define PASS_8_CHAR_MIN "Password must be at least 8 characters long."
#define REPEAT_PASS "Repeat your password: "
#define CHOOSE_PASS "Choose a password: "

#define USER_ALREADY_EXISTS "Username already exists, please choose another one."
#define SURE_USER "Are you sure you want this username? (y/n)"
#define CHOOSE_USER "Choose a username: "
#define LOG_IN_SUCCESS "Log in successful."
#define ENTER_PASSWORD "What's your password?"
#define ENTER_USER "What's your username?"
#define NO_USER_FOUND "No user is registered under that username."

// list of defined commands
#define NOT_SURE sure == 'n' || sure == 'N'
#define CHOICE_IS_YES choice == 'y' || choice == 'Y'
#define PLAYER_UPDATE player = (player % 2) ? 1:2;	// updates the player
#define UPDATE_MARK (player == 1) ? 'X' : 'O'
#define NOT_FIRST_PLAYER first_player == 'n'
#define PLAYER_1 player == 1
#define PLAYER_2 player == 2
#define TWO_PLAYERS number_players == 2
#define ONE_PLAYER number_players == 1


using namespace std;


/*  LIST OF ALL FUNCTIONS: */
bool username_exists(ifstream* userInfo, string username);
string log_in();
void register_user();
void call_game();
void logged_in(string username);
void edit_file(string username, string new_password);
void change_password(string username);


void print_board(int number_players, vector<char> square);
int checkwin(vector<char> square);
int find_in_available_squares(int move, vector<int> available_squares);
int easy_computer_move(vector<int> available_squares, char computer_mark, vector<char> square);
bool checkMove(int move, vector<char> square);
int new_move(int number_players, int player, vector<int>* available_squares,
			 char mark, char first_player, vector<char>* square);
void tictactoe(int number_players, char first_player);



#endif
