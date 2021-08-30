from selenium import webdriver

class WebKey:

    def __init__(self):
        self.driver = None

    def openbrwser(self,br='gc'):
        '''
        打开浏览器
        :param br: gc=谷歌浏览器；ff=Firefox浏览器；ie=IE浏览器
        :return:
        '''
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'edg':
            self.driver = webdriver.Edge()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print('浏览器暂不支持！请在此添加实现代码')

        #默认隐式等待20s
        self.driver.implicitly_wait(20)

    def geturl(self,url=None):
        '''
        打开网站
        :param url: 网站地址
        :return:
        '''
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()


    def quit(self):
        self.driver.quit()


    def xpath(self,ele_type='',locator=''):
        '''
        找到xpath
        :param locator: 定位器
        :return:
        '''
        ele = None
        self.ele = None
        if ele_type == 'xpath':
            ele = self.driver.find_element_by_xpath(locator)
        elif ele_type == 'id':
            ele = self.driver.find_element_by_id(locator)


        self.ele = ele
        return ele

    def click(self,ele_type=None,locator=None):
        '''
        找到，并点击元素
        :param locator: 定位器，默认xpath
        :return:
        '''
        ele = self.xpath(ele_type,locator)
        ele.click()

    def input(self,ele_type=None,locator=None,value=None):
        '''
        找到元素，并完成输入
        :param locator: 定位器，默认xpath
        :param value: 需要输入字符串
        :return:
        '''
        ele = self.xpath(ele_type,locator)
        ele.clear()
        ele.send_keys(str(value))

    def intoiframe(self,ele_type=None,locator=None):
        '''
        进入iframe
        :param locator: 定位器，默认xpath
        :return:
        '''
        ele = self.xpath(ele_type,locator)
        self.driver.switch_to.frame(ele)


    def assert_results(self,ele_type=None,locator=None,Deserved_results=None):
        self.Deserved_results = Deserved_results
        Actual_results = self.xpath(ele_type,locator).text
        return Actual_results