# -*- coding: cp936 -*-
"""
��CNKIר����ѯ���ҳ����н������õ���ѯ��Ŀ�б�
"""
import sys
from HTMLParser import HTMLParser

from my_spider import CnkiSpider

reload(sys)
sys.setdefaultencoding('utf8')


class PatentParser(HTMLParser):
    def __init__(self, append_info=''):
        HTMLParser.__init__(self)
        self.__insubtags = ['sub', 'sup']
        # �ؼ���־flagȡֵ��0�޹ر�ǩ��1ר�����йر�ǩ��ר������ǩ��2�����˱�ǩ��3�����˱�ǩ��4�������ڱ��װ���5�������ڱ�ǩ
        self.__flag = 0
        self.__insubflag = False
        self.__subject = ''
        # ���˳���������ӣ�ר�����⣬�����ˣ������ˣ��������ڣ���������
        self.__sequence = []
        self.__result = []
        self.page_count = ''
        self.__pagecountflg = False
        self.item_count = ''
        self.__itemflg = False
        self.append_info = str(append_info)

    def handle_starttag(self, tag, attrs):
        tag = tag.strip()
        # ���ר�����⡢����ר����
        if tag == 'a':
            for name, value in attrs:
                if name == 'class' and value == 'fz14':
                    self.__flag = 1
                elif name == 'href' and self.__flag == 1:
                    s = value.strip()
                    self.__sequence.append(s[s.find('filename=') + 9:])
        # �ؼ���־flagȡֵ��0�޹ر�ǩ��1ר�����йر�ǩ��ר������ǩ��2�����˱�ǩ��3�����˱�ǩ��4�������ڱ��װ���5�������ڱ�ǩ
        elif tag == 'td':
            if self.__flag in range(1, 5):
                self.__flag += 1
        # ��ǲ�ѯ��ҳ��
        elif tag == 'span':
            for name, value in attrs:
                if name == 'class' and value == 'countPageMark':
                    self.__pagecountflg = True
        # ���Ӧ����Ŀ����
        # NOTE: cnki���֧�ַ���6000����¼����ˣ�����6000���Ļ���Ӧ������ѯ���������������ڿ�ȡ����廯ר������
        elif tag == 'div':
            for name, value in attrs:
                if name == 'class' and value == 'pagerTitleCell':
                    self.__itemflg = True
        # ����ר�����������ϱꡢ�±굼�¶�η���data���绯�������ơ���ѧ���ŵȣ�
        elif tag in self.__insubtags:
            if self.__flag == 1:
                self.__insubflag = True
        else:
            self.__flag = 0

    def handle_endtag(self, tag):
        tag = tag.strip()
        # ����ר������
        if tag == 'a' and self.__flag == 1:
            self.__sequence.append(self.__subject)
            self.__insubflag = False
            self.__subject = ''
        elif tag == 'span' and self.__pagecountflg:
            self.__pagecountflg = False
        if tag == 'div' and self.__itemflg:
            self.__itemflg = False

    def handle_data(self, data):
        data = data.strip()
        if self.__pagecountflg:
            self.page_count = data[str(data).find('/') + 1:]
            self.__pagecountflg = False
        if self.__itemflg:
            self.item_count = data[3:len(data) - 4]
        if self.__flag == 1:
            self.__subject += data
        # �����ĸ��ֶΣ������ˡ������ˡ��������ڡ���������
        if self.__flag in range(2, 6) and data:
            self.__sequence.append(data)

    # �������������ز�ѯ���
    def get_result(self):
        self.__result = []
        if len(self.__sequence) % 6 != 0:
            # ���������ڼ������������ɽ���htmlʧ��
            print "Parser error!"
            # for each in self.__sequence:
            #     print each
            exit(-1)
        if self.append_info == '':
            for i in range(1, int(len(self.__sequence) / 6) + 1):
                self.__result.append(
                    [
                        self.__sequence[6 * i - 6], self.__sequence[6 * i - 5], self.__sequence[6 * i - 4],
                        self.__sequence[6 * i - 3], self.__sequence[6 * i - 2], self.__sequence[6 * i - 1]
                    ]
                )
        else:
            for i in range(1, int(len(self.__sequence) / 6) + 1):
                self.__result.append(
                    [
                        self.__sequence[6 * i - 6], self.__sequence[6 * i - 5], self.__sequence[6 * i - 4],
                        self.__sequence[6 * i - 3], self.__sequence[6 * i - 2], self.__sequence[6 * i - 1],
                        self.append_info
                    ]
                )
        self.__sequence = []
        return self.__result

    def feed(self, data):
        # �ؼ���ɾ��html�ĵ�����"&"��ͷ�ĸ���ת���ַ�
        self.rawdata = self.rawdata + self.unescape(data).replace('&', '')
        self.goahead(0)


if __name__ == '__main__':
    myparser = PatentParser('experiment')
    myparser.feed(CnkiSpider('C041', '2012-01-01', '2012-12-31').goto_page(1))
    result = myparser.get_result()
    for line in result:
        print line.decode('gbk')
