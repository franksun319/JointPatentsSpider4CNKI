# -*- coding: cp936 -*-
import codecs
import csv
import os
import sys
import time

default_encoding = "utf-8"
if default_encoding != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding(default_encoding)


# noinspection PyChainedComparisons
class CsvReader:
    def __init__(self, file_name='', start_time='2010-01-01', end_time=time.strftime('%Y-%m-%d')):
        self.file_name = file_name
        self.start_time = start_time
        self.end_time = end_time
        if not self.__is_file_exits():
            print 'File ' + self.file_name + ' does not exists!'
            self.__refresh()
            exit(-1)

    def __refresh(self):
        self.file_name = ''
        self.start_time = ''
        self.end_time = ''

    def __is_file_exits(self):
        return os.path.exists(self.file_name)

    def applicant_list(self):
        my_list = []
        if not self.__is_file_exits():
            return my_list
        with codecs.open(self.file_name, 'rb', encoding='gb18030') as cf:
            reader = csv.reader(cf)
            for row in reader:
                # 筛选条件：（1）时间start_time之后；（2）时间end_time之前；（3）不允许记录重复
                if self.start_time <= row[4] <= self.end_time and row[3] not in my_list:
                    my_list.append(row[3])
        return my_list

    def joint_applicant_list(self):
        old_list = self.applicant_list()
        new_list = []
        if not old_list:
            return new_list
        for oe in old_list:
            if str(oe).find(';') != -1:
                new_list.append(str(oe).split(';'))
        return new_list


if __name__ == '__main__':
    my_reader = CsvReader(u'D:/My Works/于东平2016国家自科/PatentSpider_2.7/已下载数据/能源电力.csv',
                          '2016-01-01', '2016-12-31')
    result = my_reader.joint_applicant_list()
    for each in result:
        print ','.join(each)
    print len(result)
