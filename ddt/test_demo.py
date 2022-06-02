#conding=utf-8
import allure
import pytest
import time
from common.cls.public import CommonPublic
from Web.em import youjian
from Web.appkeys import AppKey
from ddt.params import demo_sql_params
demo_sql = demo_sql_params('test1')
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
