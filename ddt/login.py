import allure
import pytest
import time
from Web.webkeys import WebKey
from ddt.params import yaml_params

datas=yaml_params()
@allure.feature('这是项目名字')
class Test_Commerce:
    def setup_class(self):
        self.web = WebKey()
        self.web.openbrwser()
    @allure.story('测试用例')
    @pytest.mark.parametrize('listcases', datas['loginPage'])
    def test_login(self,listcases):
        testcases = listcases['cases']
        for cases in testcases:
            listcase = list(cases.values())   #把字典转成列表值
            func = getattr(self.web,listcase[1])
            values = listcase[2:]
            print('values%s'%values)
            if listcase[1] == 'assert_results':
                assert_results = func(*values)
                Deserved_results = self.web.Deserved_results
                try:
                    assert assert_results == Deserved_results,'F'
                except AssertionError:
                    assert assert_results == Deserved_results
                else:
                    func(*values)
                finally:
                    func(*values)
            else:
                func(*values)
                print('T')
                time.sleep(0.5)


    def teardown_class(self):
        from Web.em import youjian
        fasong = youjian()
    #     self.web.quit()