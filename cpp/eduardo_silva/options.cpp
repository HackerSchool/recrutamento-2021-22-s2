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

void options(pair<int, string> &p) {


    while (true) {
        string escolha;
        cout << "|=|=|=|=|=|=|  Após fazer login é possível escolher uma das seguintes opções:  |=|=|=|=|=|=|" << endl;
        cout << "----" << endl;
        cout << "   1) Mudar a password" << endl;
        cout << "----" << endl;
        cout << "   2) Entrar numa app " << endl;
        cout << "----" << endl;
        cout << "   3) Fazer logout " << endl;
        cout << "-=-=-=-> ";
        cin >> escolha;
        if (escolha == "1" || escolha == "2" || escolha == "3") {
            if (escolha == "1") {
                changepass(p.second);
                break;
            }
            if (escolha == "2") {
                while (true) {
                    string escolha2;
                    cout << "   |" << endl;
                    cout << "   |" << endl;
                    cout << "   L> ";
                    cout << "Qual a app que deseja entrar?" << endl;
                    cout << "       ----" << endl;
                    cout << "       1) Calculadora" << endl;
                    cout << "       ----" << endl;
                    cout << "       2) ChatBot (Indisponível de momento, pedimos desculpa)" << endl;
                    cout << "       ----" << endl;
                    cout << "       3) TicTacToe (Indisponível de momento, pedimos desculpa)" << endl;
                    cout << "-=-=-=-=-=-> ";
                    cin >> escolha2;
                    if (escolha2 == "1") {
                        cout << "Bem-vindo à ||Calculadora|| da HS!" << endl;
                        calculadora(p.second);
                        break;
                        }
                    if (escolha2 == "2") {
                        cout << "Esta funcionalidade encontra-se indisponível de momento =(" << endl;
                    }
                    if (escolha2 == "3") {
                        cout << "Esta funcionalidade encontra-se indisponível de momento =(" << endl;
            
                    }
                    else {
                        cout << "\n--ERROR--" << endl;
                        cout << "Desculpe, mas não existe essa opção =( Por favor repita o que deseja fazer" << endl;
                        cout << "--ERROR--\n" << endl;
                    }
                }
            }
            if (escolha == "3") {
                cout << "Obrigado pela visita, vemo-nos em breve!" << endl;
                start();
                break;
            }
            break;
        }
        else {
            cout << "\n--ERROR--" << endl;
            cout << "Desculpe, mas não existe essa opção =( Por favor repita o que deseja fazer" << endl;
            cout << "--ERROR--\n" << endl;
        }
    }
}