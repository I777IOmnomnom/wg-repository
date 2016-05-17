import subprocess
import os.path
import csv
import sys
import glob

from PySide import QtGui, QtCore


class LibException(Exception):
    pass


class NasLib:
    def get_file_list(self, path):
        '''
        Return a list absolute paths for every file on the storage system. With get_file_list().split('/')[-1]
        the actual files can be retrieved.

        :param path:
        :return:
        '''
        files = []
        for dirpath, _, filenames in os.walk(path):
            for file in filenames:
                files.append(os.path.join(dirpath, file))

        return files

    def get_file_type(self, dir):
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

class SystemLib():

    def __init__(self):
        self.config_file = os.path.join(os.path.dirname(__file__), '..', 'conf', 'config.csv')

    def get_config_param(self, param):

        config_dict = {}

        reader = csv.reader(open(self.config_file, 'r'))
        for row in reader:
            parameter, value = row
            if param == 'all':
                config_dict[parameter] = value
            elif param == parameter:
                return value
            else:
                self.logger.alert('Missing config parameter: {} in {}.'.format(param, self.config_file))

        return config_dict

    def exec_cmd(self, cmd):
        '''
        Executes a command after checking if the command is empty.
        The return is always a string! The returncode is logged
        as Debug.
        :param cmd:
        :return:
        '''
        if cmd is None:
            raise LibException('No command given.')

        log_msg = 'Executing: {}'.format(cmd)
        self.logger.info(log_msg)

        try:
            ret = subprocess.check_output(cmd, shell=True, universal_newlines=True).strip()
        except subprocess.CalledProcessError as e:
            log_msg_alert = 'Non-Zero exit status ({}) for command: {}'.format(e.returncode, cmd)
            log_msg_debug = 'Returncode: {}, Error: {}, Command: {}'.format(e.returncode, e , cmd)
            self.logger.alert(log_msg_alert)
            self.logger.debug(log_msg_debug)
        return str(ret)

class logger():

    def info(self, msg):
        '''
        Logs with type INFO.
        :param msg:
        :return:
        '''
        date = self.get_asci_time()
        log_msg = ' - '.join([date, str(msg), '\n'])

        return sys.stdout.write(log_msg)

    def debug(self, msg):
        '''
        Logs with type DEBUG.
        :param msg:
        :return:
        '''
        date = self.get_asci_time()
        log_msg = ' - '.join([date, str(msg), '\n'])

        return sys.stdout.write(log_msg)

    def alert(self, msg):
        '''
        Logs with type DEBUG.
        :param msg:
        :return:
        '''
        date = self.get_asci_time()
        log_msg = ' - '.join([date, str(msg), '\n'])

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

        ret = str(' - '.join(['.'.join([year, month, day]), time]))

        return ret


if __name__ == '__main__':
    SystemLib().get_config_param('media_path')