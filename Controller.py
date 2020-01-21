from PyQt5 import QtCore, QtGui, QtWidgets
import os
from Model.LoginUser import Login



#use this class to control the main class
class MainController:
    def __init__(self, startFrame):
        self.mainFrame = startFrame
        self.mainFrame.raise_()
        self.userSession = ""
        self.SessionHist()


    def ChangeFrame(self):
        pass

    def SessionHist(self):
        self.sessionID = self.userSession
        self.inputHistory = ["main"]

    def LoginClicked(self,main):
        main.LoginView.raise_()
        self.inputHistory.append("login")
        self.attempt = Login()
        self.attempt.uName = self.getText(main.UnameLogin)
        self.attempt.pwd = self.getText(main.PwdLogin)

        self.attempt.login()

        if self.attempt.loginUnsuccessful:
            main.Title.setText("Try again")

        else:
            main.Title.setText(self.attempt.UserID)
            self.sessionID = self.attempt.UserID

    def CreateAccountClicked(self, main):
        main.CreateAccountView.raise_()


        newAccount = Login().CreateAccount(self.getText(main.uNameText_2),self.getText(main.pwdText_2),
                                         self.getText(main.EmailText_2), self.getText(main.fNameText_2),
                                         self.getText(main.lNameText_2))

        if newAccount == "success":
            main.LoginView.raise_()

        else:
            return





    def getText(self, QTextEdit):
        return str(QTextEdit.toPlainText())

    def Version(self):
        pass



if __name__ == "__main__":
    import sys
    import os

    #To get the full path to the directory a Python file is contained in, write this in that file
    #gets current path of file
    print(os.path.dirname(os.path.realpath((__file__))))



    #print(os.stat(str(os.getcwd())+"\\%s"%os.listdir()[0]))
    #print(list(os.walk("\\".join(os.getcwd().split("\\")))))#[:3]))
    #print(list(os.walk("\\".join(os.getcwd().split("\\")[:3]))))








