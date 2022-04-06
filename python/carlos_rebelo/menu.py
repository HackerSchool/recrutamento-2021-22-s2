# coding=utf-8
from login import Login
from register import Register
from tictactoe import TicTacToe
from calculator import Calculator

class Menu():
    '''
    Classe que define o menu inicial, com as opções de Login, registo, saída, mudança de password e apps
    '''
    def __init__(self):
        pass

    #Login - usar script à parte com as funções necessárias
    def make_login(self):
        while(1):
            username = input("Username: ")
            password = str(input("Password: "))
            l = Login(username, password)
            #Verificar se o user existe
            teste = l.check_user()
            #Caso exista, prosseguir com o código
            if teste == 1:
                print("\nBem vindo/a de novo: \n" + username)
                break
            #Se não existir, mostrar mensagem de erro
            else:
                print("Utilizador não encontrado ou password incorreta, tente novamente")
                continue

    #Registar - usar script à parte
    def make_register(self):
        while(1):
            fazer_continue = 0

            username = input("Username: ")

            db = open("database.txt", "r")

            #Caso o user já exista na db
            for line in db:
                identificador = line.split(', ')[0]
                if username == identificador:
                    print("Username já usado")
                    fazer_continue = 1
                    break

            db.close()
            if fazer_continue == 1:
                continue

            password = str(input("Password: "))
            password_conf = str(input("Confirme a password: "))

            if password != password_conf:
                print("As passwords não coincidem, por favor tente de novo")
                continue
            elif len(password) <= 6:
                print("Password muito curta, tem de ter pelo menos 7 caracteres")
                continue
            else:
                r = Register(username, password)
                r.create_user()
                break

    #Menu de login - mudar a password
    def password_change_menu(self):
        while(1):
            print("\n Confirme as suas credenciais, por favor")
            username = input("Username: ")
            password = str(input("Password: "))
            l = Login(username, password)
            #Verificar se o user existe
            teste = l.check_user()
            #Caso exista, prosseguir com o código
            if teste == 1:
                while(1):
                    nova_pass = input("Introduza a nova password: ")
                    nova_pass_confirm = input("Confirmar nova password: ")
                    if nova_pass == nova_pass_confirm:
                        l.change_password(nova_pass)
                        print("Password alterada com sucesso!")
                        break
                    else:
                        print("Passwords não coincidem!")
                        continue
                break
            #Se não existir, mostrar mensagem de erro
            else:
                print("Utilizador não encontrado ou password incorreta, tente novamente")
                continue

    #----------------MENU APPS----------------
    def app_menu(self):
        #Escolha apos fazer login
        while(1):
            print('''
Aplicações disponíveis

1 - Tic-Tac-Toe
2 - Calculadora
3 - Mudar password
4 - Logout
''')
            escolha = input("O que deseja fazer? ")
            if escolha == "1":
                while(1):
                    tictactoe = TicTacToe()
                    modo_de_jogo = int(input("Qual o modo que deseja jogar? "))
                    if modo_de_jogo == 1:
                        print("Modo Multiplayer")
                        #Iniciar um jogo multiplayer
                        tictactoe.run_multiplayer()
                    elif modo_de_jogo == 2:
                        #Iniciar um jogo single player
                        print("Modo Singeplayer")
                        tictactoe.run_singleplayer()
                    elif modo_de_jogo == 3:
                        break
                    else:
                        print("Insira um modo válido")
            elif escolha == "2":
                calculadora = Calculator()
                while(1):
                    calculadora.simple_calculator()
                    escolha_cal = input("Deseja fazer mais alguma operação? \n1 - Sim \n2 - Não\n")
                    if escolha_cal != "1":
                        break
                    else: 
                        continue
            elif escolha == "3":
                self.password_change_menu()
            elif escolha == "4":
                break
            else:
                print("Escolha uma das opcoes sugeridas")

