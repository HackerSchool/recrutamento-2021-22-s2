#include <stdio.h>
#include <iostream>

using namespace std;
    

int calculadora(){
    int a,b;
    char s;
    cout << "Bem Vindo!\nEscolha o valor de A e B e o sinal de operação(S) para A S B = ?" << endl;
    cout << "Insira o valor de A: ";
    cin >> a;
    cout << "Insira o sinal de operação S: ";
    cin >> s;
    cout << "Insira o valor de B: ";
    cin >> b;
    
    if(s == '+')
        printf("%d %c %d = %d\n",a,s,b,(a+b));
    else if (s == '-')
        printf("%d %c %d = %d\n",a,s,b,(a-b));
    else if (s == '*')
        printf("%d %c %d = %d\n",a,s,b,(a*b));
    else if (s == '/')
        printf("%d %c %d = %d\n",a,s,b,(a/b));
    else if (s == '%')
        printf("%d %c %d = %d\n",a,s,b,(a%b));

    return 0;
}