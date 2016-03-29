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
        pass

    def run(self):
        pass


if __name__ == '__main__':
    FrontEnd().init()
