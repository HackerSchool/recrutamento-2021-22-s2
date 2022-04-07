import os
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib as mpl
import matplotlib.pyplot as plt


#EVAL EM BAIO LETS GO
def evalExpression(expression):

  #lista de operadores, por ordem, funções e números engraçados
  operadores = ["^", "/", "*", "+"]
  funcs      = ["arcos", "arsin", "arctan","sin", "cos", "tan", "exp", "ln", "log", "sqrt"]
  nums       = ["e", "pi"]

  #tirar todos os espaços para não dar problemas mais à frente
  exp = expression.replace(" ", "")

  #substituir cenas tipo ---+- por +
  while(signExpression(exp)):
    exp = signExpression(exp)

  #print(exp)
  #parentesis shit
  count = 0
  flagP = 0
  leftP = 0
  rightP = 0
  for i in range(len(exp)):
    if(exp[i] == "("):
      count += 1
      if(flagP == 0):leftP = i
      flagP = 1

    if(exp[i] == ")"):
      count -= 1
      rightP = i

    if(count == 0 and flagP == 1):
      break

  if(count != 0):
    #print("Erro de Parentesis, bro")
    return

  if(rightP != 0 and flagP != 0):
    exp = exp[:leftP] + evalExpression(exp[leftP+1:rightP]) + exp[rightP+1:]

  #while("(" in exp):
    exp = evalExpression(exp)


  for signal in funcs:
    while(funcExpression(exp, signal)):
      exp = funcExpression(exp, signal)

  while(signExpression(exp)):
    exp = signExpression(exp)

  #print(exp)
  i = 1
  while i < len(exp):
    if exp[i] == "-":
      try:
        if(exp[i-1] not in ["^", "/", "*", "+", "e"]):
          exp = exp[:i] + "+" +exp[i:]
      except:
        pass

    i+=1

  #print(exp)

  #try:
  for signal in operadores:
    while(simpExpression(exp, signal)):
      #isto é para lidar com a notação científica destes gajos dass
      if(exp == simpExpression(exp, signal)) : break
      exp = simpExpression(exp, signal)

  #except:
    ##exp = evalExpression(exp)
    #print("erro")

  return exp


def signExpression(exp):

  for i in range(len(exp)-1):
    if(exp[i] == "-" or exp[i] == "+"):
      if(exp[i+1] == "-" or exp[i+1] == "+"):
        bump = 0
        sign = 1
        for k in range(i, len(exp)):
          if(exp[k] == "-"):
            bump += 1
            sign *= -1
          elif(exp[k] == "+"):
            bump+= 1
          else:
            break

        if(sign == -1):
          exp = exp[:i] + "-" + exp[i+bump:]
        else:
          if(i != 0): exp = exp[:i] + "+" + exp[i+bump:]
          else: exp = exp[i+bump:]

        return exp

  return


def funcExpression(exp, func):

  operadores = ["^", "/", "*", "-", "+"]
  index = exp.find(func)
  if(index != -1):
    i = index + len(func)

    #DIREITA DA EXPRESSÂO
    right = len(exp)
    bump = 0
    sign = 1

    bump = 0
    if(i < len(exp)-1 and (exp[i+1] == '+' or exp[i+1] == "-")): bump = 1

    for k in range(i+1+bump, len(exp), +1):
      if (exp[k] in operadores):
        if((exp[k] == "+" or exp[k] == "-") and exp[k-1] == 'e'):
            continue
        else:
          right = k
          break

    tmp = calculate(func, exp[i:right])
    exp = exp[:index] + str(tmp) + exp[right:]

    return exp

  return


def simpExpression(exp, signal):

  #print("hi mom")
  operadores = ["^", "/", "*", "+"]
  begin = 0
  if(exp[0] == "-" or exp[0] == "+"):
    begin = 1
  for i in range(begin, len(exp), +1):

    #dealing com a notação científica destes gajos man, ex: 10000000000000000000000000000000 = 10e+21
    #if(j > 1 and signal == '+' and exp[j] == 'e'):)
    if exp[i] == signal:
      if(signal == '+' and i > 0):
        if(exp[i-1] == 'e'): continue

      #basicamente vou tentar enquadrar o lado esquerdo e direito do operador que encontrou entre dois operadores
      left = -1
      right = len(exp)

      #LEFT SIDE
      for j in range(i-1, -1, -1):
        if(j > 1 and exp[j] == '+' and exp[j-1] == 'e'):
          j -= 1

        elif (exp[j] in operadores):

          left = j+1
          break
        left = j

      #RIGHT SIDE
      #ver se tem um + à frente do operador ex: 5*+5 ou 10^+21
      bump = 0
      if(exp[i+1] == '+'): bump = 1
      for k in range(i+1+bump, len(exp), +1):

        if (exp[k] in operadores):
          if(exp[k] == "+" and exp[k-1] == 'e'):
            continue

          else:
            right = k
            break

        else:
          right = k+1

      #print("left " + str(left))
      #print("right" + str(right))
      tmp = calculate(signal, exp[left:i], exp[i+1:right])
      exp = exp[:left] + str(tmp) + exp[right:]

      #print("exp: " + exp)
      return exp

  return

def calculate(operador, sleft, sright = 0):

  left = float(sleft)
  right = float(sright)
  match(operador):
    case "^":
      return left ** right

    case "/":
      return left/ right

    case "*":
      return left * right

    case "e":
      return left * 10 ** right

    case "-":
      return left - right

    case "+":
      return left + right

    case "cos":
      return np.cos(left)

    case "sin":
      return np.sin(left)

    case "tan":
      return np.tan(left)

    case "exp":
      return np.exp(left)

    case "arcos":
      return np.arccos(left)

    case "arsin":
      return np.arcsin(left)

    case "arctan":
      return np.arctan(left)

    case "ln":
      return np.log(left)

    case "log":
      return np.log10(left)

    case "sqrt":
      return np.sqrt(left)


def evalX(exp, values):
  i = 0
  y = []
  #print(values)
  for x in values:
    #print(x)
    exptmp = exp
    while (exptmp.find("x") != -1):
      i = exptmp.find("x")
      exptmp = exptmp[:i] + str(x) + exptmp[i+1:]
    #print("tmp: " + str(exptmp))
    y.append(float(evalExpression(exptmp)))

  #print(y)
  return(y)


#GUI A PARTIR DAQUI!
class CalculadoraFrame(ttk.Frame):
  def __init__(self, container, controler):

      super().__init__(container)
      self.controler = controler

      self.evalBt = ttk.Button(self, text = 'Modo Clássico', command = lambda : self.controler.change_frame("EvalFrame"))
      self.evalBt.grid(column=0, row=3, sticky = "nsew")

      self.magalhaesBt = ttk.Button(self, text = 'Modo Matriz', command = lambda : self.controler.change_frame("MainMatrizFrame"))
      self.magalhaesBt.grid(column=0, row=4, sticky = "nsew")

      self.fitteiaBt = ttk.Button(self, text = 'Modo Plot', command = lambda : self.controler.change_frame("PlotterFrame"))
      self.fitteiaBt.grid(column=0, row=5, sticky = "nsew")

      #Botão de Voltar
      self.voltarBt = ttk.Button(self, text = 'Voltar', command = self.voltar_clicked)
      self.voltarBt.grid(column=0, row=6, sticky = "nsew")


  def voltar_clicked(self):

        #aqui como estou noutro file tive de passar frame como
        #string porque não estava a dar mas agora funciona e se funciona, funciona
        self.controler.change_frame("MainMenuFrame")


class EvalFrame(ttk.Frame):
    def __init__(self, container, controler):

      super().__init__(container)
      self.controler = controler
      self.helplabel = ttk.Label(self, text = "Calculadora Lopes 1.0")
      self.helplabel.grid(column = 0, row = 0)

      self.label = ttk.Label(self, text = "Introduza a expressão a avaliar")
      self.label.grid(column = 0, row = 1)
      inputxt = tk.StringVar()
      self.inputexp = ttk.Entry(self, textvariable=inputxt)
      self.inputexp.grid(column=0, row=2)

      self.evalBt = ttk.Button(self, text = 'Calcular', command = lambda : self.eval_clicked(inputxt.get()))
      self.evalBt.grid(column=0, row=3)

      self.reslabel = ttk.Label(self, text = "Resultado:")
      self.reslabel.grid(column = 0, row = 4)

      self.moneylabel = ttk.Label(self)
      self.moneylabel.grid(column = 1, row = 4)

      #Botão de Voltar
      self.voltarBt = ttk.Button(self, text = 'Voltar', command = self.voltar_clicked)
      self.voltarBt.grid(column=0, row=6)


    def eval_clicked(self, exp):
      self.moneylabel.config(text = evalExpression(exp))


    def voltar_clicked(self):

      #reset da moneylabel
      self.moneylabel.config(text = "")

      #aqui como estou noutro file tive de passar frame como
      #string porque não estava a dar mas agora funciona e se funciona, funciona
      self.controler.change_frame("CalculadoraFrame")



#MATRIZES BAAAAABY

class MainMatrizFrame(ttk.Frame):
    def __init__(self, container, controler):

        super().__init__(container)
        self.controler = controler

        #Botão de Solver
        self.gaussBt = ttk.Button(self, text = 'Solver', command = lambda : self.controler.change_frame("MatrizSolverFrame"))
        self.gaussBt.grid(column=0, row=5)


        #Botão de Voltar
        self.voltarBt = ttk.Button(self, text = 'Voltar', command = self.voltar_clicked)
        self.voltarBt.grid(column=0, row=6)



    def voltar_clicked(self):

        self.controler.change_frame("CalculadoraFrame")


class MatrizSolverFrame(ttk.Frame):
    def __init__(self, container, controler):

        super().__init__(container)
        self.container = container
        self.controler = controler

        self.matrixsize = tk.StringVar()
        self.matrixsize.set("3")
        self.matrixsizecurrent = "0"
        self.entryarray = [[ttk.Entry(self)]]*0
        self.entryright = []*0


        #Input matrix size
        self.sizelabel = ttk.Label(self, text = "Tamanho da Matriz: ")
        self.sizelabel.grid(column=1, row=1)

        #labels de cenas
        self.separator = ttk.Label(self, text = " ")
        self.separator.grid(column=1, row=2)

        self.helplabel = ttk.Label(self, text = "Resolve a equação A*X = B")
        self.helplabel.grid(column=1, row=3)

        self.alabel = ttk.Label(self, text = "Matriz A:")
        self.alabel.grid(column=3, row=3)

        self.blabel = ttk.Label(self, text = "Vetor B:")
        self.blabel.grid(column=3, row=3+3+1)

        self.xlabel = ttk.Label(self, text = "Solução X:")
        self.xlabel.grid(column=5, row=3+3+1)

        self.errorlabel = ttk.Label(self, text = " ")
        self.errorlabel.grid(column = 1, row = 5)
        #vão ser as labels com as soluções ;)
        self.xLabels = []

        self.size_clicked()

        self.usertextbox = ttk.Entry(self, textvariable= self.matrixsize)
        self.usertextbox.grid(column=2, row=1)

        self.sizeBt = ttk.Button(self, text = 'Gerar', command = self.size_clicked)
        self.sizeBt.grid(column=3, row=1)

        #Botão de Calcular
        self.calcBt = ttk.Button(self, text = 'Calcular', command = self.calc_clicked)
        self.calcBt.grid(column=4, row=1)


        self.cleanBt = ttk.Button(self, text = 'Limpar', command = self.clear_clicked)
        self.cleanBt.grid(column=5, row=1)




        #Botão de Voltar
        self.voltarBt = ttk.Button(self, text = 'Voltar', command = self.voltar_clicked)
        self.voltarBt.grid(column=1, row=200)



    def size_clicked(self):
      try:
        self.errorlabel.config(text = " ")
        msize = int(self.matrixsize.get())
        if(self.matrixsize.get() != self.matrixsizecurrent):
          #print("YOOOOOO NOVO SIZE")
          self.matrixsizecurrent = self.matrixsize.get()

          for wd in self.entryarray:
            wd.destroy()
          for wd in self.entryright:
            wd.destroy()
          for wd in self.xLabels:
            wd.destroy()

          self.alabel.destroy()
          self.blabel.destroy()
          self.xlabel.destroy()


          self.entryarray = [[]]*msize*msize
          self.entryright = [0]*msize

          self.alabel = ttk.Label(self, text = "Matriz A:")
          self.alabel.grid(column=3, row=3)

          self.blabel = ttk.Label(self, text = "Vetor B:")
          self.blabel.grid(column=3, row=3+msize+1)

          self.xlabel = ttk.Label(self, text = "Solução X:")
          self.xlabel.grid(column=5, row=3+msize+1)

          #loop para criar as ttk.Entry
          #i = linha, k = colunas
          for i in range(0, msize):

            self.entryright[i] = ttk.Entry(self)
            self.entryright[i].grid(column = 4, row = 4+i+msize, sticky = "nsew")
            self.separator1 = ttk.Label(self, text = " ")
            self.separator1.grid(column=1, row=3+msize)

            for k in range (0, msize):
              self.entryarray[i * msize + k] = ttk.Entry(self)
              self.entryarray[i * msize + k].grid(column = 4 + k, row = 3+i, sticky = "nsew")

        #else:
          #for wd in self.entryarray:
            #wd.config(text = "")



      except:
        self.errorlabel.config(text = "Erro: Tamanho tem de ser um int!")


    def clear_clicked(self):
      for wd in self.entryarray:
        wd.destroy()
      for wd in self.entryright:
        wd.destroy()
      for wd in self.xLabels:
        wd.destroy()
      self.alabel.destroy()
      self.blabel.destroy()
      self.xlabel.destroy()


      self.matrixsizecurrent = "0"
        #print("clear")

    def calc_clicked(self):
      for wd in self.xLabels:
        wd.destroy()
      msize = int(self.matrixsize.get())
      self.xLabels = [ttk.Label(self)]*msize
      tmpmatrix = []
      for wd in self.entryarray:
        try:
          float(wd.get())
          tmpmatrix.append(float(wd.get()))
        except:
          tmpmatrix.append(0.)
      tmp = np.array(tmpmatrix)
      self.matrixA = tmp.reshape(int(self.matrixsizecurrent), int(self.matrixsizecurrent))

      tmpmatrix = []
      for wd in self.entryright:
        try:
          float(wd.get())
          tmpmatrix.append(float(wd.get()))
        except:
          tmpmatrix.append(0.)

      tmp = np.array(tmpmatrix)
      self.vectorB = tmp.reshape(int(self.matrixsizecurrent), 1)
      #print(self.matrixA)
      #print(self.vectorB)


      try:
        #ya, vou usar o numpy porque já fiz isto antes em C++ e é chato dont @me
        vectorX = np.linalg.solve(self.matrixA, self.vectorB)

        for i in range(0, msize):
          tmptxt = "x" + str(i+1) + " = " + str(vectorX[i])
          self.xLabels[i] = ttk.Label(self, text = tmptxt)
          self.xLabels[i].grid(column=6, row=3+msize+1+i, sticky = "w")
          self.errorlabel.config(text = " ")

      except:
        self.errorlabel.config(text = "Erro: O sistema não é singular!")


    def voltar_clicked(self):

        self.controler.change_frame("MainMatrizFrame")



#PLOTTER
class PlotterFrame(ttk.Frame):
    def __init__(self, container, controler):

        super().__init__(container)
        self.controler = controler
        self.container = container

        #Expression
        self.explabel = ttk.Label(self, text = "Expressão: ")
        self.explabel.grid(column=1, row=1)

        self.exp = tk.StringVar()
        self.usertextbox = ttk.Entry(self, textvariable= self.exp)
        self.usertextbox.grid(column=2, row=1)

        self.plotBt = ttk.Button(self, text = 'Plot', command = self.plot_clicked)
        self.plotBt.grid(column=3, row=1, sticky = "w")


        #Botão de Voltar
        self.voltarBt = ttk.Button(self, text = 'Voltar', command = self.voltar_clicked)
        self.voltarBt.grid(column=1, row=6)


    #isto vai pegar na expressão e mandar para o matplotlib para fazer uma imagem, dar display, apagar
    def plot_clicked(self):

        x = np.linspace(-5,5,100)

        expstr = self.exp.get()
        #print(expstr)
        y = evalX(expstr, x)
        #y = function(expstr, x)
        # setting the axes at the centre
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        # plot the function
        plt.plot(x,y, 'r')

        # show the plot
        plt.savefig("resources/plot.png")
        plot = tk.PhotoImage(file = 'resources/plot.png')
        imagelabel = ttk.Label(self, image = plot)
        imagelabel.image = plot
        imagelabel.grid(column = 1, row = 2, columnspan = 5)

    def voltar_clicked(self):

        self.controler.change_frame("CalculadoraFrame")




