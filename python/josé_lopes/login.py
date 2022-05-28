import tkinter as tk
from tkinter import ttk
import calculator as clc
import matplotlib.pyplot as plt
from tkinter.messagebox import showerror, showwarning, showinfo

def loginCredentials(user, password):

  #print("Por favor introduza as suas credenciais")
  #user = input("Utilizador: ")
  #password = input("Password: ")
  userData = open("notUserData.txt", "r")

  for line in userData:
    if(line == (user + ' - ' + password + "\n")): #tenho de meter o /n senão as strings não são iguais

      userData.close()
      return True
  userData.close()


  return False
      
def loginRegister(user, password):
  #print("Login Register!")


  if(not checkUsername(user)):
    userData = open("notUserData.txt", "a")
    userData.write(user + ' - ' + password + "\n")
    userData.close()
    return True

  else:
    return False




def changePassword(user, newPassword):
  line_number = checkUsername(user)
  if(line_number):
    with open("notUserData.txt", "r") as userData:
      data = userData.readlines()

    if(user + " - " + newPassword + "\n" != data[line_number - 1]):
      data[line_number - 1] = user + " - " + newPassword + "\n"
      with open("notUserData.txt", "w") as userData:
        userData.writelines(data)

      #print("Password alterada com sucesso!")
      return True

    else:
      #print("A password não pode ser a mesma!")
      return False


#vai retornar a linha+1, se encontrar o username, False otherwise
def checkUsername(username):
  line_number = 1
  userData = open("notUserData.txt", "r")
  for line in userData:
    if (line.split(' - ')[0] == username):
      userData.close()
      return line_number
    line_number+= 1

  userData.close()
  return False



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('LOGIN COM APPS')

        window_width = 400
        window_height = 400

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        #help menu
        self.helpmenu = tk.Menu(self)
        self.new_item = tk.Menu(self.helpmenu, tearoff=0)
        self.new_item.add_command(label = "Help", command=lambda: self.help_clicked())
        self.new_item.add_command(label = "About", command = lambda: self.about_clicked())

        self.helpmenu.add_cascade(label = "Menu", menu = self.new_item)

        self.config(menu = self.helpmenu)

        #container principal com os frames
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)

        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.framenumber = 0
        self.frames = {}
        self.username = "tmp"


        for F in (LoginFrame, RegisterFrame, MudarPassFrame, clc.CalculadoraFrame, clc.EvalFrame, clc.MainMatrizFrame,
                  clc.MatrizSolverFrame, clc.PlotterFrame):

            #vou tentar guardar no mapa (dicionário?) as keys para os frames como strings para ser mais fácil falar entre ficheiros
            #Ex: str(F) = "<class '__main__.LoginFrame'>" -> strF = "LoginFrame"
            strF = str(F)[str(F).find(".") +1 : str(F).find('>')-1]

            frame = F(self.container, self)

            self.frames[strF] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.currentframe = "LoginFrame"
        self.change_frame("LoginFrame")

    def change_frame(self, cont):
        if(cont == "MainMenuFrame"):

          frame = MainMenuFrame(self.container, self)
          self.frames[cont] = frame
          frame.grid(row = 0, column = 0, sticky ="nsew")

        self.currentframe = cont
        frame = self.frames[cont]
        frame.tkraise()

    def user_get(self):
      return self.username

    def user_set(self, user):
      self.username = user
      print (self.username)

    def about_clicked(self):
      window = About(self)
      window.grab_set()

    def help_clicked(self):
      match(self.currentframe):
        case "LoginFrame":
          message = "- Para fazer login preencha as suas credenciais e clique Login \n- Se não tem conta clique Registar"

        case "MainMenuFrame":
          message = "- Para app calculadora, clique \"Calculadora\"\n- Para mudar a password, clique \"Mudar Password\"\n- Para mudar de conta, clique \"Log off\""

        case "EvalFrame":
          message = "- Intoduz a expressão que queres e clica \"Calcular\" para ter o resultado.\n- São permitidos os operadores +,-,*,^,/ bem como () e algumas funções giras \"arcos\", \"arsin\", \"arctan\",\"sin\", \"cos\", \"tan\", \"exp\", \"ln\", \"log\", \"sqrt\".\n -known errors: -1^2 = 1, \"pi\" e \"e\" ainda não funcionam."

        case "MatrizSolverFrame":
          message = "-Resolve o sistema matricial A*X = B.\n-Podes mudar o tamanho do sistema, em cima.\n-Preenche a matriz A e o Vetor B com os valores numéricos e clica \"Calcular\" para resolver."

        case "PlotterFrame":
          message = "-Introduz uma função de x (ex: 2*x+sqrt(x)+sin(1/(2*x))) e clica para obteres o plot da função."

        case "MudarPassFrame":
          message = "Introduz a nova password, não pode conter espaços nem ser igual à anterior."

        case "RegisterFrame":
          message = "Introduz um username e uma Password (não pode conter espaços) e clica \"Register\" para criar conta."

        case "CalculadoraFrame":
          message = "-Modo Clássico para avaliar expressões simples\n-Modo Matriz para resolver sistemas matriciais\n-Modo Plot para plot de funções R->R"
        case _:
          message = "Não deve ser muito complicado"

      showinfo(title='Help',message= message)


class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('ABOUT SECTION')

        window_width = 700
        window_height = 420

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        #container principal com os frames
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        #Expression
        self.explabel = ttk.Label(container, text = "Creador: José Lopes")
        self.explabel.grid(column=0, row=0, columnspan = 2)

        eu = tk.PhotoImage(file = 'resources/sexyme.png')
        imagelabel = ttk.Label(container, image = eu)
        imagelabel.image = eu
        imagelabel.grid(column = 0, row = 1, columnspan = 1, pady = 20)

        eu2 = tk.PhotoImage(file = 'resources/hotaction.png')
        imagelabel = ttk.Label(container, image = eu2)
        imagelabel.image = eu2
        imagelabel.grid(column = 1, row = 1, columnspan = 1)

        ty = tk.PhotoImage(file = 'resources/ty.png')
        imagelabel = ttk.Label(container, image = ty)
        imagelabel.image = ty
        #Botão de Agradecer
        self.obrigadoBt = ttk.Button(container, image = ty, text = 'Obrigado', compound=tk.LEFT, command = lambda: self.destroy())
        self.obrigadoBt.grid(column=0, row=5, columnspan = 2)






class LoginFrame (ttk.Frame):
  def __init__(self, container, controller):

    super().__init__(container)

    self.controler = controller
    self.helplabel = ttk.Label(self, text = "Por favor introduza as suas credenciais")
    self.helplabel.grid(column = 2, row = 0)
    #Input Username
    userlabel = ttk.Label(self, text = "Username")
    userlabel.grid(column=1, row=1)
    user = tk.StringVar()
    self.usertextbox = ttk.Entry(self, textvariable=user)
    self.usertextbox.grid(column=2, row=1)

    #Input Password
    self.passlabel = ttk.Label(self, text = "Password")
    self.passlabel.grid(column=1, row=2)
    password = tk.StringVar()
    self.passtextbox = ttk.Entry(self, textvariable=password, show = "*")
    self.passtextbox.grid(column=2, row=2)


    #Botão de Login
    self.loginBt = ttk.Button(self, text = 'Login', command = lambda : self.login_clicked(user.get(), password.get()))
    self.loginBt.grid(column=1, row=3)


    #Botão de Registar
    self.registBt = ttk.Button(self, text = 'Registar', command = lambda : controller.change_frame("RegisterFrame"))
    self.registBt.grid(column=1, row=5)


    #Botão de Saír
    self.sairBt = ttk.Button(self, text = 'Saír', command = lambda : self.quit())
    self.sairBt.grid(column=1, row=6, sticky='w')

    #self.pack()

  def login_clicked(self, user, password):
    if(loginCredentials(user, password)):
      #print("ACESSO CONCEDIDO")
      self.controler.user_set(user)
      self.controler.change_frame("MainMenuFrame")
    else:
      self.helplabel.config(text = "A autenticação falhou!")
      showerror(title='Login',message= "A autenticação falhou!")


class MainMenuFrame(ttk.Frame):
    def __init__(self, container, controler):

      super().__init__(container)
      self.container = container
      self.label = ttk.Label(self, text = "Welcome " + controler.user_get())
      self.label.grid(column=0, row=0, sticky='nsew')

      #Botão Calculadora

      self.calcBt = ttk.Button(self, text = 'Calculadora Lopes', command = lambda : controler.change_frame("CalculadoraFrame"))
      self.calcBt.grid(column=0, row=1, sticky='nsew')

      #Botão Mudar Password

      self.mudarPass = ttk.Button(self, text = 'Mudar Password', command = lambda : controler.change_frame("MudarPassFrame"))
      self.mudarPass.grid(column=0, row=2, sticky='nsew')

      #Botão de Logout
      self.logoutBt = ttk.Button(self, text = 'Log off', command = lambda : controler.change_frame("LoginFrame"))
      self.logoutBt.grid(column=0, row=15, sticky='nsew')

      #Botão de Saír
      self.sairBt = ttk.Button(self, text = 'Saír', command = lambda : self.quit())
      self.sairBt.grid(column=1, row=15, sticky='nsew')

    def update_label(self):
      self.label.config (text = "Welcome " + controler.user_get())

class RegisterFrame(ttk.Frame):
    def __init__(self, container, controler):

      super().__init__(container)

      self.controler = controler
      self.helplabel = ttk.Label(self, text = "Por favor introduza as suas novas credenciais")
      self.helplabel.grid(column = 2, row = 0)
      #Input Username
      userlabel = ttk.Label(self, text = "Username")
      userlabel.grid(column=1, row=1)
      user = tk.StringVar()
      self.usertextbox = ttk.Entry(self, textvariable=user)
      self.usertextbox.grid(column=2, row=1)

      #Input Password
      self.passlabel = ttk.Label(self, text = "Password")
      self.passlabel.grid(column=1, row=2)
      password = tk.StringVar()
      self.passtextbox = ttk.Entry(self, textvariable=password, show = "*")
      self.passtextbox.grid(column=2, row=2)


      #Botão de Register
      self.registBt = ttk.Button(self, text = 'Register', command = lambda : self.regist_clicked(user.get(), password.get()))
      self.registBt.grid(column=1, row=3)


      #Botão de Cancelar
      self.sairBt = ttk.Button(self, text = 'Cancelar', command = lambda : controler.change_frame("LoginFrame"))
      self.sairBt.grid(column=1, row=6, sticky='w')

      #self.pack()

    def regist_clicked(self, user, password):
      if(" " in password):
        self.helplabel.config(text = "Password não pode conter \" \"")
        showerror(title='Registo',message= "Password não pode conter \" \"!")

      elif(loginRegister(user, password)):
        #print("Conta Criada")

        self.controler.change_frame("LoginFrame")
        showinfo(title='Registo',message= "Registo efetuado com sucesso!")
      else:
        self.helplabel.config(text = "Username já existe!")
        showerror(title='Registo',message= "Username já existe!")

class MudarPassFrame(ttk.Frame):
    def __init__(self, container, controler):

      super().__init__(container)

      self.controler = controler
      self.helplabel = ttk.Label(self, text = "Por favor introduza a sua nova password")
      self.helplabel.grid(column = 2, row = 0)

      #Input Password
      self.passlabel = ttk.Label(self, text = "Password")
      self.passlabel.grid(column=1, row=2)
      self.password = tk.StringVar()
      self.passtextbox = ttk.Entry(self, textvariable=self.password, show = "*")
      self.passtextbox.grid(column=2, row=2)


      #Botão de Register
      self.registBt = ttk.Button(self, text = 'Mudar Password', command = lambda : self.mudarpass_clicked(self.password.get()))
      self.registBt.grid(column=1, row=3)


      #Botão de Voltar
      self.sairBt = ttk.Button(self, text = 'Voltar', command = self.voltar_clicked)
      self.sairBt.grid(column=1, row=6, sticky='w')

      #self.pack()

    def mudarpass_clicked(self, password):
      if(" " in password):
        self.helplabel.config(text = "Password não pode conter \" \"")

      elif(changePassword(self.controler.user_get(), password)):
        self.helplabel.config(text = "Password alterada com sucesso!")
        self.password.set("")
        showinfo(title='Password',message= "Password alterada com sucesso!")
        #self.controler.change_frame(MainMenuFrame)
      else:
        self.helplabel.config(text = "A password não pode ser a mesma!")
        showerror(title='Password',message= "A password não pode ser a mesma!")
    def voltar_clicked(self):

      #reset da box da password e da helplabel
      self.helplabel.config(text = "Por favor introduza a sua nova password")
      self.password.set("")

      #self.passtextbox.delete(0, len(self.password.get()))
      self.controler.change_frame("MainMenuFrame")



if __name__ == "__main__":
    app = App()
    app.mainloop()
