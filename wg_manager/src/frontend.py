#!/usr/bin/python
import sys
from PySide import QtCore, QtGui
from wg_manager.src.wg_lib import MultiMediaLib

class FrontEndException(Exception):
    pass


class FrontEnd():
    def __init__(self):
        self.mml = MultiMediaLib()

#    def main(self, app, mw, next_element):
#        '''#
#
#        :param next_element:
#        :return:
#        '''
#        self.app = app
#        self.width = app.desktop().screenGeometry().width()
#        self.height = app.desktop().screenGeometry().height()
#        wid = self.create_widget(mw)
#        if not next_element:
#            next_element = 'init'
#        next_element = '{}UI'.format(next_element.lower())
#        call = getattr(FrontEnd(), next_element)
#        call(wid)

        #return

    def initUI(self, wid):
        print('asdf')
        self.push_button('News', wid, 210, 25)
        self.push_button('Movie', wid, 210, 225)
        self.push_button('Music', wid, 210, 425)
        self.push_button('Games', wid, 210, 625)
        self.quit_button(wid)

        wid.show()

        return

    def newsUI(self, wid):
        '''

        :return:
        '''
        self.quit_button(wid)

        return

    def movieUI(self, wid):
        self.push_button('Local Movies', wid, 210, 25)
        self.push_button('Local Series', wid, 210, 225)
        self.push_button('Netflix', wid, 210, 425)
        self.push_button('Streaming (this will take sooooo much time)', wid, 210, 625)
        self.quit_button(wid)

        wid.show()

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

    def quit_button(self, parent):
        qbtn = QtGui.QPushButton('EXIT', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(700, 125)
        qbtn.move(610, 850)

        return qbtn

    def push_button(self, name, parent, x, y):
        '''

        :param x:
        :param y:
        :param parent:
        :param name:
        :return:
        '''
        qbtn = QtGui.QPushButton(name, parent)
        qbtn.setStyleSheet("QPushButton { font-size: 32pt }" )
        qbtn.clicked.connect(lambda: self.loopy(name, parent))
        qbtn.resize(1500, 175)
        qbtn.move(x, y)

        return qbtn

    def loopy(self, name, current_wid):
        # Ich hab echt kein bock mehr mir namen für die helper meiner helper meiner helper funktionen auszudenken!
        current_wid.hide()

        return self.main(name)

if __name__ == '__main__':
    FrontEnd().main()
