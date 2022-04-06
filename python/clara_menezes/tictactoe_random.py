import random
import time

horizontal = "-----"

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
    return "O"
  elif winQ("X"):
    return "X"
  else:
    return "Tie"

def computer_play():
  aiplay = int(random.randint(1,9))
  while game[aiplay-1] != " ":
    aiplay = int(random.randint(1,9))
  else:
    return aiplay-1
    
 
def gameoverQ():
  if " " in game:
    return False
  else:
    return True


def main():
  global game
  game = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

  print("\nWelcome to the game of TicTacToe")
  print("You will be playing against the computer ")
  print("This is how the board will look like.")
  print("\n" + "1|2|3\n" +horizontal+"\n4|5|6\n" + horizontal + "\n6|7|8\n")
  print("To choose the position for each of your plays, select the number that marks the desired place.")
  print("Write exit() instead of a position to quit the game.")
  print("Would you like to play as X or as O ?")
  player = input("Player: ")
  player = player.upper()
  while player not in ["X","O"]:
    print("Choose X or O")
    player = input("Player: ")
  else:
    if player == "X":
      computer = "O"
    else:
      computer = "X"

    print("You'll be using "+player+"\nComputer is using " + computer) 
    while not gameoverQ() and not winQ("O") and not winQ("X"):
      
      print("\nChoose your play using the numbers.")
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
            game[int(play)-1] = player
      printgame()
      print("Computer's turn.")
      time.sleep(.75)
      if not gameoverQ() and not winQ("O") and not winQ("X"):
        game[computer_play()] = computer
        printgame()
      
    else:

      if announce_winner() in ["X","O"]:
        if announce_winner() == player:
          print("You won!")
        else:
          print("You lost.")
      else:
        print("Tie!")


if __name__ == "__main__":
  main()