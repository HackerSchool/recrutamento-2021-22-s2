#include <iostream>
#include <fstream>

using namespace std;

int main(){
    //create a new string, which is used to output the text file
    string myText;

    //read from the text file
    ifstream MyReadFile("data.txt");

    //use a while loop together with the getline() function to read the file line by line
    while (getline (MyReadFile, myText))
    {
        //output the text from the line in the text
        cout << myText << "\n";
    }
    //close the file
    MyReadFile.close();  
    
}
