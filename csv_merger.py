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
    def merge_by_category(dir_str, cat_list):
        dir_str = standardize_dir(dir_str)
        file_list = os.listdir(dir_str)
        for keyword in cat_list:
            if all([str(f).find(keyword) == -1 for f in file_list]):
                continue
            print 'Merging \"' + keyword.decode('gbk') + '\" related csv files ...'
            with codecs.open(keyword + '.csv', 'ab', encoding='gb18030') as merge_file:
                my_writer = csv.writer(merge_file)
                for f in file_list:
                    if f.find(keyword) != -1:
                        with codecs.open(dir_str + f, 'rb', encoding='gb18030') as cf:
                            my_reader = csv.reader(cf)
                            my_writer.writerows(my_reader)


    def merge_into_a_csv(out_csv_file, dir_str, file_list):
        dir_str = standardize_dir(dir_str)
        with codecs.open(out_csv_file, 'ab', encoding='gb18030') as merge_file:
            my_writer = csv.writer(merge_file)
            for f in file_list:
                if not os.path.exists(dir_str + f):
                    continue
                with codecs.open(dir_str + f, 'rb', encoding='gb18030') as cf:
                    my_reader = csv.reader(cf)
                    my_writer.writerows(my_reader)


    def check_dir(func):
        def __wrapper(dir_str):
            assert (os.path.exists(dir_str)), 'Such directory \"' + str(dir_str).decode('gbk') + '\" does not exists!'
            return func(dir_str)

        return __wrapper


    @check_dir
    def standardize_dir(dir_str):
        if dir_str[len(dir_str) - 1] != '/':
            return dir_str + '/'
        else:
            return dir_str


    DIR_STR = 'csv'

    CATEGORY_LIST = [
        '医药卫生方针政策与法律法规研究', '医学教育与医学边缘学科', '预防医学与卫生学', '中医学', '中药学',
        '中西医结合', '基础医学', '临床医学', '感染性疾病及传染病', '心血管系统疾病', '呼吸系统疾病',
        '消化系统疾病', '内分泌腺及全身性疾病', '外科学', '泌尿科学', '妇产科学', '儿科学', '神经病学',
        '精神病学', '肿瘤学', '眼科与耳鼻咽喉科', '口腔科学', '皮肤病与性病', '特种医学', '急救医学',
        '军事医学与卫生', '药学', '生物医学工程',
    ]
    merge_by_category(DIR_STR, CATEGORY_LIST)

    FILE_LIST = [
        '发电发电厂_全国联合专利.csv', '变压器变流器及其它电力变换器_全国联合专利.csv',
        '地热能_全国联合专利.csv', '太阳能_全国联合专利.csv', '水能利用_水电站工程_全国联合专利.csv',
        '电器_全国联合专利.csv', '电工基础理论_全国联合专利.csv', '电工材料_全国联合专利.csv',
        '电机_全国联合专利.csv', '电气化电能应用_全国联合专利.csv', '电气测量技术及仪器_全国联合专利.csv',
        '电源技术_全国联合专利.csv', '输配电工程电力网及电力系统_全国联合专利.csv',
        '风能_全国联合专利.csv', '高电压技术_全国联合专利.csv'
    ]
    out_filename = '2011-2016全国能源电力联合专利.csv'
    # merge_into_a_csv(out_filename, DIR_STR, FILE_LIST)
