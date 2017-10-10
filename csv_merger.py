# -*- coding: cp936 -*-
import codecs
import csv
import os
import sys

default_encoding = "utf-8"
if default_encoding != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding(default_encoding)


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


if __name__ == '__main__':
    CATEGORY_LIST = [
        'ҽҩ�������������뷨�ɷ����о�',
        'ҽѧ������ҽѧ��Եѧ��',
        'Ԥ��ҽѧ������ѧ',
        '��ҽѧ',
        '��ҩѧ',
        '����ҽ���',
        '����ҽѧ',
        '�ٴ�ҽѧ',
        '��Ⱦ�Լ�������Ⱦ��',
        '��Ѫ��ϵͳ����',
        '����ϵͳ����',
        '����ϵͳ����',
        '�ڷ����ټ�ȫ���Լ���',
        '���ѧ',
        '�����ѧ',
        '������ѧ',
        '����ѧ',
        '�񾭲�ѧ',
        '����ѧ',
        '����ѧ',
        '�ۿ�������ʺ��',
        '��ǻ��ѧ',
        'Ƥ�������Բ�',
        '����ҽѧ',
        '����ҽѧ',
        '����ҽѧ������',
        'ҩѧ',
        '����ҽѧ����',
    ]

    FILE_LIST = [
        '��ҽѧ_����ר��.csv',
        '��ҩѧ_����ר��.csv',
        '����ҽ���_����ר��.csv',
        '�ٴ�ҽѧ_����ר��.csv',
        'ҽҩ�������������뷨�ɷ����о�_����ר��.csv',
        '��ǻ��ѧ_����ר��.csv',
        '����ϵͳ����_����ר��.csv',
        '����ҽѧ_����ר��.csv',
        '���ѧ_����ר��.csv',
        '������ѧ_����ר��.csv',
        '��Ѫ��ϵͳ����_����ר��.csv',
        '����ҽѧ_����ר��.csv',
        '�����ѧ_����ר��.csv',
        '����ϵͳ����_����ר��.csv',
        '����ҽѧ_����ר��.csv',
        '����ҽѧ����_����ר��.csv',
        'Ƥ�������Բ�_����ר��.csv',
        '�ۿ�������ʺ��_����ר��.csv',
        '����ѧ_����ר��.csv',
        'ҩѧ_����ר��.csv',
        'Ԥ��ҽѧ������ѧ_����ר��.csv',
    ]

    DIR_STR = '2007-2016ҽҩ������ҵ����/2007-2016ȫ��ҽҩ��������'

    # merge_by_category(DIR_STR, CATEGORY_LIST)

    out_filename = '2007-2016ȫ��ҽҩ��������ר��.csv'
    # merge_into_a_csv(out_filename, DIR_STR, FILE_LIST)
