// Author: Beatriz Gavilan - 102463 - LEIC
// Login prompt and TicTacToe game - HackerSchool C++ project

// File with login functions

#include "myfunctions.h"



bool username_exists(ifstream* userInfo, string username){
	string user_in_file;
	while(getline(*userInfo, user_in_file, ' ')){
		if(user_in_file == username){
			return true;
		}
		else{
			getline(*userInfo, user_in_file, '\n');
			continue;
		}
	}
	cout << NO_USER_FOUND << endl;
	return false;
}


string log_in(){
	string username, password, pass_in_file;
	ifstream userInfo;

	userInfo.open("userInfo.txt");
	cout << ENTER_USER << endl;
	cin >> username;

	if(!username_exists(&userInfo, username)){
		return " ";
	}

	getline(userInfo, pass_in_file);
	cout << ENTER_PASSWORD << endl;
	cin >> password;

	userInfo.close();
	if (password == pass_in_file){
		cout << LOG_IN_SUCCESS << endl;
		return username;
	}
	else {
		cout << WRONG_PASS << endl;
		return " ";
	}

}


void register_user() {
	string username, password, password_check;
	char sure = 'n';
	ifstream userInfo;
	while (NOT_SURE) {
		userInfo.open("userInfo.txt");  //opens file with usernames and passwords
		cout << CHOOSE_USER;
		cin >> username;
		if (!username_exists(&userInfo, username)){ // if username doesn't exist, it can be chosen
			cout << SURE_USER << endl;
			cin >> sure;
		}
		else {
			cout << USER_ALREADY_EXISTS << endl;
		}
	}
	userInfo.close();

	bool pass_are_diff; // flag for acceptable password

	do {
		pass_are_diff = false;
		cout << CHOOSE_PASS;
		cin >> password;

		if (password.size() >= 8) {

			cout << REPEAT_PASS;
			cin >> password_check;

			if (password_check != password) {   // passwords must match
				cout << PASSES_DONT_MATCH << endl;
				pass_are_diff = true;
			}
		}
		else {  // password must be above 8 characters
			cout << PASS_8_CHAR_MIN << endl;
			pass_are_diff = true;
		}

	} while (pass_are_diff);

	cout << PASS_CONFIRMED << endl;

	sure = 'n';
	// confirm registration
	cout << SURE_TO_REGISTER << endl;
	cin >> sure;
	if (sure == 'n' || sure == 'N') {
		cout << CANCEL_REGISTRATION << endl;
		return;
	}
	// add username and password to userInfo file
	ofstream userInfo_w;
	userInfo_w.open("userInfo.txt", ios::app);
	userInfo_w << username << " " << password << endl;
	userInfo_w.close();

	cout << REGISTERED << endl;
}


void call_game(){
	int number_players;
	char first_player = 'y';
	cout << WELCOME_TO_GAME << endl;
	cout << LEAVE_OR_PLAY << endl;
	cout << PC_OR_HUMAN;
	cin >> number_players;
	if (number_players == 0)
		return;
	if (number_players != 1 && number_players != 2){
		cout << INVALID_INPUT << endl;
		call_game();
	}

	switch(number_players){
		case 1:
			cout << PRINT_ONE_PLAYER << endl;
			cout << WANNA_PLAY_FIRST;
			cin >> first_player;
			if (first_player != 'y' && first_player != 'n'){
				cout << INVALID_INPUT << endl << endl;
				call_game();
			}
			break;
		case 2:
			cout << PRINT_TWO_PLAYERS << endl;
			break;
	}
	tictactoe(number_players, first_player);

}


void edit_file(string username, string new_password){
	string user_in_file, pass_in_file;
	ofstream userInfo_w;
	int i=0;
	ifstream userInfo_r;
	userInfo_r.open("userInfo.txt");
	vector<string> content;

	while(getline(userInfo_r, user_in_file, ' ')){

		getline(userInfo_r, pass_in_file);
		if(user_in_file == username){
			content.insert(content.begin() + i, username + " " + new_password);
		}
		else{
			content.insert(content.begin() + i, user_in_file + " " + pass_in_file);
		}
		i++;
	}
	userInfo_r.close();

	// this rewrites the file:

	userInfo_w.open("userInfo.txt", ios::out);
	userInfo_w << content[0] << endl;
	userInfo_w.close();

	int content_size = content.size();
	ofstream userInfo_w2;
	userInfo_w2.open("userInfo.txt", ios::app);

	for(i=1; i < content_size; i++){
		userInfo_w2 << content[i] << endl;
	}

	userInfo_w2.close();
}


void change_password(string username){

	char choice = 'n';
	string password, pass_in_file, new_password, new_pass_check;
	ifstream userInfo;

	userInfo.open("userInfo.txt");

	if(username_exists(&userInfo, username)){	//when username is found
		getline(userInfo, pass_in_file);
		cout << CURRENT_PASS << endl;
		cin >> password;
		if (password == pass_in_file){

			bool pass_diff = false;

			do {
				cout << CHOOSE_NEW_PASS;
				cin >> new_password;
				cout << REPEAT_NEW_PASS;
				cin >> new_pass_check;
				if (new_password != new_pass_check){
					cout << PASSES_DONT_MATCH << endl;
					pass_diff = true;
				}
			} while (pass_diff);

			cout << NEW_PASS_CONFIRMED << endl;
			cout << SURE_TO_CHANGE_PASS << endl;

			cin >> choice;
			if (choice == 'y' || choice == 'Y') {

				cout << CHANGING_PASS << endl;
				edit_file(username, new_password);
				cout << SUCCESSFUL_CHANGE << endl;
			}
			else if (choice == 'n' || choice == 'N') {
				cout << CANCEL_CHANGE << endl;
			}
			else {
				cout << INVALID_BACK_TO_MAIN << endl;
				logged_in(username);
			}
		}
		else {
			cout << WRONG_PASS << endl;
			logged_in(username);
		}

	}
	userInfo.close();

}



void logged_in(string username){
	char choice;
	int choice2;
	cout << WHAT_TO_DO << endl;
	cout << LOG_OUT << endl;
	cout << SEE_APPS << endl;
	cout << CHANGE_PASS << endl;
	cin >> choice2;
	if (choice2 != 0 && choice2 != 1 && choice2 != 2){
		cout << INVALID_INPUT << endl;
		logged_in(username);
	}

	while(choice2 == 1)	{
		cout << WHICH_APP << endl;
		cout << TICTACTOE_APP << endl;
		cout << LEAVE_APP_MENU << endl;
		cin >> choice2;
		if (choice2 == 1){
			cout << WANNA_PLAY << endl;
			choice = 'n';
			cin >> choice;

			while (CHOICE_IS_YES) {
				call_game();
				cout << WANNA_PLAY_AGAIN << endl;
				cin >> choice;
			}
			cout << BACK_TO_APP_MENU << endl;
		}
		if (choice2 == 0){
			cout << BACK_TO_MAIN_PAGE << endl;
			logged_in(username);
		}
	}

	if (choice2 == 2) {
		change_password(username);
	}

	if (choice2 == 0){
		cout << SURE_TO_LOG_OUT << endl;
		cin >> choice;
		if (CHOICE_IS_YES){
			cout << LOGGING_OUT << endl;
			return;
		}
		cout << BACK_TO_APP_MENU << endl;
	}

	logged_in(username);

}



