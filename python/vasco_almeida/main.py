from calculator import calc as calculator
from tictactoe import window as tictactoewindow
from chatbot1 import chatbot_func as chatbot

class Menu_Principal():
    def __init__(self, cumps):
        self.cumps = cumps

    def write(self, username, password):
      ficheiro = open('base_dados.txt', 'a')
      ficheiro.write( username + ' - ' + password + '\n')
      ficheiro.close()

    def read(self, username):
      ficheiro = open('base_dados.txt', 'r')
      test = "0"
      for line in ficheiro:
        test_username = line.split(' - ')[0]
        if test_username == username:
          test= "1" 
      tamanho1 = len(username)
      username2 = "".join(username.split())
      tamanho2= len(username2)
      if tamanho1 != tamanho2 :
        test = "2"
      ficheiro.close()
      return test
           
    def changepassword(self, username) :
      ficheiro = open('base_dados.txt', 'r')

      while True:
          while True:
            new_password = input(" \n New Password: ")
            tamanho1 = len(new_password)
            new_password2 = "".join(new_password.split())
            tamanho2= len(new_password2)
            if tamanho1 != tamanho2 :
              print( "\n  ' ' is not valid character for your Password")
            else:
              break
          confirm_newpassword = input(" Confirm New Password: ")
          if confirm_newpassword == new_password :
           print("\n Password changed. Please login again to use an app \n")
           break
          else :
            print("\n Your passwords do not match! \n")

      count = 0
      for line in ficheiro:
              count += 1
              test_username = line.split(' - ')[0]
              if test_username == username:
                 delete_line = count

      ficheiro.close()     
      with open('base_dados.txt','r') as ficheiro:
              lines = ficheiro.readlines()

      ficheiro.close()  
      count = 0
      with open('base_dados.txt','w') as ficheiro:
              for line in lines:
                  count += 1
                  if count == delete_line:
                      ficheiro.write(username + ' - ' + new_password + '\n')
                  else:
                      ficheiro.write(line)
      ficheiro.close()  


    def quit_appmenu(self, username):
       while True:
          print(" \nAre you sure you want to quit? Y/n \n")
          opcao_q = input(" Option: ")
          if (opcao_q == 'Y') or (opcao_q == 'yes') or (opcao_q == 'y') or (opcao_q == 'Yes') or (opcao_q == 'YES'):
            print("\nSee you soon :) \n")
            exit()
          elif (opcao_q == 'n') or (opcao_q == 'no') or (opcao_q == 'N') or (opcao_q == 'No') or (opcao_q == 'NO'):
            self.app_menu(username)
            break
          else:
             print("\nPlease choose Y or n only!") 
           

      
    def app_menu(self, username):
        print('''
    Please choose one of the following:

    1 - Calculator
    2 - Tic-tac-toe
    3 - ChatBot
    4 - Change Password
    5 - Logout
      '''
            )
        option_app = input(" Option: ")
        if option_app == '1':
          calculator()
        if option_app == '2':
          tictactoewindow()
        if option_app == '3':
          chatbot()
        if option_app == '4':
          self.changepassword(username)
        if option_app == '5':
          self.quit_appmenu(username)
 


    def read_login (self, username, password):
      ficheiro = open('base_dados.txt', 'r')
      test = "0"
      for line in ficheiro:
        test_username = line.split(' - ')[0]
        test_password = line.split(' - ')[1]
        if test_username == username and password + '\n' == test_password :
          test = "1"
          break
      ficheiro.close()
      return test


    def login(self):
     while True :
       username = input("\n Username: ")
       password = input(" Password: ")
       login_test = self.read_login(username , password)
       if login_test == "1":
         self.app_menu(username)
         break
       else: 
           print ("\nLogin error. Please try again ")
       

    def register(self):
        ficheiro = open('base_dados.txt', 'a')
        while True :
          username = input(" \n Username: ")
          username_test = self.read(username)
          if username_test == "1" :
           print(" \nUsername taken. Please choose another one")
          if username_test == "2" :
           print(" \n Character ' ' is not allowed in your Username")
          if username_test == "0" :
            break
        while True:
             while True:
                password = input(" Password: ")
                tamanho1 = len(password)
                password2 = "".join(password.split())
                tamanho2= len(password2)
                if tamanho1 != tamanho2 :
                  print( "\n Character ' ' is not valid character for your password \n")
                else:
                  break

             confirm_password = input(" Confirm Password: ")
             if confirm_password == password :
              ficheiro.write(username + ' - ' + password + '\n')
              print("\n Account created with success.\n")
              ficheiro.close()
              break
             else :
              print("\n Your passwords do not match! \n")
   


    def quit(self):
      while True:
          print(" \nAre you sure you want to quit? Y/n \n")
          opcao_q = input(" Option: ")
          if (opcao_q == 'Y') or (opcao_q == 'yes') or (opcao_q == 'y') or (opcao_q == 'Yes') or (opcao_q == 'YES'):
            print("\nSee you soon :) \n")
            exit()
          elif (opcao_q == 'n') or (opcao_q == 'no') or (opcao_q == 'N') or (opcao_q == 'No') or (opcao_q == 'NO'):
              menu = Menu_Principal('''
    Please choose one of the following:

    1 - Login
    2 - Register
    3 - Quit
      ''')
              menu.escolha()
              break
          else:
             print("\nPlease choose Y or n only!") 


    def escolha(self):
      print(self.cumps)
      while True:
       opcao = input(" Option: ")
       if opcao == '1':
         menu.login()
         break
       if opcao == '2':
         menu.register()
         break
       if opcao == '3':
        menu.quit()
        break
       else:
         print( " \n Please choose 1, 2 or 3 only!\n ")



    def ler(self):
      print(self.cumps, '''\
      \nLer informação:
      Dando identificador mostra o conteúdo
      ''')
      identificador = input("Identificador:\n")
      conteúdo = self.read(identificador)
      if conteúdo == "":
        print("Não há registos com esse identificador")
      else:
        print("Conteúdo é:\n" + conteúdo)

if __name__ == "__main__":
    menu = Menu_Principal('''
    Welcome,
    Please choose one of the following:

    1 - Login
    2 - Register
    3 - Quit
      ''')
    menu.escolha()


      