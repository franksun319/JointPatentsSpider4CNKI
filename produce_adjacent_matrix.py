# -*- coding: cp936 -*-
"""
���ɸ��������ר���ڽӾ���
"""
import sys

from csv_reader import CsvReader
from graph_maker import GraphMaker

default_encoding = "utf-8"
if default_encoding != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding(default_encoding)

if __name__ == '__main__':
    # year = ['2011', '2012', '2013', '2014', '2015', '2016']
    year = ['2007', '2008', '2009', '2010']
    for y in year:
        print u'����' + y + u'���ڽӾ���'
        my_reader = CsvReader(u'D:/My Works/�ڶ�ƽ2016�����Կ�/PatentSpider_2.7/ȫ����Դ������ҵ����/2007-2010ȫ����Դ��������ר��.csv',
                              start_time=y + '-01-01', end_time=y + '-12-31')
        my_graph_maker = GraphMaker(my_reader.joint_applicant_list())
        my_graph_maker.write_adjacent_matrix('AM_��Դ����_' + y + '.csv')
