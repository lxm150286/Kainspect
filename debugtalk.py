from helper import Helper
helper = Helper()
#获取请求的公参
def get_request_params(key):
     return helper.request_params()[key]
#当前时间戳(毫秒级别)
def get_currenttemp():
  return helper.get_current_time()
#账号密码参数化
def get_acount():
    return helper.get_account_pwd()
#获取token
def get_token(token ='54260644'):
   return helper.get_token(token)

#保存门店计划----"扩排面列表"字段参数化
def prdDisplayList():
    return helper.get_prdDisplayList();
#保存门店计划---"增特陈"参数化
def get_zengTeChenList():
    return helper.get_zengTeChenList()
def get_orderParams():
    return helper.get_orderParams();
#获取列表指定角标的值,  exp: jsonpath 表达式
def getlistvalue_bykey(exp,index=0):
    return helper.getlistvalue_bykey(exp,index)




if __name__ == '__main__':
    print('------test-------')
    print(getlistvalue_bykey('manager-applicantId'))





