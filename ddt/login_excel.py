import allure
import pytest

from Web.webkeys import WebKey
from ddt.params import excel_params
table_sheet=excel_params()

@allure.feature('这是项目名字')
class Test_Commerce:

    def setup_class(self):
        self.web = WebKey()
        self.web.openbrwser()
    @allure.story('用例')
    @pytest.mark.parametrize('table', table_sheet[1:])
    def test_login(self,table):
        testcases = table[2:]
        testcases = [i for i in testcases if i != '']
        func = getattr(self.web, testcases[0])
        values = testcases[1:]
        print('values的值是：%s' %testcases[1:])

        if testcases[0] == 'assert_results':
            assert_results = func(*values)
            Deserved_results = self.web.Deserved_results
            try:
                assert assert_results == Deserved_results, '错误'
            except AssertionError as e:
                assert assert_results == Deserved_results
            else:
                func(*values)
            finally:
                    func(*values)
        else:
            print('正确')
            func(*values)



