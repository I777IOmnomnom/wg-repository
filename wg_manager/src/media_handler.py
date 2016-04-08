#!/usr/bin/python
import sys
from wg_manager.src.wg_lib import SystemLib
from wg_manager.src.wg_lib import NasLib

class MediaHandlerException(Exception):
    pass


class MediaHandler():

    def __init__(self):
        sl = SystemLib()
        nl = NasLib()
        self.storage = sl.get_config_param('media_path')
        self.media_list = nl.get_file_list(self.storage)


    def create_media_dict(self):


if __name__ == '__main__':
    MediaHandler().init()