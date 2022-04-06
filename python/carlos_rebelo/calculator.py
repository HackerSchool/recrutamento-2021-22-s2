class Calculator():
    '''
    Classe com métodos para a calculadora
    '''
    def __init__(self):
        print('''
****************************************************************************
************************* Bem-vindo/a à Calculadora ************************
****************************************************************************
''')

    def simple_calculator(self):
        while(1):
            print("Escreva dois números seguidos da operação (+, -, x, /, **, %)")

            try:
                a = float(input("1º Número: "))
            except ValueError:
                print("Introduza um número")
                continue

            try:
                b = float(input("2º Número: "))
            except ValueError:
                print("Introduza um número")
                continue
            
            op = input("Operação: ")

            #Condicionais
            if op == "+":
                print("Resultado: {}".format(a+b))
                break
            elif op == "-":
                print("Resultado: {}".format(a-b))
                break
            elif op == "x":
                print("Resultado: {}".format(a*b))
                break
            elif op == "/":
                print("Resultado: {}".format(float(a/b)))
                break
            elif op == "**":
                print("Resultado: {}".format(a**b))
                break
            elif op == "%":
                print("Resultado: {}".format(a%b))
                break
            else:
                print("Introduza uma operação válida")
        