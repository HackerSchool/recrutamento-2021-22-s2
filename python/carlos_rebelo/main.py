# coding=utf-8
from menu import Menu

def main():
    #Introducao - fazer login (e registo, caso seja necessario)
    while(1):
        print("\nBem-vindo/a a loja de apps online".upper())
        m = Menu()
        print('''
1 - Login
2 - Registo
3 - Saida 
''')

        escolha = input("O que deseja fazer? ")
        #Fazer o Login/Registo
        if escolha == "1":
            m.make_login()
            #Escolher o login no menu
        elif escolha == "2":
            m.make_register()
            print("Por favor, faca login com as novas credenciais")
            continue
            #Escolher o registo no menu
        elif escolha == "3":
            exit("Até à próxima")
        else:
            print("\nEscolha uma das opções sugeridas\n")
            continue
    
        m.app_menu()


if __name__ == "__main__":
  main()

    

