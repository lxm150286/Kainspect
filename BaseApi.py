import json

import requests
import yaml
from jsonpath import jsonpath

from utils.Utils import Utils
import pprint

class BaseApi:
    params={}
    printer=pprint.PrettyPrinter(indent=2)
    json_data=None
    dict={
    "manager":{
        "channel":3,
        "applicantId":54260644},
    "member":{
        "channel":2,
        "applicantId":""}}
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080',
    }

    @classmethod
    #完成对json格式化处理
    def verbose(cls,json_object=json_data):
        print(Utils.format(json_object))


    @classmethod
    #完成对json格式化处理
    def format(cls, r):
        cls.r=r
        #print(json.dumps(r.json(), indent=2))
        print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)

# 封装yaml文件的加载
    def api_load(self, path):
        return self.yaml_load(path)

    @classmethod
    def yaml_load(cls, path) -> list:
        with open(path,encoding='utf-8') as f:
            return yaml.safe_load(f)

    def api_send(self, req: dict):

        req['params']['access_token'] = self.get_token(self.secret)
        #模板内容替换
        # todo: 使用format
        '''
        将req对象转换成yaml文件对象，再将yaml文件内容转成json对象
        '''
        raw = yaml.dump(req)
        for key, value in self.params.items():
            raw=raw.replace(f"${{{key}}}", repr(value))
            print("replace")
        #转成字典
        req = yaml.safe_load(raw)

        r = requests.request(
            req['method'],
            url=req['url'],
            params=req['params'],
            json=req['json']
        )
        self.format(r)
        return r.json()

