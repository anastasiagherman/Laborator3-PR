import requests
from bs4 import BeautifulSoup
from OpenThroughSocket import OpenThroughSocket
from DownloadImages import DownloadImages
import re
import threading
from threading import Thread

lock = threading.Lock()

proxies = {
    'http': 'http://dcRezG:kjrDLs@193.7.199.142:8000',
    'https': 'http://dcRezG:kjrDLs@193.7.199.142:8000',
}

url_params = {
            'Cache-Control': 'no-store'
        }

class Andys(Thread):
    def __init__(self, email, password):
        Thread.__init__(self)
        self.email = email
        self.password = password
        self.login_url = 'https://andys.md/en/login'
        self.account = 'https://andys.md/en/account'
        self.main_page = 'https://andys.md/en'
        self.content = ''
        self.curSession = requests.Session()

    def getLoginCookies(self):
        values = {'email': self.email,
                  'password': self.password
                  }
        response = self.curSession.post(self.login_url, data=values, proxies=proxies)
        return response

    def downloadImages(self):
        links = OpenThroughSocket(self.getPage()).getLinks()
        print(links)
        DownloadImages(links, 'andys.md', 443).startMultiThreadind()
        
    def getPageCookies(self):
        print(self.getLoginCookies().cookies)
        request_get = self.curSession.get(self.account, proxies=proxies, cookies = self.getLoginCookies().cookies, verify = False)
        self.content = request_get.text
        print(self.content)

    def getPage(self):
        request_get = requests.get(self.main_page, proxies=proxies)
        self.content = request_get.text
        print(self.content)
        return self.content

    def headRequest(self):
        x = requests.head(self.main_page, proxies=proxies)
        print(x.request.headers)

    def optionsRequest(self):
        resp = requests.options(self.main_page, params=url_params, proxies=proxies)
        print(resp.request.headers)
