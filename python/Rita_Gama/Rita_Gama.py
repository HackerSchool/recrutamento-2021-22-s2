'''
    -especificar como devem ser escritas as expressoes
'''

class Menu():
    def apresentaMenuUtilizador(self):
        opcao = input(''' 
Bem vindo! 
Se pretender fazer:
- Login pressa 1
- Registar pressa 2
- Sair do programa pressa 3\n''')
        return opcao
    

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
    def verificaCredenciais(self, nomeUtilizador, password, listaCredenciais):   
        tamanho = len(listaCredenciais)
        IDUtilizador = 0
        idxPassword = 1

        for i in range(tamanho):
            if(listaCredenciais[i][IDUtilizador] == nomeUtilizador and listaCredenciais[i][idxPassword] == password):
                sessao = listaCredenciais[i][IDUtilizador]
                return sessao
        return -1
    
    '''
        Altera a password do utilizador registando-a no ficheiro especificado.
    '''
    def mudaPassword(self, nomeUtilizador):
        tamanho = len(listaCredenciais)
        IDUtilizador = 0
        idxPassword = 1

        nomeFicheiro = input('Insira o nome do ficheiro onde pretende guardar as credencias: ')
        fich = open(nomeFicheiro, "r")

        for i in range(tamanho):
            if(listaCredenciais[i][IDUtilizador] == nomeUtilizador):
                idxUtilizador = i

        passwordAntiga = input('Insira a sua password atual:')

        while(listaCredenciais[idxUtilizador][idxPassword] != passwordAntiga):
            print("Password errada")
            passwordAntiga = input('Insira a sua password atual:')


        passwordNova = input('Defina a nova password: ')

        #altera as credenciais no ficheiro de texto especificado

        linhas = fich.readlines()
        fich = open(nomeFicheiro, "w")

        for i in range(len(linhas)):
            fich.write(linhas[i])
            if(linhas[i] == nomeUtilizador+'\n'):
                idxUtilizadorFicheiro = i
                if(linhas[idxUtilizadorFicheiro+1] == passwordAntiga + '\n'):
                    fich.write(passwordNova)
                    fich.write('\n')
                    linhas[idxUtilizadorFicheiro+1] = passwordNova
                i += 2 #para continuar a escrever as outras informacoes do ficheiro 
        
         
        fich.close()

        #altera as credenciais no programa
        for i in range(tamanho):
            if(listaCredenciais[i][IDUtilizador] == nomeUtilizador):
                listaCredenciais[i][idxPassword] = passwordNova

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


        for ch in expressao:
            if(ch == '(' and dentro == SIM):
                current = current + ch
                numeroParentesis = numeroParentesis + 1
            if(ch == '(' and dentro == NAO):
                dentro = SIM
                numeroParentesis = numeroParentesis + 1


            if(ch not in {'(', ')'} and dentro == NAO):
                aux.append(ch)
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
        return aux
    
    '''
        Elimina todos os parentesis da expressao tornando entao a expressao numa equivalente
        onde as subexpressoes com parentesis ficaram isoladas em sublistas.
        Ex. "['2', '+', ['(3x5)', '/', '8']]" -> ['2', '+', [['3', 'x', '5'], '/', '8']]
    '''
    def eliminaParentesis(self, lista):
        tamanho = len(lista)

        for i in range(tamanho):
            if(isinstance(lista[i], list)):
                for ch in lista[i]:
                    if("(" in ch):
                        lista[i] = self.divideParentesis(str(lista[i][0]))
                        lista[i] = self.eliminaParentesis(lista[i])

        return lista

    '''
        Agrupa a expressao de forma a respeitar a prioridade de operadores quando na expressao
        inicial nao existem parentesis.
    '''
    def agrupa(self,expressao):
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

    '''
        Calcula o valor de expressoes atomicas, isto eh, com apenas dois numeros e um operador.
    '''
    def calcula(self,n1, operacao, n2):
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
    
    '''
        Calcula o valor de expressoes nao atomicas.
    '''
    def calculaMaisDeDois(self,lista):
        if(len(lista) == 3):
            return self.calcula(int(lista[0]), lista[1], int(lista[2]))
        else:
            '''
                Recursivamente calcula a operacao atomica mais ah direita.
            '''
            listaAux = self.calcula(int(lista[0]), lista[1], int(lista[2]))
            listaAux = [listaAux] + lista[3:]
            return self.calculaMaisDeDois(listaAux)

    '''
        Verifica se a expressao recebida eh uma expressao atomica.
        Uma expressao eh atomica quando esta na seguinte forma: n1 operador n2.
    '''
    def ehExpressaoAtomica(self,lista):
        tamanho = len(lista)

        if(tamanho == 1):
            if(isinstance(lista[0], str)):
                if(len(lista[0]) == 1):
                    return 0
                if(len(lista[0]) == 3): 
                    return 0
                else:
                    return -1

        if(tamanho >= 3):
            for i in range(tamanho):
                if(isinstance(lista[i], str) or isinstance(lista[i], int)):
                    if(i % 2 == 0): #o elemento deve ser um numero
                        return 0
                    if(i % 2 != 0):
                        if(not lista[i] in {'+', '-', 'x', '/', '%', '**'}):
                            return -1
                else:
                    return -1
            return 0
        else: #caso em que so tem dois elementos
            return -1

    '''
        Resolve a expressao recebida.
        A expressao eh uma lista, onde elementos atomicos(numeros e operadores) sao strings
        e operacoes sao sublistas ordenadas de acordo com a sua prioridade. 
        Caso a expressao original nao tenha parentesis, esta deve ser formatada recorrendo
        ah funcao agrupa.
    '''
    def resolveExpressao(self, lista):
        tamanho = len(lista)
        aux = list()

        if(tamanho == 1):
            if(self.ehExpressaoAtomica(lista) == 0): 
                if(len(lista[0]) == 1): #caso em que eh apenas ['numero']
                    return lista[0]
                else:
                    return self.calcula(int(lista[0][0]), lista[0][1], int(lista[0][2]))
            else:
                return lista[0]
        if(tamanho >= 3 and self.ehExpressaoAtomica(lista) == 0):
            return self.calculaMaisDeDois(lista)
        else:
            for i in range(tamanho):
                if(isinstance(lista[i], list)):
                    aux.append(self.resolveExpressao(lista[i]))
                else:
                    aux.append(lista[i])
        
        return self.resolveExpressao(aux)
    
    '''
        Pede a expressao ao utilizador e de seguida consoante esta tenha ou nao
        parentesis resolve a expressao recorrendo as funcoes divideParentesis, agrupaParentesis e 
        resolveExpressao.
    '''
    def executaCalculadora(self, expressao):
        aux = self.divideParentesis(expressao)
        print(aux)

        aux = self.eliminaParentesis(aux)
        res = self.resolveExpressao(aux)
        print("Resultado: " + str(res))


'''
    Executa o menu de login.
'''
def executaLogin():
    login = Login()

    credenciais = login.pedeCredenciais()

    idxIDUtilizador = 0
    idxPassword = 1
    nomeUtilizador = credenciais[idxIDUtilizador]
    password = credenciais[idxPassword]


    sessao = login.verificaCredenciais(nomeUtilizador, password, listaCredenciais)

    while(sessao == -1):
        print("Credenciais erradas.")
        opcao = input("Se pretender voltar a atras pressa S.")
        if(opcao == 'S'):
            return 3
        else:
            sessao = login.verificaCredenciais(nomeUtilizador, password, listaCredenciais)
    
    opcao = login.apresentaMenuLogin()

    while(opcao != 3):
        if(opcao == 1): #executa a calculadora
            calculadora = Calculadora()
            expressao = "(3+6)/(((5+1)+1)-5)x1"
            parentesis = input("Se pretende inserir uma expressao matematica com parentesis pressa S caso contrario N: ")
            if(parentesis == "S"):
                expressao = input('Insira a expressao matematica com apenas numeros e os seguintes operadores {+, -, x, /, %, **}: ')
                calculadora.executaCalculadora(expressao)
            else:
                expressao = input('Insira a expressao matematica com apenas numeros e os seguintes operadores {+, -, x, /, %, **}: ')
                aux_expressao = calculadora.agrupa(expressao)
                calculadora.executaCalculadora(aux_expressao)

        if(opcao == 2): #muda a password do utilizador
            login.mudaPassword(sessao)
        opcao = login.apresentaMenuLogin()

    return 3 #logout. Informa a funcao executaMenu que o utilizador pretende fazer logout.


'''
    Regista o utilizador, guardando as suas credenciais tanto no programa como no ficheiro de
    texto especificado pelo utilizador.
'''
def registarUtilizador():
    nomeFicheiro = input('''
Insira o nome do ficheiro onde quer guardar as suas credenciais.
Deve estar criado na mesma diretoria que o programa: ''')
    fich = open(nomeFicheiro, "w")

    nomeUtilizador = input("Defina o seu utilizador:")
    password = input("Defina a sua password: ")

    fich.write(nomeUtilizador)
    fich.write('\n')
    fich.write(password)

    fich.close()

    listaCredenciais.append([nomeUtilizador, password])


'''
    Executa o menu principal.
'''
def executaMenu():
    menu = Menu()
    opcao = menu.apresentaMenuUtilizador()

    while(opcao != 3):
        if(opcao == 1):
            if(not listaCredenciais):
                print("Deve registar-se primeiro.")
            else:
                executaLogin()
        elif(opcao == 2):
            registarUtilizador()
        else:
            print("Opcao nao definida")
        opcao = menu.apresentaMenuUtilizador()
    exit()


listaCredenciais = list() #variavel global que guarda as credenciais dos utilizadores
executaMenu()
