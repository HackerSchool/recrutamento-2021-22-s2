#include "login.h"

using namespace std;

int starting_screan_printer(){

    int choice = 0;

    cout << "\033[2J\033[1;1H"; 
    
    cout << "1. Login\n"; 
    cout << "2. Register\n";
    cout << "3. Reset Accounts\n";
    cout << "4. Exit\n";
    cout << "Choose a task: ";
    cin >> choice;

    while (choice < 1 || 4 < choice){
        cout << "Choose a proper Task number: ";
        cin >> choice;
    }
    
    return choice;
}
int resetter(){

ofstream file1;
file1.open("usernames.txt", ofstream::trunc);
file1.close();

ofstream file2;
file2.open("passwords.txt", ofstream::trunc);
file2.close();

return 0;

}
int regist(){

    string username, password;

    cout << "\033[2J\033[1;1H";
    cout << "Registrations\n";
    cout << "Username: ";
    cin >> username;
    cout << "Password: ";
    cin >> password;

    ofstream file1;
    file1.open ("usernames.txt", ios::app);
    file1 << username << endl;
    file1.close();

    ofstream file2;
    file2.open ("passwords.txt", ios::app);
    file2 << password << endl;
    file2.close();

    return 0;
}

int login(){
    
    string username, password, line;
    char dummy;
    int curLine = 1;
    int found = 0;

    cout << "\033[2J\033[1;1H";
    cout << "Login\n";
    cout << "Username: ";
    cin >> username;

    ifstream file1;
    file1.open ("usernames.txt", ios::in);

    while(getline(file1, line) && found == 0){
        if (line == username)
            found++;

        else
            curLine++;
    }

    file1.close();

    if (found == 0){
        cout << "Username not found!\n";
        cout << "Enter any char to continue...\n";
        cin >> dummy;
        return 0;
    }
    else{
        cout << "Password: ";
        cin >> password;

        ifstream file2;
        file2.open ("passwords.txt", ios::in);
        for (int i=0; i<curLine; i++)
            getline(file2, line);

        if (line == password)
            found++;

        file2.close();

        if (found == 1){
            cout << "Password is not correct!\n";
            cout << "Enter any char to continue...\n";
            cin >> dummy;
            return 0;
        }
        else{
            cout << "Login successful!\n";
            cout << "Enter any char to continue...\n";
            cin >> dummy;
            return 1;
        }
    }

    return 0;
}

int manager(){

    int task_choice, aux;

    while (true){

        task_choice = starting_screan_printer();

        switch (task_choice){
            case 1:
                aux = login();
                if (aux == 1)
                    return 1;
                break;

            case 2:
                regist();
                break;

            case 3:
                resetter();
                break;

            case 4:
                return 0;
                break;

            default:
                break;
        }
    }
}