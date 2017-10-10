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
        'ҽҩ�������������뷨�ɷ����о�', 'ҽѧ������ҽѧ��Եѧ��', 'Ԥ��ҽѧ������ѧ', '��ҽѧ', '��ҩѧ',
        '����ҽ���', '����ҽѧ', '�ٴ�ҽѧ', '��Ⱦ�Լ�������Ⱦ��', '��Ѫ��ϵͳ����', '����ϵͳ����',
        '����ϵͳ����', '�ڷ����ټ�ȫ���Լ���', '���ѧ', '�����ѧ', '������ѧ', '����ѧ', '�񾭲�ѧ',
        '����ѧ', '����ѧ', '�ۿ�������ʺ��', '��ǻ��ѧ', 'Ƥ�������Բ�', '����ҽѧ', '����ҽѧ',
        '����ҽѧ������', 'ҩѧ', '����ҽѧ����',
    ]
    merge_by_category(DIR_STR, CATEGORY_LIST)

    FILE_LIST = [
        '���緢�糧_ȫ������ר��.csv', '��ѹ�������������������任��_ȫ������ר��.csv',
        '������_ȫ������ר��.csv', '̫����_ȫ������ר��.csv', 'ˮ������_ˮ��վ����_ȫ������ר��.csv',
        '����_ȫ������ר��.csv', '�繤��������_ȫ������ר��.csv', '�繤����_ȫ������ר��.csv',
        '���_ȫ������ר��.csv', '����������Ӧ��_ȫ������ר��.csv', '������������������_ȫ������ר��.csv',
        '��Դ����_ȫ������ר��.csv', '����繤�̵�����������ϵͳ_ȫ������ר��.csv',
        '����_ȫ������ר��.csv', '�ߵ�ѹ����_ȫ������ר��.csv'
    ]
    out_filename = '2011-2016ȫ����Դ��������ר��.csv'
    # merge_into_a_csv(out_filename, DIR_STR, FILE_LIST)
