import allure
import pytest
import time
from common.cls.public import CommonPublic
from Web.webkeys import WebKey
from ddt.params import excel_params
table_sheet = excel_params()
CommonPublic = CommonPublic()


@allure.feature('web')
class TestCommerce:
    num = 0
    title = ''

    def setup_class(self):
        self.web = WebKey()

    @staticmethod
    def setup_method():
        table_ncols = table_sheet[TestCommerce.num:TestCommerce.num + 1][0]
        TestCommerce.title = table_ncols[0:][0]

    @allure.story('用例:%s' % title)
    @pytest.mark.parametrize('table', table_sheet[1:])
    def test_login(self, table):
        testcases = table[2:]
        testcasess = table[1]
        testcases = [i for i in testcases if i != '']
        func = getattr(self.web, testcases[0])
        values = testcases[1:]
        if testcases[0] == 'assert_results':
            assert_results = func(*values)
            Deserved_results = self.web.Deserved_results
            try:
                assert assert_results == Deserved_results, 'F'
                CommonPublic.log("F")
                CommonPublic.log(testcasess)
                print('T')
                print(testcasess)

            except AssertionError as msg:
                CommonPublic.log(msg)
                CommonPublic.log(testcasess)
                print(msg)
                print(testcasess)

        elif testcases[0] == 'is_displayed':
            is_displayed = func(*values)
            try:
                assert is_displayed is True
                CommonPublic.log("T")
                CommonPublic.log(testcasess)
                print('T')
                print(testcasess)
            except AssertionError:
                CommonPublic.log("F")
                CommonPublic.log(testcasess)
                print('F')
                print(testcasess)

        elif testcases[0] == 'title1':
            title = func(*values)
            try:
                assert title == testcases[1]
                CommonPublic.log("T")
                CommonPublic.log(testcasess)
                print('T')
                print(testcases)

            except AssertionError:
                CommonPublic.log("F")
                CommonPublic.log(testcasess)
                print('F')
                print(testcasess)

        else:
            func(*values)
            CommonPublic.log("T")
            CommonPublic.log(testcasess)
            print('T')
            print(testcasess)
            time.sleep(0.5)

    @staticmethod
    def teardown_method():
        TestCommerce.num = TestCommerce.num + 1
        print(TestCommerce.num)
