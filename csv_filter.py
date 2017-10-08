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
    file_list = ['���緢�糧.csv', '��ѹ�������������������任��.csv', '������.csv', '̫����.csv',
                 'ˮ������_ˮ��վ����.csv', '����.csv', '�繤��������.csv', '�繤����.csv', '���.csv',
                 '����������Ӧ��.csv', '������������������.csv', '��Դ����.csv',
                 '����繤�̵�����������ϵͳ.csv', '����.csv', '�ߵ�ѹ����.csv']
    yunnan_tokens = ['����', '����', '�ʹ�', '����', '�廪', '�ٶ�', '��ɽ', '����', '����', '����', '����',
                     '����', '����', 'ʯ��', '»Ȱ', 'Ѱ��', '����', '����', '����', 'մ��', '��Դ', '��ƽ',
                     'ʦ��', '½��', '����', '��Ϫ', '����', '����', '�ν�', 'ͨ��', '����', '����', '��ɽ',
                     '��ƽ', 'Ԫ��', '��ɽ', '¡��', 'ʩ��', '�ڳ�', '����', '����', '��ͨ', '����', '³��',
                     '�ɼ�', '�ν�', '���', '����', '�罭', '����', '����', '����', 'ˮ��', '����', '��ʤ',
                     '��ƺ', '����', '����', '�ն�', '˼é', '����', 'ī��', '����', '����', '����', '����',
                     '����', '����', '����', '�ٲ�', '����', '����', '����', '��', '˫��', '����', '��Դ',
                     '�º�', '����', '����', 'ӯ��', '¤��', 'ŭ��', '����', '��ɽ', '��ƺ', '����', '����',
                     'ά��', '����', '����', '����', '�ֶ�', '��ƽ', '����', '��Դ', '����', '����', '���',
                     '�Ͻ�', 'Ρɽ', '����', '˫��', 'Ĳ��', '�ϻ�', 'Ҧ��', '��Ҧ', '����', 'Ԫı', '�䶨',
                     '»��', '���', '����', '��Զ', '�̴�', '��ˮ', 'ʯ��', '����', '����', 'Ԫ��', '��ƽ',
                     '�ӿ�', '����', '��ɽ', '��ɽ', '����', '������', '���', '��', '����', '����',
                     '��˫����', '�º�', '����']


    def applicant_filter(applicant_str):
        applicant_str = str(applicant_str)
        # �Ƿ�����ר��
        if applicant_str.find(';') == -1:
            return False
        # �������Ƿ�ȫ�Ǹ���
        if all([len(applicant) < 12 for applicant in applicant_str.split(';')]):
            return False
        # �������Ƿ���������
        # if all([applicant_str.find(t.decode('gbk')) == -1 for t in geographical_name]):
        #     return False
        return True


    os.chdir('ȫ����Դ������ҵ����/2011-2016ȫ��ר��')
    for f in file_list:
        print 'Filtering ' + f.decode('gbk') + ' ...'
        with codecs.open(f, 'rb', encoding='gb18030') as read_file:
            my_reader = csv.reader(read_file)
            with codecs.open(f.replace('.csv', '_ȫ������ר��.csv'), 'ab', encoding='gb18030') as write_file:
                my_writer = csv.writer(write_file)
                for line in my_reader:
                    if applicant_filter(str(line[3])):
                        my_writer.writerow(line)
                        # continue
    for f in os.listdir(os.getcwd()):
        if os.path.getsize(f) == 0:
            try:
                os.remove(f)
            except:
                print 'Error!'
