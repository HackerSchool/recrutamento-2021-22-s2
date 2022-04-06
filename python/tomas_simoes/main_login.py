import datetime
import random
import mysql.connector
from twilio.rest import Client
from passlib.hash import pbkdf2_sha256
import bcrypt
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow
from recovery_dialog import Ui_Dialog

import tictactoe

### Variables
account_sid = ""  # Twilio Account SID
auth_token = ""  # Twilio Authentication Token

iterations = 200000


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.actionQuit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.about)
        self.forgot_password_button.clicked.connect(self.recoveryDialog)
        self.login_button.clicked.connect(lambda: self.login_register_helper("login"))
        self.register_button.clicked.connect(lambda: self.login_register_helper("register"))
        self.exit_button.clicked.connect(self.close)

    def recoveryDialog(self):
        dialog = recoveryDialog(self)
        dialog.exec()

    def login_register_helper(self, type):
        cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='logininfo')
        cursor = cnx.cursor()
        client = Client(account_sid, auth_token)

        number = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()

        if type == "login":
            self.login(cursor, client)
        if type == "register":
            self.register(cursor, client, cnx)

    def login(self, cursor, client):
        number = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()
        
        query = ("SELECT * FROM credentials "
                 "WHERE number= %s")
        cursor.execute(query, (number, ))

        if len(cursor.fetchall()) == 0:
            self.error("Invalid number. Are you registered?")
        else:
            query = ("SELECT iterations, salt, hash FROM credentials WHERE number=%s")
            cursor.execute(query, (number, ))

            for (iterations, salt, hash) in cursor:
                byted_salt = str.encode(salt)
                calculated_hash = pbkdf2_sha256.encrypt(password, rounds=int(iterations), salt=byted_salt)
                if calculated_hash == hash:
                    self.open_tictactoe()

                else:
                    self.error("Wrong password!")


    def register(self, cursor, client, cnx):
        number = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()

        query = ("SELECT * FROM credentials "
                 "WHERE number= %s")
        cursor.execute(query, (number, ))

        if len(cursor.fetchall()) != 0:
            self.error("Number is alredy registered.")
        else:
            try:
                casted_number = int(number)
                passed = True
            except ValueError:
                passed = False
            if (passed != True or len(number) != 9):
                self.error("Invalid number!")

            add_credential = ("INSERT INTO credentials (number, hash, created, salt, iterations) VALUES (%s, %s, %s, %s, %s)")

            salt = bcrypt.gensalt()
            hashedpassword = pbkdf2_sha256.encrypt(password, rounds=iterations, salt=salt)
            cursor.execute(add_credential, (number, hashedpassword, datetime.date.today(), salt, iterations))
            cnx.commit()
            self.confirmation("Account Registered!")

    def confirmation(self, message):
        QMessageBox.information(self, "Confirmation", message)

    def error(self, message):
        QMessageBox.critical(self, "Error", message)

    def about(self):
        QMessageBox.about(
            self,
            "About Aplicação Fixe",
            "<p>Construído com</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>"
            "<p>- MySQL</p>"
            "<p>- Twilio</p>"
            "<p>- Passlib</p>"
            "<p>- Bcrypt</p>",
        )

    def open_tictactoe(self):
        self.close()
        self.Open = tictactoe.tictactoe()
        self.Open.show()

class recoveryDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.buttonBox.rejected.connect(self.close)
        self.send_code_button.clicked.connect(self.send_code)
        self.submit_button.clicked.connect(self.change_password)

    def send_code(self):
        cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='logininfo')
        cursor = cnx.cursor()
        client = Client(account_sid, auth_token)
        number = self.number_edit.toPlainText()

        try:
            casted_number = int(number)
            passed = True
        except ValueError:
            passed = False

        if (passed != True or len(number) != 9):
            self.error("Invalid number!")
        else:
            query = ("SELECT * FROM credentials "
            "WHERE number= %s")
            cursor.execute(query, (number, ))

            if len(cursor.fetchall()) == 0:
                self.error("Invalid number. Are you registered?")
            else:
                # Global variables *should* be avoided, however, there isn't much else to do in this instance.
                global most_recent_code
                most_recent_code = random.randint(0, 99999)

                msg_body="Your code is: " + str(most_recent_code)

                message = client.messages.create(
                to="+351"+number, 
                from_="+13192532439",
                body=msg_body)
                self.confirmation("Code sent!")

    def change_password(self):
        cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='logininfo')
        cursor = cnx.cursor()
        
        number = self.number_edit.toPlainText()
        password = self.new_password_edit.toPlainText()
        code = self.code_edit.toPlainText()

        if int(code) != most_recent_code:
            self.error("Wrong code!")
        else:
            salt = bcrypt.gensalt()
            hashedpassword = pbkdf2_sha256.encrypt(password, rounds=iterations, salt=salt)
            query = ("UPDATE credentials SET hash=%s, salt=%s WHERE number=%s")
            cursor.execute(query, (hashedpassword, salt, number))
            cnx.commit()
            self.confirmation("Password changed!")

    def confirmation(self, message):
        QMessageBox.information(self, "Confirmation", message)

    def error(self, message):
        QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
