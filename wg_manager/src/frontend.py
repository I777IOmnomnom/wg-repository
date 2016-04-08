#!/usr/bin/python
import sys
from PySide import QtCore, QtGui
from wg_manager.src.wg_lib import MultiMediaLib


class FrontEndException(Exception):
    pass


class FrontEnd():
##### This might be the worst FrontEnd approach I could have choosen but it's the easiest one #####
# Every new "tap" creates its own frontend which is located in deticated methods.
# The wglib provides a basic algorithm to create buttons, widgits and function calls.

    def __init__(self):
        print('asd')
        print('asd')
        self.mml = MultiMediaLib()

        self.app = QtGui.QApplication(sys.argv)

        get_screen = self.app.desktop().screenGeometry()

        self.width = get_screen.width()
        self.height = get_screen.height()

        self.mw = self.create_main_window()
        self.mw.show()

    def initUI(self):
        self.wid = self.create_widget(self.mw)

        self.push_button('Explore something (Platzhalter)', self.newsUI, self.wid, 210, 25)
        self.push_button('Watch something...', self.mediaUI, self.wid, 210, 225)
        self.push_button('List to something...', self.musicUI, self.wid, 210, 425)
        self.push_button('Play something ...', self.gamesUI, self.wid, 210, 625)
        self.quit_button(self.wid)

        self.wid.show()
        sys.exit(self.app.exec_())

        return

    def newsUI(self):

        return

    def mediaUI(self):
        self.wid.hide()
        self.wid = self.create_widget(self.mw)

        self.push_button('Movies (not implemented)', self.movieUI, self.wid, 210, 25)
        self.push_button('Series (not implemented)', self.serieUI, self.wid, 210, 225)
        self.push_button('Netflix', self.mml.exec_netflix, self.wid, 210, 425)
        self.push_button('Amazon Prime (no native support)', self.mml.exec_amazon_prime, self.wid, 210, 625)
        self.quit_button(self.wid)

        self.wid.show()

        return

    def movieUI(self):
        print('movie')

        return

    def serieUI(self):
        print('serie')

        return

    def musicUI(self):
        self.wid.hide()
        self.wid = self.create_widget(self.mw)

        self.push_button('Spotify', self.mml.exec_spotify, self.wid, 210, 25)
        self.push_button('Soundcloud', self.helper, self.wid, 210, 225)
        self.push_button('Local Music', self.helper, self.wid, 210, 225)
        self.quit_button(self.wid)

        self.wid.show()

        return

    def gamesUI(self):
        print('games')

        return

    def helper(self):
        print('helper is helping')

        return

    def create_main_window(self):
        # Creates the main window which is used as parent for every widget.
        # Every new widget becomes the main window in front of the real main window.
        # This is due the easy access for widgets
        mw = QtGui.QMainWindow()
        mw.resize(self.width, self.height)
        mw.setWindowTitle('WGus Managerus')

        # Colors the main window
        p = mw.palette()
        p.setColor(mw.backgroundRole(), QtCore.Qt.lightGray)
        mw.setPalette(p)

        return mw

    def create_widget(self, mw):
        # Creates a new widgit using the current screen resolution
        wid = QtGui.QWidget(mw)
        wid.resize(self.width, self.height)
        wid.setWindowTitle('WGus Managerus')

        # Colors the widgit
        p = wid.palette()
        p.setColor(wid.backgroundRole(), QtCore.Qt.lightGray)
        wid.setPalette(p)

        return wid

    def quit_button(self, parent):
        qbtn = QtGui.QPushButton('EXIT', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(700, 125)
        qbtn.move(610, 850)

        return qbtn

    def push_button(self, name, function, parent, x , y):
        '''

        :param x:
        :param y:
        :param parent:
        :param name:
        :param function:
        :return:
        '''
        qbtn = QtGui.QPushButton(name, parent)
        qbtn.setStyleSheet("QPushButton { font-size: 32pt }" )
        qbtn.clicked.connect(function)
        qbtn.resize(1500, 175)
        qbtn.move(x, y)

        return qbtn



if __name__ == '__main__':
    FrontEnd().initUI()
