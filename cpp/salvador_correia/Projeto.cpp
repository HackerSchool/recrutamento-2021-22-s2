#include <string>
#include <iostream>
#include <stdlib.h>
#include "TicTacToe.h"
#include "Calculator.h"
#include "login.h"
#include "Chatbot.h"

using namespace std;

int app_choice(){
    int choice = 0;

    cout << "\033[2J\033[1;1H"; 

    cout << "1. TicTacToe\n"; 
    cout << "2. Calculator\n";
    cout << "3. ChatBot\n";
    cout << "4. Exit\n";
    cout << "Choose an app: ";
    cin >> choice;

    while (choice < 1 || 3 < choice){
        cout << "Choose a proper app number: ";
        cin >> choice;
    }
    
    return choice;
}

int app_manager(){
    
    int app;

    while (true){

        app = app_choice();
        
        switch (app){
            case 1:
                game();
                return 0;

            case 2:
                calculator();
                break;
            
            case 3:
                chatbot();
                break;

            case 4:
                return 0;

            default:
                break;
        }
    }
    
    app = app_choice();

    return 0;
}

int main(){

    int next;

    while (true){

        next = manager();

        switch (next){
            case 0:
                return 0;

            case 1:
                next = app_manager();
                break;

            default:
                break;
        }
    }

}