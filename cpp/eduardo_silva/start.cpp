#include <iostream>
#include <fstream>
#include <string>
#include "startFuncs.h"
#include <vector>
#include <algorithm>
#include <complex>
#include <termios.h>
#include <unistd.h>
#include <stdlib.h>

using namespace std;

int start() {
    
    string inicio;
    cout << "=============================================================" << endl;
    cout << "=============================================================" << endl;
    cout << "Bem vindo!\nEscolha uma das seguintes opções:\n----\n   1) Fazer login\n----\n   2) Registar\n----\n   3) Sair do programa" << endl;
    cout  << "\nSelecione 1, 2 ou 3 --> ";
    cin >> inicio;
    cout << "=============================================================" << endl;
    cout << "=============================================================" << endl;


    while (true) {
        if (inicio == "3") {
            cout << "--" << endl;
            cout << "Obrigado pela sua visita! Vemos-nos em breve!" << endl;
            cout << "--" << endl;

            return 0;
            
        }
        if (inicio == "2") {
            cout << "--" << endl;
            cout << "Para começar o seu registo é necessário inserir um nome e uma password. Vamos começar!" << endl;
            cout << "--" << endl;
            registar();
            break;
        }
        if (inicio =="1") {
            pair<int, string> p;
            p = login();
            while (p.first == 1) {
                p = login();
            }
            if(p.first == 0) {
            cout << "\n=================================================================================" << endl;
            cout << "   Login realizado com sucesso! Bem vindo, de novo, ao menu de recrutamento!" << endl;
            cout << "=================================================================================" << endl;
                options(p);
            }
            break;
        }
        else {
            string inicionew;
            cout << "\n--ERRO--" << endl;
            cout << "Input inválido, por favor selecione novamente o que pretende --> ";
            cout << "--ERRO--\n" << endl;

            cin >> inicionew;
            inicio = inicionew;
        }
    }


    return 0;
}