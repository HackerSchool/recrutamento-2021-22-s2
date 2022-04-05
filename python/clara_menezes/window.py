import ola
import os.path
import bot1
import tictactoe
import tictactoe_random
import fileinput
import sys
import requests
from tkinter import *
import time

class Utilizador:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        
    def write(self):
        file = open("newdatabase.txt", 'a')
        file.write("\n"+self.username+","+self.password)
        file.close()

    def retrieve_pass(self):
        file = open("newdatabase.txt", "r")
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
        file = open("newdatabase.txt", 'r')
        for line in file:
            user = line.strip().split(",")[0]
            if self.username == user:
                return True
                break
        file.close()
        return False
    
        
    def newpass(self,newpass):
 
       file = open("newdatabase.txt", "r+")
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
     
class operations:
    
    def option1_login():
        global login_window
        login_window = Toplevel(mainwindow)

        login_window.title("Login Window")
        
        global login_message
        login_message = Label(login_window, text = "Enter your credentials.")
        login_message.pack()
        
        global user
        user = StringVar()
        global passw 
        passw = StringVar()
        
        global user_label
        user_label = Label(login_window, text = "Username:")
        user_label.pack()
        
        global entry_user
        entry_user = Entry(login_window, textvariable=user)
        entry_user.pack()
       
        global passw_label
        passw_label = Label(login_window, text = "Password:")
        passw_label.pack()
        
        global entry_passw
        entry_passw = Entry(login_window, textvariable=passw)
        entry_passw.pack()
        
        global loginbtt
        loginbtt = Button(login_window, text= "Login", command = operations.login)
        loginbtt.pack()
        
    def login():
        print("You pressed login button on login window")
        global u
        u = Utilizador(user.get(), passw.get())
       
        passQlbl= Label(login_window, text = "")    
        userQlbl=Label(login_window, text = "")
       
       
        if not os.path.exists("newdatabase.txt"): 
         
            userQlbl.config(text = "Username does not exist.")
            userQlbl.pack()
            
        elif u.user_exists():
            userQlbl.config(text = "Username is present in our database.")
            userQlbl.pack()
            
            if u.match(passw.get()):
                 
               
                for widgets in login_window.winfo_children():
                    widgets.destroy()

                title = u.username + "'s personal area"
                login_window.title(title)
                
                global welcomelbl
                welcomelbl = Label(login_window, text = "Welcome to your personal area!")
                welcomelbl.pack()
                
                
                
                global open_bot1btt
                open_bot1btt = Button(login_window, text = "Open BOT1", command = bot1.main)
                open_bot1btt.pack()
                
                global open_tictactoebtt
                open_tictactoebtt = Button(login_window, text = "Play TicTacToe 1v1", command = tictactoe.main)
                open_tictactoebtt.pack()

                global open_tictactoeranbtt
                open_tictactoeranbtt = Button(login_window, text = "Play TicTacToe vs PC", command = tictactoe_random.main)
                open_tictactoeranbtt.pack()
                
                global change_passwbtt
                change_passwbtt = Button(login_window, text = "Change Password", command = operations.change_password_btt)
                change_passwbtt.pack()
                
                global logoutbtt
                logoutbtt = Button(login_window, text="Logout", command = login_window.destroy)
                logoutbtt.pack()
                
                
            else:
                passQlbl  = Label(login_window, text = "Password is incorrect.")
                passQlbl .pack()
        else:  
            userQlbl = Label(login_window, text = "User does not exist.")
            userQlbl.pack()
    
    def change_password_btt():
        
        for widgets in login_window.winfo_children():
            widgets.pack_forget()


        global changepassmessage
        changepassmessage = Label(login_window, text="Please enter a new password")
        changepassmessage.pack()
        
        global new_pass_tochange
        new_pass_tochange = StringVar()
        
        global new_pass_tochange_entry
        new_pass_tochange_entry = Entry(login_window,textvariable = new_pass_tochange)
        new_pass_tochange_entry.pack()
        
        global enterbtt
        enterbtt = Button(login_window, text = "Enter", command = operations.newpass_tochange_action)
        enterbtt.pack()
        
    def newpass_tochange_action():
        u.newpass(new_pass_tochange.get())
        
        new_pass_tochange_entry.pack_forget()
        enterbtt.pack_forget()
        changepassmessage.pack_forget()
            
 
       
        successchange = Label(login_window, text="Password has been changed successfully")
        successchange.pack()
       

        
        welcomelbl.pack()
        open_bot1btt.pack()
        open_tictactoebtt.pack()
        open_tictactoeranbtt.pack()
        change_passwbtt.pack()
        logoutbtt.pack()
    
    
    def option2_register(): 
        global register_window
        register_window = Toplevel(mainwindow)

        register_window.title("Register Window")
        
        register_message = Label(register_window, text = "Pick your username and a safe password.")
        register_message.pack()
        
        global user_to_register
        user_to_register = StringVar()
        global passw_to_register
        passw_to_register = StringVar()
        
        
        user_label = Label(register_window, text = "Username:")
        user_label.pack()
        
        entry_user = Entry(register_window, textvariable=user_to_register)
        entry_user.pack()
       
        
        passw_label = Label(register_window, text = "Password:")
        passw_label.pack()
        entry_passw = Entry(register_window, textvariable=passw_to_register)
        entry_passw.pack()
        
        
        registerbtt = Button(register_window, text= "Register", command = operations.register)
        registerbtt.pack()
        
    def register():
        print("You pressed the register button on the register window")
        u2 = Utilizador(user_to_register.get(), passw_to_register.get())
        
        if not os.path.exists("newdatabase.txt"):
             u2.write()
             if u2.user_exists() and u2.match(u.password):
                successlbl1 = Label(register_window, text = "User has been registered successfully!")
                successlbl1.pack()
                
        elif u2.user_exists():
                unavailbl = Label(register_window, text = "Username already exists in our database.")
                unavailbl.pack()
        
        else:    
            u2.write()
            if u2.user_exists() and u2.match(u2.password):
                successlbl2 = Label(register_window, text = "User has been registered successfully!")
                successlbl2.pack()
        
                

    
        
def main():
    global mainwindow 
    mainwindow= Tk()
    mainwindow.title("Main Window")

    first_message = Label(mainwindow, text = "Select an option:").grid(column=0, row=0)

    option1 = Button(mainwindow, text = "Login", command = operations.option1_login)
    option1.grid(column=2, row=2)
    option2 = Button(mainwindow, text = "Register", command = operations.option2_register) 
    option2.grid(column=4, row=2)
    option3 = Button(mainwindow, text = "Exit", command=mainwindow.destroy)
    option3.grid(column=6, row=0)


    mainwindow.mainloop()

     
        
     
        
if __name__ == "__main__":
    main()


    