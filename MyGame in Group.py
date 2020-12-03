import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QRadioButton, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from random import *

# set variable

global player_score
global npc_score
player_score = 0
npc_score = 0

# make game window

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle('__MyGame__')
win.setGeometry(0, 0, 1000, 600)
win.setMaximumSize(1000, 600)
win.setMinimumSize(1000, 600)



def rock_click():
    player_label.setPixmap(QPixmap("Rock.png"))
    font2 = player_label.font()
    font2.setPointSize(21)
    player_label.setFont(font2)
    player_label.move(50, 140)
    roll = randint(1, 3)
    player_label.adjustSize()
    global player_score
    global npc_score
    if(roll == 1):
        npc_label.setPixmap(QPixmap("Rock.png"))
        font4 = npc_label.font()
        font4.setPointSize(20)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        result.setText("Draw")
        result.adjustSize()
        npc_label.adjustSize()
    elif(roll == 2):
        npc_label.setPixmap(QPixmap("Paper.png"))
        font4 = npc_label.font()
        font4.setPointSize(20)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        npc_score += 1
        npc_label_score.setText('NPC  %d' % npc_score)
        result.setText("Lose")
        result.adjustSize()
        npc_label.adjustSize()
    elif(roll == 3):
        npc_label.setPixmap(QPixmap("Scissors.png"))
        font4 = npc_label.font()
        font4.setPointSize(20)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        player_score += 1
        player_label_score.setText('PLAYER  %d' % player_score)
        result.setText("Win")
        result.adjustSize()
        npc_label.adjustSize()


def scissors_click():
    player_label.setPixmap(QPixmap("Scissors.png"))
    font3 = player_label.font()
    font3.setPointSize(21)
    player_label.setFont(font3)
    player_label.move(50, 140)
    roll = randint(1, 3)
    player_label.adjustSize()
    global player_score
    global npc_score
    if(roll == 1):
        npc_label.setPixmap(QPixmap("Rock.png"))
        font4 = npc_label.font()
        font4.setPointSize(20)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        npc_score += 1
        npc_label_score.setText('NPC  %d' % npc_score)
        result.setText("Lose")
        result.adjustSize()
        npc_label.adjustSize()
    elif(roll == 2):
        npc_label.setPixmap(QPixmap("Paper.png"))
        font4 = npc_label.font()
        font4.setPointSize(20)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        player_score += 1
        player_label_score.setText('PLAYER  %d' % player_score)
        result.setText("Win")
        result.adjustSize()
        npc_label.adjustSize()
    elif(roll == 3):
        npc_label.setPixmap(QPixmap("Scissors.png"))
        font4 = npc_label.font()
        font4.setPointSize(20)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        result.setText("Draw")
        result.adjustSize()
        npc_label.adjustSize()

def paper_click():
    player_label.setPixmap(QPixmap("Paper.png"))
    font3 = player_label.font()
    font3.setPointSize(21)
    player_label.setFont(font3)
    player_label.move(50, 140)
    roll = randint(1, 3)
    player_label.adjustSize()
    global player_score
    global npc_score
    if(roll == 1):
        npc_label.setPixmap(QPixmap("Rock.png"))
        font4 = npc_label.font()
        font4.setPointSize(21)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        player_score += 1
        player_label_score.setText('PLAYER  %d' % player_score)
        result.setText("Win")
        result.adjustSize()
        npc_label.adjustSize()
    elif(roll == 2):
        npc_label.setPixmap(QPixmap("Paper.png"))
        font4 = npc_label.font()
        font4.setPointSize(21)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        result.setText("Draw")
        result.adjustSize()
        npc_label.adjustSize()
    elif(roll == 3):
        npc_label.setPixmap(QPixmap("Scissors.png"))
        font4 = npc_label.font()
        font4.setPointSize(21)
        npc_label.setFont(font4)
        npc_label.move(610, 140)
        npc_score += 1
        npc_label_score.setText('NPC  %d' % npc_score)
        result.setText("Lose")
        result.adjustSize()
        npc_label.adjustSize()

# make image rock, paper, scissors
rock = QPixmap("Rock.png")

paper = QPixmap("Paper.png")

scissors = QPixmap("Scissors.png")


player_label = QLabel(win)
player_label.setGeometry(0, 0, 1500, 300)

npc_label = QLabel(win)
npc_label.setGeometry(0, 0, 1500, 200)

npc_label_score = QLabel(win)
npc_label_score.setText('NPC  %d' % npc_score)
font = npc_label_score.font()
font.setPointSize(35)
npc_label_score.setFont(font)
npc_label_score.setGeometry(700, 0, 200, 1100)
npc_label_score.setStyleSheet("color : #F56991")

player_label_score = QLabel(win)
player_label_score.setText('PLAYER  %d' % player_score)
font1 = player_label_score.font()
font1.setPointSize(35)
player_label_score.setFont(font1)
player_label_score.setGeometry(100, 0, 300, 1100)
player_label_score.setStyleSheet("color : #5A8AF2")

game_title = QLabel(win)
game_title.setText("Rock, Paper, Scissors Game")
font5 = game_title.font()
font5.setPointSize(40)
game_title.setFont(font5)
game_title.adjustSize()
game_title.move(100, 10)
game_title.setStyleSheet("color : #8D20FA")

# make rock button
B_rock = QPushButton(win)
B_rock.setText('Rock')
B_rock.setGeometry(0, 0, 250, 50)
font6 = B_rock.font()
font6.setPointSize(24)
B_rock.setFont(font6)
B_rock.move(50, 100)
B_rock.clicked.connect(rock_click)
B_rock.setStyleSheet("background-color : #6495ED")


B_scissors = QPushButton(win)
B_scissors.setGeometry(0, 0, 250, 50)
B_scissors.setText('Scissors')
font6 = B_scissors.font()
font6.setPointSize(24)
B_scissors.setFont(font6)
B_scissors.move(375, 100)
B_scissors.clicked.connect(scissors_click)
B_scissors.setStyleSheet("background-color : #F56991")


B_paper = QPushButton(win)
B_paper.setGeometry(0, 100, 250, 50)
B_paper.setText('Paper')
font6 = B_paper.font()
font6.setPointSize(24)
B_paper.setFont(font6)
B_paper.move(700, 100)
B_paper.clicked.connect(paper_click)
B_paper.setStyleSheet("background-color : #EFFAB4")

result = QLabel(win)
font6 = result.font()
font6.setPointSize(30)
result.setFont(font6)
result.move(450, 300)

win.show()
sys.exit(app.exec_())
