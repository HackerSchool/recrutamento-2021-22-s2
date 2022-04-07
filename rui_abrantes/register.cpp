#include <fstream>
#include <cstring>
#include <iostream>
#include <string.h>

#include "register.h"

using namespace std;

/*

    [ ] check for better ways to manipulate strings
    [ ] check restrictions for password

*/

void addNewUser(string name, string pass){

    string line;

    ifstream reading; //for reading records
    reading.open("backend.txt");

    ofstream writing; //for writing new records
    writing.open("temp.txt");
    while (getline(reading, line)){
        writing << line << endl;
    }
    reading.close();
    writing.close();
    remove("backend.txt");
    rename("temp.txt", "backend.txt");

    //Now add new Record to file
    ofstream updatedFile;
    updatedFile.open("backend.txt", ios::app | ios::out);
    updatedFile<<name << '|' << pass <<endl;
}
 
int checkUserName(string name){
    string line;
  
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
            cout << "Invalid name" << endl;
            return 0;
        }
    }

    return 1;
}

void registerUser(){
    string userName ;
    string password ;
    int allValid = 1;

    do
    {
        cout << "Insert your name: ";
        // so it accepts spaces
        getline(cin >> ws, userName);

        if(!checkUserName(userName)){
            allValid = 0;
            continue; 
        }
        allValid = 1;

        cout << "Insert your password: ";
        getline(cin >> ws, password);
            
        
    } while (!allValid);
    
    addNewUser(userName, password);
}