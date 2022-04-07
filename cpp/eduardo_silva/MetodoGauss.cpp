#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include "startFuncs.h"
#include <vector>
#include <algorithm>
#include <complex>
#include <Eigen/Dense>

using namespace std;

void mGauss(Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> &A, Eigen::Matrix<double, Eigen::Dynamic, 1> &b) {
    
    vector<pair<int, int>> v_l;
    for (int y = 0; y < A.rows(); y++) {
        pair<int, int> p; //pair with i=0 --> first element != 0 and i=1 --> number of the line
        //so pair(1, 3) means that in row 4 the 2 element is the first != 0
        p.second = y;
        int j = 0;
        while (j < A.cols()) {
            if (A(y, j) != 0.0) {
                p.first = j;
                v_l.push_back(p);
                break;
            }
            j++;
        }
    }

    sort(v_l.begin(), v_l.end()); //ordem das linhas certas com o primeiro elemento

    vector<int> linhas; //da a ordem das linhas correta
    for (auto e: v_l) {
        linhas.push_back(e.second);
    }

    vector<double> vcct;
    vector<vector<double>> valores; //vetor com as os valores das (linhas por ordem)
    for (auto e: linhas) {
        vector<double> lin;
        for (int i = 0; i < A.cols(); i++) {
            double h = A(e, i);
            lin.push_back(h);
        }
        double p = b(e, 0);
        vcct.push_back(p);
        valores.push_back(lin);
    }

    for (int m = 0; m < A.rows(); m++){
        for (int y = 0; y < A.cols(); y++){
            vector<double> lin = valores[m];
            double hj = lin[y];
            A(m, y) = hj;
        }
        b(m, 0) = vcct[m];
    }




    //metodo em si 
    if (A.rows() != A.cols()) {
        cout << "ERRO --> A matriz não é quadrada" << endl;
    }
    else {
    
        for (int pivot = 0; pivot < A.rows() - 1; pivot++) {
            for (int k = pivot + 1; k < A.rows(); k++) {
                double dif = A(k, pivot) / A(pivot, pivot);
                for (int i = 0; i < A.cols(); i++) {
                    double sub;
                    sub = A(k, i) - dif * A(pivot, i);
                    A(k, i) = sub;
                }
                double cst;
                cst = b(k, 0) - dif * b(pivot, 0);
                b(k, 0) = cst;
            }
        }

		//forma de ficar 0 em baixo da diagonal e nao 3 * 10 ^-15
		for (int m = 0; m < A.rows(); m++) {
			for (int n = 0; n < A.cols(); n++) {
				if (n < m) {
					A(m, n) = 0.0;
				}
			}
		}
    }

}