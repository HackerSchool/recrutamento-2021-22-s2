//
// Created by Eduardo Nazário.
//
#include "game.h"
#include "main.h"




using namespace std;


string g_CurrentUser = "";


vector<string> readfile(string filename) {
	ifstream file;
	string entry;
	vector<string> lines;
	file.open(filename);

	while (getline(file, entry, FILEDELIM)) {
		lines.push_back(entry);
		getline(file, entry);
		lines.push_back(entry);
	}

	file.close();
	return lines;
}

void reset_password(string username, string newPass) {
	ifstream file;
	ostringstream fileBuffer;
	string fileBufferString, tempPassLen;
	size_t userPos;
	unsigned long passLen;
	int userLen;

	file.open(USERS);
	fileBuffer << file.rdbuf();
	fileBufferString = fileBuffer.str();
	userPos = fileBufferString.find(username + FILEDELIM);
	userLen = username.length();
	tempPassLen = fileBufferString.substr(userPos + userLen);
	passLen = tempPassLen.find("\n") - 1;
	fileBufferString.replace(userPos + userLen + 1, passLen, newPass);

	file.close();

	ofstream outFile(USERS);
	outFile << fileBufferString;
	outFile.close();
}

// Checks if user already exists
bool existing_user(string name) {
	vector<string> lines = readfile(USERS);
	for (int i = 0; i < lines.size(); i++) {
		if (lines[i] == name) {
			cout << "User found" << endl;
			return true;
		}
	}
	return false;
}

// Confirms if password meets the requirements
bool check_password(string password) {
	if (password.length() < PASSWORDLEN) {
		cout << "Password is big small!" << endl;
		return false;
	}

	if (password.find(FILEDELIM) != string::npos) {
		cout << "Password can't contain commas!" << endl;
		return false;
	}
	return true;
}

// Registers a new user
bool add_user(string name, string password) {
	ofstream file;

	if (existing_user(name)) {
		cout << "User already exists. Please Login!" << endl;
		return false;
	}

	if (name.find(FILEDELIM) != string::npos) {
		cout << "Invalid Username, please do not use commas" << endl;
		return false;
	}

	if (!check_password(password)) {
		return false;
	}

	file.open(USERS, ios::app);
	file << name << FILEDELIM << password << endl;
	file.close();

	cout << "User " << name << " added successfully" << endl;

	return true;

}

// Handles the logic for password reset
void handle_reset_password() {
	string newPass;
	do {
	cout << "Enter new password: ";
	cin >> newPass;
	} while (!check_password(newPass));
	reset_password(g_CurrentUser, newPass);
}

// Handles the logic for user login
bool login_check(string name, string password) {
	vector<string> lines = readfile(USERS);
	for (int i = 0; i < lines.size(); i++) {
		if (lines[i] == name) {
			if (lines[i + 1] == password) {
				cout << "Login successful" << endl;
				g_CurrentUser = name;
				return true;
			}
			cout << "Password Incorrect please try again." << endl;
			return false;
		}
	}
	cout << "Username not found" << endl;
	return false;
}


int login_sys() {
	string name, password;
	int option;

	cout << "Welcome to the login system" << endl;


	while (1) {
		cout << "1. Login" << endl;
		cout << "2. Register" << endl;
		cout << "3. Logout" << endl;
		cin >> option;
		switch (option) {
			case 1:
				cout << "Enter username" << endl;
				cin >> name;
				cout << "Enter password" << endl;
				cin >> password;
				if (login_check(name, password))
					return 1;
				break;
			case 2:
				cout << "Enter desired username" << endl;
				cin >> name;
				cout << "Enter desired password" << endl;
				cin >> password;
				add_user(name, password);
				break;
			case 3:
				cout << "Logging out..." << endl;
				return -1;
			default:
				cout << "Invalid option" << endl;
				break;
		}
	}

}

int main() {
	int option;

	switch (login_sys()) {
		case 1:
			cout << "Welcome to system3000 where you'll find a single game very cool ik" << endl;
			break;
		case -1:
			cout << "Exiting" << endl;
			return 0;
	}

	while (1) {
		cout << "1. Play Tic Tac Toe" << endl;
		cout << "2. Change User Password" << endl;
		cout << "3. Quit" << endl;
		cin >> option;

		switch (option) {
			case 1:
				cout << "Tic Tac Toe selected" << endl;
				cout << "Loading..." << endl;
				TicTacToe_App();
				break;
			case 2:
				cout << "Change User Password" << endl;
				handle_reset_password();
				break;
			case 3:
				g_CurrentUser = "";
				cout << "Logging Out..." << endl;
				return 0;
		}

	}

}
