#include "menus.h"

int principalMenu(){

    int menu;

    cout << "What do you really want to do?" <<endl;
    cout << "-Register         1" <<endl;
    cout << "-Login            2" <<endl;
    cout << "-Exit             3" <<endl;
    cin >> menu;

    return menu;
}

int loginMenu(){
    int menu;

    cout << "What do you really want to do?" <<endl;
    cout << "-Play TicTacToe   1" <<endl;
    cout << "-Change password  2" <<endl;
    cout << "-Logout           3" <<endl;
    cin >> menu;

    return menu;
}
