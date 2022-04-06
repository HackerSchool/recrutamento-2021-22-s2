# HS Recruitment Project - Python - Pedro Sarnadas
import re
from os import system, name
from my_tictactoe import main_ai_player, main_2players
from my_calculator import simple_calculator


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

class MyMenu():
    def __init__(self):
        self.current_user = ""

    def write(self, user_data):
        file = open('user_data.txt', 'a')
        file.write(user_data + '\n')
        file.close()

    def read(self, user_name, mode):
    #mode -> returns user_name, password or content if mode is 0, 1 or 2
        file = open('user_data.txt', 'r')
        content_x = ""
        for line in file:
            user = line.split(' - ')[0]
            if user == user_name:
                content_x = line.split(' - ')[mode]
                break
        file.close()
        return content_x

    def register(self):
        clear()
        print('''\
              \n Register User in Format: \
              <User Name - Password>
              ''')
        user_data = input("\n")
        matched = re.match(".* - .*", user_data)
        if bool(matched):
            user = user_data.split(' - ')[0]
            test = self.read(user, 0)
            if test != "":
                print("Username already in use\n")
                input()
            else:
                self.write(user_data)
                print("User now registered\n")
                input()
        else:
            print("User Data Does Not Fit Format\n")
            input()

    def sign_in(self):
        clear()
        print('''\
                \n Log-in with format: \
                <Username - Password>
                ''')
        user_data = input()
        matched = re.match(".* - .*", user_data)
        if bool(matched):
            user = user_data.split(' - ')[0]
            word = user_data.split(' - ')[1]
            test = self.read(user, 0)
            if test != "":
                test2 = self.read(user, 1).strip("\n") #remove new line
                if word != test2:
                    print("Incorrect password!\n")
                    input()
                else:
                    print("Sign-in completed!\n")
                    input()
                    self.current_user = user;
            else:
                print("Incorrect username!\n")
                input()
        else:
            print("\n User data does not fit format\n")
            input()

    def log_out(self):
        self.current_user = ""

# Implements:
#   def set_user_name:
#   def set_password:
    def update_user_data(self, content, mode):
        content = content.split(' ')[0].strip("\n")
        with open("user_data.txt", "r") as f:
            # list of strings
            lines = f.readlines()
        if mode == 0:
            test = self.read(content, 0)
            if test != "":
                print("New username already in use!\n")
                input()
                return
        with open("user_data.txt", "w") as f:
            for line in lines:
                if line.split(' - ')[0].strip("\n") == self.current_user:
                    if mode == 0:
                        self.current_user = content
                    line = line.replace(line.split(' - ')[mode], content)
                    f.write((line.replace(line.split(' - ')[mode], content).strip("\n")) + "\n")
                    continue
                f.write(line)

    def get_user_name(self):
        print(self.current_user)

    # Implemented via read(..., mode)
    #   def get_password:

    def clear_user(self, user_name):                #Borrowed Code (Web)
        with open("user_data.txt", "r") as f:
            # list of strings
            lines = f.readlines()
        with open("user_data.txt", "w") as f:
            for line in lines:
                if line.split(' - ')[0].strip("\n") != user_name:
                    f.write(line)

    def upper_menu(self):
        order = ''
        while True:
            clear()
            print('''REGISTER - 1\
                LOGIN - 2\
                QUIT - 0 
                ''')
            order = input()
            order = order.strip("\n")
            if order.isdigit():
                if bool(int(order) > -1) and bool(int(order) < 3):
                    if bool(int(order) == 0):
                        break
                    elif bool(int(order) == 1):
                        self.register()
                    elif bool(int(order) == 2):
                        self.sign_in()
                        if self.current_user != "":
                            self.lower_menu()
                        self.log_out()
            else:
                print("Invalid Option\n")
        exit()

    def lower_menu(self):
        while True:
            clear()
            print("Current User: " + self.current_user)
            print('''CALCULATOR - 1\
                TIC-TAC-TOE - 2\
                CHATBOT (not implemented) - 3\n
                USER MENU - 4\
                LOG OUT - 0 
                ''')
            order = input()

            if order.isdigit():
                if bool(int(order) > -1) and bool(int(order) < 5):
                    if bool(int(order) == 0):
                        break
                    elif bool(int(order) == 1):
                        clear()
                        simple_calculator()
                    elif bool(int(order) == 2):
                        self.tic_tac_toe_menu()
                    elif bool(int(order) == 3):
                        #chatbot
                        a = 3
                    elif bool(int(order) == 4):
                        self.update_user_data_menu()
                        if self.current_user == "":
                            break
            else:
                print("Invalid Option\n")

    def tic_tac_toe_menu(self):
        while True:
            clear()
            print("Current User: " + self.current_user)
            print('''TIC-TAC-TOE OPTIONS:\n
                PVP - 1\
                PVE - 2\
                RETURN - 0 
                ''')
            order = input()
            if order.isdigit():
                if bool(int(order) > -1) and bool(int(order) < 3):
                    if bool(int(order) == 0):
                        break
                    elif bool(int(order) == 1):
                        main_2players()
                    elif bool(int(order) == 2):
                        main_ai_player()
            else:
                print("Invalid Option\n")

    def update_user_data_menu(self):
        while True:
            clear()
            print("Current User: " + self.current_user)
            print('''User Data Operations:\n
                CHANGE PASSWORD - 1\
                CHANGE USERNAME - 2\
                CLEAR USER - 3\
                RETURN - 0 
                            ''')
            op = input()
            if op.isdigit():
                if bool(int(op) > -1) and bool(int(op) < 4):
                    if bool(int(op) == 0):
                        return
                    elif bool(int(op) == 1):
                        # password change
                        print("New password:\n")
                        op = input()
                        op = op.strip("\n")
                        self.update_user_data(op, 1)
                    elif bool(int(op) == 2):
                        # name change
                        print("New username:\n")
                        op = input()
                        op = op.strip("\n")
                        self.update_user_data(op, 0)
                    elif bool(int(op) == 3):
                        self.clear_user(self.current_user)
                        self.log_out()
                        break
            else:
                print("Invalid Option\n")
                input()

if __name__ == "__main__":
    mine = MyMenu()
    mine.upper_menu()
    clear()