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

void gJordan(Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> &A, Eigen::Matrix<double, Eigen::Dynamic, 1> &b) {

    for (int i = 0; i < A.rows(); i++) { //making the pivots all 1
        b(i, 0) = b(i, 0) / A(i, i);
        A.row(i) = A.row(i) / A(i, i);
    }

    for (int m = A.rows() - 2; m > -1; --m) {
        //Eigen::Matrix<double, 1, Eigen::Dynamic> jg(A.rows());
        for (int h = A.rows() - 1; h > m; --h) {
            b(m,0) = b(m,0) - (b(h,0) * A(m, h));
            A.row(m) = A.row(m) - (A.row(h) * A(m, h));
        }
    }


} 