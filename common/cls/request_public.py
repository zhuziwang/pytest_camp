# coding=utf-8
import requests
import json

from public import CommonPublic


class RequestsKeys(CommonPublic):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'cache-control': 'no-cache',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'ec-ch-ua-platform': 'Windows',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    timeout = 3

    @staticmethod
    def get(url=None, *args):
        """
        get方式请求，返回的值
        :param url:请求的url
        :param: args为payload: 请求内容{'key':'value'}
        :return: 请求后返回内容，预期值
        """
        if 'params' == args[0]:
            response = requests.get(url, params=args[1], headers=RequestsKeys.headers, timeout=RequestsKeys.timeout)
            return response.text

    @staticmethod
    def post(url=None, *args):
        """
        post方式请求，表单形式的数据，返回的值
        :param url:url
        :param args: 接收元组数据给data传参，请求内容{'key':'value'}
        :param args: args[0]为传输内容的格式，分别有data,post
        :param args: args[1]为传输的内容{'key':'value'}
        :return: 请求后返回内容，预期值
        """
        if 'data' == args[0]:
            response = requests.post(url, data=args[1], headers=RequestsKeys.headers, timeout=RequestsKeys.timeout)
            if args[2] == 'text':
                return response.text
            elif args[2] == 'json':
                return response.json()
        elif 'json' == args[0]:
            response = requests.post(url, data=args[1], headers=RequestsKeys.headers, timeout=RequestsKeys.timeout)
            if args[2] == 'text':
                return response.text
            elif args[2] == 'json':
                return response.json()

    @staticmethod
    def files(url=None, filename=''):
        """
        以post方式上传一个文件
        :param url: url地址
        :param filename: 要上传的文件的地址
        :return:
        """
        files = {'file': open(filename, 'rb')}
        r = requests.post(url, files=files, timeout=RequestsKeys.timeout)
        return r.text

