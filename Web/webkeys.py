# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
from common.cls.web_public import SeleniumKeys


class WebKey(SeleniumKeys):

    def __init__(self):
        self.driver = None

    def assert_results(self, ele_type=None, locator=None, deserved_results=None):
        """text断言"""
        deserved_results = deserved_results
        actual_results = self.test_element(ele_type, locator).text
        return actual_results

    def assert_results_img_src(self, ele_type=None, locator=None, deserved_results=None):
        """图片src断言"""
        deserved_results = deserved_results
        actual_results = self.test_element(ele_type, locator).get_attribute("src")
        return actual_results

    def is_displayed(self, ele_type=None, locator=None):
        """
        断言弹窗,查看元素是否可见
        :param ele_type: 类型
        :param locator: 值
        :return:
        """
        pp = self.test_element(ele_type, locator).is_displayed()
        return pp

    def qzdj(self, ele_type=None, locator=None):
        """
        强制点击（元素被遮挡后使用）
        :param ele_type:
        :param locator:
        :return:
        """
        qzdj = self.test_element(ele_type, locator)
        self.driver.execute_script('arguments[0].click()', qzdj)
        return qzdj

    def goto_student_level_home(self):
        """
        判断是否有查阅暑假练听说首页弹窗,如果有就关闭，没有不动
        :return:
        """
        if self.test_element('xpaths', '//*[@id="check"]'):
            self.test_element('xpath', '//*[@id="closeImg1"]/img').click()
        elif self.test_element('xpaths', '//*[@id="teacherTipsDivUl"]'):
            self.test_element('xpath', '//*[@id="teacherTipsDiv"]/div/img').click()
        else:
            pass

    def login_out(self):
        """退出登录"""
        out = self.driver.find_elements_by_class_name('loginOut')
        if out:
            self.click(out)
        else:
            pass

    def login_update(self, br='Chrome', url='', username='', password=''):
        """
        登录用例，判断首页弹窗
        :param br: 浏览器
        :param url: 网站
        :param username: 用户名
        :param password: 密码
        :DesiredCapabilities.CHROME：设置chrome浏览器，["pageLoadStrategy"] = "none"：html下载完成，不等待解析完成即返回   #用前注意
        :return:
        """
        self.open_browser(br)
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        self.geturl(url)
        self.maximize_window()
        self.login_out()
        self.click('class_name', 'login', 0)
        self.click('class_name', 'style__navList-2ZtUx', 1)
        name = self.test_element('xpath', '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/input')
        name.clear()
        name.send_keys(username)
        pws = self.test_element('xpath', '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/input')
        pws.clear()
        pws.send_keys(password)
        self.test_element('xpath', '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div[2]/div[5]').click()
        # self.gotoStudentLevelHome()

    def picture(self, url='http://ip地址/jenkins/job/SVN/allure/'):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        time.sleep(30)
        driver.refresh()
        time.sleep(5)
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        try:
            driver.get_screenshot_as_file('C:\\Users\\Administrator\\PycharmProjects\\kouyu100\\image\\picture\\'
                                          + picture_time+'.png')
            print('截图成功')
        except BaseException as msg:
            print(msg)
        return picture_time+'.png'

# 学生
    def work_info_list(self, work_info_text=''):
        """
        手机作业&成绩中小黑板中查找work_info_text文本的作业后点击
        :param work_info_text:
        :return:
        """
        for i in range(1, 13):
            xpath_num = '//*[@id="slidesindex"]/div[%s]' % i
            xpath_text = self.test_element('xpath', xpath_num).text
            if work_info_text in xpath_text:
                self.test_element('xpath', xpath_num).click()
                break
            else:
                continue

    def word_option(self):
        """
        遍历单词选项，找到选项后，配以单词是否一致
        :return:
        """
        from models.sql import PyMysql

        for i in range(0, 2):
            test = self.test_element('class_name', 'word-topic', 0).text
            print(len(test), test)
            test_str = test[4:]
            sql0 = "SELECT word from w2m_wordclass where cnText = '{}' LIMIT 1;" .format(test_str)
            sql1 = "SELECT word from w2m_wordclass where cnText like '{}%' LIMIT 1;" .format(test_str)
            fanyi0 = PyMysql.mysql(sql0)
            if str(fanyi0) == 'None':
                fanyi1 = PyMysql.mysql(sql1)
                eng_fanyi = fanyi1[0]
            else:
                eng_fanyi = fanyi0[0]

            option_a = self.test_element('class_name', 'option A').text
            option_b = self.test_element('class_name', 'option B').text
            option_c = self.test_element('class_name', 'option C').text
            print(len(option_a), option_a)

            time.sleep(1)
            if option_a[3:] == eng_fanyi:
                self.test_element('class_name', 'option A').click()
                time.sleep(2.5)
            elif option_b[3:] == eng_fanyi:
                self.test_element('class_name', 'option B').click()
                time.sleep(2.5)
            elif option_c[3:] == eng_fanyi:
                self.test_element('class_name', 'option C').click()
                time.sleep(2.5)
            else:
                self.test_element('class_name', 'option D').click()
                time.sleep(2.5)
