# -*- coding: cp936 -*-
"""
���ö�cnki�Ĳ�ѯ����
"""
import time

# ʡ����룺������
search = {'GDM': ''}


def __to_utf(string):
    return string.decode('gbk').encode('utf-8')


def __build_query(value):
    par = {'txt_1_relation': '#CNKI_AND', 'txt_1_special1': '='}
    i = 0
    for v in value:
        i = i + 1
        par['txt_%d_sel' % i] = v
        par['txt_%d_value1' % i] = __to_utf(value[v])
        par['txt_%d_relation' % i] = '#CNKI_AND'
        par['txt_%d_special1' % i] = '='
    return par


def make_parameters(patent_code, start_time, end_time):
    parameter = {
        'action': '',
        'NaviCode': patent_code,
        'ua': '1.21',
        'PageName': 'ASP.brief_result_aspx',
        'DbPrefix': 'SCPD',
        'DbCatalog': __to_utf('�й�ר�����ݿ�'),
        'ConfigFile': 'SCPD.xml',
        'db_opt': 'SCPD',
        'db_value': __to_utf('�й�ר�����ݿ�'),
        'publishdate_from': start_time,
        'publishdate_to': end_time,
        'his': '0',
        '__': time.strftime('%a %b %d %Y %H:%M:%S') + ' GMT+0800 (�й���׼ʱ��)',
        # 'recordsperpage':'50',
    }
    parameters = dict(parameter, **__build_query(search))
    return parameters
