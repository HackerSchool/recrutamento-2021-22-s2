#include <iostream>
#include <fstream>

using namespace std;

int main(){
    //create and open a text file
    ofstream MyFile("file.txt");

    //write to the file
    MyFile << "Username Password";

    //close the file
    MyFile.close();

}