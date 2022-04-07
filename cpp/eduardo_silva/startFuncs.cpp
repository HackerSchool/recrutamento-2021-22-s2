#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <complex>
#include "startFuncs.h"
#include <termios.h>
#include <unistd.h>


using namespace std;

string encrypt(string pass) {
    string newpass(pass);
    for (int i = 0; i < pass.size(); i++) {
        newpass[i] = newpass[i] + (2 * i) + 1; //para que a primeria letra não seja igual
    }
    return newpass;
}

void registar() {
    
    //read
    ifstream read;
    read.open("pass.txt");
    
    //append
    ofstream myFile;
    myFile.open("pass.txt", ios_base::app);

    
    //formato das duas primeiras linhas do ficheito .txt
    string s;
    for (int i = 0; i < 2; i++) {
        getline(read, s);
    }

    string nm, ps;
    vector<string> usernames;
    while (read >> nm >> ps) {
        usernames.push_back(nm);
    } 


    while (true) {
        cout << "Insira o nome de usuário (não pode conter espaços) --> " ;
        string nome = "";
        cin >> nome;
        string nomefixo = nome;
        getline(cin, nome);
        

        //Para que o input no terminal não seja devolvido
        string pass = "";
        cout << "Insira uma palavra-passe (sem espaços) --> ";
        termios oldt;
        tcgetattr(STDIN_FILENO, &oldt);
        termios newt = oldt;
        newt.c_lflag &= ~ECHO;
        tcsetattr(STDIN_FILENO, TCSANOW, &newt);
        getline(cin, pass);
        tcsetattr(STDIN_FILENO, TCSANOW, &oldt);

        string pass2 = "";
        cout << "\nInsira novamente a palavra-passe que deseja --> ";
        termios oldt2;
        tcgetattr(STDIN_FILENO, &oldt2);
        termios newt2 = oldt2;
        newt2.c_lflag &= ~ECHO;
        tcsetattr(STDIN_FILENO, TCSANOW, &newt2);
        getline(cin, pass2);
        tcsetattr(STDIN_FILENO, TCSANOW, &oldt2);


        if (find(usernames.begin(), usernames.end(), nomefixo) == usernames.end() && pass == pass2) {
            cout << "\nRegisto realizado com sucesso!" << endl;
            myFile << nomefixo << " " << encrypt(pass) << "\n";

            myFile.close();
            start();
            break;
        }
        cout << "Pedimos desculpa, mas esse username já existe, por favor escolha outro." << endl;
    }
}

pair<int, string> login() {

    string nome, pass;
    cout << "Insira o nome do seu user --> ";
    cin >> nome;
    string nomefixo = nome;
    getline(cin, nome);
    cout << "Insira a sua password --> ";
    termios oldt;
    tcgetattr(STDIN_FILENO, &oldt);
    termios newt = oldt;
    newt.c_lflag &= ~ECHO;
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    getline(cin, pass);
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    
    ifstream read;
    read.open("pass.txt");

    string s;
    for (int i = 0; i < 2; i++) {
        getline(read, s);
    }

    string nm, ps;
    vector<string> usernames;
    vector<string> passwords;
    while (read >> nm >> ps) {
        usernames.push_back(nm);
        passwords.push_back(ps);
    }
    int erro = 1;
    while (true) {
        for (int i = 0; i < usernames.size(); i++) {
            if (usernames[i] == nomefixo && passwords[i] == encrypt(pass)) {
                erro = 0;
                break;
            }
        }
        if (erro == 1) {
            cout << "\n--INVALID--" << endl;
            cout << "Login inválido" << endl;
            cout << "--INVALID--" << endl;
            break;
        }
        else {break;}
    }
    pair<int, string> p;
    p.first = erro;
    p.second = nomefixo;
    return p;
}