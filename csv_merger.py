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
    # prefix = ['���緢�糧', '��ѹ�������������������任��', '������', '̫����', 'ˮ������_ˮ��վ����',
    #           '����', '�繤��������', '�繤����', '���', '����������Ӧ��', '������������������',
    #           '��Դ����', '����繤�̵�����������ϵͳ', '����', '�ߵ�ѹ����']
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

    os.chdir('ȫ����Դ������ҵ����/ȫ������ר��/')
    file_list = ['���緢�糧_ȫ������ר��.csv', '��ѹ�������������������任��_ȫ������ר��.csv',
                 '������_ȫ������ר��.csv', '̫����_ȫ������ר��.csv', 'ˮ������_ˮ��վ����_ȫ������ר��.csv',
                 '����_ȫ������ר��.csv', '�繤��������_ȫ������ר��.csv', '�繤����_ȫ������ר��.csv',
                 '���_ȫ������ר��.csv', '����������Ӧ��_ȫ������ר��.csv', '������������������_ȫ������ר��.csv',
                 '��Դ����_ȫ������ר��.csv', '����繤�̵�����������ϵͳ_ȫ������ר��.csv',
                 '����_ȫ������ר��.csv', '�ߵ�ѹ����_ȫ������ר��.csv'
                 ]
    with codecs.open('2011-2016ȫ����Դ��������ר��.csv', 'ab', encoding='gb18030') as merge_file:
        mywriter = csv.writer(merge_file)
        for f in file_list:
            with codecs.open(f, 'rb', encoding='gb18030') as cf:
                myreader = csv.reader(cf)
                mywriter.writerows(myreader)
