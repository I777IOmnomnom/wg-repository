#!/usr/bin/python
from optparse import OptionParser
import sys
import time
import inspect

from PySide import QtCore, QtGui
from media_handler import MediaHandler
from wg_lib import MultiMediaLib, logger

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
        self.mml = MultiMediaLib()
        self.mh = MediaHandler()
        self.logger = logger()

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
        if not dialog:
            dialog = 'init'

        if dialog == 'init':
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

        elif dialog == 'Series':
            self.seriesUI(wid)

        elif dialog == 'Netflix':
            self.mml.exec_netflix()

        elif dialog == 'Streaming':
            self.helper()

        elif dialog == 'Spotify':
            self.mml.exec_spotify()

        elif dialog == 'Soundcloud':
            self.mml.exec_soundcloud()

        elif dialog == 'Music (local)':
            self.local_musicUI(wid)

        elif dialog == 'Steam':
            self.mml.exec_steam()

        elif dialog == 'Emulator':
            self.emulatorUI()

        elif dialog == 'Games (local)':
            self.local_gamesUI()

        elif dialog == 'Return':
            #magic incoming
            last_dialog = '{}UI'.format(last_dialog)

            class_function = inspect.getmembers(Executioner(), predicate=inspect.ismethod)

            for key in class_function:
                if key == last_dialog:
                    class_function[key]()
        else:
            sys.exit(app.exec_())

        self.logger.info('{}UI is initiated'.format(dialog))

        return

    def initUI(self, wid):
        """
        Initial dialog.

        :type wid:
        :param wid:
        :return:
        """
        self.push_button('News', wid, 210, 25)
        self.push_button('Video', wid, 210, 225)
        self.push_button('Music', wid, 210, 425)
        self.push_button('Games', wid, 210, 625)

        self.quit_button(wid)

        ret = wid.show()

        self.logger.info(ret)

        return ret

    def newsUI(self, wid):
        """

        :param wid:
        :return:
        """
        self.push_button('News are not implemented', wid, 210, 25)
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
        self.push_button('Streaming', wid, 210, 625)
        self.quit_button(wid)

        wid.show()

        return

    def musicUI(self, wid):
        """

        :return:
        """
        self.push_button('Spotify', wid, 210, 25)
        self.push_button('Soundcloud(X)', wid, 210, 225)
        self.push_button('Music (local)', wid, 210, 425)
        self.quit_button(wid)

        wid.show()

        return

    def gamesUI(self, wid):
        """

        :return:
        """
        self.push_button('Steam', wid, 210, 25)
        self.push_button('Emulator', wid, 210, 225)
        self.push_button('Games (local)', wid, 210, 425)
        self.quit_button(wid)

        return

    def moviesUI(self, wid):
        """

        :param wid:
        :return:
        """
        movie_list = self.mh.get_movie_list()
        self.create_list_view(wid, movie_list)

        return

    def seriesUI(self, wid):
        """

        :param wid:
        :return:
        """
        # TBD

        wid.show()

        return

    def local_musicUI(self, wid):
        """

        :param wid:
        :return:
        """
        # TBD

        wid.show()

        return

    def emulatorUI(self, wid):
        """

        :return:
        """
        self.push_button('Steam', wid, 210, 25)
        self.push_button('Emulator', wid, 210, 225)
        self.push_button('Games (local)', wid, 210, 425)
        self.quit_button(wid)

        return

    def local_gamesUI(self, wid):
        """

        :return:
        """
        self.push_button('Steam', wid, 210, 25)
        self.push_button('Emulator', wid, 210, 225)
        self.push_button('Games (local)', wid, 210, 425)
        self.quit_button(wid)

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

        p = wid.palette()
        p.setColor(wid.backgroundRole(), QtCore.Qt.lightGray)
        wid.setPalette(p)

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
        :param parent:
        :return:
        """
        parent.hide()

        last_dialog = str(inspect.stack()[1][3])
        current_dialog = str(name)

        return self.frontend_selector(current_dialog, last_dialog)

if __name__ == '__main__':
    Executioner().main()
