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
    def is_satisfied_filter(applicant_str, keyword_list=list()):
        applicant_str = str(applicant_str)
        # ��������ר�����򷵻�False
        if applicant_str.find(';') == -1:
            return False
        # ������ȫ�Ǹ��ˣ��򷵻�False
        if all([len(applicant) < 12 for applicant in applicant_str.split(';')]):
            return False
        # δ�����ؼ��ʣ��򷵻�False
        if all([applicant_str.find(k) == -1 for k in keyword_list]) and len(keyword_list) != 0:
            return False
        return True


    DIR_STR = '.'
    FILE_LIST = [
        '��ҽѧ.csv', '��ҩѧ.csv', '����ҽ���.csv', '�ٴ�ҽѧ.csv', 'ҽҩ�������������뷨�ɷ����о�.csv',
        '��ǻ��ѧ.csv', '����ϵͳ����.csv', '����ҽѧ.csv', '���ѧ.csv', '������ѧ.csv',
        '��Ѫ��ϵͳ����.csv', '����ҽѧ.csv', '�����ѧ.csv', '����ϵͳ����.csv', '����ҽѧ.csv',
        '����ҽѧ����.csv', 'Ƥ�������Բ�.csv', '�ۿ�������ʺ��.csv', '����ѧ.csv', 'ҩѧ.csv',
        'Ԥ��ҽѧ������ѧ.csv',
    ]
    YUNNAN_TOKEN_LIST = [
        '����', '����', '�ʹ�', '����', '�廪', '�ٶ�', '��ɽ', '����', '����', '����', '����', '����', '����',
        'ʯ��', '»Ȱ', 'Ѱ��', '����', '����', '����', 'մ��', '��Դ', '��ƽ', 'ʦ��', '½��', '����', '��Ϫ',
        '����', '����', '�ν�', 'ͨ��', '����', '����', '��ɽ', '��ƽ', 'Ԫ��', '��ɽ', '¡��', 'ʩ��', '�ڳ�',
        '����', '����', '��ͨ', '����', '³��', '�ɼ�', '�ν�', '���', '����', '�罭', '����', '����', '����',
        'ˮ��', '����', '��ʤ', '��ƺ', '����', '����', '�ն�', '˼é', '����', 'ī��', '����', '����', '����',
        '����', '����', '����', '����', '�ٲ�', '����', '����', '����', '��', '˫��', '����', '��Դ', '�º�',
        '����', '����', 'ӯ��', '¤��', 'ŭ��', '����', '��ɽ', '��ƺ', '����', '����', 'ά��', '����', '����',
        '����', '�ֶ�', '��ƽ', '����', '��Դ', '����', '����', '���', '�Ͻ�', 'Ρɽ', '����', '˫��', 'Ĳ��',
        '�ϻ�', 'Ҧ��', '��Ҧ', '����', 'Ԫı', '�䶨', '»��', '���', '����', '��Զ', '�̴�', '��ˮ', 'ʯ��',
        '����', '����', 'Ԫ��', '��ƽ', '�ӿ�', '����', '��ɽ', '��ɽ', '����', '���', '��', '����', '����',
        '������', '��˫����', '�º�', '����',
    ]

    assert (os.path.exists(DIR_STR)), 'Such directory \"' + DIR_STR + '\" does not exists!'
    os.chdir(DIR_STR)
    for f in FILE_LIST:
        if not os.path.exists(f):
            print str(f) + ' doesn\'t exist!'
            continue
        print 'Filtering ' + f.decode('gbk') + ' ...'
        with codecs.open(f, 'rb', encoding='gb18030') as read_file:
            my_reader = csv.reader(read_file)
            with codecs.open(f.replace('.csv', '_����ר��.csv'), 'ab', encoding='gb18030') as write_file:
                my_writer = csv.writer(write_file)
                for line in my_reader:
                    if is_satisfied_filter(str(line[3])):
                        my_writer.writerow(line)
                        # continue
    for f in os.listdir(os.getcwd()):
        if os.path.isdir(f):
            continue
        if os.path.getsize(f) == 0:
            try:
                os.remove(f)
            except:
                print f + ' :Error!'
