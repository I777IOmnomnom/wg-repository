from lib.wg_lib import WgLib
import os

class MediaFileManagerException(Exception):
    pass

class NasFileManager(self):
    def __init__(self, path='Multimedia'):
        '''

        :return:
        '''

        self.exec = WgLib.exec_nas_cmd(cmd)

        self.source = '/share/MD0_DATA/'
        self.current_file = 0

    def get_






        cmd = 'll ' + source + ' | grep ' + path + ' | cut -d \' \' -f4'
        source_file_count = self.exec(cmd)

        source = source + path


    def get_file_names(self, source_file_count):
        while current_file < (source_file_count - 3):

        return

    def get_initial_

    def retrieve_files(self):
        '''

        :return:
        '''
        cmd = 'll'
