import subprocess
import os.path
import csv
import sys

from PySide import QtGui, QtCore

class BasicException(Exception):
    pass

class WgLib():
    def format_list(self, list, seperator='-'):
        '''
        Takes a list and formats it. Returns a list with single elements. The seperator
        is used to identify values which are connected by them. The function will acknowledge
        the values splitted by the seperator as minimal and maximal value. The range between
        minimal and maximal value (including min. and max.) is then inserted into the list as
        single elements
        :param list:
        :param seperator:
        :return:
        '''
        list = list.split(seperator)

        for list_entry in list:
            if re.search('-', list_entry):
                mini = int(list_entry.split('-')[0])
                maxi = int(list_entry.split('-')[1]) + 1
                for _ in range(mini, maxi):
                    list.append(_)
            else:
                list.append(list_entry)

        return list

    def get_dir_list(self, path):
        '''
        Return a list paths containing the initial path and appended all
        contained files. With get_dir_list().split('/')[-1] the actual contained
        files can be retrieved.
        :param path:
        :return:
        '''
        dirs = []
        ret = os.path.listdir(path)

        for _ in ret:
            dir = os.path.join(path, _)
            dirs.append(dir)

        return dirs

    def get_dir_type(self, dir):
        '''
        Returns the filetype, weather dir or file.
        :param dir:
        :return:
        '''
        if os.path.isfile(dir) is True:
            type = 'file'
        else:
            type = 'dir'

        return type

    def exec_cmd(self, cmd):
        '''
        Executes a command after checking if the command is empty.
        The return is always a string! The returncode is logged
        as Debug.
        :param cmd:
        :return:
        '''
        if cmd is None:
            raise WgLibException('No command given.')

        log_msg = 'Executing: ' + str(cmd)
        self.logger.info(log_msg)

        try:
            ret = subprocess.check_output(cmd, shell=True, universal_newlines=True).strip()
        except subprocess.CalledProcessError as e:
            self.logger.debug(e)

        return string(ret)


class FrontEndElements():

    def __init__(self):
        pass

    def create_widget(self, width, height):
        wid = QtGui.QWidget()
        wid.resize(width, height)
        wid.setWindowTitle('WGus Managerus')
        p = wid.palette()
        p.setColor(wid.backgroundRole(), QtCore.Qt.lightGray)
        wid.setPalette(p)

        return wid

    def quit_button(self, parent):
        qbtn = QtGui.QPushButton('EXIT', parent)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(700, 180)
        qbtn.move(6010, 700)

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
        qbtn.clicked.connect(function)
        qbtn.resize(1500, 200)
        qbtn.move(x, y)

        return qbtn


class logger():

    def info(self, msg):
        '''
        Logs with type INFO.
        :param msg:
        :return:
        '''
        date = self.get_asci_time()
        log_msg = ' - '.join(date, str(msg))

        return sys.stdout.write(log_msg)

    def debug(self, msg):
        '''
        Logs with type DEBUG.
        :param msg:
        :return:
        '''
        date = self.get_asci_time()
        log_msg = ' - '.join(date, str(msg))

        return sys.stdout.write(log_msg)

    def get_asci_time(self):
        import time
        '''
        Returns the current time in YYYY.MM.DD - HH:MM:SS as string.
        :return:
        '''
        #current time is returned in WD MM DD HH:MM:SS YYYY
        time_list = time.asctime().strip().split(' ')

        year = time_list[4]
        month = time_list[1]
        day = time_list[2]
        time = time_list[3]

        ret = str(' - '.join(' '.join(year, month, day), time))

        return ret

if __name__ is '__main__':
    __init__ = DataModelLib
    __init__.generate_datamodel()
