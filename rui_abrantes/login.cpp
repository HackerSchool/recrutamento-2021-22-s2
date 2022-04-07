#include <fstream>
#include <cstring>
#include <iostream>
#include <string.h>

#include "login.h"

using namespace std;

/*
    [ ] verify if it's possible to
    change searchName for checkName in
    register

*/

int Login::searchName(string name){
    string line;
    userId = 0;
    ifstream myFile;
    myFile.open("backend.txt");

    while ( getline(myFile, line) ) {

        for(int i = 0; i < (int) line.size() ; i++){
            if(line[i] == '|'){
                line = line.substr(0, i);
                break;
            }
        }

        if(line == name){
            return 1;
        }
        userId ++;
    }
    userId = 0;
    return 0;
}

int Login::checkPassword(string name, string pass){
    int i ;
    string line;
    string tempLine;
  
    ifstream myFile;
    myFile.open("backend.txt");

    while ( getline(myFile, line) ) {
        tempLine = line;

        for( i = 0; i < (int) tempLine.size() ; i++){
            if(tempLine[i] == '|'){
                tempLine = tempLine.substr(0, i);
                break;
            }
        }

        if(tempLine == name){
        
            line = line.substr(i + 1, line.size() + 1);
            if(line == pass){
                return 1;
            }
            
        }
    }

    return 0;
}

void Login::loginUser(){

    int checkName = 0;
    int checkPass = 0;
    string userName;
    string pass;

 
    while(!checkName){
        cout << "Insert your name: ";
        getline(cin >> ws, userName);
        checkName = searchName(userName);
        if (!checkName) cout << "Name not found" << endl;
    }

    while(!checkPass){
        cout << "Insert your password: ";
        getline(cin >> ws, pass);
        checkPass = checkPassword(userName,pass);
        if (!checkPass) cout << "The password and usarname do not match " << endl;
    }
    _userName = userName;
    logged = true;
}

bool Login::verifyRepeatedPassword(string pass){
    string line;
    string name;
    ifstream myFile;
    myFile.open("backend.txt");

    while ( getline(myFile, line) ) {

        for(int i = 0; i < (int) line.size() ; i++){
            if(line[i] == '|'){
                line = line.substr(i+1, (int) line.size());
                name = line.substr(0, i);
                break;
            }
        }
        if(line == pass && name == _userName){
            cout << "Can not change to old password" << endl;
            return false;
        }
    }

    return true;
}

void Login::updatePassword(string pass){
    int counter = 0;
    string line;

    ifstream reading; //for reading records
    reading.open("backend.txt");

    ofstream writing; //for writing new records
    writing.open("temp.txt");
    while (getline(reading, line)){
        if(counter == userId){
            writing << _userName << '|' << pass << endl;
        }
        else{
            writing << line << endl;
        }
        counter++;
    }
    reading.close();
    writing.close();
    remove("backend.txt");
    rename("temp.txt", "backend.txt");
}

void Login::changePassword(string name){
    string newPass;
    bool changedPass = false;


    while(!changedPass){
        cout << "Insert your new password: ";
        getline(cin >> ws, newPass);
        changedPass = verifyRepeatedPassword(newPass);
        if(changedPass) updatePassword(newPass);

    }

}