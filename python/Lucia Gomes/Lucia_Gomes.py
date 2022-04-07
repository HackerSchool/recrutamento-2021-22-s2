import tkinter as tk
import random
import re


class Chatbot(object):
    def __init__(self):
        self.R_EATING = "Nao gosto de comer nada porwque so um bot lol"
        self.R_ADVICE = "Se fosse a ti ia maze a internet pesquisar o que acabaste de me dizer"

    def unknown(self):
        response = ["Podes dizer isso outra vez ? ",
                    "...",
                    "Parece me bom",
                    "O que é isso?"][random.randrange(4)]
        return response

    def message_probability(self, user_message, recognised_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        message_certainty = 0
        has_required_words = True

        for word in user_message:
            if word in recognised_words:
                message_certainty += 1

        percentage = float(message_certainty) / float(len(recognised_words))

        for word in required_words:
            if word not in user_message:
                has_required_words = False
                break

        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def check_all_messages(self, message):
        highest_prob_list = {}

        def response(bot_response, list_of_words, single_response=False, required_words=None):
            if required_words is None:
                required_words = []
            nonlocal highest_prob_list
            highest_prob_list[bot_response] = self.message_probability(message, list_of_words, single_response,
                                                                       required_words)


        # Responses -------------------------------------------------------------------------------------------------------
        response('Ola!', ['ola', 'wassup', 'hey', 'Hi', 'ola siri'], single_response=True)
        response('Adeus!', ['byebye', 'adeus', 'adeus siri', 'ate logo', 'ate nunca'], single_response=True)
        response('Eu tou bem e tu?', ['Como', 'estas'], required_words=['estas'])
        response('De nada', ['obrigada', 'thanks'], single_response=True)
        response('Obrigada', ['es', 'bue', 'fixe'], required_words=['fixe'])


        response(self.R_ADVICE, ['give', 'advice'], required_words=['advice'])
        response(self.R_EATING, [' what', 'you', 'eat'], required_words=['you', 'eat'])

        best_match = max(highest_prob_list, key=highest_prob_list.get)

        return self.unknown() if highest_prob_list[best_match] < 1 else best_match

    def get_response(self, user_input):

        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        response = self.check_all_messages(split_message)
        if response=='Adeus!':
            print("Adeus!")
            exit(0)

        return response


class Tictactoe(object):
    def __init__(self,gameRunning):
        self.gameRunning = gameRunning
        self.winner = None
        self.currentPlayer = "X"



    def printBoard(self,board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])



    def playerInput(self,board):
        try:
            inp = int(input("Select a spot 1-9: "))
            try:
                if board[inp-1] == "-":
                    board[inp-1] = self.currentPlayer
                else:
                    print("Oops player is already at that spot.")
            except IndexError:
                print("Input Invalid")
                exit(0)
        except ValueError:
            print("Invalid input")



    def checkHorizontle(self,board):
        global winner
        if board[0] == board[1] == board[2] and board[0] != "-":
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != "-":
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != "-":
            winner = board[6]
            return True

    def checkRow(self,board):
        global winner
        if board[0] == board[3] == board[6] and board[0] != "-":
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != "-":
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != "-":
            winner = board[3]
            return True


    def checkDiag(self,board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != "-":
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[4] != "-":
            winner = board[2]
            return True


    def checkIfWin(self,board):
        global gameRunning
        if self.checkHorizontle(board):
            self.printBoard(board)
            print(f"The winner is {winner}!")
            gameRunning = False

        elif self.checkRow(board):
            self.printBoard(board)
            print(f"The winner is {winner}!")
            gameRunning = False

        elif self.checkDiag(board):
            self.printBoard(board)
            print(f"The winner is {winner}!")
            gameRunning = False


    def checkIfTie(self,board):
        if "-" not in board:
            self.printBoard(board)
            print("It is a tie!")
            self.gameRunning = False



    def switchPlayer(self):
        if self.currentPlayer == "X":
            self.currentPlayer = "O"
        else:
            self.currentPlayer = "X"


    def computer(self,board):
        while self.currentPlayer == "O":
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"
                self.switchPlayer()


class Calculator(object):
    def __init__(self):
        self.calculation = ""

    def calculator(self,symbol):
        self.calculation += str(symbol)
        text_result.delete(1.0,"end")
        text_result.insert(1.0,self.calculation)

    def evaluate_calc(self):
        try:
            self.calculation= str(eval(self.calculation))
            text_result.delete(1.0,"end")
            text_result.insert(1.0,self.calculation)
        except:
            self.clear_field()
            text_result.insert(1.0,"Error")

    def clear_field(self):
        self.calculation = ""
        text_result.delete(1.0,"end")


class Login(object):

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def register(self):
        db = open("database.txt","r")
        self.username = input("Create username")
        self.password = input("Create password")
        password1 = input("Confirm password")
        d =[]
        f=[]
        for i in db:
            a,b= i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d,f))
        print(data)
        if self.password != password1:
            print("password dont match")
            self.register()
        else:
            if self.username in db:
                print("username exists")
                self.register()
            else:
                db = open("database.txt","a")
                db.write(self.username + ","+ self.password)
                print("success!")

    def Access(self):
        db = open("database.txt", "r")
        self.username = input("Username")
        self.password = input("Password")

        if not len(self.username or self.password) < 1:
            d =[]
            f=[]
            for i in db:
                a,b= i.split(",")
                b = b.strip()
                d.append(a)
                f.append(b)
            data = dict(zip(d,f))

            try:
                if data[self.username]:
                    try:
                        if self.password == data[self.username]:
                            print("Login success")
                            print("Ola",self.username)
                        else:
                            print("Incorrecto")
                            self.Access()
                    except:
                        print("Incorreto ")
                        self.Access()
                else:
                    print("Username nao existe")
                    self.Access()
            except:
                print("Login Error")
                exit(0)

    def change_password(self):
        passwordnew = input("Insira a nova palavra passe")
        self.password = input("Insira a antiga password")
        self.username = input("Insira o utilizador")
        db = open("database.txt", "r")
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        try:
            if data[self.username]:
                if self.password == data[self.username]:
                    self.password = passwordnew
                    print("Nova password : " + self.password)
                    db.write(self.username + "," + self.password)
                else:
                    print("Password inválida")
            else:
                print("Username nao existe")
        except:
            print("O username nao existe")

gameRunning=True
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
cb = Chatbot()
t =Tictactoe(gameRunning)
l= Login()
c = Calculator()
root = tk.Tk()
print("Bem vindo")
option = ""
opt = ""
while option != "0":
    print("0.Sair")
    print("1.Login")
    print("2.Registar")
    print("3.Alterar password")
    option = input("Qual opcao?")
    if option == "1":
        l.Access()
        while opt != "0":
            print("0.Sair")
            print("1.Calculadora")
            print("2.ChatBot")
            print("3.Tictactoe")
            opt = input("Qual opcao?")
            if opt == "1":
                root.geometry("300x275")

                text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
                text_result.grid(columnspan=5)

                btn_1 = tk.Button(root, text="1", command=lambda: c.calculator(1), width=5, font=("Arial", 14))
                btn_1.grid(row=2, column=1)
                btn_2 = tk.Button(root, text="2", command=lambda: c.calculator(2), width=5, font=("Arial", 14))
                btn_2.grid(row=2, column=2)
                btn_3 = tk.Button(root, text="3", command=lambda: c.calculator(3), width=5, font=("Arial", 14))
                btn_3.grid(row=2, column=3)
                btn_4 = tk.Button(root, text="4", command=lambda: c.calculator(4), width=5, font=("Arial", 14))
                btn_4.grid(row=3, column=1)
                btn_5 = tk.Button(root, text="5", command=lambda: c.calculator(5), width=5, font=("Arial", 14))
                btn_5.grid(row=3, column=2)
                btn_6 = tk.Button(root, text="6", command=lambda: c.calculator(6), width=5, font=("Arial", 14))
                btn_6.grid(row=3, column=3)
                btn_7 = tk.Button(root, text="7", command=lambda: c.calculator(7), width=5, font=("Arial", 14))
                btn_7.grid(row=4, column=1)
                btn_8 = tk.Button(root, text="8", command=lambda: c.calculator(8), width=5, font=("Arial", 14))
                btn_8.grid(row=4, column=2)
                btn_9 = tk.Button(root, text="9", command=lambda: c.calculator(9), width=5, font=("Arial", 14))
                btn_9.grid(row=4, column=3)
                btn_0 = tk.Button(root, text="0", command=lambda: c.calculator(0), width=5, font=("Arial", 14))
                btn_0.grid(row=5, column=2)

                btn_plus = tk.Button(root, text="+", command=lambda: c.calculator("+"), width=5, font=("Arial", 14))
                btn_plus.grid(row=2, column=4)
                btn_minus = tk.Button(root, text="-", command=lambda: c.calculator("-"), width=5, font=("Arial", 14))
                btn_minus.grid(row=3, column=4)
                btn_multp = tk.Button(root, text="*", command=lambda: c.calculator("*"), width=5, font=("Arial", 14))
                btn_multp.grid(row=4, column=4)
                btn_divide = tk.Button(root, text="/", command=lambda: c.calculator("/"), width=5, font=("Arial", 14))
                btn_divide.grid(row=5, column=4)
                btn_resto = tk.Button(root, text="%", command=lambda: c.calculator("%"), width=5, font=("Arial", 14))
                btn_resto.grid(row=6, column=4)

                btn_open = tk.Button(root, text="(", command=lambda: c.calculator("("), width=5, font=("Arial", 14))
                btn_open.grid(row=5, column=1)
                btn_close = tk.Button(root, text=")", command=lambda: c.calculator(")"), width=5, font=("Arial", 14))
                btn_close.grid(row=5, column=3)
                btn_equal = tk.Button(root, text="=", command=c.evaluate_calc, width=5, font=("Arial", 14))
                btn_equal.grid(row=6, column=3)
                btn_clear = tk.Button(root, text="C", command=lambda: c.clear_field(), width=5, font=("Arial", 14))
                btn_clear.grid(row=6, column=1, columnspan=2)
                root.mainloop()
            elif opt == "2":
                while True:
                    print('Bot: ' + cb.get_response(input('You: ')))
            elif opt == "3":
                while gameRunning == True:
                    t.printBoard(board)
                    t.playerInput(board)
                    t.checkIfWin(board)
                    t.checkIfTie(board)
                    t.switchPlayer()
                    t.computer(board)
                    t.checkIfWin(board)
                    t.checkIfTie(board)
            elif opt == "0":
                    exit(0)
            else:
                    print("Please enter a valid parameter, this is case-sensitive")
    elif option == "2":
        l.register()
    elif option == "3":
        l.change_password()
    elif option=="0":
            exit(0)
            print("Volte sempre")
    else:
            print("Please enter a valid parameter, this is case-sensitive")







