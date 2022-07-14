# coding=utf-8
import allure
import pytest
import time

import common.cls.public
from Web.em import youjian
from Web.appkeys import AppKey
from common.cls.public import CommonPublic
from ddt.params import demo_sql_params
demo_sql = demo_sql_params('nox_browser')
CommonPublic = CommonPublic()


@allure.feature('项目名称')
class TestCommerce:
    num = 0
    title = ''

    def setup_class(self):
        self.web = AppKey()

    @staticmethod
    def setup_method():
        table_ncols = demo_sql[TestCommerce.num:TestCommerce.num + 1][0]
        TestCommerce.title = table_ncols[0:][0]

    @allure.story('用例:%s' % title)
    @pytest.mark.parametrize('table', demo_sql)
    def test_login(self, table):
        testcases = table[4:]
        testcases = [i for i in testcases if i != '']
        func = getattr(self.web, testcases[0])
        values = testcases[1:]
        try:
            func(*values)
            CommonPublic.log(testcases)

        except AssertionError as msg:
            CommonPublic.log(testcases)
            CommonPublic.log(msg)

    @staticmethod
    def teardown_method():
        TestCommerce.num = TestCommerce.num + 1
