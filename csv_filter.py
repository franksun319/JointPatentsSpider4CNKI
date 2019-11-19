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
        # 不是联合专利，则返回False
        if applicant_str.find(';') == -1:
            return False
        # 申请人全是个人，则返回False
        if all([len(applicant) < 12 for applicant in applicant_str.split(';')]):
            return False
        # 未包含关键词，则返回False
        if all([applicant_str.find(k) == -1 for k in keyword_list]) and len(keyword_list) != 0:
            return False
        return True


    DIR_STR = '.'
    FILE_LIST = [
        '中医学.csv', '中药学.csv', '中西医结合.csv', '临床医学.csv', '医药卫生方针政策与法律法规研究.csv',
        '口腔科学.csv', '呼吸系统疾病.csv', '基础医学.csv', '外科学.csv', '妇产科学.csv',
        '心血管系统疾病.csv', '急救医学.csv', '泌尿科学.csv', '消化系统疾病.csv', '特种医学.csv',
        '生物医学工程.csv', '皮肤病与性病.csv', '眼科与耳鼻咽喉科.csv', '肿瘤学.csv', '药学.csv',
        '预防医学与卫生学.csv',
    ]
    YUNNAN_TOKEN_LIST = [
        '云南', '昆明', '呈贡', '盘龙', '五华', '官渡', '西山', '东川', '安宁', '晋宁', '富民', '宜良', '嵩明',
        '石林', '禄劝', '寻甸', '曲靖', '宣威', '马龙', '沾益', '富源', '罗平', '师宗', '陆良', '会泽', '玉溪',
        '红塔', '江川', '澄江', '通海', '华宁', '易门', '峨山', '新平', '元江', '保山', '隆阳', '施甸', '腾冲',
        '龙陵', '昌宁', '昭通', '昭阳', '鲁甸', '巧家', '盐津', '大关', '永善', '绥江', '镇雄', '彝良', '威信',
        '水富', '丽江', '永胜', '华坪', '玉龙', '宁蒗', '普洱', '思茅', '宁洱', '墨江', '景东', '景谷', '镇沅',
        '江城', '孟连', '澜沧', '西盟', '临沧', '临翔', '凤庆', '永德', '镇康', '双江', '耿马', '沧源', '德宏',
        '瑞丽', '梁河', '盈江', '陇川', '怒江', '福贡', '贡山', '兰坪', '迪庆', '德钦', '维西', '大理', '祥云',
        '宾川', '弥渡', '永平', '云龙', '洱源', '剑川', '鹤庆', '漾濞', '南涧', '巍山', '楚雄', '双柏', '牟定',
        '南华', '姚安', '大姚', '永仁', '元谋', '武定', '禄丰', '红河', '个旧', '开远', '绿春', '建水', '石屏',
        '弥勒', '泸西', '元阳', '金平', '河口', '屏边', '文山', '砚山', '西畴', '马关', '丘北', '广南', '富宁',
        '麻栗坡', '西双版纳', '勐海', '勐腊',
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
            with codecs.open(f.replace('.csv', '_联合专利.csv'), 'ab', encoding='gb18030') as write_file:
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
