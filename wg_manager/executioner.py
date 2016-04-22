#!/usr/bin/python
from optparse import OptionParser
import sys
import time
import inspect
from PySide import QtCore, QtGui
from media_handler import MediaHandler

# Creates the background application which is responsible for handling all PySide elements.
app = QtGui.QApplication(sys.argv)
width = app.desktop().screenGeometry().width()
height = app.desktop().screenGeometry().height()

# Creates the main window which is used to handle widgets.
mw = QtGui.QMainWindow()
mw.resize(width, height)
mw.setWindowTitle('WGus Managerus')

# Paints the main window in light grey. The main window should never appear to the user!
p = mw.palette()
p.setColor(mw.backgroundRole(), QtCore.Qt.lightGray)
mw.setPalette(p)


class ExecutionerException(Exception):
    pass


class Executioner:
    def __init__(self):
        self.mh = MediaHandler()

    def main(self):
        """

        :return:
        """
        self.frontend_selector()

        return

    def frontend_selector(self, dialog=None, last_dialog=None):
        """

        :param dialog:
        :param last_dialog:
        :return:
        """
        wid = self.create_widget()

        if dialog is None:
            self.initUI(wid)

        elif dialog == 'News':
            self.newsUI(wid)

        elif dialog == 'Video':
            self.videoUI(wid)

        elif dialog == 'Music':
            self.musicUI(wid)

        elif dialog == 'Games':
            self.gamesUI(wid)

        elif dialog == 'Movie':
            self.moviesUI(wid)

        elif dialog == 'Return':
            #magic incoming
            last_dialog = '{}UI'.format(last_dialog)

            class_function = inspect.getmembers(Executioner(), predicate=inspect.ismethod)

            for key in class_function:
                if key == last_dialog:
                    class_function[key]()
        else:
            sys.exit(app.exec_())

        return

    def initUI(self, wid):
        """
        Initial dialog.

        :param wid:
        :return:
        """
        self.push_button('News', wid, 210, 25)
        self.push_button('Video', wid, 210, 225)
        self.push_button('Music', wid, 210, 425)
        self.push_button('Games', wid, 210, 625)

        self.quit_button(wid)

        wid.show()

        return

    def newsUI(self, wid):
        """

        :param wid:
        :return:
        """
        self.push_button('not implemented', wid, 210, 25)
        self.quit_button(wid)

        return

    def videoUI(self, wid):
        """

        :param wid:
        :return:
        """
        self.push_button('Movie', wid, 210, 25)
        self.push_button('Series', wid, 210, 225)
        self.push_button('Netflix', wid, 210, 425)
        self.push_button('Streaming (this will take much time)', wid, 210, 625)
        self.quit_button(wid)

        wid.show()

        return

    def musicUI(self, wid):
        """

        :return:
        """
        self.push_button('Spotify', self.mml.exec_spotify, wid, 210, 25)
        self.push_button('Soundcloud(X)', self.helper, wid, 210, 225)
        self.push_button('Local Music(X)', self.helper, wid, 210, 225)
        self.quit_button(wid)

        wid.show()

        return

    def gamesUI(self, wid):
        """

        :return:
        """
        print('games')

        return

    def moviesUI(self, wid):
        """

        :param wid:
        :return:
        """
        movie_list = self.mh.get_movie_list()
        self.create_list_view(wid, movie_list)

    def seriesUI(self, wid):
        """

        :return:
        """
        # GET SERIES LIST

        return

    def helper(self):
        """

        :return:
        """
        print('helper is helping')

        return

    def create_widget(self):
        """
        Creates a widget where sub-elements as buttons, lists, etc are attached to. The widget is painted in light
        grey and resized to the full screen resolution.

        :return:
        """
        global mw, width, height

        wid = QtGui.QWidget(mw)
        wid.resize(width, height)
        wid.setWindowTitle('WGus Managerus')

        _ = wid.palette()
        _.setColor(wid.backgroundRole(), QtCore.Qt.lightGray)
        wid.setPalette(_)

        return wid

    def create_list_view(self, parent, file_list):
        """

        :param list:
        :return:
        """
        list = QtGui.QListView(parent)
        list.setModel(file_list)

        return list

    def push_button(self, name, parent, x, y):
        """
        Creates a button and docks it to the parent. When clicked the button executes loopy which handles the further
        execution. This needs to be abstracted to loopy as direct jumping would mess up the dialog handling.

        :param name:
        :param parent:
        :param x:
        :param y:
        :return:
        """
        qbtn = QtGui.QPushButton(name, parent)
        qbtn.setStyleSheet("QPushButton { font-size: 32pt }")
        qbtn.clicked.connect(lambda: self.loopy(name, parent))
        qbtn.resize(1500, 175)
        qbtn.move(x, y)

        return qbtn

    @staticmethod
    def quit_button(parent):
        qbtn = QtGui.QPushButton('EXIT', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(700, 125)
        qbtn.move(610, 850)

        return qbtn

    def loopy(self, name, parent):
        """
        Extracts the calling functions name using inspect. Sets the current dialog to the button name which is handled
        by the frontend selector (loopy is cool).

        :param name:
        :param current_wid:
        :return:
        """
        parent.hide()

        last_dialog = str(inspect.stack()[1][3])
        current_dialog = str(name)

        return self.frontend_selector(current_dialog, last_dialog)

if __name__ == '__main__':
    Executioner().main()
