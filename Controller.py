from PyQt5 import QtCore, QtGui, QtWidgets
import os

class ChangeFrame:
    def __init__(self, currentQFrame):
        self.currentFrame = currentQFrame
        self.currentFrame.raise_()





class SessionHist:
    def __init__(self, userSession):
        self.sessionID = userSession
        self.inputHistory = ["main"]


class Version:
    def __init__(self):
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








