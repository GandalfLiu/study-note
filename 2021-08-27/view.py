#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os

import logging

from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0




class LogHandler(logging.Logger):
    """
    LogHandler
    """

    def __init__(self, name, filename, level=DEBUG, stream=True, file=True):
        self.name = name
        self.filename = filename
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        if stream:
            self.__setStreamHandler__(INFO)
        if file:
            self.__setFileHandler__(self.filename, DEBUG)

    def __setFileHandler__(self, filename, level=None):
        """
        set file handler
        :param level:
        :return:
        """
        file_handler = RotatingFileHandler(filename, mode="w", encoding="utf-8")
        file_handler.suffix = '%Y-%m-%d.log'
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:  %(message)s')

        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        """
        set stream handler
        :param level:
        :return:
        """
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:  %(message)s')
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)
