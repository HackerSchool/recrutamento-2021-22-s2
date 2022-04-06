# coding=utf-8

class Login():
    '''
    Classe com os métodos necessários para o login
    '''
    def __init__(self, user, password):
        self.username = user
        self.password = password
    
    def check_user(self):
        #Verificar se o username + password fazem parte da db
        user_in_db = self.username + ', ' + self.password
        db = open("database.txt", "r")
        for line in db:
            if user_in_db in line:
                db.close()
                return 1
        db.close()
        return 0
    
    #Método para mudar a password
    def change_password(self, nova_password):
        db = open("database.txt", "r")
        lines = db.readlines()
        db.close()
        db = open("database.txt", "w")
        user_in_db = self.username + ', ' + self.password
        #Escrever todas as linhas menos a que tem o user com pass obsoleta
        for line in lines:
            if line.strip('\n') != user_in_db:
                db.write(line)
        db.close()
        db = open("database.txt", "a")
        db.write('\n' + self.username + ', ' + nova_password)
        self.password = nova_password
        db.close()