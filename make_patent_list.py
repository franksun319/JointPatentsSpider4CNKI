# -*- coding: cp936 -*-
"""
每次向cnki提交一组查询（条件包括：专利代码、申请时间上限、申请时间下限）。
将所有分页的查询结果写入csv文件中。
注意：每条查询最多返回6000条结果，超过此数cnki不显示，因此要控制好查询条件。
"""
import codecs
import csv
import random
import sys
import time

from my_parser import PatentParser
from my_spider import CnkiSpider

default_encoding = "utf-8"
if default_encoding != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding(default_encoding)


# noinspection PyMethodMayBeStatic
class PatentList:
    _ERROR_LOG = 'error.txt'
    _COUNT_TO_SLEEP = 13
    _MAX_RELOAD = 3
    _MEAN_SLEEP = 12
    _LOWER_SLEEP = 9
    _UPPER_SLEEP = 15
    _RAND_SIG = 4

    def __init__(self, outfile='tmp.csv', patent_code='*', start_time='2011-01-01', end_time='2011-12-31'):
        self.patent_code = patent_code
        self.start_time = start_time
        self.end_time = end_time
        self.output_file = outfile
        self.msg_prefix = self.patent_code + ' [' + self.start_time + ',' + self.end_time + ']:: '
        self.start_page = 1
        self.cnki = CnkiSpider(patent_code=self.patent_code, start_time=self.start_time, end_time=self.end_time)
        self.my_parser = PatentParser()

    @staticmethod
    def _random_lower_bounded(num, lower):
        if num < lower:
            return lower
        r = abs(int(random.normalvariate(num, PatentList._RAND_SIG)))
        while r < lower:
            r = abs(int(random.normalvariate(num, PatentList._RAND_SIG)))
        return r

    @staticmethod
    def _random_upper_bounded(num, upper):
        if num > upper:
            return upper
        r = abs(int(random.normalvariate(num, PatentList._RAND_SIG)))
        while r > upper:
            r = abs(int(random.normalvariate(num, PatentList._RAND_SIG)))
        return r

    # 为防止cnki爬虫限制，下载一定次数（COUNT_TO_SLEEP)后，程序暂停若干秒
    # 返回值：[是否需要重新连接，睡眠计数+1]
    @staticmethod
    def force_to_sleep(cnt):
        # 最低LOWER_SLEEP秒、均值MEAN_SLEEP秒
        s = PatentList._random_lower_bounded(PatentList._MEAN_SLEEP, PatentList._LOWER_SLEEP)
        if cnt % PatentList._COUNT_TO_SLEEP == 0:
            print "##### Pausing " + str(s) + " seconds! #####"
            time.sleep(s)
            return [True, cnt + 1]
        else:
            return [False, cnt + 1]

    def log_error(self, e_mes):
        print self.msg_prefix + e_mes
        with open(PatentList._ERROR_LOG, 'a') as e:
            e.write(self.msg_prefix + e_mes + '\n')

    # 该函数返回值是sleep_counter
    def make_list(self, sleep_counter):
        sleep_counter = self.force_to_sleep(sleep_counter)[1]
        # 获取搜索结果网页的第一页，必要步骤，不可省略：因为要得到页数、条目数
        self.my_parser.feed(self.cnki.goto_page(self.start_page, True))
        # 如果搜索结果为空
        if not str(self.my_parser.item_count).replace(',', '').isdigit():
            self.log_error('Invalid character in item_count: ' + str(self.my_parser.item_count) + '.')
            return sleep_counter
        elif self.my_parser.item_count == '0':
            self.log_error('Empty result.')
            return sleep_counter
        # 如果结果列表多于6000条，cnki默认一次搜索最多返回6000条结果
        elif int(str(self.my_parser.item_count).replace(',', '')) > 6000:
            self.log_error('Total item ' + self.my_parser.item_count + ' is greater than 6000!')
            return sleep_counter
        with codecs.open(self.output_file, 'wb', encoding='gb18030') as cf:
            # 解析并写入第一页的结果
            my_list = self.my_parser.get_result()
            # 是否只返回单页
            last_page = 1 if self.my_parser.page_count == '' else int(self.my_parser.page_count)
            # write into csv file
            my_write = csv.writer(cf)
            my_write.writerows(my_list)
            print self.msg_prefix + 'Page ' + str(self.start_page) + '/' + str(last_page) + \
                  ' parsed. Total item: ' + str(self.my_parser.item_count) + '.'
            # 抓取、解析并写入后续网页的结果
            if last_page > 1:
                for i in range(self.start_page + 1, last_page + 1):
                    # check to sleep if necessary
                    [rec, sleep_counter] = self.force_to_sleep(sleep_counter)
                    # fetch page #i
                    self.my_parser.feed(self.cnki.goto_page(i, rec))
                    my_list = self.my_parser.get_result()
                    # reload page #i, if last feed failed (max count: MAX_RELOAD)
                    reload_time = 0
                    while my_list == [] and reload_time <= PatentList._MAX_RELOAD:
                        print "Reloading page " + str(i) + "..."
                        [rec, sleep_counter] = self.force_to_sleep(sleep_counter)
                        self.my_parser.feed(self.cnki.goto_page(i, rec))
                        my_list = self.my_parser.get_result()
                        if my_list:
                            break
                        reload_time += 1
                    # 最终抓取网页是否失败
                    if not my_list:
                        self.log_error('Failed to fetch page ' + str(i) + '/' +
                                       str(last_page) + '. Please re-download ' + self.output_file + '.')
                    else:
                        my_write.writerows(my_list)  # adding parsed results into csv file
                        print self.msg_prefix + 'Page ' + str(i) + '/' + str(last_page) + \
                              ' parsed. Total item: ' + str(self.my_parser.item_count) + '.'
            return sleep_counter


if __name__ == '__main__':
    pl = PatentList('test.csv', patent_code='E064', start_time='2016-03-01', end_time='2016-03-31')
    pl.make_list(1)
    pass
