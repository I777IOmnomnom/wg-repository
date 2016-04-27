import subprocess
import os.path
import csv
import sys
import glob

from PySide import QtGui, QtCore


class BasicException(Exception):
    pass

class MultiMediaLib:

    def exec_netflix(self):
        pw = getpw()
        cmd = ['/usr/bin/netflix-desktop', '--enable-hw-acceleration']
        netflix = subprocess.Popen(['sudo', '-S'] + cmd,
                                    stdin=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    universal_newlines=True)
        #netflix.communicate(pw + '\n')[1]

        return

    def exec_spotify(self):
        subprocess.Popen('spotify')

        pass

    def exec_vlc(self,titel, subtitle=False, fullscreen=True, language='german'):
        pass

    def exec_amazon_prime(self):
        pass

    def exec_soundcloud(self):
        """

        :return:
        """
        app = 'firefox'
        mode = '--new-window'
        url = 'http://soundcloud.com'

        subprocess.Popen([app, mode, url],
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)

    def exec_steam(self):
        """

        :return:
        """
        app = 'steam'
        mode = '-bigpicture'

        subprocess.Popen([app, mode],
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True)

class NewsLib:

    def get_rss_feed(self, source):
        pass

    def analyze_rss_feed(self, rss_feed):
        pass

    def format_rss_feed(self, rss_feed):
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

        return str(ret)


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