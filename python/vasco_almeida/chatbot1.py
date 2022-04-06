import random
import webbrowser
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def chatbot_func():
     print(''' 
    ----------ChatBot---------- \n
 ChatBot: Hi! What's your name?
     ''') 
     name = input(" Me: ")

     print(" \n ChatBot: Hi " + name + ", nice to meet you! \n" )
     #f"Hi {name}, nice to meet you! \n"
     r1 = 0
     while True:
                  move = random.randint(1,3)
                  if move == 1 :
                      print(" ChatBot: What sports do you play? ") 
                      r1 = 1
                      break
                  if move == 2 :
                      print(" ChatBot: What do you do for a living? ") 
                      break
                  if move == 3 :
                    print(" ChatBot: What are your hobbies?") 
                    break 
     while True: 
      response1=input(" \n Me: ")
      if response1 == "nothing" or response1 == "Nothing" or response1 == "bye" or response1=="Bye" or (response1 == 'n') or (response1 == 'no') or (response1 == 'N') or (response1 == 'No') or (response1 == 'NO'):
        print("\n ChatBot: Oh ok:( \n ChatBot: It was nice talking to you, "+ name + ".\n ChatBot: See you next time! \n")
        return 0
      while True:
                  move = random.randint(1,3)
                  if move == 1 :
                      print("\n ChatBot: Wow "+ name+ ", that's so cool!") 
                      break
                  if move == 2 :
                      print("\n ChatBot: Great, " + name +"!") 
                      break
                     
      pesquisa = response1
      print(" ChatBot: This is what I found out about that: \n\n     (Please wait a few seconds) \n")
      for j in search(pesquisa, tld="co.in", num=1, stop=1, pause=1):
       #print("\n " + j) #print url
       webbrowser.open(j)
     
      i = 1
      while True:
       i += 1
       print("\n ChatBot: Was this relevant to our conversation? \n")
       opcao_q = input("\n Me: ")

       if (opcao_q == 'Y') or (opcao_q == 'yes') or (opcao_q == 'y') or (opcao_q == 'Yes') or (opcao_q == 'YES'):
        print(" \n ChatBot: Nice! What else would you like to talk about, " + name+ "? ")
        i=1
        break
       elif (opcao_q == 'n') or (opcao_q == 'no') or (opcao_q == 'N') or (opcao_q == 'No') or (opcao_q == 'NO'):
        print(" \n ChatBot: Sorry to hear that, "+ name + ". Maybe this will be more pertinent:\n ")
        for j in search(pesquisa, tld="co.in", num=5, stop=i, pause=i):
         webbrowser.open(j)


     
                 
  

    


     


