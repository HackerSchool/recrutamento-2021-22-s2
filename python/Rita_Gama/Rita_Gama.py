nomeFicheiro = "dados utilizadores.txt"
credenciais = list()

class Menu():
    def apresentaMenuUtilizador(self):
        opcao = input(''' 
Bem vindo! 
Pressione:
- 1 para Login
- 2 para Registo
- 3 para sair\n''')
        return opcao
    
    '''
    Executa o menu principal.
'''
    def registarUtilizador(self):
        '''
            Regista o utilizador, guardando as suas credenciais tanto no programa como no ficheiro de
            texto especificado pelo utilizador.
        '''
        fich = open(nomeFicheiro, "a")

        nomeUtilizador = input("Defina o seu utilizador:")
        password = input("Defina a sua password: ")

        fich.write("nome utilizador: ")
        fich.write(nomeUtilizador)
        fich.write(' + password: ')
        fich.write(password)
        fich.write('\n')

        fich.close()

    
class Login():

    def apresentaMenuLogin(self):
        opcao = input(
'''
Se pretender:
- Usar a calculadora pressa 1
- Mudar password pressa 2
- Fazer logout pressa 3
''')
        return opcao

    ''' 
        Pede credenciais(nome deutilizador e respetiva password) ao utilizador.
    '''
    def pedeCredenciais(self):
        nomeUtilizador = input("Nome Utilizador: ")
        passwordUtilizador = input("Password: ")

        return [nomeUtilizador, passwordUtilizador]

    '''
            Verifica se as credenciais recebidas sao validas, isto eh, se existe o utilizador e se a eh
            password associada a esse utilizador. 
            Retorna o nome do utilizador caso sejam validas, -1 caso contrario.
    '''
    def verificaCredenciais(self, nomeUtilizador, password):   
        tamanho = len(credenciais)
        IDUtilizador = 0

        for i in range(tamanho):
            if(credenciais[i][IDUtilizador] == nomeUtilizador and self.passwordUtilizador(nomeUtilizador) == password):
                return True
        return False

    def passwordUtilizador(self, nomeUtilizador):
        tamanho = len(credenciais)
        for i in range(tamanho):
            if(credenciais[i][0] == nomeUtilizador):
                return credenciais[i][1]
        return ""
    
    def mudaPassword(self, nomeUtilizador, passwordAntiga, passwordNova):
        fich = open(nomeFicheiro, "r")

        linhas = fich.readlines()

        for linha in linhas:
            if(nomeUtilizador in linha):
                aux = linha.replace(passwordAntiga, passwordNova)
                linhas = aux
        
        fich.close()
        
        fich = open(nomeFicheiro, "w")

        fich.writelines(linhas)

        fich.close()




def guardaDadosUtilizadores():
    '''
        Le os dados dos utilizadores do ficheiro e guarda-os.
    '''
    fich = open(nomeFicheiro, "r")

    linhas = fich.readlines()

    fich.close()

    numeroLinhas = len(linhas)

    for i in range(numeroLinhas):
        leDadosUtilizador(linhas[i])
    


def leDadosUtilizador(linha):
    '''
        Funcao auxiliar. Le o nome e password do utilizador.
    '''
    dados = linha.split(" ")
    numero = len(dados)
    idxUtilizador = 0
    idxPassword = 0

    for i in range(numero):
        if(dados[i] == "utilizador:"):
            idxUtilizador = i + 1
        if(dados[i] == "password:"):
            idxPassword = i + 1
    
    utilizador = (dados[idxUtilizador], dados[idxPassword][:-1])
    
    credenciais.append(utilizador)

def ehNumero(self):
    '''
        Verifica se o argumento eh numero.
    '''
    if(type(self) == str):
        return self.isnumeric()
    elif(type(self) in [float, int]):
        return True
    else:
        return False


class Calculadora():
    '''
        Agrupa as expressoes que estao isoladas por parentesis em sublistas.
        Se existirem expressoes tambem com parentesis dentro de outra tambem com parentesis
        apenas a exterior se transforma em sublista.
        Ex. "2+((3x5)/8)" -> ['2', '+', ['(3x5)', '/', '8']]
    '''
    def divideParentesis(self, expressao):
        aux = list()
        current = str()
        NAO = 1
        SIM = 0
        dentro = NAO
        numeroParentesis = 0
        numero = str()


        for ch in expressao:
            if(ch == '(' and dentro == SIM):
                current = current + ch
                numeroParentesis = numeroParentesis + 1
            if(ch == '(' and dentro == NAO):
                dentro = SIM
                numeroParentesis = numeroParentesis + 1


            if(ch not in {'(', ')'} and dentro == NAO):
                if(ch.isnumeric()):
                    numero += ch
                else:
                    if(numero != ''):
                        aux.append(numero)
                    aux.append(ch)
                    numero = str()

            if(ch not in {'(', ')'} and dentro == SIM):
                current = current + ch
            

            if(ch == ')' and dentro == SIM):
                numeroParentesis = numeroParentesis - 1
                if(numeroParentesis == 0): #significa que e o ultimo logo nao usamos esse
                    aux.append([current])
                    dentro = NAO
                    current =  str()
                else:
                    current = current + ch

        if(numero != ''):  
            aux.append(numero)

        return aux

    
    
    def eliminaParentesis(self, lista):
        '''
            Elimina todos os parentesis da expressao tornando entao a expressao numa equivalente
            onde as subexpressoes com parentesis ficaram isoladas em sublistas.
            Ex. "['2', '+', ['(3x5)', '/', '8']]" -> ['2', '+', [['3', 'x', '5'], '/', '8']]
        ''' 
        tamanho = len(lista)

        for i in range(tamanho):
            if(isinstance(lista[i], list)):
                for ch in lista[i]:
                    if("(" in ch):
                        lista[i] = self.divideParentesis(str(lista[i][0]))
                        lista[i] = self.eliminaParentesis(lista[i])

        return lista


    def agrupa(self,expressao):
        '''
            Agrupa a expressao de forma a respeitar a prioridade de operadores quando na expressao
            inicial nao existem parentesis.
        '''
        novaExpressao = str()
        aux = "("
        
        for each in expressao:
            if(each in "x/"):
                aux = aux + ")" + str(each)
                novaExpressao += aux
                aux = "("
            else:
                aux += each
        #como no final nao ha operador eh necessario fazer a concatenacao fora do for
        novaExpressao = novaExpressao + aux + ")"
        return novaExpressao


    def calcula(self,n1, operacao, n2):
        '''
            Calcula o valor de expressoes atomicas, isto eh, com apenas dois numeros e um operador.
        '''
        if(operacao == '+'):
            return n1 + n2
        elif(operacao == '-'):
            return n1 - n2
        elif(operacao == '/'):
            return n1 / n2
        elif(operacao == 'x'):
            return n1 * n2
        elif(operacao == '**'):
            return pow(n1, n2)
        elif(operacao == '%'):
            return n1 % n2
        else:
            print("Operacao nao definida")
            return 0
    
    
    def calculaMaisDeDois(self,lista):
        '''
            Calcula o valor de expressoes nao atomicas.
        '''
        if(len(lista) == 3 and ehNumero(lista[0]) and ehNumero(lista[2])):
            return self.calcula(int(lista[0]), lista[1], int(lista[2]))
        else:
            '''
                Recursivamente calcula a operacao atomica mais ah direita.
            '''
            print(lista)
            listaAux = self.calcula(int(lista[0]), lista[1], int(lista[2]))
            listaAux = [listaAux] + lista[3:]
            return self.calculaMaisDeDois(listaAux)


    def ehExpressaoAtomica(self,lista):
        '''
            Verifica se a expressao recebida eh uma expressao atomica.
            Uma expressao eh atomica quando esta na seguinte forma: n1 operador n2.
        '''
        tamanho = len(lista)

        if(tamanho == 1):
            if(type(lista[0]) == str):
                if(ehNumero(lista[0][0]) and ehNumero(lista[0][2])):
                    return True
            if(type(lista[0]) in [float, int]):
                return True
            return False
        if(tamanho >= 3):
            for i in range(tamanho):
                if(i % 2 == 0 and ehNumero(lista[i]) == False):
                    return False
                if(i % 2 != 0 and lista[i] not in {'+', '-', 'x', '/', '%', '**'}):
                    return False
            return True
        else:
            return False
    
    def converteEmNumeros(self, lista):
        '''
            Converte uma lista com apenas uma string, que, por sua vez, eh uma expressao, 
            numa lista equivalente desta vez com numeros.
        '''
        numero = 0
        aux = list()

        if(type(lista[0]) == str):
            for each in lista[0]:
                if(each >= '0' and each <= '9'):
                    numero *= 10
                    numero += (int(each) - int('0'))
                    ultimo = each
                else:
                    if(ultimo == "*" and each == "*"):
                        ultimo += each
                        aux.append(ultimo)
                        numero = 0
                    elif(ultimo != "*" and each == "*"):
                        aux.append(numero)
                        ultimo = each
                    else:
                        aux.append(numero)
                        numero = 0
                        ultimo = each
        
        aux.append(numero)

        return aux


    def resolveExpressao(self, lista):
        '''
            Resolve a expressao recebida.
            A expressao eh uma lista, onde elementos atomicos(numeros e operadores) sao strings
            e operacoes sao sublistas ordenadas de acordo com a sua prioridade. 
            Caso a expressao original nao tenha parentesis, esta deve ser formatada recorrendo
            ah funcao agrupa.
        '''
        tamanho = len(lista)
        aux = list()

        if(tamanho == 1 and type(lista[0]) != list):
            if(type(lista[0]) == str):
                lista = self.converteEmNumeros(lista)
            if(self.ehExpressaoAtomica(lista)): 
                if(len(lista) == 1 and type(lista[0]) == int): #caso em que eh apenas ['numero']
                    return lista[0]
                else:
                    return self.calcula(lista[0], lista[1], lista[2])
            else:
                return lista[0]
        if(tamanho == 3 and self.ehExpressaoAtomica(lista)):
            return self.calculaMaisDeDois(lista)
        else:
            for i in range(tamanho):
                if(isinstance(lista[i], list)):
                    aux.append(self.resolveExpressao(lista[i]))
                else:
                    aux.append(lista[i])
        
        return self.resolveExpressao(aux)
    

    def executaCalculadora(self, expressao):
        '''
            Pede a expressao ao utilizador e de seguida consoante esta tenha ou nao
            parentesis resolve a expressao recorrendo as funcoes divideParentesis, agrupaParentesis e 
            resolveExpressao.
        '''
        aux = self.divideParentesis(expressao)
        print(aux)

        aux = self.eliminaParentesis(aux)
        print(aux)

        res = self.resolveExpressao(aux)
        print("Resultado: " + str(res))
   


def executaMenu():
    menu = Menu()
    opcao = menu.apresentaMenuUtilizador()

    while(opcao != '3'):
        if(opcao == '1'):
            opcao = executaLogin()
            while(opcao != '3'):
                opcao = executaLogin()
            opcao = menu.apresentaMenuUtilizador()
            break
        elif(opcao == '2'):
            menu.registarUtilizador()
        else:
            print("Opcao nao definida")
        opcao = menu.apresentaMenuUtilizador()
    exit()


def executaLogin():
    login = Login()

    guardaDadosUtilizadores()

    utilizador = login.pedeCredenciais()
    if(login.verificaCredenciais(utilizador[0], utilizador[1]) == False):
        print("Credenciais invalidas\n")
    
    opcao = login.apresentaMenuLogin()

    while(opcao != '3'):
        if(opcao == '1'):
            calculadora = Calculadora()
            parentesis = input("Se pretende inserir uma expressao matematica com parentesis pressa S caso contrario N: ")
            if(parentesis == "S"):
                expressao = input('Insira a expressao matematica com apenas numeros e os seguintes operadores {+, -, x, /, %, **}: ')
                calculadora.executaCalculadora(expressao)

        if(opcao == '2'): #muda a password do utilizador
            passwordNova = input("Nova password: ")
            login.mudaPassword(utilizador[0], login.passwordUtilizador(utilizador[0]),passwordNova)
        opcao = login.apresentaMenuLogin()

    return opcao
    

executaMenu()