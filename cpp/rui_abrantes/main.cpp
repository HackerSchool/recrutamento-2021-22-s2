#include "menus.h"
#include "login.h"
#include "register.h"   
#include "tictactoe.h"

int main(){
    int exit = 0;
    Login login;
       
    while(!exit){
        switch(principalMenu()){
            case 1:
                registerUser();
                break;
            case 2:
                login.loginUser();
                break;
            case 3:
                exit = 1;
                break;
            default:
                cout << "That is not an option\n" << endl;
        }
        while(login.isLogged()){
            TicTacToe newTicTacToe(login.getUserName());

            switch ( loginMenu() ) {
            case 1:
                newTicTacToe.inicializeGame();
                newTicTacToe.playGame();
                break;
            case 2:
                login.changePassword(login.getUserName());
                break;
            case 3:
                login.logOut();
                break;
            
            default:
                break;
            }
        }
    }
    


    return 0;
}