# coding=utf-8
import allure
import pytest
from Web.webkeys import WebKey
from common.cls.public import CommonPublic
from ddt.params import demo_sql_params_group


@allure.feature('项目名称：用例分组')
class TestCommerce:
    demo_sql = demo_sql_params_group('nox_browser')
    CommonPublic = CommonPublic()
    num = 0
    title = ''

    def setup_class(self):
        self.web = WebKey()
        self.table = TestCommerce.demo_sql

    @staticmethod
    def setup_method():
        table_ncols = TestCommerce.demo_sql[TestCommerce.num:TestCommerce.num + 1][0][0]
        TestCommerce.title = table_ncols[0:][2]

    @allure.story('用例:%s' % title)
    @pytest.mark.parametrize('table', demo_sql)
    def test_login(self, table):
        for len_table_case in range(0, len(table)):
            table_case_test = table[len_table_case]
            testcases = table_case_test[4:]
            testcases = [i for i in testcases if i != '']
            func = getattr(self.web, testcases[0])
            values = testcases[1:]
            try:
                func(*values)
                self.CommonPublic.log(testcases)

            except AssertionError as msg:
                self.CommonPublic.log(testcases)
                self.CommonPublic.log(msg)

    @staticmethod
    def teardown_method():
        TestCommerce.num = TestCommerce.num + 1
