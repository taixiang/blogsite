'''
Created by auto_sdk on 2018.11.08
'''
from top.api.base import RestApi


class TbkItemGuessLikeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.adzone_id = None
        self.os = None
        self.ip = None
        self.ua = None
        self.net = None
        self.page_no = None
        self.page_size = None

    def getapiname(self):
        return 'taobao.tbk.item.guess.like'
