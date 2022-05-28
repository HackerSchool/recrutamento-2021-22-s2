import ola
import os.path
import bot1
import fileinput
import sys
import tictactoe
import tictactoe_random

class Utilizador:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        
    def write(self):
        file = open("database.txt", 'a')
        file.write("\n"+self.username+","+self.password)
        file.close()

    def retrieve_pass(self):
        file = open("database.txt", "r")
        palavra_passe = ""
        for line in file:
            user = line.strip().split(",")[0]
            if self.username == user:
                palavra_passe = line.strip().split(",")[1]
                break
        file.close()
        return palavra_passe  
    
    def match(self, word):
        
        if self.retrieve_pass() == word:
            return True
        else:
            return False
    
    def user_exists(self): 
        file = open("database.txt", 'r')
        for line in file:
            user = line.strip().split(",")[0]
            if self.username == user:
                return True
                break
        file.close()
        return False
    
        
    def newpass(self,newpass):
 
       file = open("database.txt", "r+")
       contents=[]
       for line in file:
           if self.username in line:
               contents = contents + [self.username+","+newpass+"\n"]
           else:
               contents = contents + [line]
       file.seek(0)
       file.truncate(0)
       file.writelines(contents)
       file.close()
       print("Just tried to change your password")
        
               
               
#Classe auxiliar para quem esta a programar poder ver que usuarioas há, e permite ver se estao com
# caracteres invisiveis que estejam a levar a erros              
class Functions:
    def usuarios(file):
        file_open = open (file,"r+")
        usuarios =[]
        for line in file_open:
            usuarios = usuarios + [line.strip().split(",")[0]]
        return usuarios, len(usuarios[0])
            
   
    
        
def main():
  nome = input("What's your name?\n")
  print("\n")
  ola.ola(nome)

  while True:
    
    print('''\nSelect an option:
    1 - Login
    2 - Register 
    3 - Exit 
    ''')
    opção = input("Option: ")
    
    if opção == '1':
        print("\nPlease complete with your credentials:")
        user = input("Username: ")
        passw = input("Password: ")
        u = Utilizador(user, passw)
        
        if not os.path.exists("database.txt"): 
            print("Username does not exist. Select option 2 to register a new user.")
            
        elif u.user_exists():
            print("\nUsername is present in our database.")
            if(u.match(passw)):
                print("Password is correct.")
                print("Login was successful!")
                r=1
                
                while r==1:
    
                    print('''\nSelect an option:
                          1 - Change password
                          2 - Open "Bot1"
                          3 - Open "TicTacToe vs PC"
                          4 - Open "TicTacToe vs Friend"
                          5 - Logout and go back to main menu
                          ''')
                    option = input("Option: ")
                          
                    if option == "1":
                        
                        newpass = input("New Password:")
                        u.newpass(newpass)
                    elif option  == "2":
                        bot1.main()
                    elif option  == "3":
                        tictactoe_random.main()
                    elif option == "4":
                        tictactoe.main()
                    else:
                        r=0
            else:
                print("Wrong password.")
                          
        else:
            print("Username does not exist. Select option 2 to register a new user.")
            
   
            
    elif opção == '2':
        print("Pick your username and a safe password.")
        user = input("Username: ")
        passw = input("Password: ")
        u = Utilizador(user, passw)
        if not u.user_exists():
            u.write()
            if u.user_exists() and u.match(u.password):
                print("User has been registered successfully!")
        else:    
            print("\nUsername already exists in our database.")
            
        
         
    elif opção == '3':
      ola.adeus(nome)
      return False
  
    else:
      print("Please select a valid option.")
      
     
        
     
        
if __name__ == "__main__":
  f = Functions.usuarios("database.txt")
  print(f)
  main()
