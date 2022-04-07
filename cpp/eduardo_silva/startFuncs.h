#include <Eigen/Dense>
#include <Eigen/Core>

using namespace std;

std::string encrypt(std::string);

void registar();

std::pair<int, std::string> login();

void options(std::pair<int, std::string> &);

void calculadora(std::string);

int start();

void changepass(std::string);

void mGauss(Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> &, Eigen::Matrix<double, Eigen::Dynamic, 1> &);

void gJordan(Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> &, Eigen::Matrix<double, Eigen::Dynamic, 1> &);

void opstrings(std::string);