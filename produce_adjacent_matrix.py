# -*- coding: cp936 -*-
"""
生成各年的联合专利邻接矩阵
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
INPUT_CSV = u'2007-2016医药卫生行业数据/2007-2016全国医药卫生联合专利.csv'
PREFIX_LABEL = 'AM_医药卫生'

if __name__ == '__main__':
    assert (os.path.exists(INPUT_CSV)), 'Such file \"' + INPUT_CSV + '\" does not exists!'
    for y in YEAR:
        y = str(y)
        my_reader = CsvReader(INPUT_CSV, start_time=y + '-01-01', end_time=y + '-12-31')
        print u'生成' + y + u'年邻接矩阵'
        my_graph_maker = GraphMaker(my_reader.joint_applicant_list())
        my_graph_maker.write_adjacent_matrix(PREFIX_LABEL + '_' + y + '.csv')
