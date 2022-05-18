# -*- coding:utf-8 -*-

from djangoProject.base_log.log import Log

class Test():

    def __init__(self):
        log = Log()
        self.logger = log.get_log()
    def test1(self):
        self.logger.debug("张三,ceshiyixia")

test = Test()
test.test1()


