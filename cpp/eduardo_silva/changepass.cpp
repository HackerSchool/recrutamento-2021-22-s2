#include <iostream>
#include <fstream>
#include <string>
#include "startFuncs.h"
#include <vector>
#include <algorithm>
#include <complex>
#include <termios.h>
#include <unistd.h>

using namespace std;

void changepass(string nome) {

    cout << "======================================================" << endl;
    cout << "----------------ALTERAÇÃO DE PASSWORD-----------------" << endl;
    cout << "======================================================" << endl;
    while (true) {
        string pass, newpass1, newpass2;
        cout << "\n\n" << endl;
        cout << "Para alterar a sua password é necessário colocar a palavra passe antiga e depois criar uma nova" << endl;
        cout << "A mudar palavra passe para @ utilizador@ " << nome << endl;
        
        //read
        ifstream read;
        read.open("pass.txt");
        
        //append
        ofstream myFile("outfile.txt");

        
        //formato das duas primeiras duas linhas
        string s;
        for (int i = 0; i < 2; i++) {
            getline(read, s);
        }

        string nm, ps;
        vector<string> usernames;
        vector<string> passwords;
        int counter = 0;
        while (read >> nm >> ps) {
            usernames.push_back(nm);
            passwords.push_back(ps);
            counter++;
        }
        int k;
        for (int i = 0; i < usernames.size(); i++) {
            if (usernames[i] == nome) {
                k = i;
            }
        }
        cout << "\nPor favor introduza a sua pass antiga --> ";
        //esta solução faz a pass antiga aparecer, mas a nova não
        cin >> pass;
        string passfixa = pass;
        getline(cin, pass);


        cout << "\nAgora por favor coloque a sua password nova --> ";
        termios oldt2;
        tcgetattr(STDIN_FILENO, &oldt2);
        termios newt2 = oldt2;
        newt2.c_lflag &= ~ECHO;
        tcsetattr(STDIN_FILENO, TCSANOW, &newt2);
        getline(cin, newpass1);
        tcsetattr(STDIN_FILENO, TCSANOW, &oldt2);


        cout << "\nPor favor verifique mais uma vez --> ";
        termios oldt3;
        tcgetattr(STDIN_FILENO, &oldt3);
        termios newt3 = oldt3;
        newt3.c_lflag &= ~ECHO;
        tcsetattr(STDIN_FILENO, TCSANOW, &newt3);
        getline(cin, newpass2);
        tcsetattr(STDIN_FILENO, TCSANOW, &oldt3);

        //verificar se é válido e depois passar tudo para o outfilxe
        if (encrypt(passfixa)==passwords[k] && newpass1 == newpass2 && passfixa != newpass1) {
            myFile << "#file for usernames and passwords \n";
            myFile << "#format: name (whitespace) pass \n";
            for (int j = 0; j < counter; j++) {
                if (passwords[j] != encrypt(passfixa)){
                    myFile << usernames[j] << " " << passwords[j] << "\n";
                }
            }
            myFile << nome << " " << encrypt(newpass1) << "\n";
            myFile.close();
            remove("pass.txt");
            rename("outfile.txt", "pass.txt"); //renomear para não haver conflito com login
            cout << "\n----" << endl;
            cout << "Alteração realizada com sucesso!" << endl;
            cout << "----" << endl;
            pair<int, string> p;
            p.first = 0;
            p.second = nome;
            options(p);
            break;
        }
        else {
            cout << "\n----ERRO----" << endl;
            cout << "Argumentos inválidos" << endl;
            cout << "----ERRO----" << endl;
        }
    }
}