#ifndef Login_h
#define Login_h

#include <iostream>
using namespace std;

class Login {
private:
    bool logged{false};
    int userId=0;
    string _userName;

    int searchName(string name);
    int checkPassword(string name, string pass);
    bool verifyRepeatedPassword(string pass);
    void updatePassword(string pass);
public:
    void loginUser();

    string getUserName(){return _userName;};
    void changePassword(string name);

    bool isLogged(){return logged;};
    void logOut(){logged = false;};
};


#endif