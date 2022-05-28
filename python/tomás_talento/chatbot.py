import random
from datetime import datetime
import os
        
def pick_answer(answers):
    n = random.randint(0,len(answers)-1)
    return answers[n]
    
def generate_answer(question):
     file = open("chat_bot.txt", 'r')
     data = file.readlines()
     pdata = []
     for line in data:
         q_a = line.split(' - ')
         q = q_a[0].split('; ')
         a = q_a[1].split('; ')[:-1]
         pdata = pdata + [[q,a]]
     #print(pdata)
        
     aux1 = question.split('!')
     aux2 = aux1[0].split('?')
     aux3 = aux2[0].split('.')
     q_words = aux3[0].split(' ')
     #print(q_words)
     
     count=0
     for theme in pdata:
         count +=1
         q = theme[0]
         l2 = []
         for i in q:
             l1 = []
             for j in q_words:
                 l1 = l1 + [i==j]
             l2 = l2 + [any(l1)]
         #print(l2)
         
         if any(l2):
             a = theme[1]
             if a[0]=='001':
                 print("Opening spotify...")
                 os.system("spotify")
                 break
             elif a[0]=='002':
                 now = datetime.now()
                 current_time = now.strftime("%H:%M:%S")
                 print("Current Time is :", current_time)
                 break
             else:
                 print(pick_answer(a))
                 break
         elif count == len(pdata):
             print("I could't find a plausible answer try asking me something else like the weather")
             
     file.close()


#generate_answer('play some music')
