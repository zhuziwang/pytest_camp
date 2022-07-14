# coding=utf-8
from common.base_log.log import Log
from pathlib import Path

import pytesseract
import cv2 as cv
import cv2
import random

from aip import AipOcr


class CommonPublic:
    def __init__(self):
        log = Log()
        self.logger = log.get_log()

    def log(self, msg):
        self.logger.debug(msg)

    @staticmethod
    def base_dir():
        """
        获取项目地址：C:\\Users\\duia\\PycharmProjects\\pytest_camp
        :return:
        """
        base_dir = Path(__file__).resolve().parent.parent.parent
        return base_dir

    @staticmethod
    def words_ocr(im_path=''):
        # -l 识别中文
        # --oem 使用LSTM作为OCR引擎，可选值为0、1、2、3；
        # 0  Legacy engine only.
        # 1  Neural nets LSTM engine only.
        # 2  Legacy + LSTM engines.
        # 3  Default, based on what is available.
        # --psm 设置Page Segmentation模式为自动
        config = '-l chi_sim --oem 1 --psm 3'
        # cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
        # cv2.IMREAD_GRAYSCALE：读入灰度图片
        # cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
        im = cv2.imread(im_path, cv2.IMREAD_COLOR)
        text = pytesseract.image_to_string(im, config=config)
        return text

    def read_file(self, image_path):
        f = None
        try:
            f = open(image_path, 'rb')
            return f.read()
        except AssertionError as msg:
            self.log(msg)
            return None
        finally:
            if f:
                f.close()

    def baidu_ocr(self, image_path):
        # 2. 接入百度智云文字识别服务
        # 安装baidu-aip。
        # 从aip中导入AipOcr
        # 替换APP_ID，API_KEY，SECRET_KEY
        APP_ID = '26030780'
        API_KEY = 'BM4wXk7l54tvW9GLSilCBWia'
        SECRET_KEY = 'ksWfdmT5949GTvDEDNhhC3fuKSIlG8bl'
        # 新建一个AipOcr，并赋值给变量client
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        # 调用通用文字识别
        # 如果有可选参数
        # 创建字典options，并将可选参数detect_direction的值设置为"true"
        options = {"detect_direction": "true"}
        # 调用通用文字识别接口并把结果赋值给result, file: "D:/image/verifyCode.png"
        image = self.read_file(image_path)
        result = client.basicAccurate(image, options)
        # 输出result
        ending = result["words_result"]
        self.log('百度文字识别返回的结果是：%s' % ending)
        return ending

    @staticmethod
    def add(x, y):
        return x+y

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
        # gray_image = gray_image.convert("RGB")gray_image = gray_image.convert("RGB")
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
        # 找出矩阵中的最大值和最小值，给出它们中的坐标   归一化的相关系数匹配方法：完全匹配会得到1，完全负相关匹配会得到-1，完全不匹配会得到0。
        value = cv.minMaxLoc(res)
        return value[2:][0][0], value[2:][1][0]

    @staticmethod
    def random_num_vaccine_person_total(maxValue, num):
        """生成总和固定的整数序列
        maxValue: 序列总和
        num：要生成的整数个数
        return []正数
        per_all_persons:list,指定 num个接种点各自待接种的人数
        """
        maxvalue = int(maxValue)
        suiji_ser = random.sample(range(0, maxvalue), k=num - 1)  # 在1~maxValue之间，采集20个数据
        suiji_ser.append(0)  # 加上数据开头
        suiji_ser.append(maxvalue)
        suiji_ser = sorted(suiji_ser)
        per_all_persons = [suiji_ser[i] - suiji_ser[i - 1] for i in range(1, len(suiji_ser))]  # 列表推导式，计算列表中每两个数之间的间隔
        return per_all_persons


