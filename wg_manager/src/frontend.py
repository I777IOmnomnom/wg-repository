#!/usr/bin/python
import sys
from PySide import QtCore, QtGui
from wg_manager.src.wg_lib import FrontEndElements

gui, core = config()

def config():
    # I shouldn't do the bellow here but this frontend shit fucks me up
    app = QtGui.QApplication(sys.argv)
    get_screen = app.desktop().screenGeometry()
    width, height = get_screen.width(), get_screen.height()
    mw = FrontEndElements.create_main_window(width, height)
    mw.show()
    gui = QtGui
    core = QtCore

    return gui, core


class FrontEndException(Exception):
    pass


class FrontEnd():
##### This might be the worst FrontEnd approach I could have choosen but it's the easiest one #####
# Every new "tap" creates its own frontend which is located in deticated methods.
# The wglib provides a basic algorithm to create buttons, widgits and function calls.

    def __init__(self):
        self.fee = FrontEndElements()

    def initUI(self):
        wid = self.fee.create_widget(width, height)

        self.fee.push_button('Explore something (Platzhalter)', self.movieUI, wid, 210, 25)
        self.fee.push_button('Watch something...', self.serieUI, wid, 210, 225)
        self.fee.push_button('List to something...', self.musicUI, wid, 210, 425)
        self.fee.push_button('Play something ...', self.gamesUI, wid, 210, 625)
        self.fee.quit_button(wid)

        wid.show()
        sys.exit(app.exec_())

        return

    def newsUI(self):
        pass

    def mediaUI(self):
        self.wid.hide()
        wid = self.fee.create_widget(width, height)

        self.fee.push_button('Watch movie from NAS', self.helper, wid, 210, 25)
        self.fee.push_button('Watch serie from NAs', self.helper, wid, 210, 225)
        self.fee.push_button('Watch Netflix', self.helper, wid, 210, 425)
        self.fee.quit_button(wid)

        sys.exit(app.exec_())

    def movieUI(self):
        print('movie')

    def serieUI(self):
        print('serie')

    def musicUI(self):
        print('music')

    def gamesUI(self):
        print('games')

    def helper(self):
        print('helper is helping')
if __name__ == '__main__':
    FrontEnd().initUI()
