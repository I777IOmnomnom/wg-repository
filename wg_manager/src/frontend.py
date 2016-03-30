#!/usr/bin/python
import sys
from PySide import QtCore, QtGui

app = QtGui.QApplication(sys.argv)
gui = QtGui
core = QtCore


class FrontEndException(Exception):
    pass


class FrontEnd():

    def __init__(self):
        get_screen = app.desktop().screenGeometry()
        self.width, self.height = get_screen.width(), get_screen.height()

    def init(self):
        wid = QtGui.QWidget()
        wid.resize(self.width, self.height)
        wid.setWindowTitle('WGus Managerus')
        p = wid.palette()
        p.setColor(wid.backgroundRole(), QtCore.Qt.lightGray)
        wid.setPalette(p)
        self.quit_button(wid)
        self.movie_button(wid)
        self.music_button(wid)
        self.setting_button(wid)
        self.game_button(wid)
        wid.show()
        sys.exit(app.exec_())

    def movie_button(self, parent):
        qbtn = QtGui.QPushButton('Watch a movie', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(1500, 200)
        qbtn.move(210, 25)

    def music_button(self, parent):
        qbtn = QtGui.QPushButton('Listen to music', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(1500, 200)
        qbtn.move(210, 250)

    def game_button(self, parent):
        qbtn = QtGui.QPushButton('Play a game', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(1500, 200)
        qbtn.move(210, 475)

    def setting_button(self, parent):
        qbtn = QtGui.QPushButton('Settings', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(700, 180)
        qbtn.move(210, 700)

    def quit_button(self, parent):
        qbtn = QtGui.QPushButton('EXIT', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(700, 180)
        qbtn.move(1010, 700)



    def run(self):
        pass


if __name__ == '__main__':
    FrontEnd().init()
