#include <stdio.h>
#include <map>
#include <iostream>
#include <fstream>
#include <string.h>
#include "tictactoe.cpp"
#include "calculadora.cpp"

using namespace std;

map<string,string> dados_utilizadores;

int login(string username);
void write_file(string username,string password);
void change_pass_file(string username, string new_pass);
int apps();
int calculadora();
int chatbot();
int tictactoe();

int main(){
    int option;
    string username,password;
    ofstream file;
    file.open("dados.txt",std::ofstream::trunc);
    do{
        cout << "Escolha uma das opções:\n1) Login\n2) Registar conta\n0) Sair\n";
        cin >> option;
        switch(option){
            //login
            case 1:
                cout << "-Login-\nUsername: ";
                cin >> username;
                cout << "Password: ";
                cin >> password;
                //ver se a password está correta
                cout << dados_utilizadores[username] <<endl;
                cout << password <<endl;
                if(dados_utilizadores[username] == password){
                    login(username);
                    cout << "\n\n";
                }
                else{
                    cout << "Password incorreta\n" << endl;
                }
                break;
            //registar conta    
            case 2:
                cout << "-Registar conta-\nUsername: ";
                cin >> username;
                cout << "Password: ";
                cin >> password;
                //ver se o username ainda não existe
                if(dados_utilizadores.count(username) == 0){
                    dados_utilizadores[username] = password;
                    write_file(username,password);
                    cout << "\n";
                }
                else{
                    cout << "Username já existente\n" << endl;
                }
                
                break;
            //sair da app
            case 0:
                cout << "Bye Bye!\n";
                return 0;

        }
    } while(option != 0);


    return 0;
}

int login(string username){
    int option;
    string new_password;
    do{
        cout << "Escolha uma das opções:\n1) Apps\n2) Mudar password\n0) Logout\n";
        cin >> option;
        switch(option){
            case 1:
                apps();
                break;
            case 2:
                cout << "-Mudar password-\nNova password: ";
                cin >> new_password;
                dados_utilizadores[username] = new_password;
                change_pass_file(username,new_password);
                cout << "Password foi alterada\n" << endl;
                break;
            case 0:
                cout << "Logout\n" << endl;
                return 0;
        }
    } while(option != 0);
    return 0;
}

int apps(){
    int option;
    do{
        cout << "Escolha uma das opções:\n1) Calculadora\n2) ChatBot\n3) Tic Tac Toe\n0) Sair\n";
        cin >> option;
        switch(option){
            case 1:
                calculadora();
                break;
            case 2:
                chatbot();
                break;
            case 3:
                tictactoe();
                break;
            case 0:
                cout << "Sair\n" << endl;
                return 0;
        }
    } while(option != 0);
    return 0;
}


int chatbot(){
    return 0;
}
int tictactoe(){
    int option;
    do{
        cout << "Escolha uma das opções:\n1) Multiplayer\n2) Vs Computer\n0) Sair\n";
        cin >> option;
        switch(option){
            case 1:
                jogo_multiplayer();
                break;
            case 2:
                jogo_computador();
                break;
            case 0:
                cout << "Sair\n" << endl;
                return 0;
        }
    } while(option != 0);
    return 0;
}

void write_file(string username,string password){
    ofstream file;
    file.open("dados.txt",std::ofstream::app);
    file << username;
    file << "-";
    file << password << endl;
    file.close();
}

void change_pass_file(string username, string new_pass){
    ifstream file;
    string line;
    int i;
    file.open("dados.txt",std::ifstream::app);
    while(getline(file,line)){
        int len = line.length();
        char line1[len+1];
        strcpy(line1,line.c_str());
        cout << line1 << endl;
        char user[100];
        for(i = 0; i <= len; i++){
            if(line1[i] != '-'){
                user[i] = line1[i];
            }
            else    
                break;
        }
        cout << user << endl;
        if(strcmp(user,username.c_str())){
            printf("aaa\n");
            cout << new_pass << endl;
            line.replace(i+1,1,new_pass);
            cout << line <<endl;
        }
    }
}