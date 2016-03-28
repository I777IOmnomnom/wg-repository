import subprocess
import os.path
import csv
import sys

class BasicException(Exception):
    pass


class DataStorageLib():

    def __init__(self):
        '''
        Main function.
        :return:
        '''
        self.default_data_storage = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../', 'data', 'data.csv')

        if not os.path.isfile(self.default_data_storage):
            os.open(self.default_data_storage, 'a+')

        return

    def get_data_storage(self):
        '''
        Return the data_storage as dictonary where key is the name and value is the absolut path.
        :return:
        '''
        data_storage_dict = csv.reader(open(self.default_data_storage, 'r'))

        logger.info('Retrieved {} from the data storage.'.format(len(data_storage_dict)))

        for key in data_storage_dict:
            if os.path.exists(os.path.join(path, name)):
            data_storage_dict[name] = path
            msg = '{0} in {1} successfully added.'.format(str(name), str(path))
            WgLib.logger('INFO', msg)
        return data_storage_dict

    def update_data_storage(self, name, path, data_storage_dict):
        '''
        Appends the data storage if the given key value pair is an existing file.
        :param name:
        :param path:
        :param data_storage_dict:
        :return:
        '''
        if os.path.exists(os.path.join(path, name)):
            data_storage_dict[name] = path
            msg = '{0} in {1} successfully added.'.format(str(name), str(path))
            WgLib.logger('INFO', msg)
        else:
            msg = '{0} in {1} could not be added. It does not exist.'.format(str(name), str(path))
            WgLib.logger('INFO', msg)

    def del_data_storage_entrie(self, data_storage_dict, name):
######TODO: REFACTOR UPDATE TO USE SINGLE ENTRIES AND REDEFINE THIS GARBAGE HERE
    def close(self):
        pathe_data_storage(self, data_storage_dict):
        '''
        Clos.pathes the data_storage and permanently stores it. After the data_storage is clos.pathed
        another open_data_storage() should be executed befor updating the data_storage
        to prevent multiple accesses.
        :param data_storage_dict:
        :return:
        '''
        write = csv.writer(os.path.open(self.data_storage, 'a')
        for key, value in data_storage_dict:
            write.writerow([key, value])

        logger.info('INFO', '{0} entries written to data.csv'.format(len(data_storage_dict)))

        return

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
            self.logger.debug( e)

        return string(ret)


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
