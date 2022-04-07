#include <iostream>
#include <string>
#include <cmath>
#include "startFuncs.h"
#include <vector>
#include <algorithm>
#include <complex>
#include <Eigen/Dense>

//ROOT
#include "TCanvas.h"
#include "TApplication.h"
#include "TGraph.h"
#include "TSystem.h"
#include "TH1D.h"
#include "TMultiGraph.h"
#include "TF1.h"

using namespace std;

//infelizmente nesta função usei várias vezes umas linhas de código
//para saber se o utilizador queria continuar na aplicação ou não
//inicialmente tinha criado uma função auxiliar que continha essas linhas, 
//contudo dava-me problemas com questões de ter funções a correr por cima e por baixo de outras
//então tive de deixar assim
void calculadora(string nome) {

    cout << "==============================================================================" << endl;
    cout << "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||" << endl;
    cout << "==============================================================================" << endl;
    cout << "   ____________                  |           |             ____________      " << endl;
    cout << "   |                             |           |             |                 " << endl;
    cout << "   |                             |___________|             |___________      " << endl;
    cout << "   |                             |           |                         |     " << endl;
    cout << "   |                             |           |                         |     " << endl;
    cout << "   |___________ ALCULADORA       |           | ACKER       ____________| CHOOL     " << endl;
    cout << "==============================================================================" << endl;
    cout << "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||" << endl;
    cout << "==============================================================================" << endl; 



    while (true) {
        string escolha;
        cout << "\n\nA nossa calculadora apresenta X modos diferentes, qual deseja usar? " << endl; //falta trocar X
        cout << "----" << endl;
        cout << "   1) Recebe dois números, uma operação" << endl;
        cout << "----" << endl;
        
        cout << "   2) Recebe uma string" << endl;
        cout << "----" << endl;
        
        cout << "   3) Resolve uma equação" << endl;
        cout << "----" << endl;
        cout << "   4) Resolve um sistema matricial" << endl;
        cout << "----" << endl;
        cout << "   5) Representar um gráfico de uma função de uma variável" << endl;
        cout << "----" << endl;
        cout << "-=-=-=> ";
        cin >> escolha;
        if (escolha == "1" || escolha == "2" || escolha == "3" || escolha == "4" || escolha == "5") {
            if (escolha == "1") {
                long double n1, n2;
                string oper;
                cout << "Insira o primeiro número --> ";
                cin >> n1;
                cout << "Insira o segundo número --> ";
                cin >> n2;
                cout << "Qual a operação que deseja? (+, -, *, /, ^, //, %) --> ";
                cin >> oper;
                cout << "################" << endl;
                cout << "A calcular " << n1 << " " << oper << " " << n2 << endl;
                long double conta = 1.0;
                if (oper == "+") {conta = n1 + n2;}
                if (oper == "-") {conta = n1 - n2;}
                if (oper == "*") {conta = n1 * n2;}
                if (oper == "/") {conta = n1 / n2;}
                if (oper == "^") {conta = pow(n1, n2);}
                if (oper == "//") {conta = floor(n1/n2);}
                if (oper == "%") {conta = n1 - (floor(n1/n2) * n2);}
                cout << "O resultado é :: " << conta << endl;                
                string simnao;
                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                cin >> simnao;
                if (simnao == "n") {
                    pair<int, string> p;
                    p.first = 0;
                    p.second = nome;
                    options(p);
                    break;
                }
                while (simnao != "n" && simnao != "S") {
                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                    cin >> simnao;
                }
            }
            if (escolha == "2") {
                cout << "Neste modo calculamos uma string, tendo em conta as prioridades das operações!" << endl;
                cout << "Qual a expressão que deseja calcular?" << endl;
                cout << "--> ";
                string expression;
                getline(cin >> std::ws, expression);
                opstrings(expression);
                string simnao;
                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                cin >> simnao;
                if (simnao == "n") {
                    pair<int, string> p;
                    p.first = 0;
                    p.second = nome;
                    options(p);
                    break;
                }
                while (simnao != "n" && simnao != "S") {
                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                    cin >> simnao;
                }

            }
            if (escolha == "3") {
                string eqq;
                cout << "A nossa calculadora permite resolver equações polinomiais, trignométricas, exponenciais e logaritmicas." << endl;
                cout << "--" << endl;
                cout << "   1) Polinomiais" << endl;
                cout << "--" << endl;
                cout << "   2) Trignométricas" << endl;
                cout << "--" << endl;
                cout << "   3) Exponenciais/Logarítmicas" << endl;
                cout << "--" << endl;
                cout << "Deseja realizar uma equação de que tipo? --> ";
                cin >> eqq;
                if (eqq  == "1" || eqq == "2" || eqq == "3") {
                    if (eqq == "1") {
                        string eqq2;
                        cout << "--" << endl;
                        cout << "Deseja resolver a equação a 1 ou 2 variáveis? --> ";
                        cin >> eqq2;
                        if (eqq2 == "1") { //polinomial de 1 variavel
                            long double A, B, C;
                            cout << "Substitua os valores de A, B e C na expressão Ax^2 + Bx + C = 0" << endl;
                            cout << "A = ";
                            cin >> A;
                            cout << "B = ";
                            cin >> B;
                            cout << "C = ";
                            cin >> C;
                            cout << "A resolver a equação " << A << "x^2 +(" << B << "x) +(" << C << ") = 0" << endl;
                            if (A == 0.0) {
                                long double conta = ((-1) * C) / B;
                                cout << "O resultado é :: x = " << conta << endl;         
                            }
                            if (A != 0.0) {
                                if (sqrt((B * B) - (4 * A * C)) > 0.0) {
                                long double conta1 = (-B + sqrt((B * B) - (4 * A * C))) / (2 * A);
                                long double conta2 = (-B - sqrt((B * B) - (4 * A * C))) / (2 * A);
                                
                                cout << "######" << endl;
                                cout << "O resultado é :: x1 = " << min(conta1, conta2) << " || x2 = " << max(conta1, conta2) << endl;
                                cout << "######" << endl;

                                }
                                else {
                                    long double REAL = -B / (2 * A);
                                    long double IMAG = sqrt((-1)*((B * B) - (4 * A * C))) / (2 * A);
                                    cout << "######" << endl;
                                    cout << "O resultado é:: x1 = " << REAL << " +" << IMAG << " i || x2 = " << REAL << " -" << IMAG << " i" << endl;
                                    cout << "######" << endl;
                                }
                            }
                            auto G3 = new TApplication("A" , nullptr, nullptr);
                            auto canvas = new TCanvas("canvas", "", 1200, 800);

                            auto frec = [](double * x, double * par) { //função
                                return par[0] * pow(x[0], 2) + par[1] * x[0] + par[2];
                            };
                            auto frec2 = [](double * x, double * par) { //eixo xx
                                return x[0] * 0.0;
                            };
                            auto F2 = new TF1("eixo dos zeros", frec2, -100, 100, 0);
                            auto F1 = new TF1("quadratic formula", frec, -20.0, 20.0, 3);
                            F1 -> SetParameters(A, B, C);
                            F2 -> SetLineColor(kBlue+2);
                            F1 -> SetLineColor(kRed+2);
                            F1 -> SetLineWidth(4);
                            F2 -> SetLineWidth(4);
                            F1 -> Draw();
                            F2 -> Draw("same");
                            canvas -> Update();
                            canvas -> WaitPrimitive();
                            gSystem -> ProcessEvents();

                            string simnao;
                            cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                            cin >> simnao;
                            if (simnao == "n") {
                                pair<int, string> p;
                                p.first = 0;
                                p.second = nome;
                                options(p);
                                break;
                            }
                            while (simnao != "n" && simnao != "S") {
                                cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                cin >> simnao;
                            }
                        }
                        if (eqq2 == "2") { //polinomial de 2 variaveis
                            cout << "Escolha os valores de A, B, C, D, E, F, tal que: Ax + By = C & Dx + Ey = F" << endl;
                            long double A, B, C, D, E, F;
                            cout << "A = ";
                            cin >> A;
                            cout << "B = ";
                            cin >> B;
                            cout << "C = ";
                            cin >> C;
                            cout << "D = ";
                            cin >> D;
                            cout << "E = ";
                            cin >> E;
                            cout << "F = ";
                            cin >> F;
                            //supostamente isto é a Cramers Rule
                            long double DX = C*E - B*F;
                            long double DY = A*F - C*D;
                            long double D1 = A*E - D*B;
                            if (D1 != 0.0) {
                                cout << "O resultado é :: x = " << DX/D1 << " || y = " << DY/D1 << endl;
                            }
                            else {
                                cout << "O sistema é impossível ou possível indeterminado não sendo possível retornar valores exatos para x e y" << endl;
                            }
                            string simnao;
                            cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                            cin >> simnao;
                            if (simnao == "n") {
                                pair<int, string> p;
                                p.first = 0;
                                p.second = nome;
                                options(p);
                                break;
                            }
                            while (simnao != "n" && simnao != "S") {
                                cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                cin >> simnao;
                            }
                        }
                    }
                    if (eqq == "2") { //trignometrica de 1 variavel
                        cout << "Qual das seguintes expressões deseja usar?" << endl;
                        cout << "--" << endl;
                        cout << "   1) sin(x) = y" << endl;
                        cout << "   2) cos(x) = y" << endl;
                        cout << "   3) tan(x) = y" << endl;
                        string trig;
                        cout << "--> ";
                        cin >> trig;
                        if (trig == "1" || trig == "2" || trig == "3") {
                            string trig2;
                            cout << "Deseja calcular o valor de x ou y? --> ";
                            cin >> trig2;
                            if (trig2 == "x" || trig2 == "y") {
                                if (trig2 == "y" && trig == "1") {//trignometrica para calcular y
                                    long double x;
                                    cout << "Introduza o valor para x em graus --> ";
                                    cin >> x;
                                    long double xRadians = x*M_PI/180.0;
                                    long double conta = sin(xRadians);
                                    cout << "O resultado é :: sin(" << x << "º) = " << conta;
                                    string simnao;
                                    cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                    cin >> simnao;
                                    if (simnao == "n") {
                                        pair<int, string> p;
                                        p.first = 0;
                                        p.second = nome;
                                        options(p);
                                        break;
                                    }
                                    while (simnao != "n" && simnao != "S") {
                                        cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                        cin >> simnao;
                                    }
                                }
                                if (trig2 == "y" && trig == "2") {//trignometrica para calcular y
                                    long double x;
                                    cout << "Introduza o valor para x em graus --> ";
                                    cin >> x;
                                    long double xRadians = x*M_PI/180.0;
                                    long double conta = cos(xRadians);
                                    cout << "O resultado é :: cos(" << x << "º) = " << conta;
                                    string simnao;
                                    cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                    cin >> simnao;
                                    if (simnao == "n") {
                                        pair<int, string> p;
                                        p.first = 0;
                                        p.second = nome;
                                        options(p);
                                        break;
                                    }
                                    while (simnao != "n" && simnao != "S") {
                                        cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                        cin >> simnao;
                                    }
                                }
                                if (trig2 == "y" && trig == "3") {//trignometrica para calcular y
                                    long double x;
                                    cout << "Introduza o valor para x em graus --> ";
                                    cin >> x;
                                    long double xRadians = x*M_PI/180.0;
                                    double k = x / 90;
                                    if (k == 1.0 || k == 2.0 || k == -1.0 || k == -2.0 || k == 3.0 || k == 4.0 || k == -3.0 || k == -4.0 ) {
                                        cout << "Argumento inválido, o valor de x não pode ser múltiplo de 90!" << endl;
                                    }
                                    else {
                                        long double conta = sin(xRadians) / cos(xRadians);
                                        cout << "O resultado é :: tan(" << x << "º) = " << conta;
                                        string simnao;
                                        cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                        cin >> simnao;
                                        if (simnao == "n") {
                                            pair<int, string> p;
                                            p.first = 0;
                                            p.second = nome;
                                            options(p);
                                            break;
                                        }
                                        while (simnao != "n" && simnao != "S") {
                                            cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                            cin >> simnao;
                                        }
                                    }
                                }
                                if (trig2 == "x" && trig == "1") {//trignometrica para calcular x
                                    long double y;
                                    cout << "Introduza o valor para y entre [-1, 1] --> ";
                                    cin >> y;
                                    if (y <= 1 && y >= -1) {
                                        cout << "O resultado é :: sin(x) = " << y << " => x = " << asin(y) * 180.0 / M_PI;
                                        string simnao;
                                        cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                        cin >> simnao;
                                        if (simnao == "n") {
                                            pair<int, string> p;
                                            p.first = 0;
                                            p.second = nome;
                                            options(p);
                                            break;
                                        }
                                        while (simnao != "n" && simnao != "S") {
                                            cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                            cin >> simnao;
                                        }
                                    }
                                    else {
                                        cout << "O valor de y deve estar compreendido entre -1 e 1" << endl;
                                    }
                                }
                                if (trig2 == "x" && trig == "2") {//trignometrica para calcular x
                                    long double y;
                                    cout << "Introduza o valor para y entre [-1, 1] --> ";
                                    cin >> y;
                                    if (y <= 1 && y >= -1) {
                                        cout << "O resultado é :: cos(x) = " << y << " => x = " << acos(y) * 180.0 / M_PI;
                                        string simnao;
                                        cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                        cin >> simnao;
                                        if (simnao == "n") {
                                            pair<int, string> p;
                                            p.first = 0;
                                            p.second = nome;
                                            options(p);
                                            break;
                                        }
                                        while (simnao != "n" && simnao != "S") {
                                            cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                            cin >> simnao;
                                        }
                                    }
                                    else {
                                        cout << "O valor de y deve estar compreendido entre -1 e 1" << endl;
                                    }
                                }
                                if (trig2 == "x" && trig == "3") {//trignometrica para calcular x
                                    long double y;
                                    cout << "Introduza o valor para y --> ";
                                    cin >> y; //o dominio de arctan = R
                                    cout << "O resultado é :: tan(x) = " << y << " => x = " << atan(y) * 180.0 / M_PI;
                                    string simnao;
                                    cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                    cin >> simnao;
                                    if (simnao == "n") {
                                        pair<int, string> p;
                                        p.first = 0;
                                        p.second = nome;
                                        options(p);
                                        break;
                                    }
                                    while (simnao != "n" && simnao != "S") {
                                        cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                        cin >> simnao;
                                    }
                                    
                                }                                                                                                      
                            }
                            else {
                                    cout << "Input inválido, tente novamente" << endl;
                                }

                                
                            }
                            else {
                                cout << "Input inválido, tente novamente" << endl;
                            }                           
                    }
                    if (eqq == "3") {
                        string exlo;
                        cout << "Deseja realizar que tipo de operação, substituindo o valor de x?" << endl;
                        cout << "--" << endl;
                        cout << "   1) e^x = y" << endl;
                        cout << "--" << endl;
                        cout << "   2) log(x) = y" << endl;
                        cout << "--> ";
                        cin >> exlo;
                        if (exlo == "1" || exlo == "2"){
                            if (exlo == "1") {
                                long double x1;
                                cout << "Qual o valor de x? --> ";
                                cin >> x1;
                                long double conta = exp(x1);
                                cout << "O resultado é :: e^" << x1 << " = " << conta << endl;
                                string simnao;
                                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                cin >> simnao;
                                if (simnao == "n") {
                                    pair<int, string> p;
                                    p.first = 0;
                                    p.second = nome;
                                    options(p);
                                    break;
                                }
                                while (simnao != "n" && simnao != "S") {
                                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                    cin >> simnao;
                                }
                            }
                            if (exlo == "2") {

                                long double x2;
                                cout << "Qual o valor de x? --> ";
                                cin >> x2;
                                long double conta = log(x2);
                                cout << "O resultado é :: log(" << x2 << ") = " << conta << endl;
                                string simnao;
                                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                cin >> simnao;
                                if (simnao == "n") {
                                    pair<int, string> p;
                                    p.first = 0;
                                    p.second = nome;
                                    options(p);
                                    break;
                                }
                                while (simnao != "n" && simnao != "S") {
                                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                    cin >> simnao;
                                }

                            }
                        }
                        else {
                            cout << "Input inválido, tente novamente" << endl;
                        }  
                    }
                }
                else {
                    cout  << "Input inválido, por favor repita o que deseja" << endl;
                }

            }
            if (escolha == "4") { //sistema matricial
                cout << "\nNeste modo da calculadora é possível resolver sistemas com N variáveís e com N equações\nTendo o formato A11 + A12 + ... A1N = B1 até AN1 + AN2 + ... ANN = BN" << endl;
                int quantos;
                cout << "Quantas variáveis deseja usar? --> ";
                cin >> quantos;
                const int N = quantos;
                Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> M(N, N);
				Eigen::Matrix<double, Eigen::Dynamic, 1> b(N);
                for (int i = 0; i < N; i++) { //matrix cof
                    cout << "\nCoeficientes para a #" << i+1 << " linha do sistema" << endl;
                    for (int k = 0; k < N + 1; k++) {
						if (k < N) {
							double cof;
							cout << "Coeficiente para a #" << k+1 << " variável --> ";
							cin >> cof;
							M(i, k) = cof;
						}
						else {
							double cot;
							cout << "A expressão é igual a --> ";
							cin >> cot;
							b(i, 0) = cot;
						}

                    }

                }
                cout <<"Vamos resolver o seguinte sistema!" << endl;
				cout << "Matriz:\n" << M << endl;            
                cout << "Vetor dos constantes:\n"<< b << endl;

                mGauss(M, b);
                gJordan(M, b);

                for (int y = 0; y < b.rows(); y++) {
                    cout << "A #" << y+1 << " variável é igual a " << b(y, 0) << endl;
                }
				string simnao;
                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                cin >> simnao;
                if (simnao == "n") {
                    pair<int, string> p;
                    p.first = 0;
                    p.second = nome;
                    options(p);
                    break;
                }
                while (simnao != "n" && simnao != "S") {
                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                    cin >> simnao;
                }



            }
            if (escolha == "5") {
                string eqq;
                cout << "Neste modo a nossa calculadora desenha gráficos da secção 2)" <<endl;
                cout << "Assim sendo que tipo de gráfico deseja?" << endl;
                cout << "--" << endl;
                cout << "   1) Polinomial" << endl;
                cout << "--" << endl;
                cout << "   2) Trignométrico" << endl;
                cout << "--" << endl;
                cout << "   3) Exponencial/Logarítmico" << endl;
                cout << "--" << endl;
                cout << "--> ";
                cin >> eqq;
                if (eqq == "1" || eqq == "2" || eqq == "3") {
                    auto G3 = new TApplication("A" , nullptr, nullptr);
                    auto canvas = new TCanvas("canvas", "", 1200, 800);
                    if (eqq == "1") {
                        cout << "Este modo permite calcular o gráfico de a1X^n + a2X^(n-1) + a3X^(n-2) + ... + a(n-1)X + an" << endl;
                        int grau;
                        cout << "De que grau deseja que seja a função --> ";
                        cin >> grau;
                        const int graufixo = grau;

                        vector<double> coeffs;
                        for (int m = 0; m <= graufixo; m++) {
                            int grugru;
                            cout << "Qual o coeficiente para X de grau #" << graufixo - m << "--> ";
                            cin >> grugru;
                            coeffs.push_back(grugru);
                        }

                 
                        
                        
                        auto frec = [coeffs, graufixo](double * x, double * par) {
                            double conta = 0;
                            for (int n = 0; n < coeffs.size(); n++) {
                                conta += coeffs[n] * pow(x[0], (graufixo - n)); 
                            }
                            return conta;
                        };

                        auto frec2 = [](double * x, double * par) { //eixo xx
                            return x[0] * 0.0;
                        };

                        auto F2 = new TF1("eixo dos zeros", frec2, -100, 100, 0);
                        auto F1 = new TF1("grafico", frec, -20.0, 20.0, 0);
                        F2 -> SetLineColor(kBlue+2);
                        F1 -> SetLineColor(kRed+2);
                        F1 -> SetLineWidth(4);
                        F2 -> SetLineWidth(4);
                        F1 -> Draw();
                        F2 -> Draw("same");
                        canvas -> Update();
                        canvas -> WaitPrimitive();
                        gSystem -> ProcessEvents();

                        string simnao;
                        cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                        cin >> simnao;
                        if (simnao == "n") {
                            pair<int, string> p;
                            p.first = 0;
                            p.second = nome;
                            options(p);
                            break;
                        }
                        while (simnao != "n" && simnao != "S") {
                            cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                            cin >> simnao;
                        }

                        

                    }
                    if (eqq == "2") {
                        string eqq2;
                        cout << "Que tipo de função trignométrica deseja desenhar?" << endl;
                        cout << "--" << endl;
                        cout << "   1) sin(ax + b) + c" << endl;
                        cout << "--" << endl;
                        cout << "   2) cos(ax + b) + c" << endl;
                        cout << "--" << endl;
                        cout << "   3) tan(ax + b) + c" << endl;
                        cout << "--> ";
                        cin >> eqq2;
                        if (eqq2 == "1" || eqq2 == "2" || eqq2 == "3") {
                            if (eqq2 == "1") {
                                double a, b, c;
                                cout << "Sendo que a expressão é sin(ax + b) + c, qual os valores de a, b, e c?" << endl;
                                cout << "a --> ";
                                cin >> a;
                                cout << "b --> ";
                                cin >> b;
                                cout << "c --> ";
                                cin >> c;
                      
                                
                                
                                auto frec = [a, b, c](double * x, double * par) {
                                    return sin((a * x[0]) + b) + c;
                                };

                                auto frec2 = [](double * x, double * par) { //eixo xx
                                    return x[0] * 0.0;
                                };

                                auto F2 = new TF1("eixo dos zeros", frec2, -100, 100, 0);
                                auto F1 = new TF1("grafico", frec, -20.0, 20.0, 0);
                                F2 -> SetLineColor(kBlue+2);
                                F1 -> SetLineColor(kRed+2);
                                F1 -> SetLineWidth(4);
                                F2 -> SetLineWidth(4);
                                F1 -> Draw();
                                F2 -> Draw("same");
                                canvas -> Update();
                                canvas -> WaitPrimitive();
                                gSystem -> ProcessEvents();

                                string simnao;
                                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                cin >> simnao;
                                if (simnao == "n") {
                                    pair<int, string> p;
                                    p.first = 0;
                                    p.second = nome;
                                    options(p);
                                    break;
                                }
                                while (simnao != "n" && simnao != "S") {
                                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                    cin >> simnao;
                                }


                            }
                            if (eqq2 == "2") {
                                double a, b, c;
                                cout << "Sendo que a expressão é cos(ax + b) + c, qual os valores de a, b, e c?" << endl;
                                cout << "a --> ";
                                cin >> a;
                                cout << "b --> ";
                                cin >> b;
                                cout << "c --> ";
                                cin >> c;
            
                                
                                
                                auto frec = [a, b, c](double * x, double * par) {
                                    return cos((a * x[0]) + b) + c;
                                };

                                auto frec2 = [](double * x, double * par) { //eixo xx
                                    return x[0] * 0.0;
                                };

                                auto F2 = new TF1("eixo dos zeros", frec2, -100, 100, 0);
                                auto F1 = new TF1("grafico", frec, -20.0, 20.0, 0);
                                F2 -> SetLineColor(kBlue+2);
                                F1 -> SetLineColor(kRed+2);
                                F1 -> SetLineWidth(4);
                                F2 -> SetLineWidth(4);
                                F1 -> Draw();
                                F2 -> Draw("same");
                                canvas -> Update();
                                canvas -> WaitPrimitive();
                                gSystem -> ProcessEvents();

                                string simnao;
                                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                cin >> simnao;
                                if (simnao == "n") {
                                    pair<int, string> p;
                                    p.first = 0;
                                    p.second = nome;
                                    options(p);
                                    break;
                                }
                                while (simnao != "n" && simnao != "S") {
                                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                    cin >> simnao;
                                }

                            }
                            if (eqq2 == "3") {
                                double a, b, c;
                                cout << "Sendo que a expressão é tan(ax + b) + c, qual os valores de a, b, e c?" << endl;
                                cout << "Esta função só será demonstrada para -pi+b < x < pi-b" << endl;
                                cout << "a --> ";
                                cin >> a;
                                cout << "b --> ";
                                cin >> b;
                                cout << "c --> ";
                                cin >> c;
       
                                
                                auto frec = [a, b, c](double * x, double * par) {
                                    return tan((a * x[0]) + b) + c;
                                };

                                auto frec2 = [](double * x, double * par) { //eixo xx
                                    return x[0] * 0.0;
                                };

                                auto F2 = new TF1("eixo dos zeros", frec2, -100, 100, 0);
                                auto F1 = new TF1("grafico", frec, -M_PI+0.001+b, M_PI-0.001-b, 0);
                                F2 -> SetLineColor(kBlue+2);
                                F1 -> SetLineColor(kRed+2);
                                F1 -> SetLineWidth(4);
                                F2 -> SetLineWidth(4);
                                F1 -> Draw();
                                F2 -> Draw("same");
                                canvas -> Update();
                                canvas -> WaitPrimitive();
                                gSystem -> ProcessEvents();

                                string simnao;
                                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                cin >> simnao;
                                if (simnao == "n") {
                                    pair<int, string> p;
                                    p.first = 0;
                                    p.second = nome;
                                    options(p);
                                    break;
                                }
                                while (simnao != "n" && simnao != "S") {
                                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                    cin >> simnao;
                                }
                            }

                        }
                        else {
                            cout << "Input inválido =(" << endl;
                        }

                    }
                    if (eqq == "3") {
                        string eqq2;
                        cout << "Deseja visualizar o gráfico de uma função exponencial ou logarítmica?" << endl;
                        cout << "--" << endl;
                        cout << "   1) Exponencial" << endl;
                        cout << "--" << endl;
                        cout << "   2) Logarítmica" << endl;
                        cout << "--> ";
                        cin >> eqq2;
                        if (eqq2 == "1" || eqq2 == "2") {
                            if (eqq2 == "1") {
                                double a, b, c;
                                cout << "A expressão tem o formato a + e^(bx + c); quais os valores de a, b e c?" << endl;
                                cout << "a --> ";
                                cin >> a;
                                cout << "b --> ";
                                cin >> b;
                                cout << "c --> ";
                                cin >> c;

                           
                                
                                
                                auto frec = [a, b, c](double * x, double * par) {
                                    return a + exp((b * x[0]) + c);
                                };

                                auto frec2 = [](double * x, double * par) { //eixo xx
                                    return x[0] * 0.0;
                                };

                                auto F2 = new TF1("eixo dos zeros", frec2, -100, 100, 0);
                                auto F1 = new TF1("grafico", frec, -20.0, 20.0, 0);
                                F2 -> SetLineColor(kBlue+2);
                                F1 -> SetLineColor(kRed+2);
                                F1 -> SetLineWidth(4);
                                F2 -> SetLineWidth(4);
                                F1 -> Draw();
                                F2 -> Draw("same");
                                canvas -> Update();
                                canvas -> WaitPrimitive();
                                gSystem -> ProcessEvents();

                                string simnao;
                                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                cin >> simnao;
                                if (simnao == "n") {
                                    pair<int, string> p;
                                    p.first = 0;
                                    p.second = nome;
                                    options(p);
                                    break;
                                }
                                while (simnao != "n" && simnao != "S") {
                                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                    cin >> simnao;
                                }

                            }
                            if (eqq2 == "2") {

                                double a, b, c;
                                cout << "A expressão tem o formato a + log(bx + c); quais os valores de a, b e c?" << endl;
                                cout << "a --> ";
                                cin >> a;
                                cout << "b --> ";
                                cin >> b;
                                cout << "c --> ";
                                cin >> c;

                       
                                
                                
                                auto frec = [a, b, c](double * x, double * par) {
                                    return a + log((b * x[0]) + c);
                                };

                                auto frec2 = [](double * x, double * par) { //eixo xx
                                    return x[0] * 0.0;
                                };

                                auto F2 = new TF1("eixo dos zeros", frec2, -100, 100, 0);
                                auto F1 = new TF1("grafico", frec, -c + 0.0001, 20.0, 0); //dominio de log
                                F2 -> SetLineColor(kBlue+2);
                                F1 -> SetLineColor(kRed+2);
                                F1 -> SetLineWidth(4);
                                F2 -> SetLineWidth(4);
                                F1 -> Draw();
                                F2 -> Draw("same");
                                canvas -> Update();
                                canvas -> WaitPrimitive();
                                gSystem -> ProcessEvents();

                                string simnao;
                                cout << "\nDeseja realizar mais alguma operação? (S/n) --> ";
                                cin >> simnao;
                                if (simnao == "n") {
                                    pair<int, string> p;
                                    p.first = 0;
                                    p.second = nome;
                                    options(p);
                                    break;
                                }
                                while (simnao != "n" && simnao != "S") {
                                    cout << "Input inválido, por favor repita o que deseja (S/n) --> ";
                                    cin >> simnao;
                                }
                            }
                        }
                        else {
                            cout << "Input inválido =(" << endl;
                        }

                    }
                }
                else {
                    cout << "Input inválido, por repita o que deseja =(" << endl;
                }

            }
        }
        else {
            cout << "\n--ERROR--" << endl;
            cout << "Pedimos desculpa mas esse input não é válido =( Tente novamente" << endl;
            cout << "--ERROR--\n" << endl;
        }
    }
}