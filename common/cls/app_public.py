# coding=utf-8
import time
from appium import webdriver
import os
from models.sql import PyMysql

from public import CommonPublic


class AppiumKeys(CommonPublic):
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
        all_apppackage = os.popen('adb shell pm list packages').read()
        app_package = 'com.android.browser'
        if app_package in all_apppackage:
            android_version = os.popen('adb shell getprop ro.build.version.release').read()
            AppiumKeys.desired_caps_phone['platformVersion'] = android_version
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', AppiumKeys.desired_caps_phone)
        else:
            AppiumKeys.log(self, "没有该app：%s" % app_package)
            print("没有该app：%s" % app_package)

    def switch_context(self, contexts):
        """
        前置条件：WebView.setWebContentsDebuggingEnabled(true)
        :param contexts: 切换
        : 切换app和webview
        :param : WEBVIEW_com.android_browser / NATIVE_APP / undefined
        :return:
        """
        if contexts == 'WEBVIEW':
            webview = self.driver.contexts.last
            self.driver.switch_to.context(webview)
        else:
            self.driver.switch_to.context(self.driver.contexts.first)

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
        :param ele_type: 元素的类型
        :param locator: 元素的值
        :param send: 输入的内容
        :param num: 元素是第几个
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

    PyMysql = PyMysql()

    @staticmethod
    def pymysql(sql=None):
        PyMysql.mysql(sql)
