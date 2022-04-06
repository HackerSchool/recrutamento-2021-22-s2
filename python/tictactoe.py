from tkinter import *
import random

#Variáveis Globais
i  = 0
i1 = 0 
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0
i8 = 0
i9 = 0
first = -1

def restart_global (): #Restart do jogo
    global i,i1,i2,i3,i4,i5,i6,i7,i8,i9,first
    i  = 0
    i1 = 0 
    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    i6 = 0
    i7 = 0
    i8 = 0
    i9 = 0
    first = -1
    window()

def window ():
    
    def eu(): #Eu jogo primeiro
        global first
        first = 0
        popup1.destroy()

    def ai (): #Computador joga primeiro
        global first
        first = 1
        popup1.destroy()

    popup1 = Tk() 
    popup1.title(" First Move ")
    popup1.configure(width=300, height=300)
    popup1.configure(bg='white')
    popup1.eval('tk::PlaceWindow . center')
    label1=Label(popup1,text=" Who goes first? ",font=(50), bg="white",fg="black")
    button_eu=Button(popup1, text= " Me ", height = 10, width = 10,command = eu)
    button_ai=Button(popup1, text=" AI ",height = 10, width = 10 ,command = ai)
    label1.pack()
    button_eu.pack()
    button_ai.pack()
    popup1.mainloop()
     
    ################################### Jogador joga primeiro ####################################################

    if first == 0:
     #so chamando funcoes é que tens um loop
     def quit (): #fecha o programa
               exit()
               
     def objectdestroy (): #destroi objetos
            window.destroy()


     def gameover(): # condições para o jogo acabar
           def restart ():
               popup.destroy()
               objectdestroy()
               restart_global()

           if i1 == i4 == i7 ==1 or i2 == i5 == i8 ==1 or i3 == i6 == i9 ==1 or i1 == i2 == i3 ==1 or i4 == i5 == i6 ==1 or i7 == i8 == i9 ==1 or i1 == i5 == i9 ==1 or i7 == i5 == i3 ==1 :
               master.configure(bg='black')
               button1['text'] = 'G'
               button2['text'] = 'A'
               button3['text'] = 'M'
               button4['text'] = 'E'
               button5['text'] = 'O'
               button6['text'] = 'V'
               button7['text'] = 'E'
               button8['text'] = 'R'
               button9['text'] = '!'
               popup = Tk() 
               popup.title(" Game Over ")
               popup.configure(width=300, height=300)
               popup.configure(bg='white')
               popup.eval('tk::PlaceWindow . center')
               label=Label(popup,text=" X won! ",font=(50), bg="white",fg="black")
               button_restart=Button(popup, text= " Restart", height = 10, width = 10,command = restart)
               button_quit=Button(popup, text=" Quit ",height = 10, width = 10 ,command = quit)
               label.pack()
               button_restart.pack()
               button_quit.pack()
               return 1
          

           if i1 == i4 == i7 ==2 or i2 == i5 == i8 ==2 or i3 == i6 == i9 ==2 or i1 == i2 == i3 ==2 or i4 == i5 == i6 ==2 or i7 == i8 == i9 ==2 or i1 == i5 == i9 ==2 or i7 == i5 == i3 ==2 :
               master.configure(bg='black')
               button1['text'] = 'G'
               button2['text'] = 'A'
               button3['text'] = 'M'
               button4['text'] = 'E'
               button5['text'] = 'O'
               button6['text'] = 'V'
               button7['text'] = 'E'
               button8['text'] = 'R'
               button9['text'] = '!'
               popup = Tk() 
               popup.title(" Game Over ")
               popup.configure(width=300, height=300)
               popup.configure(bg='white')
               popup.eval('tk::PlaceWindow . center')
               label=Label(popup,text=" O won! ",font=(100), bg="white",fg="black")
               button_restart=Button(popup, text= " Restart", height = 10, width = 10,command = restart)
               button_quit=Button(popup, text=" Quit ",height = 10, width = 10 ,command = quit)
               label.pack()
               button_restart.pack()
               button_quit.pack()
               return 1
           elif i >=9 :
               master.configure(bg='black')
               button1['text'] = 'G'
               button2['text'] = 'A'
               button3['text'] = 'M'
               button4['text'] = 'E'
               button5['text'] = 'O'
               button6['text'] = 'V'
               button7['text'] = 'E'
               button8['text'] = 'R'
               button9['text'] = '!'
               popup = Tk() 
               popup.title(" Game Over ")
               popup.configure(width=300, height=300)
               popup.configure(bg='white')
               popup.eval('tk::PlaceWindow . center')
               label=Label(popup,text=" Tie ",font=(100), bg="white",fg="black")
               button_restart=Button(popup, text= " Restart", height = 10, width = 10,command = restart)
               button_quit=Button(popup, text=" Quit ",height = 10, width = 10 ,command = quit)
               label.pack()
               button_restart.pack()
               button_quit.pack()
               return 1
           else:
             return 0

     
     def algoritmo (): #define jogada do computador

          #Primeira jogada do computador (optimal play)
          if i == 1 and (i1 ==1 or i3 == 1 or i7 == 1 or i9 ==1) :
              press5()
          if i == 1 and i2 == 1:
              press8()
          if i == 1 and i4 == 1:
              press6()
          if i == 1 and i6 == 1:
              press4()
          if i == 1 and i8 == 1:
              press2()
          if i == 1 and i5 == 1:
              press7()

          #Jogar aleatoriamente
          random_ = 1
          if(i>1) and random_ == 1 and (i%2)==1:
          #if random_ == 1 and (i%2)==1:
                while True:
                  move = random.randint(1,9)
                  if move == 1 and i1 == 0:
                      press1() 
                      break
                  if move == 2 and i2 == 0:
                      press2() 
                      break
                  if move == 3 and i3 == 0:
                      press3() 
                      break  
                  if move == 4 and i4 == 0:
                      press4() 
                      break
                  if move == 5 and i5 == 0:
                      press5() 
                      break
                  if move == 6 and i6 == 0:
                      press6() 
                      break
                  if move == 7 and i7 == 0:
                      press7() 
                      break
                  if move == 8 and i8 == 0:
                      press8()
                      break 
                  if move == 9 and i9 == 0:
                      press9() 
                      break
              
            
     #Funções de cada botão      
     def press1():
           global i
           global i1
           if (i%2)==0 and i1 == 0:      
            button1['text'] = 'X'
            i += 1 
            i1 =1 
           if (i%2)==1 and i1 == 0:      
            button1['text'] = 'O' 
            i += 1  
            i1 = 2 
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()   

     def press2():  
           global i
           global i2
           if (i%2)==0 and i2 == 0:      
            button2['text'] = 'X'
            i += 1 
            i2 =1 
           if (i%2)==1 and i2 == 0:      
            button2['text'] = 'O' 
            i += 1  
            i2 = 2
           game_over = gameover() 
           if game_over == 0:
             algoritmo ()      

     def press3():  
           global i
           global i3
           if (i%2)==0 and i3 == 0:      
            button3['text'] = 'X'
            i += 1 
            i3 =1 
           if (i%2)==1 and i3 == 0:      
            button3['text'] = 'O' 
            i += 1  
            i3 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()        

     def press4():  
           global i
           global i4
           if (i%2)==0 and i4 == 0:      
            button4['text'] = 'X'
            i += 1 
            i4 =1 
           if (i%2)==1 and i4 == 0:      
            button4['text'] = 'O' 
            i += 1  
            i4 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()       

     def press5():  
           global i
           global i5
           if (i%2)==0 and i5 == 0:      
            button5['text'] = 'X'
            i += 1 
            i5 =1 
           if (i%2)==1 and i5 == 0:      
            button5['text'] = 'O' 
            i += 1  
            i5 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()    

     def press6():  
           global i
           global i6
           if (i%2)==0 and i6 == 0:      
            button6['text'] = 'X'
            i += 1 
            i6 =1 
           if (i%2)==1 and i6 == 0:      
            button6['text'] = 'O' 
            i += 1  
            i6 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()

     def press7():  
           global i
           global i7
           if (i%2)==0 and i7 == 0:      
            button7['text'] = 'X'
            i += 1 
            i7 =1 
           if (i%2)==1 and i7 == 0:      
            button7['text'] = 'O' 
            i += 1  
            i7 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()   

     def press8():  
           global i
           global i8
           if (i%2)==0 and i8 == 0:      
            button8['text'] = 'X'
            i += 1 
            i8 =1 
           if (i%2)==1 and i8 == 0:      
            button8['text'] = 'O' 
            i += 1  
            i8 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()      
     def press9():  
           global i
           global i9
           if (i%2)==0 and i9 == 0:      
            button9['text'] = 'X'
            i += 1 
            i9 =1 
           if (i%2)==1 and i9 == 0:      
            button9['text'] = 'O' 
            i += 1  
            i9 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()   


     """    if (i%2)==1:
          def press1():  
           button1['text'] = 'O'

          def press2():  
           button2['text'] = 'O'

          def press3():  
           button3['text'] = 'O'
          def press4():  
           button4['text'] = 'O'
          def press5():  
           button5['text'] = 'O'
          def press6():  
           button6['text'] = 'O'
          def press7():  
           button7['text'] = 'O'
          def press8():  
           button8['text'] = 'O'
          def press9():  
           button9['text'] = 'O' """
     
     
     window = Tk() 
     window.title("Tic-Tac-Toe")
     window.configure(width=900, height=600)
     window.configure(bg='white')
     window.eval('tk::PlaceWindow . center')
     #window.geometry("900x600")
     master = Canvas(window, width=1000, height=800)
     master.configure(bg='white')

     button1=Button(master, text= " ", height = 10, width = 20,command = press1)
     """ photo = PhotoImage(file = r"C:/home/vascao/projeto/x_image.png") 
     photoimage = photo.subsample(3, 3)
     button1=Button(master, height = 10, width = 20, image = photoimage,
                    compound = LEFT) """

     button2=Button(master, text=" ",height = 10, width = 20 ,command = press2)

     button3=Button(master, text=" ", height = 10, width = 20, command = press3)

     button4=Button(master, text=" ", height = 10, width = 20, command = press4)

     button5=Button(master, text=" ", height = 10, width = 20, command = press5)

     button6=Button(master, text=" ", height = 10, width = 20, command = press6)

     button7=Button(master, text=" ", height = 10, width = 20, command = press7)

     button8=Button(master, text=" ", height = 10, width = 20, command = press8)

     button9=Button(master, text=" ", height = 10, width = 20, command = press9)

     button1.place(x=150, y=100)
     button2.place(x=450, y=100)
     button3.place(x=750, y=100)
     button4.place(x=150, y=300)
     button5.place(x=450, y=300)
     button6.place(x=750, y=300)
     button7.place(x=150, y=500)
     button8.place(x=450, y=500)
     button9.place(x=750, y=500)

     master.create_line(400, 25, 400, 750, width = 10)
     master.create_line(700, 25, 700, 750, width = 10)
     master.create_line(100, 290, 975, 290, width = 10)
     master.create_line(100, 490, 975, 490, width = 10)

     master.pack()

     window.mainloop() 
    
    ################################### Computador joga primeiro ####################################################

    if first == 1:
     #so chamando funcoes é que tens um loop
     def quit (): #fecha o programa
               exit()
               
     def objectdestroy (): #destroi objetos
            window.destroy()


     def gameover(): # condições para o jogo acabar
           def restart ():
               popup.destroy()
               objectdestroy()
               restart_global()

           if i1 == i4 == i7 ==1 or i2 == i5 == i8 ==1 or i3 == i6 == i9 ==1 or i1 == i2 == i3 ==1 or i4 == i5 == i6 ==1 or i7 == i8 == i9 ==1 or i1 == i5 == i9 ==1 or i7 == i5 == i3 ==1 :
               master.configure(bg='black')
               button1['text'] = 'G'
               button2['text'] = 'A'
               button3['text'] = 'M'
               button4['text'] = 'E'
               button5['text'] = 'O'
               button6['text'] = 'V'
               button7['text'] = 'E'
               button8['text'] = 'R'
               button9['text'] = '!'
               popup = Tk() 
               popup.title(" Game Over ")
               popup.configure(width=300, height=300)
               popup.configure(bg='white')
               popup.eval('tk::PlaceWindow . center')
               label=Label(popup,text=" X won! ",font=(50), bg="white",fg="black")
               button_restart=Button(popup, text= " Restart", height = 10, width = 10,command = restart)
               button_quit=Button(popup, text=" Quit ",height = 10, width = 10 ,command = quit)
               label.pack()
               button_restart.pack()
               button_quit.pack()
               return 1
          

           if i1 == i4 == i7 ==2 or i2 == i5 == i8 ==2 or i3 == i6 == i9 ==2 or i1 == i2 == i3 ==2 or i4 == i5 == i6 ==2 or i7 == i8 == i9 ==2 or i1 == i5 == i9 ==2 or i7 == i5 == i3 ==2 :
               master.configure(bg='black')
               button1['text'] = 'G'
               button2['text'] = 'A'
               button3['text'] = 'M'
               button4['text'] = 'E'
               button5['text'] = 'O'
               button6['text'] = 'V'
               button7['text'] = 'E'
               button8['text'] = 'R'
               button9['text'] = '!'
               popup = Tk() 
               popup.title(" Game Over ")
               popup.configure(width=300, height=300)
               popup.configure(bg='white')
               popup.eval('tk::PlaceWindow . center')
               label=Label(popup,text=" O won! ",font=(100), bg="white",fg="black")
               button_restart=Button(popup, text= " Restart", height = 10, width = 10,command = restart)
               button_quit=Button(popup, text=" Quit ",height = 10, width = 10 ,command = quit)
               label.pack()
               button_restart.pack()
               button_quit.pack()
               return 1
           elif i >=9 :
               master.configure(bg='black')
               button1['text'] = 'G'
               button2['text'] = 'A'
               button3['text'] = 'M'
               button4['text'] = 'E'
               button5['text'] = 'O'
               button6['text'] = 'V'
               button7['text'] = 'E'
               button8['text'] = 'R'
               button9['text'] = '!'
               popup = Tk() 
               popup.title(" Game Over ")
               popup.configure(width=300, height=300)
               popup.configure(bg='white')
               popup.eval('tk::PlaceWindow . center')
               label=Label(popup,text=" Tie ",font=(100), bg="white",fg="black")
               button_restart=Button(popup, text= " Restart", height = 10, width = 10,command = restart)
               button_quit=Button(popup, text=" Quit ",height = 10, width = 10 ,command = quit)
               label.pack()
               button_restart.pack()
               button_quit.pack()
               return 1
           else:
             return 0

     
     def algoritmo (): #define jogada do computador

          #Jogar aleatoriamente
          random_ = 1
          if(i>0) and random_ == 1 and (i%2)==0:
          #if random_ == 1 and (i%2)==1:
                while True:
                  move = random.randint(1,9)
                  if move == 1 and i1 == 0:
                      press1() 
                      break
                  if move == 2 and i2 == 0:
                      press2() 
                      break
                  if move == 3 and i3 == 0:
                      press3() 
                      break  
                  if move == 4 and i4 == 0:
                      press4() 
                      break
                  if move == 5 and i5 == 0:
                      press5() 
                      break
                  if move == 6 and i6 == 0:
                      press6() 
                      break
                  if move == 7 and i7 == 0:
                      press7() 
                      break
                  if move == 8 and i8 == 0:
                      press8()
                      break 
                  if move == 9 and i9 == 0:
                      press9() 
                      break
              
            
     #Funções de cada botão    
     def press1():
           global i
           global i1
           if (i%2)==0 and i1 == 0:      
            button1['text'] = 'X'
            i += 1 
            i1 =1 
           if (i%2)==1 and i1 == 0:      
            button1['text'] = 'O' 
            i += 1  
            i1 = 2 
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()   

     def press2():  
           global i
           global i2
           if (i%2)==0 and i2 == 0:      
            button2['text'] = 'X'
            i += 1 
            i2 =1 
           if (i%2)==1 and i2 == 0:      
            button2['text'] = 'O' 
            i += 1  
            i2 = 2
           game_over = gameover() 
           if game_over == 0:
             algoritmo ()      

     def press3():  
           global i
           global i3
           if (i%2)==0 and i3 == 0:      
            button3['text'] = 'X'
            i += 1 
            i3 =1 
           if (i%2)==1 and i3 == 0:      
            button3['text'] = 'O' 
            i += 1  
            i3 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()        

     def press4():  
           global i
           global i4
           if (i%2)==0 and i4 == 0:      
            button4['text'] = 'X'
            i += 1 
            i4 =1 
           if (i%2)==1 and i4 == 0:      
            button4['text'] = 'O' 
            i += 1  
            i4 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()       

     def press5():  
           global i
           global i5
           if (i%2)==0 and i5 == 0:      
            button5['text'] = 'X'
            i += 1 
            i5 =1 
           if (i%2)==1 and i5 == 0:      
            button5['text'] = 'O' 
            i += 1  
            i5 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()    

     def press6():  
           global i
           global i6
           if (i%2)==0 and i6 == 0:      
            button6['text'] = 'X'
            i += 1 
            i6 =1 
           if (i%2)==1 and i6 == 0:      
            button6['text'] = 'O' 
            i += 1  
            i6 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()

     def press7():  
           global i
           global i7
           if (i%2)==0 and i7 == 0:      
            button7['text'] = 'X'
            i += 1 
            i7 =1 
           if (i%2)==1 and i7 == 0:      
            button7['text'] = 'O' 
            i += 1  
            i7 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()   

     def press8():  
           global i
           global i8
           if (i%2)==0 and i8 == 0:      
            button8['text'] = 'X'
            i += 1 
            i8 =1 
           if (i%2)==1 and i8 == 0:      
            button8['text'] = 'O' 
            i += 1  
            i8 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()      
     def press9():  
           global i
           global i9
           if (i%2)==0 and i9 == 0:      
            button9['text'] = 'X'
            i += 1 
            i9 =1 
           if (i%2)==1 and i9 == 0:      
            button9['text'] = 'O' 
            i += 1  
            i9 = 2   
           game_over = gameover() 
           if game_over == 0:
            algoritmo ()   


     """    if (i%2)==1:
          def press1():  
           button1['text'] = 'O'

          def press2():  
           button2['text'] = 'O'

          def press3():  
           button3['text'] = 'O'
          def press4():  
           button4['text'] = 'O'
          def press5():  
           button5['text'] = 'O'
          def press6():  
           button6['text'] = 'O'
          def press7():  
           button7['text'] = 'O'
          def press8():  
           button8['text'] = 'O'
          def press9():  
           button9['text'] = 'O' """
     
     
     window = Tk() 
     window.title("Tic-Tac-Toe")
     window.configure(width=900, height=600)
     window.configure(bg='white')
     window.eval('tk::PlaceWindow . center')
     #window.geometry("900x600")
     master = Canvas(window, width=1000, height=800)
     master.configure(bg='white')

     button1=Button(master, text= " ", height = 10, width = 20,command = press1)
     """ photo = PhotoImage(file = r"C:/home/vascao/projeto/x_image.png") 
     photoimage = photo.subsample(3, 3)
     button1=Button(master, height = 10, width = 20, image = photoimage,
                    compound = LEFT) """

     button2=Button(master, text=" ",height = 10, width = 20 ,command = press2)
     #button2.grid(row=1,column=2)

     button3=Button(master, text=" ", height = 10, width = 20, command = press3)
     #button3.grid(row=1,column=3)

     button4=Button(master, text=" ", height = 10, width = 20, command = press4)
     #button4.grid(row=2,column=1)

     button5=Button(master, text=" ", height = 10, width = 20, command = press5)
     #button5.grid(row=2,column=2)

     button6=Button(master, text=" ", height = 10, width = 20, command = press6)
     #button6.grid(row=2,column=3)

     button7=Button(master, text=" ", height = 10, width = 20, command = press7)
     #button7.grid(row=3,column=1)

     button8=Button(master, text=" ", height = 10, width = 20, command = press8)
     #button8.grid(row=3,column=2)

     button9=Button(master, text=" ", height = 10, width = 20, command = press9)
     #button9.grid(row=3,column=3)

     button1.place(x=150, y=100)
     button2.place(x=450, y=100)
     button3.place(x=750, y=100)
     button4.place(x=150, y=300)
     button5.place(x=450, y=300)
     button6.place(x=750, y=300)
     button7.place(x=150, y=500)
     button8.place(x=450, y=500)
     button9.place(x=750, y=500)

     master.create_line(400, 25, 400, 750, width = 10)
     master.create_line(700, 25, 700, 750, width = 10)
     master.create_line(100, 290, 975, 290, width = 10)
     master.create_line(100, 490, 975, 490, width = 10)
     
       

     master.pack()

     while True: # Ai's First move
                  move = random.randint(1,9)
                  if move == 1 and i1 == 0:
                      press1() 
                      break
                  if move == 2 and i2 == 0:
                      press2() 
                      break
                  if move == 3 and i3 == 0:
                      press3() 
                      break  
                  if move == 4 and i4 == 0:
                      press4() 
                      break
                  if move == 5 and i5 == 0:
                      press5() 
                      break
                  if move == 6 and i6 == 0:
                      press6() 
                      break
                  if move == 7 and i7 == 0:
                      press7() 
                      break
                  if move == 8 and i8 == 0:
                      press8()
                      break 
                  if move == 9 and i9 == 0:
                      press9() 
                      break

     window.mainloop() 


