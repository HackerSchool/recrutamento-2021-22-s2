game = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
horizontal = "-----"
current_player = ""

def printgame():
  print("\n" + game[0]+"|"+ game[1]+"|" + game[2] +"\t 1|2|3\n" +horizontal+"\t "+horizontal+ "\n"+ game[3]+"|"+ game[4]+"|" + game[5]+ "\t 4|5|6\n" + horizontal + "\t " + horizontal + "\n"+ game[6]+"|"+ game[7]+"|"+ game[8]+"\t 7|8|9\n")

def winQ(s):
  # ha oito maneiras de ter ganho 
  if game[0] == game[1] == game[2] == s:
    return True
  elif game[3] == game[4] == game[5] == s:
    return True
  elif game[6] == game[7] == game[8] == s:
    return True
  elif game[0] == game[3] == game[6] == s:
    return True
  elif game[1] == game[4] == game[7] == s:
    return True
  elif game[2] == game[5] == game[8] == s:
    return True
  elif game[0] == game[4] == game[8] == s:
    return True
  elif game[2] == game[4] == game[6] == s:
    return True
  else:
    return False
 

# so deve ser chamada quando o jogo estiver completo, nesse caso, todo cheio 
def announce_winner():
  if winQ("O"):
    print("Winner is player O!")
  elif winQ("X"):
    print("Winner is player X!")
  else:
    print("Tie!")

def alternate_player():
  global current_player
  if current_player != "O":
     current_player = "O"
  else:
     current_player = "X"


def gameoverQ():
  if " " in game:
    return False
  else:
    return True


def main():

  print("\nWelcome to the game of TicTacToe")
  print("You should play with a friend on the console, one at a time. ")
  print("This is how the board will look like.")
  print("\n" + "1|2|3\n" +horizontal+"\n4|5|6\n" + horizontal + "\n6|7|8\n")
  print("To choose the position for each of your plays, select the number that marks the desired place.")
  print("Write exit() instead of a position to quit the game.")
  while not gameoverQ() and not winQ("O") and not winQ("X"):
    alternate_player()
    print("Current player: "+current_player+"\nChoose your play using the numbers.")
    play = input("Position: ")

    if play == "exit()":
        break
    else:
      while int(play) not in range(10):
        print("Invalid choice. Pick a position 1-9.")
        play = input("Position: ")
      else:
        while game[int(play)-1] != " ":
          print("Position in not available. Pick a different one.")
          play = input("Position: ")
        else:
          game[int(play)-1] = current_player

    printgame()
  else:
    announce_winner()


if __name__ == "__main__":
  main()