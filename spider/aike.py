import re
import itchat
from requests import Request, session
from bs4 import BeautifulSoup as bs


class Aike:

    session = session()
    url = 'http://www.icourse8.com/login.jsp'
    # url = 'https://www.ike8.cn/api/'
    username = 'jaychou114118'
    password = 'l1141180'
    value = ''
    payload = {
        'user_login': username,
        'password': password
    }
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    headers = {'User-Agent': user_agent}

    def __fetch_content(self):
        req = Request(
            'post',
            self.url,
            data=self.payload,
            headers=dict(referer=self.url)
        )
        prepped = req.prepare()

        # 将处理的请求参数通过session请求对象发送过去
        resp = self.session.send(prepped)

        # 用BeautifulSoup处理登录之后返回的数据
        soup = bs(resp.content, "html.parser")

        # 打印输出
        print(soup.prettify())

    def start(self):
        self.__fetch_content()


aike = Aike()
aike.start()