from PyQt5 import QtCore, QtGui, QtWidgets
from hangman import *
from rps_game import *
from tictactoe2p import *
from tictaetoeeasy import *
import random

'''
นายคณานนท์ ก้ามจำรูญ 63090500420
นายนิติพัฒน์ ศรีธระชิยานนท์ 63090500426 
นายพิษณุ บุญญาอนันต์ 63090500429
นายพรพล ต้ังอดุลย์รัตน์ 63090500439
'''


class Ui_Form(object):

    def hangman(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_Hangman()
        self.ui.setupHangman(self.window)
        self.window.show()


    def rps(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_RPS()
        self.ui.setupRPS(self.window)
        self.window.show()

    def TTT2P(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_TTT2P()
        self.ui.setupTTT2P(self.window)
        self.window.show()

    def TTT(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TTT()
        self.ui.setupTTT(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Sembold")
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setStyleSheet("background-image: url(:/newPrefix/rocket.png);")
        self.goto_RSP = QtWidgets.QPushButton(Form)
        self.goto_RSP.setGeometry(QtCore.QRect(70, 210, 171, 241))
        self.goto_RSP.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.goto_RSP.setStyleSheet("background-image: url(:/newPrefix/rsp2.png);")
        self.goto_RSP.setText("")
        self.goto_RSP.setObjectName("goto_RSP")
        self.goto_RSP.clicked.connect(self.rps)
        self.goto_TTT = QtWidgets.QPushButton(Form)
        self.goto_TTT.setGeometry(QtCore.QRect(300, 210, 171, 130))
        self.goto_TTT.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.goto_TTT.setText("1 PLAYER")
        self.goto_TTT.setObjectName("goto_TTT")
        self.goto_TTT.setStyleSheet("color: rgb(0, 255, 127);")
        self.goto_TTT.setStyleSheet("background-image: url(:/newPrefix/white.png);")
        self.goto_TTT.clicked.connect(self.TTT2P)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.goto_TTT.setFont(font)
        self.goto_TTT_2 = QtWidgets.QPushButton(Form)
        self.goto_TTT_2.setGeometry(QtCore.QRect(300, 340, 171, 120))
        self.goto_TTT_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.goto_TTT_2.setText("2 PLAYERS")
        self.goto_TTT_2.setObjectName("goto_TTT_2")
        self.goto_TTT_2.setStyleSheet("color: rgb(0, 255, 127);")
        self.goto_TTT_2.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.goto_TTT_2.setStyleSheet("background-image: url(:/newPrefix/white.png);")
        self.goto_TTT_2.clicked.connect(self.TTT)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.goto_TTT_2.setFont(font)
        self.goto_hangman = QtWidgets.QPushButton(Form)
        self.goto_hangman.setGeometry(QtCore.QRect(530, 210, 171, 241))
        self.goto_hangman.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.goto_hangman.setStyleSheet("background-image: url(:/newPrefix/hm.png);")
        self.goto_hangman.setText("")
        self.goto_hangman.setObjectName("goto_hangman")
        self.goto_hangman.clicked.connect(self.hangman)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(70, 450, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(85, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 450, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 450, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 0, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(130, 10, 531, 144))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 0, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(226, 193, 5);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "rock paper scissors"))
        self.pushButton_2.setText(_translate("Form", "tic tac toe"))
        self.pushButton_3.setText(_translate("Form", "hangman"))
        self.label.setText(_translate("Form", "Rocket"))
        self.label_2.setText(_translate("Form", "Games"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
