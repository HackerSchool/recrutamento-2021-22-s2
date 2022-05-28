import random
import time

def ttt():
    s = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    print_game(s)
        
    print("U are the Xs")
    
    first = random.randint(0,1)
    next_player = first
    
    game=False
    count=0
    while not game and count < 9:
        if next_player==0:
            print("My turn!")
            time.sleep(1.5)
            empty = False
            while not empty:
                i = random.randint(0,2)
                j = random.randint(0,2)
                empty = s[i][j]==' '
            s[i][j] = 'O'
            next_player = 1
            
        elif next_player==1:  
            p = input("Your turn:\n")
            i = int(p.split(',')[0])-1
            j = int(p.split(',')[1])-1
            empty = s[i][j]==' '
            while not empty:
                p = input("That cell is already ocupied, try another one:\n")
                i = int(p.split(',')[0])-1
                j = int(p.split(',')[1])-1
                empty = s[i][j]==' '
            s[i][j] = 'X'
            next_player = 0
            
        count+=1
        game = win(s)
        print_game(s)
        
    if game and next_player==0:
        print("YOU WON!!!\n")
    elif game and next_player==1:
        print("You lost! :( \n")
    else:
        print("Draw!!")
        
        
def print_game(s):
    print(f"\n              |       |          \n\
          {s[0][0]}   |   {s[0][1]}   |   {s[0][2]}      \n\
       _______|_______|_______   \n\
              |       |          \n\
          {s[1][0]}   |   {s[1][1]}   |   {s[1][2]}      \n\
       _______|_______|_______   \n\
              |       |          \n\
          {s[2][0]}   |   {s[2][1]}   |   {s[2][2]}      \n\
              |       |          \n")
          
def win(s):
    aux = False
    for i in range(3):
        aux = aux or s[i][0]==s[i][1]==s[i][2]!=' '
    for j in range(3):
        aux = aux or s[0][j]==s[1][j]==s[2][j]!=' '
    aux = aux or s[0][0]==s[1][1]==s[2][2]!=' '
    aux = aux or s[0][2]==s[1][1]==s[2][0]!=' '
    return aux


#ttt()