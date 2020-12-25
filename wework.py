import requests

from BaseApi import BaseApi


class WeWork(BaseApi):
    token_url='https://tmallapi.bluemoon.com.cn/bmcrm-control/user/ssoLogin'
    client={
    "client":"ios",
    "cuid":"FECB9336-93F7-4DD7-A9CA-1EF7517076EE",
    "format":"json",
    "sign":"61a921a3c390fb4204279429873da264",
    "source":"sfa",
    "time":"1605787062000",
    "version":"2.5.1"
}
    deviceNum='e8d2df7e3b88b1e30fbdbd8c05fdbd7c'
    password='p7Gx4TKqh5quPqjTlU+csw=='
    account=None;
    token={}



    @classmethod
    def get_token(cls, account=account):
        if account is None:
            return cls.token[account]
            # 避免重复请求，提高速度
        if account not in cls.token.keys():
            r = cls.get_access_token(account)
            cls.token[account] = r["token"]#追加在字典里面
        print('----------')
        print(cls.token)
        return cls.token[account]



    @classmethod
    def get_access_token(cls,account):
        r = requests.post(cls.token_url,
                         params=cls.client,
                         json={'deviceNum':cls.deviceNum,'account':account,'password':cls.password},
                         verify=False,proxies=cls.proxies)
        cls.format(r)
        assert r.json()["isSuccess"] == True
        return r.json()


#WeWork.get_token('54260644');
dict={'54260644': '573f2776e99ebac96b5752a531ddd640'}
if __name__ == '__main__':

    print(dict['54260644'])