# -*- coding: cp936 -*-
"""
生成各年的联合专利邻接矩阵
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
        print u'生成' + y + u'年邻接矩阵'
        my_reader = CsvReader(u'D:/My Works/于东平2016国家自科/PatentSpider_2.7/全国能源电力行业数据/2007-2010全国能源电力联合专利.csv',
                              start_time=y + '-01-01', end_time=y + '-12-31')
        my_graph_maker = GraphMaker(my_reader.joint_applicant_list())
        my_graph_maker.write_adjacent_matrix('AM_能源电力_' + y + '.csv')
