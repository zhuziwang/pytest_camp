# coding=utf-8
import allure
import pytest
import time

import common.cls.public
from Web.em import youjian
from Web.webkeys import WebKey
from common.cls.public import CommonPublic
from ddt.params import demo_sql_params
demo_sql = demo_sql_params('yongli1')
CommonPublic = CommonPublic()


@allure.feature('项目名称')
class TestCommerce:
    num = 0
    title = ''

    def setup_class(self):
        self.web = WebKey()

    @staticmethod
    def setup_method():
        table_ncols = demo_sql[TestCommerce.num:TestCommerce.num + 1][0]
        TestCommerce.title = table_ncols[0:][0]

    @allure.story('用例:%s' % title)
    @pytest.mark.parametrize('table', demo_sql)
    def test_login(self, table):
        testcases = table[2:]
        testcasess = table[1]
        for table_num in range(1, len(testcases)):
            if testcases[table_num] is None:
                testcases[table_num] = ''
            else:
                testcases[table_num] = testcases[table_num]
        testcases = [i for i in testcases if i != '']
        func = getattr(self.web, testcases[0])
        values = testcases[1:]
        try:
            func(*values)
            CommonPublic.log(testcasess)

        except AssertionError as msg:
            CommonPublic.log(testcases)
            CommonPublic.log(msg)

    @staticmethod
    def teardown_method():
        TestCommerce.num = TestCommerce.num + 1
