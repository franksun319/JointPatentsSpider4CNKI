# -*- coding: cp936 -*-
import codecs
import csv
import os
import sys

default_encoding = "utf-8"
if default_encoding != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding(default_encoding)

if __name__ == '__main__':
    # prefix = ['发电发电厂', '变压器变流器及其它电力变换器', '地热能', '太阳能', '水能利用_水电站工程',
    #           '电器', '电工基础理论', '电工材料', '电机', '电气化电能应用', '电气测量技术及仪器',
    #           '电源技术', '输配电工程电力网及电力系统', '风能', '高电压技术']
    # os.chdir('csv')
    # file_list = os.listdir(os.getcwd())
    # for p in prefix:
    #     print 'Merging ' + p.decode('gbk') + ' related csv files ...'
    #     with codecs.open(p + '.csv', 'ab', encoding='gb18030') as merge_file:
    #         mywriter = csv.writer(merge_file)
    #         for f in file_list:
    #             if f.find(p) == 0:
    #                 with codecs.open(f, 'rb', encoding='gb18030') as cf:
    #                     myreader = csv.reader(cf)
    #                     mywriter.writerows(myreader)

    os.chdir('全国能源电力行业数据/全国联合专利/')
    file_list = ['发电发电厂_全国联合专利.csv', '变压器变流器及其它电力变换器_全国联合专利.csv',
                 '地热能_全国联合专利.csv', '太阳能_全国联合专利.csv', '水能利用_水电站工程_全国联合专利.csv',
                 '电器_全国联合专利.csv', '电工基础理论_全国联合专利.csv', '电工材料_全国联合专利.csv',
                 '电机_全国联合专利.csv', '电气化电能应用_全国联合专利.csv', '电气测量技术及仪器_全国联合专利.csv',
                 '电源技术_全国联合专利.csv', '输配电工程电力网及电力系统_全国联合专利.csv',
                 '风能_全国联合专利.csv', '高电压技术_全国联合专利.csv'
                 ]
    with codecs.open('2011-2016全国能源电力联合专利.csv', 'ab', encoding='gb18030') as merge_file:
        mywriter = csv.writer(merge_file)
        for f in file_list:
            with codecs.open(f, 'rb', encoding='gb18030') as cf:
                myreader = csv.reader(cf)
                mywriter.writerows(myreader)
