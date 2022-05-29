#include "Calculator.h"

int option_screan_printer(){

    int choice = 0;

    cout << "\033[2J\033[1;1H"; 
    
    cout << "1. Simple Operation\n"; 
    cout << "2. Exit\n";
    cout << "Choose a task: ";
    cin >> choice;

    while (choice < 1 || 2 < choice){
        cout << "Choose a proper Task number: ";
        cin >> choice;
    }
    
    return choice;
}

int simple_operation(){

    int num1, num2, result;
    char operation, dummy;

    cout << "\033[2J\033[1;1H";
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;
    cout << "Enter the operation: ";
    cin >> operation;

    switch (operation){
        case '+':
            result = num1 + num2;
            cout << "The result is: \n" << result << endl;
            break;
        case '-':
            result = num1 - num2;
            cout << "The result is: \n" << result << endl;
            break;
        case '*':
            result = num1 * num2;
            cout << "The result is: \n" << result << endl;
            break;
        case '/':
            result = num1 / num2;
            cout << "The result is: " << result << "\n" << endl;
            break;
        default:   
            cout << "Not an operation \n" << endl;
            break;
    }
    cout << "Enter any char to continue...\n";
    cin >> dummy;
    return 0;
}


int calculator(){

    int task_choice, aux;

    while (true){

        task_choice = option_screan_printer();

        switch (task_choice){
            case 1:
                simple_operation();
                break;

            case 2:
                return 0;
                break;

            default:
                break;
        }
    }
}