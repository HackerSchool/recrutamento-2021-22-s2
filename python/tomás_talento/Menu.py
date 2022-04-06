import chatbot
import tictactoe as ttt

class Menu():
    
    def __init__(self, name, options):
        self.name = name
        self.options = options
        
    def write(self, user, passs):
        file = open("programa.txt", 'a')
        file.write(user + ' - ' + passs + '\n')
        file.close()
        
    def read(self, user):
        file = open("programa.txt", 'r')
        passss = ""
        for line in file:
            user_iter = line.split(' - ')[0]
            if user == user_iter:
                passs = line.split(' - ')[1]
                passss = passs.split('\n')[0]
                break
        file.close()
        return passss
    
    def change_pass(self, user):
        file = open("programa.txt", 'r')
        data = file.readlines()
        new_passs = input("Enter your new password:\n")
        for i in range(len(data)):
            user_iter = data[i].split(' - ')[0]
            if user_iter == user:
                data[i] = user + ' - ' + new_passs +'\n'
                break
        #print (data)
        file = open("programa.txt", 'w')
        file.writelines(data)
        file.close()


    def register(self):
        print(self.name, '''Register algo no seguinte formato:
              identificador - conteudo
              ''')
        user = input("User name:\n")
        test = self.read(user)
        if test != "":
            print("username already used")
        else:
            passs = input("New password:\n")
            self.write(user, passs)
            
    def login(self):
        user = input("User name:\n")
        test = self.read(user)
        if test == "":
            print("user not found; try again")
            return False
        else:
            passs = input("Password:\n")
            ##print(self.read(user))
            if self.read(user)==passs:
                self.name = user
                return True
            else:
                print("Incorrect password, try again!")
                return False
                
    def options_f(self):
        print("Options:\n")
        i = 1
        for option in self.options:
            print(option + " (" + str(i) + ")\n")
            i+=1
        choice = int(input("Type de number of the desired action:\n")) - 1
        return self.options[choice]
    
def main():
    open("programa.txt", 'a+').close()
    
        
    menu1 = Menu('start_menu',["Login", "Register", "Exit"])
    menu2 = Menu('app_menu',["Tic Tac Toe", "Chat Bot", "Change password", "Logout"])
    current_menu = 1
    
    while current_menu == 1:
        nextaction = menu1.options_f()
        if nextaction == "Login":
            acess = menu1.login()
            if acess==False:
                current_menu = 1
            else:
                current_menu = 2
                menu2.name = menu1.name
                menu1.name = 'start_menu'
                
                while current_menu == 2:
                    nextaction = menu2.options_f()
                    if nextaction == "Change password":
                        menu2.change_pass(menu2.name)
                        
                    elif nextaction == "Logout":
                        current_menu = 1
                        
                    elif nextaction == "Chat Bot":
                        menu_chatbot = Menu('Chat Bot',["Write","Exit"])
                        current_menu = 3
                        while current_menu == 3:
                             nextaction = menu_chatbot.options_f()
                             if nextaction == "Exit":
                                 current_menu = 2
                             elif nextaction == "Write":
                                 print("--------------------------------------------")
                                 question = input("Ask me something... \n")
                                 chatbot.generate_answer(question)
                                 print("\n--------------------------------------------\n")
                                 
                    elif nextaction == "Tic Tac Toe":
                        menu_ttt = Menu('Tic Tac Toe',["Play","Exit"])
                        current_menu = 3
                        while current_menu == 3:
                            nextaction = menu_ttt.options_f()
                            if nextaction == "Exit":
                                current_menu = 2
                            else:
                                input("To make your play type the number of the row, followed by a comma, and then the column number. Ex: 1,2 \nTap anything to continue:")
                                print("--------------------------------------------")
                                ttt.ttt()
                                print("--------------------------------------------\n")
                                
                
                
        elif nextaction == "Register":
            menu1.register()
        else:
            current_menu = 0
            

main()