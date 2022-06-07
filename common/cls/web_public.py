# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import os

import cv2 as cv
from functools import reduce
from PIL import Image

# words_ocr,find_pic,generate_tracks,do_match,match_code
import urllib
import urllib.request

from .public import CommonPublic


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
            file_path = str(base_dir)+'\\download\\Chrome_download\\'+str_time+'\\'
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

    @staticmethod
    def driver_time(time_time=None):
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

    @staticmethod
    def str_time():
        """
        :return: 返回当前系统时间：格式为：2016-03-20形式
        """
        str_time = time.strftime("%Y-%m-%d", time.localtime())
        return str_time

    @staticmethod
    def str_time_hms():
        str_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
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
        a = datetime.datetime.now()
        b = (a + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        ele = self.test_element(ele_type, locator)
        ele.clear()
        ele.send_keys(str(b))

    @staticmethod
    def get_allfile(file_path):
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

    def set_window_size(self, outer_width=None, outer_height=None):
        """
        设置浏览器窗口的宽高
        Parameters
        ----------
        outer_width：浏览器窗口的宽
        outer_height：浏览器窗口的高
        Returns
        -------
        """
        self.driver.set_window_size(outer_width, outer_height)

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
        element = self.test_element(ele_type, locator)
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

    def alert(self, choice=None, keys_to_send=None):
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
            del_alert.send_keys(keys_to_send)

    def select(self, ele_type=None, locator=None, select_by=None, value=None):
        """
        :select_by :
                    1、select_by_value: select标签的value属性的值
                    2、select_by_index:下拉框的索引
                    3、select_by_visible_testx:下拉框的文本值
        value: 输入的value值
        """
        sel = self.test_element(ele_type, locator)
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

    def title1(self):
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
        filename = self.driver.execute_script("return document.querySelector('downloads-manager')"
                                              ".shadowRoot.querySelector('#downloadsList downloads-item')"
                                              ".shadowRoot.querySelector('div#content  #file-link').text")
        # get the latest downloaded file url
        source_url = self.driver.execute_script("return document.querySelector('downloads-manager')"
                                                ".shadowRoot.querySelector('#downloadsList downloads-item')"
                                                ".shadowRoot.querySelector('div#content  #file-link').href")
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

    @staticmethod
    def resize_img(img, sign):
        """
        下载的图片把网页中的图片进行了放大，所以将图片还原成原尺寸
        :param sign: 标记，1为背景图，2为滑块图
        :param img: 图片
        :return: 返回还原后的图片
        """
        str_time_hms = SeleniumKeys.str_time_hms()
        str_time_hms = str(str_time_hms)
        base_dir = SeleniumKeys.base_dir()
        if sign == 1:
            image_path = str(base_dir) + '\\image\\OCR\\img_bg_path\\' + str_time_hms + '.jpg'
        else:
            image_path = str(base_dir) + '\\image\\OCR\\img_slider_path\\' + str_time_hms + '.png'

        a = 0.85  # 通过本地图片与原网页图片的比较，计算出的缩放比例
        img = Image.open(img)
        x = img.width
        y = img.height
        x_resize = int(x * a)
        y_resize = int(y * a)
        img = img.resize((x_resize, y_resize), Image.ANTIALIAS)
        img.save(image_path)
        return image_path

    @staticmethod
    def find_pic(img_bg_path, img_slider_path):
        """
        找出图像中最佳匹配位置
        :param img_bg_path: 滑块背景图本地路径
        :param img_slider_path: 滑块图片本地路径
        :return: 返回最差匹配、最佳匹配对应的x坐标
        """
        # 背景图片和滑块分别进行灰度 然后二值化 最后用TM_CCOEFF_NORMED进行对比
        # 背景图片 把导入图片img_bg_path 以cv.imread()读取出宽高通道数据
        img_bg = cv.imread(img_bg_path)
        # 背景图片 把图片img_bg 进行色彩空间转换，转换为RGB <---> Gray：CV_RGB2GRAY
        gray_image = cv.cvtColor(img_bg, cv.COLOR_BGR2GRAY)
        # 背景图片 设定图片的灰色像素阈值点，使图片变成灰色图片   返回参数ret：当前图片像素阈值与设置的一致，参数thresh：返回的图片
        ret, thresh = cv.threshold(gray_image, 127, 255, cv.THRESH_TOZERO)
        # 背景图片 图片保存到img_bg_path位置
        cv.imwrite(img_bg_path, thresh)
        # 背景图片 读取img_bg_path图片
        img_bg = cv.imread(img_bg_path)
        # 背景图片 图片转换为灰度图片
        img_bg_gray = cv.cvtColor(img_bg, cv.COLOR_BGR2GRAY)
        # 滑块图片 0：读入灰色通道图片    1：读入彩色图片
        img_slider_gray = cv.imread(img_slider_path, 0)
        # 滑块图片 设定图片的灰色像素阈值点为170，最大80，类型2
        ret, thresh = cv.threshold(img_slider_gray, 170, 80, cv.THRESH_TRUNC)
        # 滑块图片 图片保存
        cv.imwrite(img_slider_path, thresh)
        #  滑块图片 读入灰色通道图片
        img_slider_gray = cv.imread(img_slider_path, 0)

        # matchTemplate：模板匹配的函数   img_bg_gray：背景图片  img_slider_gray：滑块图片    cv.TM_CCOEFF_NORMED：相关性系数匹配方法
        res = cv.matchTemplate(img_bg_gray, img_slider_gray, cv.TM_CCOEFF_NORMED)
        # 找出矩阵中的最大值和最小值，给出它们中的坐标
        value = cv.minMaxLoc(res)
        return value[2:][0][0], value[2:][1][0]

    # 返回两个数组：一个用于加速拖动滑块，一个用于减速拖动滑块
    @staticmethod
    def generate_tracks(distance):
        # 给距离加上20，这20像素用在滑块滑过缺口后，减速折返回到缺口
        distance += 20
        v = 0
        t = 0.2
        forward_tracks = []
        current = 0
        mid = distance * 3 / 5  # 减速阀值
        while current < distance:
            if current < mid:
                a = 2  # 加速度为+2
            else:
                a = -3  # 加速度-3
            s = v * t + 0.5 * a * (t ** 2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        ft_sum = reduce(lambda x, y: x + y, forward_tracks)
        distance -= 20
        back_tracks_sum = ft_sum - distance
        back_tracks = CommonPublic.random_num_vaccine_person_total(back_tracks_sum, 5)
        back_tracks = [-x for x in back_tracks]
        return forward_tracks, back_tracks

    def do_match(self, bg_locator, slider_locator, mode='slow'):
        """
        :param driver:
        :param bg_type: 背景图片的元素的类型  By.ID,By.CLASS_NAME,By.NAME
        :param bg_locator: 背景图片的元素的值
        :param slider_type: 滑块图片的元素的类型  By.ID,By.CLASS_NAME,By.NAME
        :param slider_locator:滑块图片的元素的值
        :param mode: 一直等于slow，
        :return: 释放滑块
        """
        wait = WebDriverWait(self.driver, 10)
        bg_image = wait.until(expected_conditions.presence_of_element_located((By.XPATH, bg_locator)))
        # 背景图片
        time.sleep(1)
        bg_image_url = bg_image.get_attribute('src')
        str_time_hms = SeleniumKeys.str_time_hms()
        str_time_hms = str(str_time_hms)
        base_dir = SeleniumKeys.base_dir()
        img_bg_path = str(base_dir) + '\\image\\OCR\\img_bg_path\\' + str_time_hms + '.jpg'
        # 背景图片，将URL表示的网络对象复制到本地文件
        urllib.request.urlretrieve(bg_image_url, img_bg_path)
        # 把本地下载的网络图片，进行缩放，缩放到网页显示尺寸
        img_bg_path = SeleniumKeys.resize_img(img_bg_path, 1)
        # 等待wait秒，判断是否加载
        slider = wait.until(expected_conditions.presence_of_element_located((By.XPATH, slider_locator)))
        # 滑动模块图片
        slider_url = slider.get_attribute('src')
        img_slider_path = str(base_dir) + '\\image\\OCR\\img_slider_path\\' + str_time_hms + '.png'
        # 滑动图片，将URL表示的网络对象复制到本地文件
        urllib.request.urlretrieve(slider_url, img_slider_path)
        # 把本地下载的网络图片，进行缩放，缩放到网页显示尺寸
        img_slider_path = SeleniumKeys.resize_img(img_slider_path, 2)
        value_1, value_2 = SeleniumKeys.find_pic(img_bg_path, img_slider_path)  # 最差匹配，最佳匹配
        action = ActionChains(self.driver)
        # 可能不对，slider返回的是信息
        action.move_to_element(slider)
        # 按住滑块slider，slider：需要是一个定位
        action.click_and_hold(slider).perform()
        if mode == 'slow':
            forward_tracks, back_tracks = SeleniumKeys.generate_tracks(value_2)

            for x in forward_tracks:
                # #移动滑块 0：y轴的移动距离
                action.move_by_offset(x, 0).perform()  # 前进移动滑块
            for x in back_tracks:
                action.move_by_offset(x, 0).perform()  # 后退移动滑块
        else:
            action.move_by_offset(value_2, 0).perform()  # 前进移动滑块
        # 释放滑块
        action.release().perform()

    def match_code(self, bg_locator, slider_locator, mode='slow'):
        while True:
            try:
                self.do_match(bg_locator, slider_locator, mode)
                break
            except AssertionError as msg:
                print(msg)
