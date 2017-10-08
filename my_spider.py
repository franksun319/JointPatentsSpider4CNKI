# -*- coding: cp936 -*-
"""
CNKI专利爬虫
注意：CNKI为utf-8编码而非gbk编码。但是，文档中的中文默认为gbk编码，所以中文需要先gbk解码再进行utf-8编码
"""

import cookielib
import socket
import time
import urllib
import urllib2

import paraset

socket.setdefaulttimeout(20)


class CnkiSpider:
    __MAX_CONNECTION = 3
    __TIME_OUT = 15
    __WAIT_TIME = 10

    def __init__(self, patent_code='*', start_time='2010-01-01', end_time=time.strftime('%Y-%m-%d')):
        self.__refresh()
        self.patent_code = patent_code
        self.start_time = start_time
        self.end_time = end_time
        # 构建头结构，模拟浏览器
        self.header = {'Connection': 'Keep-Alive',
                       'Accept': 'text/html,*/*',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'}
        # self.__reconnection()

    def __refresh(self):
        self.cookie = {}
        self.opener = None

    def __reconnection(self):
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie), urllib2.HTTPHandler)
        url = 'http://kns.cnki.net/KNS/request/SearchHandler.ashx?'
        postdata = urllib.urlencode(
            paraset.make_parameters(self.patent_code, self.start_time, self.end_time))  # 将参数url编码
        try:
            req = urllib2.Request(url + postdata, headers=self.header)  # 提交申请
            self.opener.open(req).read()
        except:
            print '... query submission error! wait ' + str(CnkiSpider.__WAIT_TIME) + ' seconds ...'
            time.sleep(CnkiSpider.__WAIT_TIME)

    # 返回值：[运行结果，获取网页]。
    # 运行结果==True时，获取网页=网页代码字符串
    # 运行结果==False时，获取网页=''
    def __goto_page_helper(self, page_num=1):
        query_string = urllib.urlencode(
            {'curpage': page_num, 'RecordsPerPage': '50', 'QueryID': '16', 'ID': '', 'turnpage': '1',
             'tpagemode': 'L', 'dbPrefix': 'SCPD', 'Fields': '', 'DisplayMode': 'listmode',
             'PageName': 'ASP.brief_result_aspx', 'sKuaKuID': '16'}
        )
        req = urllib2.Request('http://kns.cnki.net/kns/brief/brief.aspx?' + query_string, headers=self.header)
        try:
            result = self.opener.open(req, timeout=CnkiSpider.__TIME_OUT)
            html = result.read()
        except:
            print '... page ' + str(page_num) + ' fetch error! wait ' + str(CnkiSpider.__WAIT_TIME) + ' seconds ...'
            time.sleep(CnkiSpider.__WAIT_TIME)
            return [False, '']
        else:
            # with open('test.htm','w') as h:
            #     h.write(html)
            # print html
            return [True, html]

    def goto_page(self, page_num=1, reconnect=True):
        if reconnect:
            self.__reconnection()
        reconnect_time = 0
        while reconnect_time < CnkiSpider.__MAX_CONNECTION:
            r = self.__goto_page_helper(page_num)
            # successfully fetch web page
            if r[0]:
                return r[1]
            self.__reconnection()
            reconnect_time += 1
            print '... page ' + str(page_num) + ' reconnect times: ' + str(reconnect_time) + '.'
        print 'Always can not fetch page ' + str(page_num) + '.'
        return ''


if __name__ == '__main__':
    cnki = CnkiSpider('C041', '2012-01-01', '2012-12-31')
    print cnki.goto_page(3)
