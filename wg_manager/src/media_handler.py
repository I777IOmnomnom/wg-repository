#!/usr/bin/python
import sys
from wg_manager.src.wg_lib import NasLib


class MediaHandlerException(Exception):
    pass


class MediaHandler():

    def __init__(self):
        storage =