# -*- coding: cp936 -*-
"""
���ɸ��������ר���ڽӾ���
"""
import os
import sys

from csv_reader import CsvReader
from graph_maker import GraphMaker

default_encoding = "utf-8"
if default_encoding != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding(default_encoding)

YEAR = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
INPUT_CSV = u'2007-2016ҽҩ������ҵ����/2007-2016ȫ��ҽҩ��������ר��.csv'
PREFIX_LABEL = 'AM_ҽҩ����'

if __name__ == '__main__':
    assert (os.path.exists(INPUT_CSV)), 'Such file \"' + INPUT_CSV + '\" does not exists!'
    for y in YEAR:
        y = str(y)
        my_reader = CsvReader(INPUT_CSV, start_time=y + '-01-01', end_time=y + '-12-31')
        print u'����' + y + u'���ڽӾ���'
        my_graph_maker = GraphMaker(my_reader.joint_applicant_list())
        my_graph_maker.write_adjacent_matrix(PREFIX_LABEL + '_' + y + '.csv')
