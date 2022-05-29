#include <iostream>
#include <string>
#include <map>

#include "ttt.hpp"

using namespace std;

int main() {
    bool quit = false;
    map<string, string> accounts;

    cout << "Welcome buddy!\n";

    while (!quit) {
        cout << "Enter (l) to login, (r) to register or (q) to quit: ";
        char s;
        cin >> s;

        if (s == 'l') {
            string u, p;
            cout << "Username: ";
            cin >> u;
            cout << "Password: ";
            cin >> p;

            auto it = accounts.find(u);
            if (it == accounts.end()) {
                std::cout << "Incorrect username or password :(\n";
            } else {
                if (p == it->second) {
                    bool logout = false;

                    cout << "SUCCESS!!! :D\n";

                    while (!logout) {
                        cout << "Enter (t) to play Tic-Tac-Toe, (c) to change the password or (l) logout: ";
                        char x;
                        cin >> x;

                        if (x == 't') {
                            runTTT();
                        } else if (x == 'c') {
                            string npass;
                            cout << "Username: " << u << "\n";
                            cout << "New password: ";
                            cin >> npass;
                            accounts[u] = npass;
                            cout << "Your password has been changed!\n";
                        } else if (x == 'l') {
                            logout = true;
                        } else {
                            cout << "Unknown option " << x << " :(\n";
                        }
                    }
                } else {
                    std::cout << "Incorrect username or password :(\n";
                }
            }
        } else if (s == 'r') {
            string user, pass;
            cout << "Username: ";
            cin >> user;
            cout << "Password: ";
            cin >> pass;

            auto it = accounts.find(user);
            if (it == accounts.end()) {
                accounts[user] = pass;
            } else {
                cout << "This username already exists...\n";
            }
        } else if (s == 'q') {
            quit = true;
        } else {
            cout << "Unknown option " << s << " :(\n";
        }
    }

    return 0;
}