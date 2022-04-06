import random

class TicTacToe ():
    '''
    Classe que contem todos os métodos para o jogo do Tic-Tac-Toe
    '''
    def __init__(self):
        print('''
****************************************************************************
***** Bem-vindo/a ao Tic-Tac-Toe. Tem dois modos de jogo disponíveis! ******
****************************************************************************

1 - Multiplayer
2 - Single player
3 - Voltar
                ''')
        #Usar list comprehension para criar o tabuleiro (na forma de matriz) - cada posição tem um hifen
        self.tabuleiro = [[ '-' for x in range(3)] for y in range(3)]

    #Método que desenha o tabuleiro
    def desenho_tabuleiro(self):
        print()
        i=0
        for row in self.tabuleiro:
            j=0
            for column in row:
                if j <= 1:
                    print("   {}   |".format(column), end=" ")
                else:
                    print("   {}   ".format(column), end=" ")
                j+= 1
            i += 1
            if i < 3:
                print("\n - - - - - - - - - - - - - ") 
            else:
                print("\n\n")
    
    #Método que verifica se já há vencedor
    def verificar_vencedor(self, jogador):
        #Verificar linhas - se o jogador estiver numa linha inteira, ganha o jogo
        for i in range(3):
            vitoria = True
            for j in range(3):
                if jogador != self.tabuleiro[i][j]:
                    #Se algum for diferente, essa linha nao tem o jogador como vencedor e por isso podemos passar para a iteração seguinte
                    vitoria = False
                    break
            if vitoria:
                return True

        #Verificar colunas - se o jogador estiver numa coluna inteira, ganha o jogo
        for i in range(3):
            vitoria = True
            for j in range(3):
                if jogador != self.tabuleiro[j][i]:
                    #Se algum for diferente, essa linha nao tem o jogador como vencedor e por isso podemos passar para a iteração seguinte
                    vitoria = False
                    break
            if vitoria:
                return True

        #Verificar diagonais - se o jogador estiver numa das diagonais, ganha o jogo
        contador_diagonais = 0
        #Primeira diagonal - principal
        for i in range(3):
            if jogador == self.tabuleiro[i][i]:
                contador_diagonais += 1
            if contador_diagonais == 3:
                return True
        
        contador_diagonais = 0
        #Segunda diagonal
        for i in range(3):
            if jogador == self.tabuleiro[i][2-i]:
                contador_diagonais += 1
            if contador_diagonais == 3:
                return True

        return False

    #Método que corre o jogo multiplayer
    def run_multiplayer(self):
        i=0
        while(i<9):
            self.desenho_tabuleiro()

            if i%2 == 0:
                print("É a vez do jogador X")
                jogador = 'X'
            else:
                print("É a vez do jogador O")
                jogador = 'O'
            
            #Receber a jogada e substituir na lista do tabuleiro '-' pelo jogador respetivo
            print("Insira a linha e a coluna onde quer jogar (Ex: 1 1)")
            posicao1, posicao2 = input("Posição: ").split()

            if int(posicao1) > 3 or int(posicao2) > 3:
                    print("\nJogue num sítio disponível".upper())
                    continue
            elif int(posicao1) < 0 or int(posicao2) < 0:
                print("\nJogue num sítio disponível".upper())
                continue

            if(self.tabuleiro[int(posicao1)-1][int(posicao2)-1] == '-'):
                self.tabuleiro[int(posicao1)-1][int(posicao2)-1] = jogador
            else:
                print("\nJogue num sítio disponível".upper())
                continue
        
            #Verificar se alguem ganhou
            if self.verificar_vencedor(jogador):
                self.desenho_tabuleiro()
                print("Jogador {} ganhou".format(jogador))
                escolha = input("Deseja jogar novamente?\n 1 - Sim\n 2 - Não: ")
                if escolha == "1":
                    self.tabuleiro = [[ '-' for x in range(3)] for y in range(3)]
                    i = -1
                else:
                    break

            #Se ninguém ganhar - imprimir empate
            if i == 8:
                print("Jogo empatado!")
                escolha = input("Deseja jogar novamente?\n 1 - Sim\n 2 - Não: ")
                if escolha == 1:
                    self.tabuleiro = [[ '-' for x in range(3)] for y in range(3)]
                    i = -1
                else:
                    break
            
            i += 1
    
    #Método que corre singleplayer
    def run_singleplayer(self):
        i=0
        while(i<9):
            self.desenho_tabuleiro()

            #Jogada do jogador no terminal
            if i%2 == 0:
                print("É a vez do jogador X")
                jogador = 'X'

                #Receber a jogada e substituir na lista do tabuleiro '-' pelo jogador respetivo
                print("Insira a linha e a coluna onde quer jogar (Ex: 1 1)")
                posicao1, posicao2 = input("Posição: ").split()

                if int(posicao1) > 3 or int(posicao2) > 3:
                    print("\nJogue num sítio disponível".upper())
                    continue
                elif int(posicao1) < 0 or int(posicao2) < 0:
                    print("\nJogue num sítio disponível".upper())
                    continue

                if(self.tabuleiro[int(posicao1)-1][int(posicao2)-1] == '-'):
                    self.tabuleiro[int(posicao1)-1][int(posicao2)-1] = jogador
                else:
                    print("\nJogue num sítio disponível".upper())
                    continue

            #Jogada aleatória
            else:
                print("É a vez do jogador O")
                jogador = 'O'

                #Gerar números aleatórios com as posições em que o computador joga
                bol = False
                while not bol:
                    x = random.randint(1,3)
                    y = random.randint(1,3)
                    if(self.tabuleiro[x-1][y-1] == '-'):
                        self.tabuleiro[x-1][y-1] = jogador
                        bol = True

            #Verificar se alguem ganhou
            if self.verificar_vencedor(jogador):
                self.desenho_tabuleiro()
                print("Jogador {} ganhou".format(jogador))
                escolha = input("Deseja jogar novamente?\n 1 - Sim\n 2 - Não: ")
                if escolha == "1":
                    self.tabuleiro = [[ '-' for x in range(3)] for y in range(3)]
                    i = -1
                else:
                    break

            #Se ninguém ganhar - imprimir empate
            if i == 8:
                print("Jogo empatado!")
                escolha = input("Deseja jogar novamente?\n 1 - Sim\n 2 - Não: ")
                if escolha == 1:
                    self.tabuleiro = [[ '-' for x in range(3)] for y in range(3)]
                    i = -1
                else:
                    break
            
            i += 1
            
            
    
