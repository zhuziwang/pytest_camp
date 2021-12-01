import pytesseract
import sys
import cv2

class Tesseract:
    def image(self,imPath=''):
        # -l 识别中文
        # --oem 使用LSTM作为OCR引擎，可选值为0、1、2、3；
        #0  Legacy engine only.
        #1  Neural nets LSTM engine only.
        #2  Legacy + LSTM engines.
        #3  Default, based on what is available.
        #--psm 设置Page Segmentation模式为自动
        config = ('-l chi_sim --oem 1 --psm 3')
        # cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
        # cv2.IMREAD_GRAYSCALE：读入灰度图片
        # cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
        im = cv2.imread(imPath,cv2.IMREAD_COLOR)
        text = pytesseract.image_to_string(im,config=config)
        return text

if __name__ =='__main__':
    path='C:/Users/Administrator/Desktop/126.jpg'
    a=Tesseract().image(path)