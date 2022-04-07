//
// Created by Eduardo Nazário.
//

#ifndef HS_TICTACTOE_MAIN_H
#define HS_TICTACTOE_MAIN_H



vector<string> readfile(string filename);
void reset_password(string username, string newPass);
bool existing_user(string name);
bool check_password(string password);
bool add_user(string name, string password);
void handle_reset_password();
bool login_check(string name, string password);
int login_sys();

#endif //HS_TICTACTOE_MAIN_H
