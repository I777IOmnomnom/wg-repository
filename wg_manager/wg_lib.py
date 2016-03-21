import logging as logging
import subprocess
import os

class WgLibException(Exception):
    pass

class DataQuerrierLib():
    pass

class WgLib():
    def get_dir_list(self, path):
        '''
        Return a list paths containing the initial path and appended all
        contained files. With get_dir_list().split('/')[-1] the actual contained
        files can be retrieved.

        :param path:
        :return:
        '''
        dirs = []
        ret = os.listdir(path)

        for _ in ret:
            dir = os.path.join(path, _)
            dirs.append(dir)

        return dirs

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
        self.logger('INFO', log_msg)

        try:
            ret = subprocess.check_output(cmd, shell=True, universal_newlines=True).strip()
        except subprocess.CalledProcessError as e:
            self.logger('DEBUG', e)

        return string(ret)

    def logger(type, msg):
        '''
        Logs in INFO or Debug after checking is the msg is not empty.

        :param self:
        :param type:
        :param msg:
        :return:
        '''
        logger = logging.getLogger()
        if type is 'INFO':
            logger.info(msg)
        elif type is 'DEBUG':
            logger.debug(msg)
        else:
            raise WgLibException('No suitable type given. Please use only INFO and DEBUG.')

        return