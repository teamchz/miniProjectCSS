# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rps.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random
from main import *


class Ui_RPS(object):

    global player_score
    global npc_score
    player_score = 0
    npc_score = 0

    def setupRPS(self, RPS):
        RPS.setObjectName("Form")
        RPS.resize(800, 600)
        RPS.setMinimumSize(QtCore.QSize(800, 600))
        RPS.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(28)
        RPS.setFont(font)
        RPS.setStyleSheet("background-color: rgb(199, 206, 234);")
        self.label = QtWidgets.QLabel(RPS)
        self.label.setGeometry(QtCore.QRect(120, 30, 531, 91))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 0, 127);")
        self.label.setObjectName("label")
        self.p_pic = QtWidgets.QLabel(RPS)
        self.p_pic.setGeometry(QtCore.QRect(50, 240, 321, 269))
        self.p_pic.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.p_pic.setText("")
        self.p_pic.setObjectName("p_pic")
        self.n_pic = QtWidgets.QLabel(RPS)
        self.n_pic.setGeometry(QtCore.QRect(434, 241, 321, 271))
        self.n_pic.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.n_pic.setText("")
        self.n_pic.setObjectName("n_pic")
        self.label_5 = QtWidgets.QLabel(RPS)
        self.label_5.setGeometry(QtCore.QRect(590, 540, 100, 48))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.p_score = QtWidgets.QLabel(RPS)
        self.p_score.setGeometry(QtCore.QRect(220, 544, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.p_score.setFont(font)
        self.p_score.setObjectName("p_score")
        self.n_score = QtWidgets.QLabel(RPS)
        self.n_score.setGeometry(QtCore.QRect(710, 540, 171, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.n_score.setFont(font)
        self.n_score.setObjectName("n_score")
        self.result = QtWidgets.QLabel(RPS)
        self.result.setGeometry(QtCore.QRect(340, 520, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.widget = QtWidgets.QWidget(RPS)
        self.widget.setGeometry(QtCore.QRect(30, 150, 731, 59))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 154, 162);\n"
                                      "color: rgb(170, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(226, 240, 203);\n"
                                        "color: rgb(0, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(162, 215, 234);\n"
                                        "color: rgb(0, 0, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.label_4 = QtWidgets.QLabel(RPS)
        self.label_4.setGeometry(QtCore.QRect(50, 540, 150, 48))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(RPS)
        QtCore.QMetaObject.connectSlotsByName(RPS)

    def retranslateUi(self, RPS):
        _translate = QtCore.QCoreApplication.translate
        RPS.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "rock paper scissors game"))
        self.label_5.setText(_translate("Form", "NPC: "))
        self.p_score.setText(_translate("Form", "0"))
        self.n_score.setText(_translate("Form", "0"))
        self.pushButton.setText(_translate("Form", "rock"))
        self.pushButton_2.setText(_translate("Form", "paper"))
        self.pushButton_3.setText(_translate("Form", "scissors"))
        self.label_4.setText(_translate("Form", "PLAYER:"))
        self.pushButton.clicked.connect(self.rock_click)
        self.pushButton_2.clicked.connect(self.paper_click)
        self.pushButton_3.clicked.connect(self.scissors_click)

    def rock_click(self):
        self.p_pic.setPixmap(QtGui.QPixmap("Rock.png"))
        roll = random.randint(1, 3)
        global player_score, npc_score

        if (roll == 1):
            self.n_pic.setPixmap(QtGui.QPixmap("Rock.png"))
            self.result.setText("Draw")
        elif (roll == 2):
            self.n_pic.setPixmap(QtGui.QPixmap("Paper.png"))
            npc_score += 1
            self.result.setText("Lose")
        elif (roll == 3):
            self.n_pic.setPixmap(QtGui.QPixmap("Scissors.png"))
            player_score += 1
            self.result.setText("Win")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.p_score.setText(str(player_score))
        self.n_score.setText(str(npc_score))

    def paper_click(self):
        self.p_pic.setPixmap(QtGui.QPixmap("Paper.png"))
        roll = random.randint(1, 3)
        global player_score, npc_score
        if (roll == 1):
            self.n_pic.setPixmap(QtGui.QPixmap("Rock.png"))
            player_score += 1
            self.result.setText("Win")
        elif (roll == 2):
            self.n_pic.setPixmap(QtGui.QPixmap("Paper.png"))
            self.result.setText("Draw")
        elif (roll == 3):
            self.n_pic.setPixmap(QtGui.QPixmap("Scissors.png"))
            npc_score += 1
            self.result.setText("Lose")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.p_score.setText(str(player_score))
        self.n_score.setText(str(npc_score))

    def scissors_click(self):
        self.p_pic.setPixmap(QtGui.QPixmap("Scissors.png"))
        roll = random.randint(1, 3)
        global player_score, npc_score
        if (roll == 1):
            self.n_pic.setPixmap(QtGui.QPixmap("Rock.png"))
            npc_score += 1
            self.result.setText("Lose")
        elif (roll == 2):
            self.n_pic.setPixmap(QtGui.QPixmap("Paper.png"))
            player_score += 1
            self.result.setText("Win")
        elif (roll == 3):
            self.n_pic.setPixmap(QtGui.QPixmap("Scissors.png"))
            self.result.setText("Draw")

        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.p_score.setText(str(player_score))
        self.n_score.setText(str(npc_score))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RPS = QtWidgets.QWidget()
    ui = Ui_RPS()
    ui.setupRPS(RPS)
    RPS.show()
    sys.exit(app.exec_())