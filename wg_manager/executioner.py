#!/usr/bin/python

import sys
import time
from PySide import QtCore, QtGui
from wg_manager.src.frontend import FrontEnd
from wg_manager.src.wg_lib import SystemLib

class ExecutionerException(Exception):
    pass

class Executioner():
    def __init__(self):
        self.sl = SystemLib()
        self.gui = FrontEnd()

    def main(self):
        '''
        Defines the main execution loop of the application.

        :return:
        '''
        # Creates the background application which is responsible for handling all PySide elements.
        app = QtGui.QApplication(sys.argv)
        self.width = app.desktop().screenGeometry().width()
        self.height = app.desktop().screenGeometry().height()

        # Creates the main window which is used to handle widgets.
        mw = QtGui.QMainWindow()
        mw.resize(self.width, self.height)
        mw.setWindowTitle('WGus Managerus')

        # Paints the main window in light grey. The main window should never appear to the user!
        p = mw.palette()
        p.setColor(mw.backgroundRole(), QtCore.Qt.lightGray)
        mw.setPalette(p)

        mw.show()

        next_element = 'init'

        while True:
            wid = self.create_widget(mw)
            next_element = '{}UI()'.format(next_element)
            call = globals()[next_element]
            self.gui.call()

        sys.exit(app.exec_())

    def create_widget(self, mw):
        wid = QtGui.QWidget(mw)
        wid.resize(self.width, self.height)
        wid.setWindowTitle('WGus Managerus')

        p = wid.palette()
        p.setColor(wid.backgroundRole(), QtCore.Qt.lightGray)
        wid.setPalette(p)

        return wid
if __name__ == '__main__':
    Executioner().main()