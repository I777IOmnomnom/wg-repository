#!/usr/bin/python3
import sys
import time
import os

from wg_lib import NasLib, SystemLib, logger

class MediaHandlerException(Exception):
    pass


class MediaHandler():

    def __init__(self):
        self.sl = SystemLib()
        self.nl = NasLib()
        self.logger = logger()

    def get_movie_list(self):
        """

        :return:
        """
        file_list = self.nl.get_file_list()
        movie_list = MediaClassificationEngine().get_media_list_by_type(file_list, 'movie')

        return movie_list

class MediaClassificationEngine:
    def __init__(self):
        self.logger = logger()
        self.video_codec_list = ['avi', 'cam', 'mkv', 'mov', 'mpeg', 'mpg', 'mpe', 'svi', 'wmv',]
        self.music_codec_list = ['jpeg', 'png', 'ppm', 'jpg', 'tga']
        self.image_codec_list = []
        self.doc_codec_list = []


    def get_media_list_by_type(self, file_list, type=None):
        """
        Extracts all files from a list and classifies them. If type is given, only a dict for the given file type is
        returned
        :param file_list:
        :param type:
        :return:
        """
        movie_list = []
        series_list = []
        music_list = []
        doc_list = []
        image_list = []

        begin = time.time()

        for index, file in enumerate(file_list):
            postfix = file.split('.')[-1]
            filesize = os.stat(file).st_size

            if postfix in self.video_codec_list:
                self.logger.info('{} is classified as video with a size of {}'.format(file, filesize))

                if postfix == 'mkv' and filesize <= '3000000000':
                    media_type = 'series'
                    series_list.append(file)

                elif postfix == 'mkv':
                    media_type = 'movie'
                    movie_list.append(file)

                elif postfix != 'mkv' and filesize <= '1000000000':
                    media_type = 'series'
                    series_list.append(file)

                else:
                    media_type = 'movie'
                    movie_list.append(file)

            elif postfix in self.music_codec_list:
                self.logger.info('{} is classified as music with a size of {}'.format(file, filesize))

                music_list.append(file)

            elif postfix in self.image_codec_list:
                self.logger.info('{} is classified as image with a size of {}'.format(file, filesize))

                image_list.append(file)

            elif postfix in self.doc_codec_list:
                self.logger.info('{} is classified as document with a size of {}'.format(file, filesize))

                doc_list.append(file)

            else:
                self.logger.alert('Postfix {} of {} is an unknown codec and therefor ignored!'.format(postfix, file))

        end = time.time()
        duration = float(end) - float(begin)

        self.logger.info('It took {} seconds to process {} different files!'.format(duration, index))

        if type == 'movie':
            return movie_list
        elif type == 'series':
            return series_list
        elif type == 'music':
            return music_list
        elif type == 'document':
            return doc_list

        return movie_list, series_list, music_list, doc_list

if __name__ == '__main__':
    MediaHandler().init()
