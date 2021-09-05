# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import os
import time
class WebKey:

    def __init__(self):
        self.driver = None

    def openbrwser(self,br='Chrome'):
        '''
        打开浏览器
        :param br:
        :return:
        '''
        if br == 'Chrome':
            self.driver = webdriver.Chrome()
        elif br == 'edg':
            self.driver = webdriver.Edge()
        elif br == 'Firefox':
            self.driver = webdriver.Firefox()
        elif br == 'Ie':
            self.driver = webdriver.Ie()
        else:
            print('F')

        #默认隐式等待20s
        self.driver.implicitly_wait(20)

    def driver_time(self):
        time.sleep(5)

    def geturl(self,url=None):
        '''
        打开URL
        :param url: 地址
        :return:
        '''
        self.driver.get(url)

    def back(self):
        '''
        浏览器后退
        Returns
        -------
        '''
        self.back()

    def forward(self):
        '''
        浏览器前进
        Returns
        -------
        '''
        self.forward()

    def refresh(self):
        '''刷新'''
        self.driver.refresh()

    def clear(self):
        '''
        清空文本
        Returns
        -------
        '''
        self.driver.clear()

    def submit(self):
        '''
        提交表单
        Returns
        -------
        '''
        self.driver.submit()

    def quit(self):
        '''退出'''
        self.driver.quit()

    def strftime(self,ele_type=None,locator=None):
        '''
        :return: 返回当前系统时间：格式为：2016-03-20 11:45:39形式
        '''
        strftime = time.strftime("%Y-%m-%d", time.localtime())
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(strftime)

    def maximize_window(self):
        '''
        浏览器最大化
        '''
        self.driver.maximize_window()

    def set_window_size(self,outerWidth=None,outerHeight=None):
        '''
        设置浏览器窗口的宽高
        Parameters
        ----------
        outerWidth：浏览器窗口的宽
        outerHeight：浏览器窗口的高
        Returns
        -------
        '''
        self.driver.set_window_size(outerWidth,outerHeight)

    def test_element(self,ele_type='',locator='',numb=None):
        '''
        定位方法
        :param ele_type: 类型
        :param locator:
        :return:
        '''
        ele = None
        self.ele = None
        if ele_type == 'id':
            ele = self.driver.find_element_by_id(locator)
        elif ele_type == 'name':
            ele = self.driver.find_element_by_name(locator)
        elif ele_type == 'class_name':
            ele = self.driver.find_element_by_class_name(locator)
        elif ele_type == 'tag_name':
            ele = self.driver.find_element_by_tag_name(locator)
        elif ele_type == 'css':
            ele = self.driver.find_element_by_css_selector(locator)
        elif ele_type == 'xpath':
            ele = self.driver.find_element_by_xpath(locator)
        elif ele_type == 'link_text':
            ele = self.driver.find_element_by_link_text(locator)
        elif ele_type == 'partial_link_text':
            ele = self.driver.find_element_by_partial_link_text(locator)
        self.ele = ele
        return ele

    def size(self,ele_type=None,locator=None):
        '''
        返回元素的尺寸
        Parameters
        ----------
        height：xx
        width：xx
        Returns
        -------
        '''
        ele = self.test_element(ele_type,locator)
        size = ele.size()
        return size

    def click(self,ele_type=None,locator=None):
        '''点击'''
        ele = self.test_element(ele_type,locator)
        ele.click()


    def click2(self,ele_type=None,locator=None):
        '''点击'''
        ele = self.test_element(ele_type,locator)
        ele.click()

    def context_click(self,ele_type=None,locator=None):
        '''
        右击
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        '''
        ele = self.test_element(ele_type,locator)
        ele.context_click()

    def double_click(self,ele_type=None,locator=None):
        '''
        双击
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        '''
        ele = self.test_element(ele_type,locator)
        ele.double_click()

    def drag_and_drop(self,source_ele_type=None,source_locator=None,target_ele_type=None,target_locator=None):
        '''
        拖动鼠标
        Parameters
        ----------
        source_ele_type：拖动开始的type
        source_locator：拖动开始的locator
        target_ele_type：拖动目标终点的type
        target_locator：拖动目标终点的locator
        drag_and_drop：拖动的方法
        Returns
        -------
        '''
        source = self.test_element(source_ele_type,source_locator)
        target = self.test_element(target_ele_type,target_locator)
        Action = ActionChains(self.driver)
        Action.drag_and_drop(source,target)

    def move_to_element(self,ele_type=None,locator=None):
        '''
        执行鼠标悬停操作
        Parameters
        ----------
        element：定位需要悬停的元素怒
        ActionChains(self.driver)：构造ActionChains对象
        perform()：执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作
        Returns：返回悬停显示的文本
        -------
        '''
        element = self.test_element(ele_type,locator)
        Action = ActionChains(self.driver).move_to_element(element).perform()
        return Action.text()

    def send_keys(self,ele_type=None,locator=None,value=None,ctrl_value=None):
        '''
        键盘输入
        Parameters
        ----------
        Keys.BACK_SPACE：删除键
        Keys.SPACE：空格键
        Keys.TAB：制表键
        Keys.ESCAPE：回退键
        Keys.ENTER：回车键
        组合键
        Keys.CONTROL,‘a’：全选（Ctrl+A）
        Keys.CONTROL,‘c’：复制（Ctrl+C）
        Keys.CONTROL,‘x’：剪切（Ctrl+X）
        Keys.CONTROL,‘v’：粘贴（Ctrl+V）
        Keys.F1…Fn：键盘 F1…Fn
        Returns
        -------
        '''
        ele = self.test_element(ele_type,locator)
        ele.send_keys(value,str(ctrl_value))

    def input(self,ele_type=None,locator=None,value=None):
        '''
        模拟键盘按键
        :param ele_type:
        :param locator:
        :param value: 输入text
        :return:
        '''
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(str(value))

    def text(self,ele_type=None,locator=None):
        '''
        获取文本内容
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        '''
        text = self.test_element(ele_type,locator).text
        return text

    def intoiframe(self,ele_type=None,locator=None):
        '''
        进入iframe
        :param locator:
        :return:
        '''
        ele = self.test_element(ele_type,locator)
        self.driver.switch_to.frame(ele)

    def default_content(self):
        '''
        从iframe跳到最外层
        Returns
        -------
        '''
        self.driver.switch_to.default_content()

    def current_window_handle(self):
        '''
        获取当前窗口的句柄
        Returns
        -------
        '''
        sreach_windows = self.driver.current_windows_handle
        return sreach_windows

    def window_handles(self):
        '''
        返回所有窗口的句柄
        Returns
        -------
        '''
        all_handles = self.driver.window_handles
        return all_handles

    def switch_to_window(self):
        '''
        切换到新打开的窗口
        Returns
        -------
        sreach_windows：第一页（未切换窗口时第一个窗口）的句柄
        all_handles：所有窗口的句柄
        '''
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.switch_to.window(handle)
                print('切换句柄到新窗口')
            pass
        pass

    def switch_to_window_close(self):
        '''
        切换到之前的窗口
        Returns
        -------
        '''
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.switch_to.window(handle)
                print('切换句柄到之前窗口')
            pass
        pass

    def close(self):
        '''
        关闭非当前定位到句柄的窗口
        Returns
        -------
        '''
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.close()
            pass
        pass

    def alert(self,choice = None,keysToSend = None):
        '''
        :text: 返回警告框文本
        :accept: 接受现有警告框
        :dismiss: 解散现有警告框
        :send_keys: 发送文本至警告框。keysToSend：将文本发送至警告框。
        '''
        if choice == 'text':
            alert_text = self.driver.switch_to.alert.text()
            return alert_text
        elif choice == 'accept':
            self.driver.switch_to.alert.accept()
        elif choice == 'dismiss':
            self.driver.switch_to.alert.dismiss()
        elif choice == 'send_keys':
            self.driver.switch_to.alert.send_keys(keysToSend)

    def select(self,ele_type=None,locator=None,select_by=None,value=None):
        '''
        :select_by :
                    1、select_by_value: select标签的value属性的值
                    2、select_by_index:下拉框的索引
                    3、select_by_visible_testx:下拉框的文本值
        value: 输入的value值
        '''
        sel = self.test_element(ele_type,locator)
        if select_by == 'select_by_value':
            Select(sel).select_by_value(value)
        elif select_by == 'select_by_index':
            Select(sel).select_by_index(value)
        elif select_by == 'select_by_visible_testx':
            Select(sel).select_by_visible_text(value)

    def file_path(self,ele_type=None,locator=None,file_path=None):
        '''
        :file_path: 上传文件的地址，格式：'D:\\upload_file.txt'
        '''
        self.test_element(ele_type,locator).send_keys(file_path)

    def cookies(self,name=None,key=None,cookie_dict=None):
        '''
        :get_cookies: 获得所有cookie信息
        :get_cookie(key): 返回字典的key为“key”的cookie信息
        :add_cookie(cookie_dict): 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值
        :delete_all_cookies(): 删除所有cookie信息
        '''
        if name == 'get_cookies()':
            cookies = self.driver.get_cookies()
            return cookies
        elif name == 'get_cookie(%s)%key':
            cookies_value = self.driver.get_cookies(key)
            return cookies_value
        elif name == 'add_cookie(%s)%cookie_dict':
            self.driver.add_cookie(cookie_dict)
        elif name == 'delete_all_cookies()':
            self.driver.delete_all_cookies()

    def execute_script(self,left=None,top=None):
        '''
        滚动条
        :param left: 左边距
        :param top: 上边距
        '''
        javascript = "window.scrollTo(%d,%d);"%(left,top)
        self.driver.execute_script(javascript)

    def get_screenshot_as_file(self,filename=None):
        '''
        窗口截图
        :param filename: 用于截取当前窗口，并把图片保存到本地，格式为：D:\\baidu.jpg
        '''
        self.driver.get_screenshot_as_file(filename)

    def current_url(self):
        '''
        获得当前页面的URL
        Returns
        -------
        '''
        now_url = self.driver.current_url
        return now_url

    def title1(self,test=None):
        '''
       获得当前页面的标题
        Returns
        -------
        '''
        title1 = self.driver.title
        print(title1)
        return title1

    def get_attribute(self, name=None):
        '''
        获取元素属性
        Parameters
        ----------
        name：1、获取元素标签的内容(文本信息)：textContent
              2、获取元素内的全部HTML：innerHTML
              3、获取包含选中元素的HTML：outerHTML
        Returns
        -------
        '''
        get_attribute = self.driver.get_attribute(name)
        return get_attribute

    def assert_results(self,ele_type=None,locator=None,Deserved_results=None):
        '''text断言'''
        self.Deserved_results = Deserved_results
        Actual_results = self.test_element(ele_type,locator).text
        return Actual_results

    def is_displayed(self,ele_type=None,locator=None):
        '''
        断言弹窗,查看元素是否可见
        :param locator:
        :return:
        '''
        pp = self.test_element(ele_type,locator).is_displayed()
        return pp

    def qzdj(self,ele_type=None,locator=None):
        '''
        强制点击（元素被遮挡后使用）
        :param ele_type:
        :param locator:
        :return:
        '''
        qzdj = self.test_element(ele_type,locator)
        self.driver.execute_script('arguments[0].click()',qzdj)
        return qzdj

    def stattime(self,ele_type=None,locator=None):
        '''时间输入框，输入明天的时间，格式XXXX/XX/XX'''
        import datetime
        a= datetime.datetime.now()
        b = (a + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        ele = self.test_element(ele_type,locator)
        ele.clear()
        ele.send_keys(str(b))

