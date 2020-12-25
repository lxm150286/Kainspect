import json

from jsonpath import jsonpath


class Utils:
    @classmethod
    #完成对json的格式化处理
    def format(cls,json_object):
        return json.dumps(json_object,indent=2);


    @classmethod
    #json_object  json对象
    # expr  jsonpath 取值表达式
    def jsonpath(cls,json_object,expr):
        return jsonpath(json_object,expr)

    '''
        通过传入要提取json对象 以及jsonpath表达式获取valye
        json_object  json对象
        expr  jsonpath 取值表达式
    '''

    @classmethod
    def get_jsonpath(cls, json_object, expr):
        return jsonpath(json_object, expr)

    '''
    传入列表，默认获取列表的第一个元素
    list 为列表  index默认传0
    '''

    @classmethod
    def getListvalue(cls, list=[], index=0):
        return list[index]