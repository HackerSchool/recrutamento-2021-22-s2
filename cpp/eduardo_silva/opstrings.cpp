#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include "startFuncs.h"
#include <vector>
#include <algorithm>
#include <complex>
#include <Eigen/Dense>
#include <termios.h>
#include <unistd.h>
#include <unordered_map>
#include <cstdlib>

using namespace std;


void opstrings(string expression) {

    //vou usar a notação RPN (reverse polish notation)

    unordered_map<string, int> ordens = {
        { "*", 2},
        { "/", 2},
        { "+", 1},
        { "-", 1},
        { "(", -1},
        { ")", -1},
    };

    //dividir a string em elementos essenciais (digitos/operadores)
    vector<string> antesRPN;
    for(char c : expression) {
        if ( c == ' ') { 
            continue;
        }
        else {
            string temp(1, c);
            antesRPN.push_back(temp);
        }
    }


    //passar de normal para RPN
    vector<string> depoisRPN = {};
    vector<string> auxiliar = { "("};
    antesRPN.push_back(")");
    for (string c : antesRPN) {
        
        if(ordens.find(c) == ordens.end()) {
            depoisRPN.push_back(c);
        }
        
        else if ( c == "(") {
            auxiliar.push_back(c);
        }
        else if (c == ")") {
            while(auxiliar.back() != "(") {
                depoisRPN.push_back(auxiliar.back());
                auxiliar.pop_back();
            }
            auxiliar.pop_back();
        }
        else {
            while(auxiliar.size() > 0 && ordens[c] <= ordens[auxiliar.back()]) {
                depoisRPN.push_back(auxiliar.back());
                auxiliar.pop_back();
            }
            auxiliar.push_back(c);
        }
    }



    //conta em si
    vector<float> evaluationStack = {};
    for(string c : depoisRPN)
    {
        if(ordens.find(c) != ordens.end())
        {
            float n1 = evaluationStack[evaluationStack.size() - 1]; 
            float n2 = evaluationStack[evaluationStack.size() - 2];

            switch(c[0])
            {
                case '+':
                    n2 = n2 + n1;
                    break;
                case '-':
                    n2 = n2 - n1;
                    break;
                case '*':
                    n2 = n2 * n1;
                    break;
                case '/':
                    n2 = n2 / n1;
                    break;
            }
            evaluationStack.pop_back();
            evaluationStack.pop_back();
            evaluationStack.push_back(n2);
        }
        else
        {
            evaluationStack.push_back(atof(c.c_str()));
        }
    }
    cout << "O resultado desta operação é: " << endl;
    cout << expression << " = " << evaluationStack[0] << endl;
}
