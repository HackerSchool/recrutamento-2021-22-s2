#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <stdlib.h>
#include <vector>
using namespace std;

class Login
{
public:
    string username;
    string password;
    string password2;

    void hello()
    {
        cout << "> Hello, " << username << endl;
    };

    string getCredentials()
    {
        ifstream Data("data.txt");
        string login;
    
        while(getline(Data, login))
        {
            cout << "------------------------------------------------------\n";
            cout << "> Username: \n";
            cin >> username;   
            cout << "> Password: \n";
            cin >> password; 
            cout << "-------------------------------------------------------\n"; 
            string data = username + " " + password;
            if (login != data)
            {
                cout << "Your credentials do not exist, yet. Try Registiring!\n";
                break;
            }  
            else if (login ==  data)
            {
                break;
            }
        }

        return username, password;
    };

    string regist()
    {
        cout << "------------------------------------------------------ \n";
        cout << "> Set an Username and a Password for your account. \n";
        
        do{
            cout << "> Username: \n";
            cin >> username;
            if (username.length() >= 20){
                cout << "Your password is too long.\n";
            }
        }while (username.length() >= 20);

        do{
            cout << "> Password: \n";
            cin >> password; 
            cout << "> Confirm Password: \n";
            cin >> password2;
        
            if (!(password2 == password))
            {
                cout << "--------------------------------------------------\n";
                cout << "> Your passwords don't match. \n> Try again. \n";
                cout << "--------------------------------------------------\n";
            }
            else if (password2 == password)
            {
                cout << "--------------------------------------------------\n";
                cout << "> You are registered!\n> Restart and login!\n";
                cout << "--------------------------------------------------\n";
                cout << "> Your credentials are: \n";
                cout << "> Username: " << username << endl;
                cout << "> Password: " << password << endl;
                cout << "--------------------------------------------------\n";
            }
        }while(!(password2 == password));

        return username, password;
    };

    void changePassword(string username2, string oldPassword)
    {
        username2 = username;
        
        string data, newdata, login;
        string newPassword;
        string result;
        cout << "-------------------------------------------------\n";
        cout << "Nem Password:\n";
        cin >> newPassword;

        fstream Data("data.txt", ios::app);
        newdata = username2 + " " + newPassword;
        Data << "\n" << newdata;

        /* !!! FALTA APAGAR CREDENCIAIS ANTIGAS !!!
        data = username2 + " " + password;
        oldPassword = password;
        while(getline(Data, login))
        {
            if (login == data)
            {            
                result = remove(const char*_"data.txt");
            }
                    
        } */

        Data.close();      
    };

    string menu2()
    {
        string task2;
        cout << "----------------------------------------------------\n";
        cout << "> What would you like to do: \n (Write the number of your option)\n";
        cout << " > (1) Change Password  \n > (2) App \n > (3) Logout \n";
        cin >> task2;

        return task2;
    };

    string menu1()
    {
        string task1;
        cout << "> What would you like to do: \n (Write the number of your option)\n"; 
        cout << " > (1) Login \n > (2) Register \n > (3) Leave \n";
        cin >> task1;

        return task1;
    }
};

void app(){
    string userAnswer;
    string userAnswer2;
    string botAnswer;
    vector<string> botAnswers;
    ifstream answers("chatBot.txt");

    //contar o total de linhas
    int total = 0;
    while(getline(answers,botAnswer))
    {
       total++; 
    // Method to Convert a Char to a String.
    botAnswers.push_back(botAnswer);  
    }

    cout << "-----------------------------------------------\n";
    cout << "> Bem Vind@ ao TrocaPaços! \n";
    cout << "> Vamos ver quem confuz quem! \n";
    cout << "> (Despede-te com um: adeus)\n";
    
    do{
        //receber input to user
        getline(cin, userAnswer);
        //escolher frase aleatória do ficheiro chatBot.txt
        // escolhe um numero aleatorio entre 0 e o numero de linhas do ficheiro
        int random = rand()%total;
        //imprime a linha referente ao numero aleatório dado anteriormente
        cout << "> " << botAnswers[random] << endl;
    }while (!(userAnswer == "adeus"));
};

int main()
{
string task1, task2;
string username, password, password2; 
string login, data;
Login credentials;

task1 = credentials.menu1();

if (task1 == "1")
{
    username, password = credentials.getCredentials();

    //check if combinations exists in database (data.txt)
    //...
    data = credentials.username + " " + credentials.password;
    ifstream Data("data.txt");
    
    while(getline(Data, login))
    {
        if (login == data)
        {            
            credentials.hello();
            
            menu2: 
                task2 = credentials.menu2(); 
                if (task2 == "1"){
                    credentials.changePassword(username, password);
                    goto menu2;
                }         
                else if (task2 == "2"){
                    cout << "-----------------------------------------------------------\n";
                    cout << "> Have fun! \n";
                    app();

                }
                else{
                    cout << "-----------------------------------------------------------\n";
                    cout << "> Bye! \n";
                    cout << "-----------------------------------------------------------\n";
                }
            
            
            break;
        }
                  
    }

    Data.close();
}
else if (task1 == "2")
{

    username, password = credentials.regist();

    //opens, writes and reads the data.txt file
    //ios::app = The Append mode. The output sent to the file is appended to it.
    fstream Data("data.txt", ios::app);

    //add new registration to database (data.txt)
    data = credentials.username + " " + credentials.password;
    Data << "\n" << data;

    //Why do we close the file? It is considered good practice, and it can clean up unnecessary memory space.
    Data.close();

}
else if (task1 == "3")
{
    cout << "> Bye! \n";
}

return 0;

}