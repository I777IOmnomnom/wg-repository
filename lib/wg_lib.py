import logging as logging
import subprocess

from conf import config as cfg


class WgLibException(Exception):
    pass

class DataQuerrierLib(self):
    pass

class WgLib()
    def exec_nas_cmd(self, cmd):
        user, password = cfg.Identifier.get_identifications('NAS')

        cmd = ('sshpass -p ' + password + ' ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -q -p 22 ' +
               user + '@wgserv' + ' ' + '\'' + cmd + '\'')

        return exec_cmd(cmd)

    def exec_cmd(cmd):
        '''

        :param cmd:
        :return:
        '''
        if not cmd:
            logger('INFO', 'No cmd given. Nothing happend.')

        return subprocess.check_output(cmd)

    def logger(type, msg):
        '''

        :param self:
        :param type:
        :param msg:
        :return:
        '''
        logger = logging.getLogger()
        if type is 'INFO':
            logger.info(msg)
        elif type is 'DEBUG':
            logger.warning(msg)
        else type is 'warning':
            raise WgLibException('No suitable type given. Please use only INFO and DEBUG.')

        return