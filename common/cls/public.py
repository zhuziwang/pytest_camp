# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
from common.base_log.log import Log
from pathlib import Path
import time
from appium import webdriver
import os
from models.sql import py_mysql



class CommonPublic:
    def __init__(self):
        log = Log()
        self.logger = log.get_log()

    def log(self, msg):
        self.logger.debug(msg)

    def base_dir(self):
        """
        获取项目地址：C:\\Users\\duia\\PycharmProjects\\pytest_camp
        :return:
        """
        base_dir = Path(__file__).resolve().parent.parent
        return base_dir

class AppniumKeys(CommonPublic):
    def __init__(self):
        self.driver = None
        self.ele = None

    desired_caps_phone = {
        'platformName': 'Android',
        'platformVersion': '11',  # 手机android版本111
        'deviceName': '正常手机设备',  # 设别名称，随意填写
        'appPackage': 'com.android.browser',  # 启动的app名称
        'appActivity': '.BrowserActivity',  # 启动的main页面
        'unicodeKeyboard': False,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App
        'newCommandTimeout': 6000,
        'antomationName': 'UiAutomator2'
    }

    def open_app(self):
        all_appPackage = os.popen('adb shell pm list packages').read()
        appPackage = 'com.duia.duiaapp'
        if appPackage in all_appPackage:
            AndroidVersion = os.popen('adb shell getprop ro.build.version.release').read()
            AppniumKeys.desired_caps_phone['platformVersion'] = AndroidVersion
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', AppniumKeys.desired_caps_phone)
        else:
            AppniumKeys.log(self, "没有该app：%s" % appPackage)
            print("没有该app：%s" % appPackage)

    def context(self, context):
        """
        : 切换app和webview
        :param switch: WEBVIEW / NATIVEAPP / undefined
        :return:
        """
        self.driver.switch_to.context(context)

    def test_element(self, ele_type='', locator='', num=''):
        """
        accessibility_id对应content-desc
        :param ele_type:    textContains：文本包含
                            textMatches：文本正则
                            textStartsWith：文本起始匹配
        :param locator:
        :return:
        """
        if ele_type == 'accessibility_id':
            ele = self.driver.find_element_by_accessibility_id(locator)
        elif ele_type == 'id':
            ele = self.driver.find_element_by_id(locator)
        elif ele_type == 'xpath':
            ele = self.driver.find_element_by_xpath(locator)
        elif ele_type == 'class_name':
            ele = self.driver.find_elements_by_class_name(locator)
        elif ele_type == 'name':
            ele = self.driver.find_elements_by_name(locator)
        elif ele_type == 'text':
            ele = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % locator)
        elif ele_type == 'textContains':
            ele = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("%s")' % locator)
        elif ele_type == 'textMatches':
            ele = self.driver.find_element_by_android_uiautomator('new UiSelector().textMatches("%s")' % locator)
        elif ele_type == 'textStartsWith':
            ele = self.driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith("%s")' % locator)
        elif ele_type == 'xpaths':
            ele = self.driver.find_elements_by_xpath(locator)
        return ele

    def clear(self, ele_type='', locator=''):
        """
        清空内容
        :param ele_type:
        :param locator:
        :return:
        """
        ele = self.test_element(ele_type, locator)
        ele.clear()

    def click(self, ele_type='', locator='', num=None):
        """
        点击
        """
        time.sleep(2)
        if num is None:
            self.test_element(ele_type, locator).click()
        else:
            ele = self.test_element(ele_type, locator, num)
            ele[num].click()

    def send_keys(self, ele_type='', locator='', send='', num=None):
        """
        输入内容
        """
        if num is None:
            self.test_element(ele_type, locator).click()
            self.test_element(ele_type, locator).send_keys(send)
        else:
            ele = self.test_element(ele_type, locator, num)
            ele[num].send_keys(send)

    @staticmethod
    def driver_time(d_time=None):
        time.sleep(float(d_time))

    def background_app(self, time_time=None):
        """
        :backgroud_app: 把应用置于后台time时间后唤醒到前台
        :return:
        """
        self.driver.background_app(int(time_time))

    def lock(self, time_time=None):
        """
        :lock: 手机进入锁屏状态time时间后，再次唤醒
        :return:
        """
        self.driver.lock(time_time)

    def hide_keyboard(self):
        """
        :hide_keyboard: 隐藏键盘
        """
        self.driver.hide_keyboard()

    def start_activity(self, app_package='', app_activity=''):
        """
        启动一个app或者在当前app中打开一个新的activity，仅适用于android
        :param app_activity: 默认为空，启动的app名称
        :param app_package: 默认为空，启动的main页面
        :return:
        """
        self.driver.start_activity(app_package, app_activity)

    def is_app_installed(self, app_package=''):
        """
        检查app是否被安装
        :param app_package: 默认为空，app名称
        :return:
        """
        app_installed = self.driver.is_app_installed(app_package)
        return app_installed

    def install_app(self, app_package=''):
        """
        安装app
        :param app_package: app名称 例如：xx.apk
        :return:
        """
        self.driver.install_app(app_package)

    def remove_app(self, app_package=''):
        """
        卸载app
        :param app_package: app名称
        :return:
        """
        self.driver.remove_app(app_package)

    def close_app(self):
        """
        关闭app
        :return:
        """
        self.driver.close_app()

    def launch_app(self):
        """
        如果测试中的应用程序（AUT）已关闭，或处于后台，它将启动它。如果AUT已经打开，它将对其进行背景设置并重新启动。
        :return:
        """
        self.driver.launch_app()

    def press_keycode(self, ele_type='', locator='', send='', keycode=None, num=None):
        """
        输入键值：UiAutomator2中有bug无法使用，可以切换为Appnium或者使用搜狗输入法输入后，在执行一下代码
                使用搜狗输入法的教程地址：“ https://blog.csdn.net/qq_60566718/article/details/122868696 ”
        :param keycode: 3、HOME键
                    82、菜单键
                    4、返回键
                    26、电源键
                    66、回车键
                    64、退格键
        :return:
        """
        sougou = 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'
        os.system(sougou)
        if num is None:
            self.test_element(ele_type, locator).click()
            self.test_element(ele_type, locator).send_keys(send)
            self.driver.press_keycode(keycode)
        else:
            ele = self.test_element(ele_type, locator, num)
            ele[num].send_keys(send)
            self.driver.press_keycode(keycode)

    def get_window_size(self):
        """
        获取当前窗口大小
        :return:
        """
        get_windows_size = self.driver.get_window_size()
        return get_windows_size

    def swipe(self, start_x=None, start_y=None, end_x=None, end_y=None, duration=None):
        """
        滑动屏幕
        :param start_y: 开始x坐标
        :param start_x: 开始y坐标
        :param end_x: 结束x坐标
        :param end_y: 结束y坐标
        :param duration: 移动的时间间隔
        :return:
        """
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def get_screenshot_as_file(self, file_path=''):
        """
        截图，并保存
        :param file_path: 路径
        :return:
        """
        self.driver.get_screenshot_as_file(file_path)

    def text(self, ele_type='', locator=''):
        """
        获取元素的text属性值
        :param ele_type:
        :param locator:
        :return:
        """
        text = self.test_element(ele_type, locator).text
        return text

    def content_desc(self, ele_type='', locator=''):
        """
        获取元素content_desc属性值
        :param ele_type:
        :param locator:
        :return:
        """
        content_desc = self.test_element(ele_type, locator)
        return content_desc

    def remove_element_occlusion(self, ele_type=None, locator=None):
        """
        强制点击（元素被遮挡后使用）
        :param ele_type:
        :param locator:
        :return:
        """
        remove_element_occlusion = self.test_element(ele_type, locator)
        self.driver.execute_script('arguments[0].click()', remove_element_occlusion)
        return remove_element_occlusion

    def current_url(self):
        """
        获得当前页面的URL
        Returns
        -------
        """
        now_url = self.driver.current_url
        return now_url

    def title(self):
        """
       获得当前页面的标题
        Returns
        -------
        """
        title = self.driver.title
        print(title)
        return title

    py_mysql = py_mysql()

    @staticmethod
    def pymysql(sql=None):
        py_mysql.mysql(sql)

class SeleniumKeys(CommonPublic):
    def __init__(self):
        self.driver = None
        self.ele = None

    def open_browser(self, br='Chrome'):
        """
        打开浏览器
        :param br: 如果是谷歌，profile.default_content_settings.popups：设置为0禁止弹出下载窗口
        :return:
        """
        if br == 'Chrome':
            str_time = self.str_time()
            str_time = str(str_time)
            base_dir = self.base_dir()
            file_path = base_dir+'\\download\\Chrome_download\\'+str_time+'\\'
            options = webdriver.ChromeOptions()
            prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': file_path}
            options.add_experimental_option('prefs', prefs)
            self.driver = webdriver.Chrome(chrome_options=options)
        elif br == 'edg':
            self.driver = webdriver.Edge()
        elif br == 'Firefox':
            self.driver = webdriver.Firefox()
        elif br == 'Ie':
            self.driver = webdriver.Ie()
        else:
            print('F')

        # 默认隐式等待20s
        self.driver.implicitly_wait(5)

    def driver_time(self, time_time=None):
        time.sleep(float(time_time))

    def geturl(self, url=None):
        """
        打开URL
        :param url: 地址
        :return:
        """
        self.driver.get(url)

    def back(self):
        """
        浏览器后退
        Returns
        -------
        """
        self.back()

    def forward(self):
        """
        浏览器前进
        Returns
        -------
        """
        self.forward()

    def refresh(self):
        """
        刷新
        """
        self.driver.refresh()

    def clear(self):
        """
        清空文本
        """
        self.driver.clear()

    def submit(self):
        """
        提交表单
        """
        self.driver.submit()

    def quit(self):
        """
        退出
        """
        self.driver.quit()

    def str_time(self):
        """
        :return: 返回当前系统时间：格式为：2016-03-20形式
        """
        str_time = time.strftime("%Y-%m-%d", time.localtime())
        return str_time

    def strftime(self, ele_type=None, locator=None):
        """
        :return: 输入框输入返回的当前系统时间：格式为：2016-03-20形式
        """
        strftime = time.strftime("%Y-%m-%d", time.localtime())
        ele = self.test_element(ele_type, locator)
        ele.clear()
        ele.send_keys(strftime)

    def strftime_hms(self, ele_type=None, locator=None):
        """
        :return: 返回当前系统时间：格式为：2016-03-20 11:45:39形式
        """
        strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        ele = self.test_element(ele_type, locator)
        ele.clear()
        ele.send_keys(strftime)

    def stattime(self, ele_type=None, locator=None):
        """
        时间输入框，输入明天的时间，格式XXXX/XX/XX
        """
        import datetime
        a = datetime.datetime.now()
        b = (a + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        ele = self.test_element(ele_type, locator)
        ele.clear()
        ele.send_keys(str(b))

    def stattime_hms(self, ele_type=None, locator=None):
        """
        时间输入框，输入明天的时间，格式XXXX/XX/XX2016-03-20 11:45:39
        """
        import datetime
        a= datetime.datetime.now()
        b = (a + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        ele = self.test_element(ele_type, locator)
        ele.clear()
        ele.send_keys(str(b))

    def get_allfile(self, file_path):
        """
        获取所有文件
        listdir返回文件中所有目录
        """
        all_file = []
        for f in os.listdir(file_path):
            f_name = os.path.join(file_path, f)
            all_file.append(f_name)
        return all_file

    def maximize_window(self):
        """
        浏览器最大化
        """
        self.driver.maximize_window()

    def set_window_size(self, outerWidth=None, outerHeight=None):
        """
        设置浏览器窗口的宽高
        Parameters
        ----------
        outerWidth：浏览器窗口的宽
        outerHeight：浏览器窗口的高
        Returns
        -------
        """
        self.driver.set_window_size(outerWidth, outerHeight)

    def test_element(self, ele_type='', locator='', num=None):
        """
        定位方法
        :param ele_type: 类型
        :param locator:
        :return:
        """
        if ele_type == 'id':
            ele = self.driver.find_element_by_id(locator)
        elif ele_type == 'name':
            ele = self.driver.find_elements_by_name(locator)
        elif ele_type == 'class_name':
            ele = self.driver.find_elements_by_class_name(locator)
        elif ele_type == 'tag_name':
            ele = self.driver.find_elements_by_tag_name(locator)
        elif ele_type == 'css':
            ele = self.driver.find_elements_by_css_selector(locator)
        elif ele_type == 'xpath':
            ele = self.driver.find_element_by_xpath(locator)
        elif ele_type == 'link_text':
            ele = self.driver.find_element_by_link_text(locator)
        elif ele_type == 'partial_link_text':
            ele = self.driver.find_elements_by_partial_link_text(locator)
        elif ele_type == 'xpaths':
            ele = self.driver.find_elements_by_xpath(locator)
        return ele

    def size(self, ele_type=None, locator=None):
        """
        返回元素的尺寸
        Parameters
        ----------
        height：xx
        width：xx
        Returns
        -------
        """
        ele = self.test_element(ele_type, locator)
        size = ele.size()
        return size

    def click(self, ele_type=None, locator=None, num=None):
        """
        点击
        """
        if num is None:
            self.test_element(ele_type, locator).click()
        else:
            ele = self.test_element(ele_type, locator, num)
            ele[num].click()

    def context_click(self, ele_type=None, locator=None):
        """
        右击
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        """
        ele = self.test_element(ele_type, locator)
        ele.context_click()

    def double_click(self, ele_type=None, locator=None):
        """
        双击
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        """
        ele = self.test_element(ele_type, locator)
        ele.double_click()

    def drag_and_drop(self, source_ele_type=None, source_locator=None, target_ele_type=None, target_locator=None):
        """
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
        """
        source = self.test_element(source_ele_type, source_locator)
        target = self.test_element(target_ele_type, target_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target)

    def move_to_element(self, ele_type=None, locator=None):
        """
        执行鼠标悬停操作
        Parameters
        ----------
        element：定位需要悬停的元素怒
        ActionChains(self.driver)：构造ActionChains对象
        perform()：执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作
        Returns：返回悬停显示的文本
        -------
        """
        element = self.test_element(ele_type,locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def send_keys(self, ele_type=None, locator=None, value=None, ctrl_value=None):
        """
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
        :param ctrl_value: 输入的键
        :param value: 输入的值
        :param locator: 定位的值
        :param ele_type:定位的类型
        """
        ele = self.test_element(ele_type, locator)
        ele.send_keys(value, str(ctrl_value))

    def input(self, ele_type=None, locator=None, value=None, num=None):
        """
        :param num: elements为多个值时，选择第num个值
        :param ele_type:定位的类型
        :param locator:定位的值
        :param value: 输入的值
        :return:
        """
        if num is None:
            ele = self.test_element(ele_type, locator)
            ele.clear()
            ele.send_keys(value)
        else:
            ele = self.test_element(ele_type, locator, num)
            ele.clear()
            ele[num].send_keys(value)

    def text(self, ele_type=None, locator=None):
        """
        获取文本内容
        Parameters
        ----------
        ele_type
        locator
        Returns
        -------
        """
        text = self.test_element(ele_type, locator).text
        return text

    def intoiframe(self, ele_type=None, locator=None):
        """
        进入iframe
        :param ele_type: 定位的类型
        :param locator:定位的值
        :return:
        """
        ele = self.test_element(ele_type, locator)
        self.driver.switch_to.frame(ele)

    def default_content(self):
        """
        从iframe跳到最外层
        Returns
        -------
        """
        self.driver.switch_to.default_content()

    def current_window_handle(self):
        """
        获取当前窗口的句柄
        Returns
        -------
        """
        sreach_windows = self.driver.current_windows_handle
        return sreach_windows

    def window_handles(self):
        """
        返回所有窗口的句柄
        Returns
        -------
        """
        all_handles = self.driver.window_handles
        return all_handles

    def switch_to_window(self):
        """
        切换到新打开的窗口
        Returns
        -------
        sreach_windows：第一页（未切换窗口时第一个窗口）的句柄
        all_handles：所有窗口的句柄
        """
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.switch_to.window(handle)
                print('切换句柄到新窗口,handle是%s' % handle)
            pass
        pass

    def switch_to_window_close(self):
        """
        切换到之前的窗口
        Returns
        -------
        """
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                print(handle)
                self.driver.switch_to.window(handle)
                print('切换句柄到之前窗口,handle是%s' % handle)
            pass
        pass

    def window_close(self):
        """
        关闭当前定位到句柄的窗口,并定位到其他窗口（两个窗口的情况下是定位到另一个窗口）
        Returns
        -------
        """
        sreach_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != sreach_windows:
                self.driver.close()
                self.driver.switch_to.window(handle)
            pass
        pass

    def alert(self, choice=None, keysToSend=None):
        """
        :text: 返回警告框文本
        :accept: 接受现有警告框
        :dismiss: 解散现有警告框
        :send_keys: 发送文本至警告框。keysToSend：将文本发送至警告框。
        """
        if choice == 'text':
            del_alert = self.driver.switch_to.alert
            alert_text = del_alert.text()
            return alert_text
        elif choice == 'accept':
            del_alert = self.driver.switch_to.alert
            del_alert.accept()
        elif choice == 'dismiss':
            del_alert = self.driver.switch_to.alert
            del_alert.dismiss()
        elif choice == 'send_keys':
            del_alert = self.driver.switch_to.alert
            del_alert.send_keys(keysToSend)

    def select(self, ele_type=None, locator=None, select_by=None, value=None):
        """
        :select_by :
                    1、select_by_value: select标签的value属性的值
                    2、select_by_index:下拉框的索引
                    3、select_by_visible_testx:下拉框的文本值
        value: 输入的value值
        """
        sel = self.test_element(ele_type,locator)
        if select_by == 'select_by_value':
            Select(sel).select_by_value(value)
        elif select_by == 'select_by_index':
            Select(sel).select_by_index(value)
        elif select_by == 'select_by_visible_testx':
            Select(sel).select_by_visible_text(value)

    def file_path(self, ele_type=None, locator=None, file_path=None):
        """
        :file_path: 上传文件的地址，格式：'D:\\upload_file.txt'
        """
        self.test_element(ele_type, locator).send_keys(file_path)

    def cookies(self, name=None, key=None, cookie_dict=None):
        """
        :get_cookies: 获得所有cookie信息
        :get_cookie(key): 返回字典的key为“key”的cookie信息
        :add_cookie(cookie_dict): 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值
        :delete_all_cookies(): 删除所有cookie信息
        """
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

    def execute_script(self, left=None, top=None):
        """
        滚动条
        :param left: 左边距
        :param top: 上边距
        """
        javascript = "window.scrollTo(%d,%d);" % (left, top)
        self.driver.execute_script(javascript)

    def get_screenshot_as_file(self, filename=None):
        """
        窗口截图
        :param filename: 用于截取当前窗口，并把图片保存到本地，格式为：D:\\baidu.png
        """
        self.driver.get_screenshot_as_file(filename)

    def current_url(self):
        """
        获得当前页面的URL
        Returns
        -------
        """
        now_url = self.driver.current_url
        return now_url

    def title1(self, test=None):
        """
       获得当前页面的标题
        Returns
        -------
        """
        title1 = self.driver.title
        # print(title1)
        return title1

    def get_attribute(self, name=None):
        """
        获取元素属性
        Parameters
        ----------
        name：1、获取元素标签的内容(文本信息)：textContent
              2、获取元素内的全部HTML：innerHTML
              3、获取包含选中元素的HTML：outerHTML
        Returns
        -------
        """
        get_attribute = self.driver.get_attribute(name)
        return get_attribute

    def get_downloaded_filename(self):
        """
        fileName：获取下载的文件的名称
        sourceURL：获取下载的文件的url
        :return:
        """
        # open a new tab
        self.driver.execute_script("window.open()")
        # switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # navigate to chrome downloads
        self.driver.get('chrome://downloads')
        # get the latest downloaded file name
        filename = self.driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
        # get the latest downloaded file url
        source_url = self.driver.execute_script("return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').href")
        # close the downloads tab2
        self.driver.close()
        # switch back to main window
        self.driver.switch_to.window(self.driver.window_handles[0])
        return filename

    def move_to_element_text(self, ele_type=None, locator=None):
        """
        执行鼠标悬停操作
        Parameters
        ----------
        element：定位需要悬停的元素怒
        ActionChains(self.driver)：构造ActionChains对象
        perform()：执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作
        Returns：返回悬停显示的文本
        -------
        """
        element = self.test_element(ele_type, locator)
        action = ActionChains(self.driver).move_to_element(element).perform()
        return action.text()


