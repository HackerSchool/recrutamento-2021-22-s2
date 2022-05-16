# Bianca Fonseca 
import os
from calculadora import calculator

def str_nula(str):
    if len(str)<1:
        print("Soa-me demasiado curto!")
        return 1
    return 0

def weak_pass(password):
    letra = numero = outro = 0

    for i in range(len(password)):
        if(password[i].isdigit()):
            numero = numero + 1
        elif(password[i].isalpha()):
            letra = letra + 1
        else:
            outro = outro + 1
    
    if (numero<2 or outro<1 or letra<5):
        return 1
    else:
        return 0


class Utilizador:
    def __init__(self, nome, apelido, username, password, mail):
        self.nome = nome
        self.apelido = apelido
        self.username = username
        self.password = password
        self.mail = mail

lista=[]
f=open("database.txt", "r")
for line in f:
    lista.append(line.split())
f.close()

def registar():
    nome = input("Nome próprio: ")
    while str_nula(nome):
        nome = input("Nome próprio: ")
    
    apelido = input("Apelido: ")
    while str_nula(apelido):
        apelido = input("Apelido: ")

    username = input("Username: ")
    while str_nula(username):
        username = input("Username: ")

    for i in lista:
        while i[2] == username:
            print("Este username já está a ser usado. Escolhe outro.")
            username = input("Username: ")

    password = input("Password: ")
    while str_nula(password):
        password = input("Password: ")
    while weak_pass(password):
        print("Password fraca. A password deve ter, pelo menos, 2 números, 1 carácter especial e 5 letras.")
        password = input("Password: ")

    mail = input("E-mail: ")  
    while str_nula(mail):
        mail = input("E-mail: ")  

    for i in lista:
        while i[4] == mail:
            print("Este email está associado a outra conta.")
            mail = input("E-mail: ")

    user = Utilizador(nome, apelido, username, password, mail)
    f=open("database.txt", "a")
    f.write(nome+" "+ apelido+" "+ username+" "+ password+" "+ mail+"\n")
    f.close()
    a=[nome, apelido, username, password, mail]
    lista.append(a)
    print("Registo efetuado com sucesso!")
    return user


def newpassword(username, password):
    oldpass = input("Password antiga: ")
    while oldpass==password:
        newpass= input("Password nova: ")
        while weak_pass(newpass):
                print("Password fraca. A password deve ter, pelo menos, 2 números, 1 carácter especial e 5 letras.")
                newpass= input("Password nova: ")

        newpass1 = input("Confirma a password nova: ")

        while newpass == newpass1:
            while newpass==password:
                print("Esta password já foi usada.")
                newpass= input("Password nova: ")
                newpass1 = input("Confirma a password nova: ")
                if weak_pass(newpass):
                    print("Password fraca. A password deve ter, pelo menos, 2 números, 1 carácter especial e 5 letras.")
                    newpass= input("Password nova: ")
                    newpass1 = input("Confirma a password nova: ")

            for i in lista:
                if i[2] == username:
                    i[3] = newpass
                    print("A tua nova password já está prontinha a usar!")
                    f=open("database.txt", "w")
                    for i in lista:
                        f.write(i[0]+" "+i[1]+" "+ i[2]+" "+ i[3]+ " "+ i[4]+"\n")
                    f.close()
                    hackcalculate(username, password)
    
        else:
            print("As passwords não são iguais.")
    else:
        print("Password incorreta.")
        newpassword(username, password)


def hackcalculate(username, password):
    while 1:
        print("Opções: CALCULATOR | NEW PASSWORD | LOGOUT")
        opcao = input("- ")
        if opcao == "CALCULATOR":
            calculator()
        elif opcao == "NEW PASSWORD":
            newpassword(username, password)
        elif opcao == "LOGOUT":
            print("Sessão terminada com sucesso.")
            menu()
        else:
            print(opcao + "- UPSSS!! Esta opção não existe. Tenta outra vez.")


def login():
    j=0
    username = input("Username: ")
    for i in lista:
            if i[2] == username:
                password = input("Password: ")
                while(j<=2):
                    if i[3] == password:
                        print("Olá,",i[0], i[1]+"!")
                        hackcalculate(username, password)
                    else:
                        print("Password incorreta.")
                        if(j<2): 
                            password = input("Password: ")
                        j+=1
                if ((j==3) and (i[3] != password)):
                    print("Esqueceste-te da tua password? Não faz mal, mandámos-te um mail.")
                    menu()
            else:
                print("Username inválido.")
                login()


def menu():
    while 1:
        print("Bem-vindo(a) ao HackCalculate! Regista-te ou faz login.\nOpções: REGISTAR | LOGIN | SAIR")
        opcao = input("- ")
        if opcao == "REGISTAR":
            registar()
        elif opcao == "LOGIN":
            login()
        elif opcao == "SAIR":
            print("Vamos ter saudades. Volta rápido!")
            quit()
        else:
            print(opcao + "- UPSSS!! Esta opção não existe. Tenta outra vez.")


menu()

