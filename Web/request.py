#coding=utf-8
import time
import requests
import json

#谷歌浏览器
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
'cache-control': 'no-cache',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'ec-ch-ua-platform':'Windows',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'

}

class Request():


    def get(self,url=None,payload=None,Deserved_results=None):
        '''
        get方式请求，返回的值
        :param url:
        :param payload: 请求内容{'key':'value'}
        :param Deserved_results: 预期值
        :return: 请求后返回内容，预期值
        '''
        response = requests.get(url,params=payload,headers=headers)
        return response.text,Deserved_results

    def post(self, url=None, payload=None):
        '''
        post方式请求，表单形式的数据，返回的值
        :param url:
        :param payload: 请求内容{'key':'value'}
        :return: 请求后返回内容，预期值
        '''
        response = requests.post(url, data=payload, headers=headers)
        return response

    def post_json(self, url=None, payload=None, Deserved_results=None):
        '''
        post方式请求, 使用 json 参数直接传递, 返回的值
        :param url:
        :param payload: 请求内容{'key':'value'}
        :param Deserved_results: 预期值
        :return: 请求后返回内容，预期值
        '''
        response = requests.post(url, json=payload, headers=headers)
        return response, Deserved_results

    def files(self,url=None ,filename=''):
        files = {'file': open(filename, 'rb')}
        requests.post(url, files=files)

class Request_web(Request):
    def fanyi(self):
        a='够'
        verify = 'C:/Users/nicai/Desktop/zhengshu.cer'
        #requests.get('https://fanyi.baidu.com/#zh/en/%s'%a,headers=headers,verify=False)
        r = requests.post('https://fanyi.baidu.com/#zh/en/%s'%a,data={'token':'a8b7123ebcd57bfc77e8f4c9ca671cea'},headers=headers,verify=False)
        print(r.url)

if __name__ == '__main__':
    a=Request_web()
    a.fanyi()