#!/usr/bin/python
import sys
from PySide import QtCore, QtGui
from wg_manager.src.wg_lib import FrontEndElements

app = QtGui.QApplication(sys.argv)
gui = QtGui
core = QtCore


class FrontEndException(Exception):
    pass


class FrontEnd():

    def __init__(self):
        self.fee = FrontEndElements()
        get_screen = app.desktop().screenGeometry()
        self.width, self.height = get_screen.width(), get_screen.height()

    def init(self):
        wid = self.fee.create_widget(self.width, self.height)
        self.fee.push_button('Movie', self.help(), wid, 210, 25)
        self.fee.push_button('Serie', self.help(), wid, 210, 250)
        self.fee.push_button('Music', self.help(), wid, 210, 475)
        self.fee.push_button('Games', self.help(), wid, 210, 700)
        self.fee.quit_button()
        wid.show()
        sys.exit(app.exec_())

    def help(self):
        print('success')
if __name__ == '__main__':
    FrontEnd().init()
