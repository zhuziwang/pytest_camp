# coding=utf-8
from common.base_log.log import Log
from pathlib import Path

import pytesseract
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


