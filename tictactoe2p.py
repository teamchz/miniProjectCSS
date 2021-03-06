# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
# UI


class Ui_TTT2P(object):
    global count, box
    count = 0
    box = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def setupTTT2P(self, TTT2P):
        TTT2P.setObjectName("TTT2P")
        TTT2P.setWindowModality(QtCore.Qt.NonModal)
        TTT2P.setEnabled(True)
        TTT2P.resize(800, 800)
        TTT2P.setMinimumSize(QtCore.QSize(800, 800))
        TTT2P.setMaximumSize(QtCore.QSize(800, 800))
        TTT2P.setMouseTracking(True)
        TTT2P.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(TTT2P)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setObjectName("centralwidget")
        self.lineh1 = QtWidgets.QFrame(self.centralwidget)
        self.lineh1.setEnabled(False)
        self.lineh1.setGeometry(QtCore.QRect(25, 200, 750, 3))
        self.lineh1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lineh1.setLineWidth(1)
        self.lineh1.setMidLineWidth(5)
        self.lineh1.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineh1.setObjectName("lineh1")
        self.lineh2 = QtWidgets.QFrame(self.centralwidget)
        self.lineh2.setEnabled(False)
        self.lineh2.setGeometry(QtCore.QRect(25, 400, 750, 3))
        self.lineh2.setStyleSheet("")
        self.lineh2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lineh2.setMidLineWidth(5)
        self.lineh2.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineh2.setObjectName("lineh2")
        self.linev1 = QtWidgets.QFrame(self.centralwidget)
        self.linev1.setEnabled(False)
        self.linev1.setGeometry(QtCore.QRect(265, 25, 3, 550))
        self.linev1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.linev1.setMidLineWidth(5)
        self.linev1.setFrameShape(QtWidgets.QFrame.VLine)
        self.linev1.setObjectName("linev1")
        self.linev2 = QtWidgets.QFrame(self.centralwidget)
        self.linev2.setEnabled(False)
        self.linev2.setGeometry(QtCore.QRect(534, 25, 3, 550))
        self.linev2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.linev2.setMidLineWidth(5)
        self.linev2.setFrameShape(QtWidgets.QFrame.VLine)
        self.linev2.setObjectName("linev2")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setEnabled(True)
        self.B1.setGeometry(QtCore.QRect(25, 25, 240, 175))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B1.setFont(font)
        self.B1.setMouseTracking(False)
        self.B1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B1.setAcceptDrops(False)
        self.B1.setToolTip("")
        self.B1.setText("")
        self.B1.setShortcut("")
        self.B1.setCheckable(False)
        self.B1.setChecked(False)
        self.B1.setAutoRepeat(False)
        self.B1.setAutoExclusive(False)
        self.B1.setDefault(False)
        self.B1.setFlat(True)
        self.B1.setObjectName("B1")
        self.B2 = QtWidgets.QPushButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(268, 25, 266, 175))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B2.setFont(font)
        self.B2.setMouseTracking(False)
        self.B2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B2.setAcceptDrops(False)
        self.B2.setToolTip("")
        self.B2.setText("")
        self.B2.setShortcut("")
        self.B2.setCheckable(False)
        self.B2.setChecked(False)
        self.B2.setAutoRepeat(False)
        self.B2.setAutoExclusive(False)
        self.B2.setDefault(False)
        self.B2.setFlat(True)
        self.B2.setObjectName("B2")
        self.B3 = QtWidgets.QPushButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(537, 25, 239, 175))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B3.setFont(font)
        self.B3.setMouseTracking(False)
        self.B3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B3.setAcceptDrops(False)
        self.B3.setToolTip("")
        self.B3.setText("")
        self.B3.setShortcut("")
        self.B3.setCheckable(False)
        self.B3.setChecked(False)
        self.B3.setAutoRepeat(False)
        self.B3.setAutoExclusive(False)
        self.B3.setDefault(False)
        self.B3.setFlat(True)
        self.B3.setObjectName("B3")
        self.B4 = QtWidgets.QPushButton(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(25, 203, 240, 197))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B4.setFont(font)
        self.B4.setMouseTracking(False)
        self.B4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B4.setAcceptDrops(False)
        self.B4.setToolTip("")
        self.B4.setText("")
        self.B4.setShortcut("")
        self.B4.setCheckable(False)
        self.B4.setChecked(False)
        self.B4.setAutoRepeat(False)
        self.B4.setAutoExclusive(False)
        self.B4.setDefault(False)
        self.B4.setFlat(True)
        self.B4.setObjectName("B4")
        self.B5 = QtWidgets.QPushButton(self.centralwidget)
        self.B5.setGeometry(QtCore.QRect(268, 203, 266, 197))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B5.setFont(font)
        self.B5.setMouseTracking(False)
        self.B5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B5.setAcceptDrops(False)
        self.B5.setToolTip("")
        self.B5.setText("")
        self.B5.setShortcut("")
        self.B5.setCheckable(False)
        self.B5.setChecked(False)
        self.B5.setAutoRepeat(False)
        self.B5.setAutoExclusive(False)
        self.B5.setDefault(False)
        self.B5.setFlat(True)
        self.B5.setObjectName("B5")
        self.B6 = QtWidgets.QPushButton(self.centralwidget)
        self.B6.setGeometry(QtCore.QRect(537, 203, 239, 197))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B6.setFont(font)
        self.B6.setMouseTracking(False)
        self.B6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B6.setAcceptDrops(False)
        self.B6.setToolTip("")
        self.B6.setText("")
        self.B6.setShortcut("")
        self.B6.setCheckable(False)
        self.B6.setChecked(False)
        self.B6.setAutoRepeat(False)
        self.B6.setAutoExclusive(False)
        self.B6.setDefault(False)
        self.B6.setFlat(True)
        self.B6.setObjectName("B6")
        self.B7 = QtWidgets.QPushButton(self.centralwidget)
        self.B7.setGeometry(QtCore.QRect(25, 403, 240, 173))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B7.setFont(font)
        self.B7.setMouseTracking(False)
        self.B7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B7.setAcceptDrops(False)
        self.B7.setToolTip("")
        self.B7.setText("")
        self.B7.setShortcut("")
        self.B7.setCheckable(False)
        self.B7.setChecked(False)
        self.B7.setAutoRepeat(False)
        self.B7.setAutoExclusive(False)
        self.B7.setDefault(False)
        self.B7.setFlat(True)
        self.B7.setObjectName("B7")
        self.B8 = QtWidgets.QPushButton(self.centralwidget)
        self.B8.setGeometry(QtCore.QRect(268, 403, 266, 173))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B8.setFont(font)
        self.B8.setMouseTracking(False)
        self.B8.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B8.setAcceptDrops(False)
        self.B8.setToolTip("")
        self.B8.setText("")
        self.B8.setShortcut("")
        self.B8.setCheckable(False)
        self.B8.setChecked(False)
        self.B8.setAutoRepeat(False)
        self.B8.setAutoExclusive(False)
        self.B8.setDefault(False)
        self.B8.setFlat(True)
        self.B8.setObjectName("B8")
        self.B9 = QtWidgets.QPushButton(self.centralwidget)
        self.B9.setGeometry(QtCore.QRect(537, 403, 239, 173))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(96)
        self.B9.setFont(font)
        self.B9.setMouseTracking(False)
        self.B9.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.B9.setAcceptDrops(False)
        self.B9.setToolTip("")
        self.B9.setText("")
        self.B9.setShortcut("")
        self.B9.setCheckable(False)
        self.B9.setChecked(False)
        self.B9.setAutoRepeat(False)
        self.B9.setAutoExclusive(False)
        self.B9.setDefault(False)
        self.B9.setFlat(True)
        self.B9.setObjectName("B9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(268, 615, 266, 50))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 680, 200, 75))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        TTT2P.setCentralWidget(self.centralwidget)
        self.B1.setStyleSheet("color: rgb(0, 0, 0);")
        self.B2.setStyleSheet("color: rgb(0, 0, 0);")
        self.B3.setStyleSheet("color: rgb(0, 0, 0);")
        self.B4.setStyleSheet("color: rgb(0, 0, 0);")
        self.B5.setStyleSheet("color: rgb(0, 0, 0);")
        self.B6.setStyleSheet("color: rgb(0, 0, 0);")
        self.B7.setStyleSheet("color: rgb(0, 0, 0);")
        self.B8.setStyleSheet("color: rgb(0, 0, 0);")
        self.B9.setStyleSheet("color: rgb(0, 0, 0);")

        self.retranslateUi(TTT2P)
        QtCore.QMetaObject.connectSlotsByName(TTT2P)

        self.B1.clicked.connect(self.rule_xo_1)
        self.B2.clicked.connect(self.rule_xo_2)
        self.B3.clicked.connect(self.rule_xo_3)
        self.B4.clicked.connect(self.rule_xo_4)
        self.B5.clicked.connect(self.rule_xo_5)
        self.B6.clicked.connect(self.rule_xo_6)
        self.B7.clicked.connect(self.rule_xo_7)
        self.B8.clicked.connect(self.rule_xo_8)
        self.B9.clicked.connect(self.rule_xo_9)
        self.pushButton.clicked.connect(self.reset)

    def retranslateUi(self, TTT2P):
        _translate = QtCore.QCoreApplication.translate
        TTT2P.setWindowTitle(_translate("TTT2P", "2 Player"))
        self.pushButton.setText(_translate("TTT2P", "Reset"))

    # This function will update x, o on button at each click
    def rule_xo_1(self):
        global count, box
        if count % 2 != 0:
            self.B1.setText("X")
            box[0][0] = 1
        else:
            self.B1.setText("O")
            box[0][0] = 2
        count += 1
        self.B1.setEnabled(False)
        self.check_correctly()

    def rule_xo_2(self):
        global count, box
        if count % 2 != 0:
            self.B2.setText("X")
            box[0][1] = 1
        else:
            self.B2.setText("O")
            box[0][1] = 2
        count += 1
        self.B2.setEnabled(False)
        self.check_correctly()

    def rule_xo_3(self):
        global count, box
        if count % 2 != 0:
            self.B3.setText("X")
            box[0][2] = 1
        else:
            self.B3.setText("O")
            box[0][2] = 2
        count += 1
        self.B3.setEnabled(False)
        self.check_correctly()

    def rule_xo_4(self):
        global count, box
        if count % 2 != 0:
            self.B4.setText("X")
            box[1][0] = 1
        else:
            self.B4.setText("O")
            box[1][0] = 2
        count += 1
        self.B4.setEnabled(False)
        self.check_correctly()

    def rule_xo_5(self):
        global count, box
        if count % 2 != 0:
            self.B5.setText("X")
            box[1][1] = 1
        else:
            self.B5.setText("O")
            box[1][1] = 2
        count += 1
        self.B5.setEnabled(False)
        self.check_correctly()

    def rule_xo_6(self):
        global count, box
        if count % 2 != 0:
            self.B6.setText("X")
            box[1][2] = 1
        else:
            self.B6.setText("O")
            box[1][2] = 2
        count += 1
        self.B6.setEnabled(False)
        self.check_correctly()

    def rule_xo_7(self):
        global count, box
        if count % 2 != 0:
            self.B7.setText("X")
            box[2][0] = 1
        else:
            self.B7.setText("O")
            box[2][0] = 2
        count += 1
        self.B7.setEnabled(False)
        self.check_correctly()

    def rule_xo_8(self):
        global count, box
        if count % 2 != 0:
            self.B8.setText("X")
            box[2][1] = 1
        else:
            self.B8.setText("O")
            box[2][1] = 2
        count += 1
        self.B8.setEnabled(False)
        self.check_correctly()

    def rule_xo_9(self):
        global count, box
        if count % 2 != 0:
            self.B9.setText("X")
            box[2][2] = 1
        else:
            self.B9.setText("O")
            box[2][2] = 2
        count += 1
        self.B9.setEnabled(False)
        self.check_correctly()

    def check_correctly(self):
        # Vertical win
        if box[0][0] == 1 and box [1][0] == 1and box [2][0] == 1:
            self.B1.setStyleSheet("color: rgb(85, 255, 0);")
            self.B4.setStyleSheet("color: rgb(85, 255, 0);")
            self.B7.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("X win")
            self.button_false()

        elif box[0][0] == 2 and box[1][0] == 2 and box[2][0] == 2:
            self.B1.setStyleSheet("color: rgb(85, 255, 0);")
            self.B4.setStyleSheet("color: rgb(85, 255, 0);")
            self.B7.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("O win")
            self.button_false()

        elif box[0][1] == 1 and box[1][1] == 1 and box[2][1] == 1:
            self.B2.setStyleSheet("color: rgb(85, 255, 0);")
            self.B5.setStyleSheet("color: rgb(85, 255, 0);")
            self.B8.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("X win")
            self.button_false()

        elif box[0][1] == 2 and box[1][1] == 2 and box[2][1] == 2:
            self.B2.setStyleSheet("color: rgb(85, 255, 0);")
            self.B5.setStyleSheet("color: rgb(85, 255, 0);")
            self.B8.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("O win")
            self.button_false()

        elif box[0][2] == 1 and box[1][2] == 1 and box[2][2] == 1:
            self.B3.setStyleSheet("color: rgb(85, 255, 0);")
            self.B6.setStyleSheet("color: rgb(85, 255, 0);")
            self.B9.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("X win")
            self.button_false()

        elif box[0][2] == 2 and box[1][2] == 2 and box[2][2] == 2:
            self.B3.setStyleSheet("color: rgb(85, 255, 0);")
            self.B6.setStyleSheet("color: rgb(85, 255, 0);")
            self.B9.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("O win")
            self.button_false()

        # Horizontal win
        elif box[0][0] == 1 and box [0][1] == 1 and box [0][2] == 1:
            self.B1.setStyleSheet("color: rgb(85, 255, 0);")
            self.B2.setStyleSheet("color: rgb(85, 255, 0);")
            self.B3.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("X win")
            self.button_false()

        elif box[0][0] == 2 and box [0][1] == 2 and box [0][2] == 2:
            self.B1.setStyleSheet("color: rgb(85, 255, 0);")
            self.B2.setStyleSheet("color: rgb(85, 255, 0);")
            self.B3.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("O win")
            self.button_false()

        elif box[1][0] == 1 and box [1][1] == 1 and box [1][2] == 1:
            self.B4.setStyleSheet("color: rgb(85, 255, 0);")
            self.B5.setStyleSheet("color: rgb(85, 255, 0);")
            self.B6.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("X win")
            self.button_false()

        elif box[1][0] == 2 and box[1][1] == 2 and box[1][2] == 2:
            self.B4.setStyleSheet("color: rgb(85, 255, 0);")
            self.B5.setStyleSheet("color: rgb(85, 255, 0);")
            self.B6.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("O win")
            self.button_false()

        elif box[2][0] == 1 and box [2][1] == 1 and box [2][2] == 1:
            self.B7.setStyleSheet("color: rgb(85, 255, 0);")
            self.B8.setStyleSheet("color: rgb(85, 255, 0);")
            self.B9.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("X win")
            self.button_false()

        elif box[2][0] == 2 and box [2][1] == 2 and box [2][2] == 2:
            self.B7.setStyleSheet("color: rgb(85, 255, 0);")
            self.B8.setStyleSheet("color: rgb(85, 255, 0);")
            self.B9.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("O win")
            self.button_false()

        # Diagonal win
        elif box[0][0] == 1 and box[1][1] == 1 and box[2][2] == 1:
            self.B1.setStyleSheet("color: rgb(85, 255, 0);")
            self.B5.setStyleSheet("color: rgb(85, 255, 0);")
            self.B9.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("X win")
            self.button_false()

        elif box[0][0] == 2 and box[1][1] == 2 and box[2][2] == 2:
            self.B1.setStyleSheet("color: rgb(85, 255, 0);")
            self.B5.setStyleSheet("color: rgb(85, 255, 0);")
            self.B9.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("O win")
            self.button_false()

        elif box[0][2] == 1 and box[1][1] == 1 and box[2][0] == 1:
            self.B3.setStyleSheet("color: rgb(85, 255, 0);")
            self.B5.setStyleSheet("color: rgb(85, 255, 0);")
            self.B7.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("X win")
            self.button_false()

        elif box[0][2] == 2 and box[1][1] == 2 and box[2][0] == 2:
            self.B3.setStyleSheet("color: rgb(85, 255, 0);")
            self.B5.setStyleSheet("color: rgb(85, 255, 0);")
            self.B7.setStyleSheet("color: rgb(85, 255, 0);")
            self.label.setText("O win")
            self.button_false()
        else:
            if (count) == 9:
                self.B1.setStyleSheet("color: rgb(170, 0, 0);")
                self.B2.setStyleSheet("color: rgb(170, 0, 0);")
                self.B3.setStyleSheet("color: rgb(170, 0, 0);")
                self.B4.setStyleSheet("color: rgb(170, 0, 0);")
                self.B5.setStyleSheet("color: rgb(170, 0, 0);")
                self.B6.setStyleSheet("color: rgb(170, 0, 0);")
                self.B7.setStyleSheet("color: rgb(170, 0, 0);")
                self.B8.setStyleSheet("color: rgb(170, 0, 0);")
                self.B9.setStyleSheet("color: rgb(170, 0, 0);")
                self.label.setText("Draw")

    def button_false(self):
        self.B1.setEnabled(False)
        self.B2.setEnabled(False)
        self.B3.setEnabled(False)
        self.B4.setEnabled(False)
        self.B5.setEnabled(False)
        self.B6.setEnabled(False)
        self.B7.setEnabled(False)
        self.B8.setEnabled(False)
        self.B9.setEnabled(False)

    def button_true(self):
        self.B1.setEnabled(True)
        self.B2.setEnabled(True)
        self.B3.setEnabled(True)
        self.B4.setEnabled(True)
        self.B5.setEnabled(True)
        self.B6.setEnabled(True)
        self.B7.setEnabled(True)
        self.B8.setEnabled(True)
        self.B9.setEnabled(True)

    def reset(self):
        global count, box
        self.button_true()
        self.B1.setText("")
        self.B2.setText("")
        self.B3.setText("")
        self.B4.setText("")
        self.B5.setText("")
        self.B6.setText("")
        self.B7.setText("")
        self.B8.setText("")
        self.B9.setText("")
        self.B1.setStyleSheet("color: rgb(0, 0, 0);")
        self.B2.setStyleSheet("color: rgb(0, 0, 0);")
        self.B3.setStyleSheet("color: rgb(0, 0, 0);")
        self.B4.setStyleSheet("color: rgb(0, 0, 0);")
        self.B5.setStyleSheet("color: rgb(0, 0, 0);")
        self.B6.setStyleSheet("color: rgb(0, 0, 0);")
        self.B7.setStyleSheet("color: rgb(0, 0, 0);")
        self.B8.setStyleSheet("color: rgb(0, 0, 0);")
        self.B9.setStyleSheet("color: rgb(0, 0, 0);")
        count = 0
        box = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.label.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TTT2P = QtWidgets.QWidget()
    ui = Ui_TTT2P()
    ui.setupTTT2P(TTT2P)
    TTT2P.show()
    sys.exit(app.exec_())
