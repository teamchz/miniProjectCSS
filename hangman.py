from PyQt5 import QtCore, QtGui, QtWidgets
import random
from main import *


class Ui_Hangman(object):

    # Set up UI
    def setupHangman(self, Hangman):
        Hangman.setObjectName("Hangman")
        Hangman.resize(800, 600)
        Hangman.setMinimumSize(QtCore.QSize(800, 600))
        Hangman.setMaximumSize(QtCore.QSize(800, 600))
        Hangman.setAcceptDrops(False)
        Hangman.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.graphicsView = QtWidgets.QGraphicsView(Hangman)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 781, 401))
        self.graphicsView.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(Hangman)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 420, 781, 119))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        self.layoutWidget.setFont(font)
        self.layoutWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_A = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_A.setFont(font)
        self.pushButton_A.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_A.setStyleSheet("background-color: rgb(255, 154, 162);")
        self.pushButton_A.setAutoDefault(False)
        self.pushButton_A.setObjectName("pushButton_A")
        self.horizontalLayout_3.addWidget(self.pushButton_A)
        self.pushButton_B = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_B.setFont(font)
        self.pushButton_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_B.setStyleSheet("background-color: rgb(255, 183, 178);\n"
                                        "")
        self.pushButton_B.setObjectName("pushButton_B")
        self.horizontalLayout_3.addWidget(self.pushButton_B)
        self.pushButton_C = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_C.setFont(font)
        self.pushButton_C.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_C.setStyleSheet("background-color: rgb(255, 218, 193);")
        self.pushButton_C.setObjectName("pushButton_C")
        self.horizontalLayout_3.addWidget(self.pushButton_C)
        self.pushButton_D = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_D.setFont(font)
        self.pushButton_D.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_D.setStyleSheet("background-color: rgb(255, 253, 194);")
        self.pushButton_D.setObjectName("pushButton_D")
        self.horizontalLayout_3.addWidget(self.pushButton_D)
        self.pushButton_E = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_E.setFont(font)
        self.pushButton_E.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_E.setStyleSheet("background-color: rgb(226, 240, 203);")
        self.pushButton_E.setObjectName("pushButton_E")
        self.horizontalLayout_3.addWidget(self.pushButton_E)
        self.pushButton_F = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_F.setFont(font)
        self.pushButton_F.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_F.setStyleSheet("background-color: rgb(181, 234, 215);")
        self.pushButton_F.setObjectName("pushButton_F")
        self.horizontalLayout_3.addWidget(self.pushButton_F)
        self.pushButton_G = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_G.setFont(font)
        self.pushButton_G.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_G.setStyleSheet("background-color: rgb(162, 215, 234);")
        self.pushButton_G.setObjectName("pushButton_G")
        self.horizontalLayout_3.addWidget(self.pushButton_G)
        self.pushButton_H = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_H.setFont(font)
        self.pushButton_H.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_H.setStyleSheet("background-color: rgb(199, 206, 234);")
        self.pushButton_H.setObjectName("pushButton_H")
        self.horizontalLayout_3.addWidget(self.pushButton_H)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_I = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_I.setFont(font)
        self.pushButton_I.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_I.setStyleSheet("background-color: rgb(255, 154, 162);")
        self.pushButton_I.setObjectName("pushButton_I")
        self.horizontalLayout_2.addWidget(self.pushButton_I)
        self.pushButton_J = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_J.setFont(font)
        self.pushButton_J.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_J.setStyleSheet("background-color: rgb(255, 183, 178);\n"
                                        "")
        self.pushButton_J.setObjectName("pushButton_J")
        self.horizontalLayout_2.addWidget(self.pushButton_J)
        self.pushButton_K = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_K.setFont(font)
        self.pushButton_K.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_K.setStyleSheet("background-color: rgb(255, 218, 193);")
        self.pushButton_K.setObjectName("pushButton_K")
        self.horizontalLayout_2.addWidget(self.pushButton_K)
        self.pushButton_L = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_L.setFont(font)
        self.pushButton_L.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_L.setStyleSheet("background-color: rgb(255, 253, 194);")
        self.pushButton_L.setObjectName("pushButton_L")
        self.horizontalLayout_2.addWidget(self.pushButton_L)
        self.pushButton_M = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_M.setFont(font)
        self.pushButton_M.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_M.setStyleSheet("background-color: rgb(226, 240, 203);")
        self.pushButton_M.setObjectName("pushButton_M")
        self.horizontalLayout_2.addWidget(self.pushButton_M)
        self.pushButton_N = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_N.setFont(font)
        self.pushButton_N.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_N.setStyleSheet("background-color: rgb(181, 234, 215);")
        self.pushButton_N.setObjectName("pushButton_N")
        self.horizontalLayout_2.addWidget(self.pushButton_N)
        self.pushButton_O = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_O.setFont(font)
        self.pushButton_O.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_O.setStyleSheet("background-color: rgb(162, 215, 234);")
        self.pushButton_O.setObjectName("pushButton_O")
        self.horizontalLayout_2.addWidget(self.pushButton_O)
        self.pushButton_P = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_P.setFont(font)
        self.pushButton_P.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_P.setStyleSheet("background-color: rgb(199, 206, 234);")
        self.pushButton_P.setObjectName("pushButton_P")
        self.horizontalLayout_2.addWidget(self.pushButton_P)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_Q = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_Q.setFont(font)
        self.pushButton_Q.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Q.setStyleSheet("background-color: rgb(255, 154, 162);")
        self.pushButton_Q.setObjectName("pushButton_Q")
        self.horizontalLayout_4.addWidget(self.pushButton_Q)
        self.pushButton_R = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_R.setFont(font)
        self.pushButton_R.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_R.setStyleSheet("background-color: rgb(255, 183, 178);\n"
                                        "")
        self.pushButton_R.setObjectName("pushButton_R")
        self.horizontalLayout_4.addWidget(self.pushButton_R)
        self.pushButton_S = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_S.setFont(font)
        self.pushButton_S.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_S.setStyleSheet("background-color: rgb(255, 218, 193);")
        self.pushButton_S.setObjectName("pushButton_S")
        self.horizontalLayout_4.addWidget(self.pushButton_S)
        self.pushButton_T = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_T.setFont(font)
        self.pushButton_T.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_T.setStyleSheet("background-color: rgb(255, 253, 194);")
        self.pushButton_T.setObjectName("pushButton_T")
        self.horizontalLayout_4.addWidget(self.pushButton_T)
        self.pushButton_U = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_U.setFont(font)
        self.pushButton_U.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_U.setStyleSheet("background-color: rgb(226, 240, 203);")
        self.pushButton_U.setObjectName("pushButton_U")
        self.horizontalLayout_4.addWidget(self.pushButton_U)
        self.pushButton_V = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_V.setFont(font)
        self.pushButton_V.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_V.setStyleSheet("background-color: rgb(181, 234, 215);")
        self.pushButton_V.setObjectName("pushButton_V")
        self.horizontalLayout_4.addWidget(self.pushButton_V)
        self.pushButton_W = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_W.setFont(font)
        self.pushButton_W.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_W.setStyleSheet("background-color: rgb(162, 215, 234);")
        self.pushButton_W.setObjectName("pushButton_W")
        self.horizontalLayout_4.addWidget(self.pushButton_W)
        self.pushButton_X = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_X.setFont(font)
        self.pushButton_X.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_X.setStyleSheet("background-color: rgb(199, 206, 234);")
        self.pushButton_X.setObjectName("pushButton_X")
        self.horizontalLayout_4.addWidget(self.pushButton_X)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Hangman)
        self.layoutWidget1.setGeometry(QtCore.QRect(300, 540, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Y = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_Y.setFont(font)
        self.pushButton_Y.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Y.setStyleSheet("background-color: rgb(255, 253, 194);")
        self.pushButton_Y.setObjectName("pushButton_Y")
        self.gridLayout_2.addWidget(self.pushButton_Y, 1, 0, 1, 1)
        self.pushButton_Z = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(16)
        self.pushButton_Z.setFont(font)
        self.pushButton_Z.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Z.setStyleSheet("background-color: rgb(226, 240, 203);")
        self.pushButton_Z.setObjectName("pushButton_Z")
        self.gridLayout_2.addWidget(self.pushButton_Z, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Hangman)
        self.label.setGeometry(QtCore.QRect(30, 310, 741, 91))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Zilla Slab Medium")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.label.setObjectName("label")
        self.pushButton_back = QtWidgets.QPushButton(Hangman)
        self.pushButton_back.setGeometry(QtCore.QRect(10, 550, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(20)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back.setStyleSheet("color: rgb(0, 0, 127);\n"
                                           "background-color: rgb(255, 154, 162);")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back_2 = QtWidgets.QPushButton(Hangman)
        self.pushButton_back_2.setGeometry(QtCore.QRect(740, 550, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Zilla Slab SemiBold")
        font.setPointSize(20)
        self.pushButton_back_2.setFont(font)
        self.pushButton_back_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back_2.setStyleSheet("color: rgb(0, 0, 127);\n"
                                             "background-color: rgb(199, 206, 234);")
        self.pushButton_back_2.setObjectName("pushButton_back_2")
        self.pushButton_back_2.setObjectName("pushButton_back_2")
        self.label_2 = QtWidgets.QLabel(Hangman)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 741, 251))
        self.label_2.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Hangman-0.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.retranslateUi(Hangman)
        QtCore.QMetaObject.connectSlotsByName(Hangman)

    # Set up button A-Z, exit and start.
    def retranslateUi(self, Hangman):
        _translate = QtCore.QCoreApplication.translate
        Hangman.setWindowTitle(_translate("Hangman", "Hangman"))
        self.pushButton_A.setText(_translate("Hangman", "A"))
        self.pushButton_B.setText(_translate("Hangman", "B"))
        self.pushButton_C.setText(_translate("Hangman", "C"))
        self.pushButton_D.setText(_translate("Hangman", "D"))
        self.pushButton_E.setText(_translate("Hangman", "E"))
        self.pushButton_F.setText(_translate("Hangman", "F"))
        self.pushButton_G.setText(_translate("Hangman", "G"))
        self.pushButton_H.setText(_translate("Hangman", "H"))
        self.pushButton_I.setText(_translate("Hangman", "I"))
        self.pushButton_J.setText(_translate("Hangman", "J"))
        self.pushButton_K.setText(_translate("Hangman", "K"))
        self.pushButton_L.setText(_translate("Hangman", "L"))
        self.pushButton_M.setText(_translate("Hangman", "M"))
        self.pushButton_N.setText(_translate("Hangman", "N"))
        self.pushButton_O.setText(_translate("Hangman", "O"))
        self.pushButton_P.setText(_translate("Hangman", "P"))
        self.pushButton_Q.setText(_translate("Hangman", "Q"))
        self.pushButton_R.setText(_translate("Hangman", "R"))
        self.pushButton_S.setText(_translate("Hangman", "S"))
        self.pushButton_T.setText(_translate("Hangman", "T"))
        self.pushButton_U.setText(_translate("Hangman", "U"))
        self.pushButton_V.setText(_translate("Hangman", "V"))
        self.pushButton_W.setText(_translate("Hangman", "W"))
        self.pushButton_X.setText(_translate("Hangman", "X"))
        self.pushButton_Y.setText(_translate("Hangman", "Y"))
        self.pushButton_Z.setText(_translate("Hangman", "Z"))
        self.label.setText(_translate("Hangman", "Welcome To Hangman!!"))
        self.pushButton_back.setText(_translate("Hangman", "<<<"))
        self.pushButton_back.clicked.connect(exit)
        self.pushButton_back_2.setText(_translate("Hangman", ">>>"))
        self.pushButton_back_2.clicked.connect(self.start)
        self.button_false()
        self.pushButton_A.clicked.connect(self.a_append)
        self.pushButton_B.clicked.connect(self.b_append)
        self.pushButton_C.clicked.connect(self.c_append)
        self.pushButton_D.clicked.connect(self.d_append)
        self.pushButton_E.clicked.connect(self.e_append)
        self.pushButton_F.clicked.connect(self.f_append)
        self.pushButton_G.clicked.connect(self.g_append)
        self.pushButton_H.clicked.connect(self.h_append)
        self.pushButton_I.clicked.connect(self.i_append)
        self.pushButton_J.clicked.connect(self.j_append)
        self.pushButton_K.clicked.connect(self.k_append)
        self.pushButton_L.clicked.connect(self.l_append)
        self.pushButton_M.clicked.connect(self.m_append)
        self.pushButton_N.clicked.connect(self.n_append)
        self.pushButton_O.clicked.connect(self.o_append)
        self.pushButton_P.clicked.connect(self.p_append)
        self.pushButton_Q.clicked.connect(self.q_append)
        self.pushButton_R.clicked.connect(self.r_append)
        self.pushButton_S.clicked.connect(self.s_append)
        self.pushButton_T.clicked.connect(self.t_append)
        self.pushButton_U.clicked.connect(self.u_append)
        self.pushButton_V.clicked.connect(self.v_append)
        self.pushButton_W.clicked.connect(self.w_append)
        self.pushButton_X.clicked.connect(self.x_append)
        self.pushButton_Y.clicked.connect(self.y_append)
        self.pushButton_Z.clicked.connect(self.z_append)

    # This function is will show the first word you need to guess.
    def start(self):
        global box, full_word, guess_word, word, life, c
        life = 6
        box = []
        full_word = []
        guess_word = []
        word = ["computer", "science", "orange", "exit", "mini", "project", "engineering", "world", "python",
                "stack", "data", "statistic", "constant", "calculus", "process", "device", "coding", "flowing",
                "index", "widgets", "application", "physic", "power", "spam", "hacking"]
        c = random.randint(0, 24)
        last = len(word[c])
        show_one = random.randint(0, last - 1)
        full_word.append(word[c])
        box = (list(word[c]))
        self.label.setStyleSheet("background-color: rgb(135, 135, 135);")  # Set background color.
        self.label_2.setPixmap(QtGui.QPixmap("Hangman-0.png"))  # Set image to Default.
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # Set image to center.
        # If word <= 6 show 1 hint.
        if len(word[c]) <= 6:
            guess_word.append((word[c])[show_one])  # show 1 hint.
        # If word > 6 show 2 hints.
        else:
            show_two = random.randint(5, last - 1)
            guess_word.append((word[c])[show_one])
            guess_word.append((word[c])[show_two])  # show 2 hints .
            guess_word = set(guess_word)  # Turn list into set to remove the same elements in list.
            guess_word = list(guess_word)  # Turn it back to list.

        # Make random word didn't show full word, Replace with "_"
        # And make add some hint
        first_word = []
        for i in full_word[0]:
            for j in guess_word:
                if j == i:
                    first_word.append(j)
        final = [letter if letter in set(guess_word) else "_" for letter in full_word[0]]
        self.label.setText(" ".join(final))  # Show First word.
        self.pushButton_back_2.setEnabled(False)  # Make it Disable when clicked.
        self.button_true()

    # These function will add letter(A-Z) you clicked to guess word,
    # If not correct life -1,
    # And if you clicked button twice it will disable.
    def a_append(self):
        global guess_word, life
        if "a" in guess_word:
            self.pushButton_A.setEnabled(False)
        else:
            guess_word.append("a")
        if "a" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def b_append(self):
        global guess_word, life
        if "b" in guess_word:
            self.pushButton_B.setEnabled(False)
        else:
            guess_word.append("b")
        if "b" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def c_append(self):
        global guess_word, life
        if "c" in guess_word:
            self.pushButton_C.setEnabled(False)
        else:
            guess_word.append("c")
        if "c" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def d_append(self):
        global guess_word, life
        if "d" in guess_word:
            self.pushButton_D.setEnabled(False)
        else:
            guess_word.append("d")
        if "d" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def e_append(self):
        global guess_word, life
        if "e" in guess_word:
            self.pushButton_E.setEnabled(False)
        else:
            guess_word.append("e")
        if "e" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def f_append(self):
        global guess_word, life
        if "f" in guess_word:
            self.pushButton_F.setEnabled(False)
        else:
            guess_word.append("f")
        if "f" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def g_append(self):
        global guess_word, life
        if "g" in guess_word:
            self.pushButton_G.setEnabled(False)
        else:
            guess_word.append("g")
        if "g" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def h_append(self):
        global guess_word, life
        if "h" in guess_word:
            self.pushButton_H.setEnabled(False)
        else:
            guess_word.append("h")
        if "h" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def i_append(self):
        global guess_word, life
        if "i" in guess_word:
            self.pushButton_I.setEnabled(False)
        else:
            guess_word.append("i")
        if "i" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def j_append(self):
        global guess_word, life
        if "j" in guess_word:
            self.pushButton_J.setEnabled(False)
        else:
            guess_word.append("j")
        if "j" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def k_append(self):
        global guess_word, life
        if "k" in guess_word:
            self.pushButton_K.setEnabled(False)
        else:
            guess_word.append("k")
        if "k" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def l_append(self):
        global guess_word, life
        if "l" in guess_word:
            self.pushButton_L.setEnabled(False)
        else:
            guess_word.append("l")
        if "l" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def m_append(self):
        global guess_word, life
        if "m" in guess_word:
            self.pushButton_M.setEnabled(False)
        else:
            guess_word.append("m")
        if "m" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def n_append(self):
        global guess_word, life
        if "n" in guess_word:
            self.pushButton_N.setEnabled(False)
        else:
            guess_word.append("n")
        if "n" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def o_append(self):
        global guess_word, life
        if "o" in guess_word:
            self.pushButton_O.setEnabled(False)
        else:
            guess_word.append("o")
        if "o" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def p_append(self):
        global guess_word, life
        if "p" in guess_word:
            self.pushButton_P.setEnabled(False)
        else:
            guess_word.append("p")
        if "p" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def q_append(self):
        global guess_word, life
        if "q" in guess_word:
            self.pushButton_Q.setEnabled(False)
        else:
            guess_word.append("q")
        if "q" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def r_append(self):
        global guess_word, life
        if "r" in guess_word:
            self.pushButton_R.setEnabled(False)
        else:
            guess_word.append("r")
        if "r" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def s_append(self):
        global guess_word, life
        if "s" in guess_word:
            self.pushButton_S.setEnabled(False)
        else:
            guess_word.append("s")
        if "s" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def t_append(self):
        global guess_word, life
        if "t" in guess_word:
            self.pushButton_T.setEnabled(False)
        else:
            guess_word.append("t")
        if "t" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def u_append(self):
        global guess_word, life
        if "u" in guess_word:
            self.pushButton_U.setEnabled(False)
        else:
            guess_word.append("u")
        if "u" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def v_append(self):
        global guess_word, life
        if "v" in guess_word:
            self.pushButton_V.setEnabled(False)
        else:
            guess_word.append("v")
        if "v" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def w_append(self):
        global guess_word, life
        if "w" in guess_word:
            self.pushButton_W.setEnabled(False)
        else:
            guess_word.append("w")
        if "w" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def x_append(self):
        global guess_word, life
        if "x" in guess_word:
            self.pushButton_X.setEnabled(False)
        else:
            guess_word.append("x")
        if "x" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def y_append(self):
        global guess_word, life
        if "y" in guess_word:
            self.pushButton_Y.setEnabled(False)
        else:
            guess_word.append("y")
        if "y" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    def z_append(self):
        global guess_word, life
        if "z" in guess_word:
            self.pushButton_Z.setEnabled(False)
        else:
            guess_word.append("z")
        if "z" not in list(full_word[0]):
            life -= 1
        self.check_correctly()

    # if guess word equal full word then button got to next word will enable.
    def check_correctly(self):
        global c
        first_word = []
        for i in full_word[0]:
            for j in guess_word:
                if j == i:
                    first_word.append(j)
        result = all(elm in list(set(guess_word)) for elm in list(set(list(full_word[0]))))
        final = [letter if letter in set(guess_word) else "_" for letter in full_word[0]]
        self.label.setText(" ".join(final))

        if result:  # if guess word equal full word then button next will enable.
            self.pushButton_back_2.setEnabled(True)
            self.label.setStyleSheet("color: rgb(85, 255, 0);")
            self.button_false()
        if life == 5:
            self.label_2.setPixmap(QtGui.QPixmap("Hangman-1.png"))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        elif life == 4:
            self.label_2.setPixmap(QtGui.QPixmap("Hangman-2.png"))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        elif life == 3:
            self.label_2.setPixmap(QtGui.QPixmap("Hangman-3.png"))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        elif life == 2:
            self.label_2.setPixmap(QtGui.QPixmap("Hangman-4.png"))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        elif life == 1:
            self.label_2.setPixmap(QtGui.QPixmap("Hangman-5.png"))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        elif life == 0:
            self.label.setText(word[c])
            self.label.setStyleSheet("color: rgb(255, 0, 0);")
            self.button_false()
            self.label_2.setPixmap(QtGui.QPixmap("Hangman-6.png"))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
            self.pushButton_back_2.setEnabled(True)


    # set A-Z buttons disable.
    def button_false(self):
        self.pushButton_A.setEnabled(False)
        self.pushButton_B.setEnabled(False)
        self.pushButton_C.setEnabled(False)
        self.pushButton_D.setEnabled(False)
        self.pushButton_E.setEnabled(False)
        self.pushButton_F.setEnabled(False)
        self.pushButton_G.setEnabled(False)
        self.pushButton_H.setEnabled(False)
        self.pushButton_I.setEnabled(False)
        self.pushButton_J.setEnabled(False)
        self.pushButton_K.setEnabled(False)
        self.pushButton_L.setEnabled(False)
        self.pushButton_M.setEnabled(False)
        self.pushButton_N.setEnabled(False)
        self.pushButton_O.setEnabled(False)
        self.pushButton_P.setEnabled(False)
        self.pushButton_Q.setEnabled(False)
        self.pushButton_R.setEnabled(False)
        self.pushButton_S.setEnabled(False)
        self.pushButton_T.setEnabled(False)
        self.pushButton_U.setEnabled(False)
        self.pushButton_V.setEnabled(False)
        self.pushButton_W.setEnabled(False)
        self.pushButton_X.setEnabled(False)
        self.pushButton_Y.setEnabled(False)
        self.pushButton_Z.setEnabled(False)

    # set A-Z buttons enable.
    def button_true(self):
        self.pushButton_A.setEnabled(True)
        self.pushButton_B.setEnabled(True)
        self.pushButton_C.setEnabled(True)
        self.pushButton_D.setEnabled(True)
        self.pushButton_E.setEnabled(True)
        self.pushButton_F.setEnabled(True)
        self.pushButton_G.setEnabled(True)
        self.pushButton_H.setEnabled(True)
        self.pushButton_I.setEnabled(True)
        self.pushButton_J.setEnabled(True)
        self.pushButton_K.setEnabled(True)
        self.pushButton_L.setEnabled(True)
        self.pushButton_M.setEnabled(True)
        self.pushButton_N.setEnabled(True)
        self.pushButton_O.setEnabled(True)
        self.pushButton_P.setEnabled(True)
        self.pushButton_Q.setEnabled(True)
        self.pushButton_R.setEnabled(True)
        self.pushButton_S.setEnabled(True)
        self.pushButton_T.setEnabled(True)
        self.pushButton_U.setEnabled(True)
        self.pushButton_V.setEnabled(True)
        self.pushButton_W.setEnabled(True)
        self.pushButton_X.setEnabled(True)
        self.pushButton_Y.setEnabled(True)
        self.pushButton_Z.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hangman = QtWidgets.QWidget()
    ui = Ui_Hangman()
    ui.setupHangman(Hangman)
    Hangman.show()
    sys.exit(app.exec_())

# KMUTT-CSS MINI PROJECT
