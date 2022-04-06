# coding=utf-8
class Register():
    '''
    Classe com métodos necessários para fazer registo na plataforma
    '''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #Método que introduz o username e respetiva password na db
    def create_user(self):
        db = open("database.txt", "a")
        db.write('\n' + self.username + ', ' + self.password)
        print("Utilizador Registado!")
        db.close()