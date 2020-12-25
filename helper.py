#coding:utf-8
import time

from utils.Utils import Utils
from wework import WeWork


class Helper(WeWork):
  #
  @classmethod
  def get_current_time(cls):
      now_time = time.time()
      s=int(round(now_time * 1000))
      print(s)
      return s
   #请求公参
  def request_params(self):
      jsonstr={"get_headers":{
                "Content-Type": "application/json"
            },"get_params":{
            "client":"ios",
            "cuid":"FECB9336-93F7-4DD7-A9CA-1EF7517076EE",
            "format":"json",
            "sign":"61a921a3c390fb4204279429873da264",
            "source":"sfa",
            "time":"1605787062000",
            "version":"2.5.1"
            }}

      return jsonstr
  #账号密码参数化
  def get_account_pwd(self):
      return  [{
		"title": "错误用户名码",
		"account": "133444",
		"password": "ewfw",
		"responseCode": -1,
		"isSuccess": False
	},
	{
		"title": "错误用户名密码",
		"account": "133444",
		"password": "ewfw",
		"responseCode": -1,
		"isSuccess": False
	},
	{
		"title": "错误用户名密码",
		"account": "133444",
		"password": "ewfw",
		"responseCode": -1,
		"isSuccess": False
	},
	{
		"title": "正确用户名密码",
		"account": "54260644",
		"password": "p7Gx4TKqh5quPqjTlU+csw==",
		"responseCode": 0,
		"isSuccess": True
	}]
  #参数化“扩排面”列表
  def get_prdDisplayList(self):
	  return [
    {
        "prdDisplayList":[
            {
                "depthNum":13,
                "widthNum":12,
                "prdId":"10000004",
                "prdName":"500g羽绒液"
            }
        ],
        "title":"测试只有一个品"
    },
    {
        "prdDisplayList":[
            {
                "prdId":"10000012",
                "prdName":"自然香洁净洗衣液袋装15g×180",
                "depthNum":125,
                "widthNum":126
            },
            {
                "prdId":"10000014",
                "prdName":"500g洁净瓶-自然",
                "depthNum":135,
                "widthNum":126
            },
            {
                "prdId":"10001394",
                "prdName":"500g芦荟袋(新)",
                "depthNum":253,
                "widthNum":256
            }
        ],"title":"测试三个品"
    },{
        "prdDisplayList":[
            {
                "depthNum":999999999999,
                "widthNum":12,
                "prdId":"10000004",
                "prdName":"500g羽绒液"
            }
        ],
        "title":"测试最大边界值"
    },{
        "prdDisplayList":[
            {
                "depthNum":0,
                "widthNum":12,
                "prdId":"10000004",
                "prdName":"500g羽绒液"
            }
        ],
        "title":"测试0"
    },{
        "prdDisplayList":[
            {
                "depthNum":-1,
                "widthNum":12,
                "prdId":"10000004",
                "prdName":"500g羽绒液"
            }
        ],
        "title":"测试负数"
    }
]
  #参数化“增特陈”
  def get_zengTeChenList(self):
      print("test_time")
      print(self.get_current_time())
      return [{
    "zengTeChenList":[
        {
            "displayType":"1",
            "startTime":self.get_current_time(),
            "endTime":self.get_current_time(),
            "prdList":[
                {
                    "prdId":"10000004",
                    "prdName":"500g羽绒液"
                },
                {
                    "prdId":"10000015",
                    "prdName":"500g洁净瓶-薰"
                },
                {
                    "prdId":"10000005",
                    "prdName":"250g羽绒液"
                },
                {
                    "prdId":"10000018",
                    "prdName":"1kg洁净瓶-自然"
                }
            ],
            "displayNum":157,
            "displayPartNum":None,
            "displayArea":99.99,
            "displayDesc":"堆头"
        }
    ]
,"title":"4个品"},{
    "zengTeChenList":[
        {
            "displayType":"1",
            "startTime":self.get_current_time(),
            "endTime":self.get_current_time(),
            "prdList":[
                
            ],
            "displayNum":157,
            "displayPartNum":None,
            "displayArea":99.99,
            "displayDesc":"堆头"
        }
    ]
,"title":"0个品"},{
    "zengTeChenList":[
        {
            "displayType":"1",
            "startTime":self.get_current_time(),
            "endTime":self.get_current_time(),
            "prdList":[
                {
                        "prdId":"10000004",
                        "prdName":"500g羽绒液"
                    }
            ],
            "displayNum":157,
            "displayPartNum":None,
            "displayArea":99.99,
            "displayDesc":"堆头"
        }
    ]
,"title":"1个品"},{
    "zengTeChenList":[
        {
            "displayType":"1",
            "startTime":self.get_current_time(),
            "endTime":self.get_current_time(),
            "prdList":[
                {
                        "prdId":"10000004",
                        "prdName":"500g羽绒液"
                    }
            ],
            "displayNum":1000000000,
            "displayPartNum":None,
            "displayArea":99.99,
            "displayDesc":"堆头"
        }
    ]
,"title":"测试displayNum边界值"}]
  #参数化"订单"
  def get_orderParams(self):
      return [{  "title":"正常场景测试",
                "prdId":"10000018",
                "prdName":"1kg洁净瓶-自然",
                "prdPrice":1364,
                "suitPrice":1364,
                "groupBuyPrice":1364,
                "suitNum":25,
                "singleNum":1,
                "groupBuyNum":5
            },{  "title":"prdId为空",
                "prdId":"",
                "prdName":"1kg洁净瓶-自然",
                "prdPrice":1364,
                "suitPrice":1364,
                "groupBuyPrice":1364,
                "suitNum":25,
                "singleNum":1,
                "groupBuyNum":5
            },{  "title":"prdPrice为负数",
                "prdId":"",
                "prdName":"1kg洁净瓶-自然",
                "prdPrice":-2,
                "suitPrice":1364,
                "groupBuyPrice":1364,
                "suitNum":25,
                "singleNum":1,
                "groupBuyNum":5
            },{  "title":"suitNum边界值",
                "prdId":"",
                "prdName":"1kg洁净瓶-自然",
                "prdPrice":1364,
                "suitPrice":1364,
                "groupBuyPrice":1364,
                "suitNum":9999999999,
                "singleNum":1,
                "groupBuyNum":5
            }]

  @classmethod
  # json_object: json对象;  expr: 提取json字段表达式
  def get_jsonpath(cls,json_object,expr):
     return Utils.jsonpath(json_object,expr)
  '''
  通过jsonpath表达式提取json对象返回是一个列表，获取列表指定的元素
  exp:jsonpath表达式
  index:列表指定角标
  '''
  @classmethod
  def getlistvalue_bykey(cls,exp,index=0):
      list=[]
      list=cls.get_jsonpath(Helper.dict,exp);
      return Utils.getListvalue(list,index)
if __name__ == '__main__':
    #print(Helper.get_paramsByKey('manager'))
    #dict = {"manager": {"channel": 3, "applicantId": 54260644}}
    print(Helper.getlistvalue_bykey('$..manager[channel]'))












