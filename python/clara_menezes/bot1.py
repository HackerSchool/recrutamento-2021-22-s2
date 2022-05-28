import random 
greetings1 = ("Helloooo!", "Heyo", "Hi!", "Salut", "Hola!")
greetings2 = ("Nice to meet you", "Funny name", "Good to see you ", "Can't wait to get to know you")
goodbye= ("Bye!", "See you.", "Okay bye then!", "Talk to you later!", "Adios!")
ask_me = ("Ask me a question", "Let's chat! Ask me anything about myself", "Ask me something", "What do you wanna know about me?")
ask_you = ("How about you?", "How old are you?", "Are you having fun?", "Why do you hate me?", "Do you hate me, be honest")
error = ("I baby. i dont understand", "My mom didnt teach me that yet", "Ngl, I have no clue what you just said", "Please say something simple", "hEhe what?", "ask me about the weather or something")

keyphrases = ("your name", "your age", "old","how are", "feel", "weather", "know", "robot", "friends", "yes", "no")

associations = { "your name": ["My name is babyBot01", "I am babyBot01", "My mom named me babyBot01"],
                "your age": ["I am 1 week old", "Roughly 7 days old", "I've been existing for about a week"],
                "old":["I am 1 week old", "Roughly 7 days old", "I've been existing for about a week"],
                "how are":["Personally, I've felt better ngl", "This AI life sucks", "I dont know how i feel, im barely even a bot"],
                "feel": ["Personally, I've felt better ngl", "This AI life sucks", "I dont know how i feel, im barely even a bot"],
                "weather": ["The weather today sucks imo", "I'ts not sunny is it?", "I think it's gonna rain"],
                "know": ["I know nothing atm", "I wish i knew stuff", "I am so dumb i dont know anything" ],
                "robot": ["I think robots are gonna take over the planet one day?", "I want to watch that iRobot movie sometime"],
                "friends": ["Have you seen friends, the show?", "My best friend is a mouse :(", "I once heard that friends are like avocados", "Would u like to be my friend?", "Are we friends?"],
                "yes": ["Nice", "Thats interesting i guess", "Lol", "How come?", "Why tho?", "What do you mean?"],
                "friend": ["Have you seen friends, the show?", "My best friend is a mouse :(", "I once heard that friends are like avocados", "Would u like to be my friend?", "Are we friends?"],
                "no": ["Do you say no to everything?", "You should say yes more", "In which ways do you mean that?"]}

def simplify(user_input):

   
       user_input = user_input.lower()
   
       for keyphrase in keyphrases: 
            if keyphrase in user_input:
                return keyphrase, True
 
       return user_input, False



def main():
    print("\n Welcome to the chat. You will be talking to a baby bot who doesn't yet understand human language very well. Please be kind to the baby. \n Ask them questions!\n")
    print("PS: To stop talking to bot1 type exit(). Tell him your name first though.\n")
    print("\t",random.choice(greetings1), "\n")
    name = input("\t What's your name?\n").split(" ")[-1]
    print("\t",random.choice(greetings2),name, "!")
    print("\t",random.choice(ask_me))
    user_input = input()
    while user_input != "exit()":
        
        user_input = simplify(user_input)

        if user_input[1] == True:
            print("\t",random.choice(associations[user_input[0]]))
            print("\t",random.choice(ask_you))
        else:
            print("\t",random.choice(error))
            print("\t",random.choice(ask_me))
        user_input = input()
        
        
    else: 
        print("\t", random.choice(goodbye))

if __name__ == "__main__":
  main()

