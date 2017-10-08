# -*- coding: cp936 -*-
import codecs
import csv
import sys

from csv_reader import CsvReader

default_encoding = "utf-8"
if default_encoding != sys.getdefaultencoding():
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class GraphMaker:
    def __init__(self, llist=None):
        if llist is None:
            llist = []
        self.__llist = llist
        self.label_dict = {}
        self.__make_node_label()
        self.adjacent_matrix = []
        self.__init_adjacent_matrix()
        self.__make_adjacent_matrix()

    def __make_node_label(self):
        if not self.__llist:
            self.label_dict = {}
            return
        for ll in self.__llist:
            for each in ll:
                if each not in self.label_dict:
                    self.label_dict[each] = 0
        no = 0
        for key in self.label_dict:
            self.label_dict[key] = no
            no += 1

    def __make_adjacent_matrix(self):
        if self.__llist == [] or self.label_dict == {}:
            self.adjacent_matrix = []
            return
        # llist的每一行
        for row in self.__llist:
            # row中的每一个元素
            for i in range(len(row)):
                # row的第i个元素之后的每个元素
                for j in range(i + 1, len(row)):
                    self.adjacent_matrix[self.label_dict.get(row[i])][self.label_dict.get(row[j])] = 1
                    self.adjacent_matrix[self.label_dict.get(row[j])][self.label_dict.get(row[i])] = 1

    def __init_adjacent_matrix(self):
        for i in range(len(self.label_dict)):
            row_list = []
            for j in range(len(self.label_dict)):
                row_list.append(0)
            self.adjacent_matrix.append(row_list)

    def write_adjacent_matrix(self, output_file='adjacent_matrix.csv'):
        if self.__llist == [] and self.label_dict == {}:
            print 'No nodes, edges as well as networks!'
            exit(-1)
        with codecs.open(output_file, 'wb', encoding='gb18030') as cf:
            my_writer = csv.writer(cf)
            # 写标题行
            row = self.label_dict.values()
            row.insert(0, '')
            my_writer.writerow(row)
            # 写每条记录[no, 记录]
            for no in self.label_dict.values():
                row = list(self.adjacent_matrix[no])
                row.insert(0, no)
                my_writer.writerow(row)
        # 为方便R-igraph程序运行，将组织名以代码替代
        with codecs.open(str(output_file.split('.')[0]) + '_名单.csv', 'wb', encoding='gb18030') as nl:
            my_writer = csv.writer(nl)
            for label, no in self.label_dict.items():
                my_writer.writerow([no, label])


if __name__ == '__main__':
    r = CsvReader(u'D:/My Works/于东平2016国家自科/PatentSpider_2.7/输配电工程电力网及电力系统_云南联合专利.csv')
    ll = r.joint_applicant_list()
    for e in ll:
        print ','.join(e)
    gm = GraphMaker(ll)
    gm.write_adjacent_matrix('test.csv')
    # print gm.adjacent_matrix
