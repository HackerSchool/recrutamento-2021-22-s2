def calculator():
    num1 = input("Número 1: ")
    num2 = input("Número 2: ")
    operacao = input("Operação: ")

    if ((operacao!="+") and (operacao!="-") and (operacao!="x") and (operacao!="/") and
        (operacao!= "**") and (operacao!="%")):
        print("Operação inválida.")
        operacao = input("Operação: ")
    
    if operacao== "+":
        x= int(num1)+int(num2)
    
    elif operacao== "-":
        x= int(num1)-int(num2)
    
    elif operacao== "x":
        x= int(num1)*int(num2)
    
    elif operacao== "/":
        x= int(num1)/int(num2)
    
    elif operacao== "**":
        x= int(num1)**int(num2)

    elif operacao== "%":
        x= int(num1)%int(num2)
    
    print("O resultado é: "+str(x))
    string=input("Queres continuar na HackCalculate?\nOpções: sim, s | não, n\n")
    if (string=="sim" or string=="s"):
        calculator()

#as melhores tentativas do nível 7 da calculadora
"""
Tentativa 1:
def calculator():
    string= input("Expressão: ")
    x= string.split("(")
    list=[]

    for i in x:
        y= i.split(")")
        list.append(y)

    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    
    for i in list:
        for j in i:
            l=j.split("+")
            a.append(l)

            for t in j:
                l=t.split("-")
                b.append(l)

                for s in t:
                    l=s.split("x")
                    c.append(l)

                    for u in s:
                        l=u.split("/")
                        d.append(l)

                        for g in u:
                            l=g.split("%")
                            e.append(l)

                            for r in g:
                                l=r.split("**")
                                f.append(l)
                                w=0
                                for i in f:
                                    i[w]**i[w+1]

Eu notei que ao fazer split com os parênteses, a expressão que vinha com índice 0
era sempre a mais prioritária. A partir daí começava a dar split por ordem dos operadores
menos prioritários para isolar cada vez mais as operações com prioridade.
No fim de todos os splits, a ideia era recuar ao mesmo tempo que se realizavam as operações.

Exemplo:
calculator("(4+2)**2+5(9x5)")
x= ["", "4+2)**2+5", "9x5)"]
list= ["", ["4+2", "**2+5"], ["9x5", ""]]

(Teria que iterar sobre a lista para apagar os vazios "")
"4+2" e "9x5" são de índice 0 na iteração sobre os elementos da lista
e eram as expressões que estavam dentro de parênteses.

Depois cada lista a, b, c, d, e, f estaria a guardar os números que diziam respeito 
à operação correspondente e começar-se-ia o recuo com as operações.

"""
"""
Tentativa 2:
Aqui a ideia era igualmente adiar as operações. Cada ciclo for entrava 
num parênteses diferente. Sendo que o segundo ciclo for apareceria com as operações
do primeiro ciclo resolvidas (as que estavam dentro de parênteses).
A maior parte das vezem em que igualo y a string[(listright[i][1])+1 : (listleft[i][1])],
o que faria sentido era string ser y.

def calculator():
    string= input("Expressão: ")
    size= len(string)
    listright=[]
    listleft=[]
    rightp =0
    leftp=0

    for i in range(size):
        if string[i] == "(":
            rightp +=1  #contador de parêntes do lado direito
            listright.append((rightp, i))
        if string[i] == ")":
            leftp +=1 #contador de parêntes do lado esquerdo
            listleft.append((leftp, i))
        
    listright.reverse() #para começarmos com os parênteses mais inferiores de todos

    for i in range (len(listright)):
        y=string[(listright[i][1])+1 : (listleft[i][1])]

        for j in range(0, len(y)-1):
            if (y[j]== "*" and y[j+1]== "*"):
                o=j-1
                p=j+2
                numberleft=0
                numberright=0
                while(y[o].isdigit, o>-1):
                    numberleft= numberleft*10+y[o]
                    o-=1
                
                while(y[p].isdigit, p<len(y)):
                    numberright= numberright*10+y[o]
                    p+=1
         
                numholder1= numberleft**numberright
          
                y=y[:(listright[i][1][o])] + str(numholder1) + y[(listleft[i][1][p]+1):]

        for j in range(0, len(y)-1):
            if y[j]== "%":
                o=j
                p=j
                numberleft=0
                numberright=0
                while(y[o].isdigit):
                    numberleft= numberleft*10+int(y[o])
                    o-=1
                while(y[p].isdigit):
                    numberright= numberright*10+int(y[o])
                    p+=1
                numholder1= numberleft%numberright
                y=y[:(listright[i][1][o])] + str(numholder1) + y[(listleft[i][1][p]+1):]
            if y[j]== "/":
                o=j
                p=j
                numberleft=0
                numberright=0
                while(y[o].isdigit):
                    numberleft= numberleft*10+int(y[o])
                    o-=1
                while(y[p].isdigit):
                    numberright= numberright*10+int(y[o])
                    p+=1
                numholder1= numberleft/numberright
                y=y[:listright[i][1][o]] + str(numholder1) + y[(listleft[i][1][p]+1):]
            if y[j]== "x":
                o=j
                p=j
                numberleft=0
                numberright=0
                while(y[o].isdigit):
                    numberleft= numberleft*10+int(y[o])
                    o-=1
                while(y[p].isdigit):
                    numberright= numberright*10+int(y[o])
                    p+=1
                numholder1= numberleft*numberright
                y=y[:listright[i][1][o]] + str(numholder1) + y[(listleft[i][1][p]+1):]

        for j in range(0, len(y)-1):
            if y[j]== "+":
                o=j
                p=j
                numberleft=0
                numberright=0
                while(y[o].isdigit):
                    numberleft= numberleft*10+int(y[o])
                    o-=1
                while(y[p].isdigit):
                    numberright= numberright*10+int(y[o])
                    p+=1
                numholder1= numberleft+numberright
                y=y[:listright[i][1][o]] + str(numholder1) + y[(listleft[i][1][p]+1):]
            if y[j]== "-":
                o=j
                p=j
                numberleft=0
                numberright=0
                while(y[o].isdigit):
                    numberleft= numberleft*10+int(y[o])
                    o-=1
                while(y[p].isdigit):
                    numberright= numberright*10+int(y[o])
                    p+=1
                numholder1= numberleft-numberright
                y=y[:listright[i][1][o]] + str(numholder1) + y[(listleft[i][1][p]+1):]


"""