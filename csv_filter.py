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
    file_list = ['发电发电厂.csv', '变压器变流器及其它电力变换器.csv', '地热能.csv', '太阳能.csv',
                 '水能利用_水电站工程.csv', '电器.csv', '电工基础理论.csv', '电工材料.csv', '电机.csv',
                 '电气化电能应用.csv', '电气测量技术及仪器.csv', '电源技术.csv',
                 '输配电工程电力网及电力系统.csv', '风能.csv', '高电压技术.csv']
    yunnan_tokens = ['云南', '昆明', '呈贡', '盘龙', '五华', '官渡', '西山', '东川', '安宁', '晋宁', '富民',
                     '宜良', '嵩明', '石林', '禄劝', '寻甸', '曲靖', '宣威', '马龙', '沾益', '富源', '罗平',
                     '师宗', '陆良', '会泽', '玉溪', '红塔', '江川', '澄江', '通海', '华宁', '易门', '峨山',
                     '新平', '元江', '保山', '隆阳', '施甸', '腾冲', '龙陵', '昌宁', '昭通', '昭阳', '鲁甸',
                     '巧家', '盐津', '大关', '永善', '绥江', '镇雄', '彝良', '威信', '水富', '丽江', '永胜',
                     '华坪', '玉龙', '宁蒗', '普洱', '思茅', '宁洱', '墨江', '景东', '景谷', '镇沅', '江城',
                     '孟连', '澜沧', '西盟', '临沧', '临翔', '凤庆', '永德', '镇康', '双江', '耿马', '沧源',
                     '德宏', '瑞丽', '梁河', '盈江', '陇川', '怒江', '福贡', '贡山', '兰坪', '迪庆', '德钦',
                     '维西', '大理', '祥云', '宾川', '弥渡', '永平', '云龙', '洱源', '剑川', '鹤庆', '漾濞',
                     '南涧', '巍山', '楚雄', '双柏', '牟定', '南华', '姚安', '大姚', '永仁', '元谋', '武定',
                     '禄丰', '红河', '个旧', '开远', '绿春', '建水', '石屏', '弥勒', '泸西', '元阳', '金平',
                     '河口', '屏边', '文山', '砚山', '西畴', '麻栗坡', '马关', '丘北', '广南', '富宁',
                     '西双版纳', '勐海', '勐腊']


    def applicant_filter(applicant_str):
        applicant_str = str(applicant_str)
        # 是否联合专利
        if applicant_str.find(';') == -1:
            return False
        # 申请人是否全是个人
        if all([len(applicant) < 12 for applicant in applicant_str.split(';')]):
            return False
        # 申请人是否来自云南
        # if all([applicant_str.find(t.decode('gbk')) == -1 for t in geographical_name]):
        #     return False
        return True


    os.chdir('全国能源电力行业数据/2011-2016全部专利')
    for f in file_list:
        print 'Filtering ' + f.decode('gbk') + ' ...'
        with codecs.open(f, 'rb', encoding='gb18030') as read_file:
            my_reader = csv.reader(read_file)
            with codecs.open(f.replace('.csv', '_全国联合专利.csv'), 'ab', encoding='gb18030') as write_file:
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
