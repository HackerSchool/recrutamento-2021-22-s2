#include "Chatbot.h"

int chatbot(){

    int random;
    string input;

    cout << "\033[2J\033[1;1H"; 
    cout << "If you wish to leave input: ""exit""\n"; 

    cout << "Chat Bot: Hello, I'm Chatbot.\n";

    random = rand() % 4;

    while (input != "exit"){
        cout << "You:";
        cin >> input;

        random = rand() % 4;

        switch (random){
            case 1:
                cout << "Chat Bot: Hi!\n";
                break;

            case 2:
                cout << "Chat Bot: Hello I hope you're having a great day!\n";
                break;

            case 3:
                cout << "Chat Bot: I'm glad you're here!\n";
                break;

            case 4:
                cout << "Chat Bot: Lmao\n";
                break;

            default:
                break;
        }
    }
    return 0;
}