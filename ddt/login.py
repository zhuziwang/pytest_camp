import allure
import pytest
import time
from Web.em import youjian
from Web.webkeys import WebKey
from ddt.params import app_excel_params
app_table_sheet = app_excel_params()


@allure.feature('kou')
class TestCommerce:
    num = 1
    title = ''

    def setup_class(self):
        self.web = WebKey()

    @staticmethod
    def setup_method():
        table_ncols = app_table_sheet[TestCommerce.num:TestCommerce.num + 1][0]
        TestCommerce.title = table_ncols[0:][0]

    @allure.story('用例:%s' % title)
    @pytest.mark.parametrize('table', app_table_sheet[1:])
    def test_login(self, table):
        testcases = table[2:]
        testcasess = table[1]
        testcases = [i for i in testcases if i != '']
        func = getattr(self.web, testcases[0])
        values = testcases[1:]
        try:
            func(*values), 'T'
            self.web.log("T")
            self.web.log(testcasess)
            print('T')
            print(testcasess)

        except AssertionError as msg:
            self.web.log(msg)
            self.web.log(testcasess)
            print(msg)
            print(testcasess)

    @staticmethod
    def teardown_method():
        TestCommerce.num = TestCommerce.num + 1
