#!/usr/bin/env python

import urllib2
import lxml.html as lh


class MediaFileException(Exception):
    pass


class MediaFileClassificationEngine():

    def __main__(self):
        """
        @brief: Initial call function
        """

        return

    def init(self):
        '''
        @brief: init function
        '''
        self.get_source_code_html()

        return

    def get_source_code_html(self):
        title_count = 0
        board = 'http://www.boerse.sx'
        movie = '/boerse/videoboerse/hd-area/'
        serie = '/boerse/videoboerse/serien/'
        self.media_file_title = []
        self.media_file_url = []

        source = lh.parse(urllib2.urlopen(board + movie))
        #print(source)
        root = source.getroot()
        foundurls = 0
        for link in root.iter('a'):
            foundurls += 1
            print(link.attrib)
            if 'href' and 'id' in link.attrib.keys():
                if "720p" in str(link.text) or "1080p" in str(link.text) and "thread_title" in link.attrib['id']:
                    print('Title: ' + str(link.text) + ' - URL: ' + str(link.attrib['href']))
                    self.store_media_file_entries(str(link.attrib['href'], str(link.text))) # TBD
                    title_count += 1


        print('Received titles: ' + str(title_count))
        if title_count == 0:
            raise MediaFileException('Nothing found but the site is available')
        elif foundurls == 0:
            raise MediaFileException('No sourcecode could be retrieved, maybe ' + board + ' is offline')  # noqa

        return

    def store_media_file_entries(self, url, name):
        '''
        @brief:
        '''
        self.media_file_title.append(name)
        self.media_file_url.append(url)

        print(self.media_file_title)
        print(self.media_file_url)

        pass

if __name__ == "__main__":
    classification = MediaFileClassificationEngine()
    classification.init()