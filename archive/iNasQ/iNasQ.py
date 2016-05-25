#!/usr/bin/python3
import os
import time
from lib import logger


class iNasQException(Exception):
    pass


class iNasQ():
    """
    iNasQ, the intelligent network attached storage Querrier is designed to clean up NAS systems after a predefined
    schema, including:
    * renaming after a certain patter
    * reording content after its content classification results
    * creating an easy to access file based data structure for further processing of NAS contents
    * dynamic working with all accessible files
    """
    def __init__(self):
        pass
