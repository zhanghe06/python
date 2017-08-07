#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: liebiao.py
@time: 2017/8/23 上午10:34
"""


import lxml.html
import requests


header_cate = {
    'Host': 'shanghai.liebiao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

header_city = {
    'Host': 'www.liebiao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

s = requests.session()


city_map = {
    'anshan': 2103,  # 鞍山
    'anyang': 4105,  # 安阳
    'anshun': 5204,  # 安顺
    'anqing': 3408,  # 安庆
    'ankang': 6109,  # 安康
    'ali': 5425,  # 阿里
    'aletai': 6543,  # 阿勒泰
    'alashan': 1529,  # 阿拉善
    'alaer': 6545,  # 阿拉尔
    'akesu': 6529,  # 阿克苏
    'aba': 5132,  # 阿坝
    'beijing': 11,  # 北京
    'baoding': 1306,  # 保定
    'baotou': 1502,  # 包头
    'binzhou': 3716,  # 滨州
    'baicheng': 2208,  # 白城
    'bengbu': 3403,  # 蚌埠
    'benxi': 2105,  # 本溪
    'bijie': 5224,  # 毕节
    'boertala': 6527,  # 博尔塔拉
    'beihai': 4505,  # 北海
    'bazhong': 5119,  # 巴中
    'bayinguoleng': 6528,  # 巴音郭楞
    'bayannaoer': 1508,  # 巴彦淖尔
    'baoshan': 5305,  # 保山
    'baoji': 6103,  # 宝鸡
    'baiyin': 6204,  # 白银
    'baishan': 2206,  # 白山
    'baise': 4510,  # 百色
    'bozhou': 3416,  # 亳州
    'baisha': 43,  # 白沙
    'baoting': 6325,  # 保亭
    'chongqing': 50,  # 重庆
    'chengdu': 5101,  # 成都
    'changchun': 2201,  # 长春
    'changsha': 4301,  # 长沙
    'changzhou': 3204,  # 常州
    'cangzhou': 1309,  # 沧州
    'changde': 4307,  # 常德
    'chuxiong': 5323,  # 楚雄
    'chongzuo': 4514,  # 崇左
    'changdu': 5421,  # 昌都
    'chaozhou': 4451,  # 潮州
    'chenzhou': 4310,  # 郴州
    'chizhou': 3417,  # 池州
    'chaohu': 3414,  # 巢湖
    'chuzhou': 3411,  # 滁州
    'chaoyang': 2113,  # 朝阳
    'chifeng': 1504,  # 赤峰
    'changzhi': 1404,  # 长治
    'chengde': 1308,  # 承德
    'changji': 6523,  # 昌吉
    'changjiang': 6325,  # 昌江
    'chengmai': 6325,  # 澄迈
    'dalian': 2102,  # 大连
    'daqing': 2306,  # 大庆
    'dongguan': 4419,  # 东莞
    'dongying': 3705,  # 东营
    'dezhou': 3714,  # 德州
    'diqing': 5334,  # 迪庆
    'dehong': 5331,  # 德宏
    'dali': 5329,  # 大理
    'dazhou': 5117,  # 达州
    'deyang': 5106,  # 德阳
    'datong': 1402,  # 大同
    'daxinganling': 2327,  # 大兴安岭
    'dandong': 2106,  # 丹东
    'dingxi': 6211,  # 定西
    'danzhou': 4605,  # 儋州
    'dongfang': 4608,  # 东方
    'dingan': 6325,  # 定安
    'eerduosi': 1506,  # 鄂尔多斯
    'enshi': 4228,  # 恩施
    'ezhou': 4207,  # 鄂州
    'fuzhou': 3501,  # 福州
    'foshan': 4406,  # 佛山
    'fangchenggang': 4506,  # 防城港
    'fushun': 2104,  # 抚顺
    'fuxin': 2109,  # 阜新
    'fuyang': 3412,  # 阜阳
    'fz': 3610,  # 抚州
    'guangzhou': 4401,  # 广州
    'guiyang': 5201,  # 贵阳
    'guilin': 4503,  # 桂林
    'guoluo': 6326,  # 果洛
    'guigang': 4508,  # 贵港
    'gannan': 6230,  # 甘南
    'guangyuan': 5108,  # 广元
    'guangan': 5116,  # 广安
    'ganzi': 5133,  # 甘孜
    'ganzhou': 3607,  # 赣州
    'guyuan': 6404,  # 固原
    'hangzhou': 3301,  # 杭州
    'haerbin': 2301,  # 哈尔滨
    'hefei': 3401,  # 合肥
    'haikou': 4601,  # 海口
    'handan': 1304,  # 邯郸
    'huizhou': 4413,  # 惠州
    'huhehaote': 1501,  # 呼和浩特
    'huzhou': 3305,  # 湖州
    'hengyang': 4304,  # 衡阳
    'huaian': 3208,  # 淮安
    'hengshui': 1311,  # 衡水
    'hezhou': 4511,  # 贺州
    'heyuan': 4416,  # 河源
    'hechi': 4512,  # 河池
    'honghe': 53,  # 红河
    'hanzhong': 6107,  # 汉中
    'haidong': 6321,  # 海东
    'haibei': 6322,  # 海北
    'huangnan': 6323,  # 黄南
    'hami': 6522,  # 哈密
    'haixi': 6328,  # 海西
    'huaihua': 4312,  # 怀化
    'hulunbeier': 1507,  # 呼伦贝尔
    'huludao': 2114,  # 葫芦岛
    'hegang': 2304,  # 鹤岗
    'heihe': 2311,  # 黑河
    'huainan': 3404,  # 淮南
    'huaibei': 3406,  # 淮北
    'huangshan': 3410,  # 黄山
    'heze': 3717,  # 菏泽
    'hebi': 4106,  # 鹤壁
    'huangshi': 4202,  # 黄石
    'huanggang': 4211,  # 黄冈
    'hetian': 6532,  # 和田
    'jinan': 3701,  # 济南
    'jining': 3708,  # 济宁
    'jiaxing': 3304,  # 嘉兴
    'jinhua': 3307,  # 金华
    'jiangmen': 4407,  # 江门
    'jilin': 22,  # 吉林
    'jieyang': 4452,  # 揭阳
    'jinchang': 6203,  # 金昌
    'jingzhou': 4210,  # 荆州
    'jingmen': 4208,  # 荆门
    'jiyuan': 4118,  # 济源
    'jiaozuo': 4108,  # 焦作
    'jiayuguan': 6202,  # 嘉峪关
    'jincheng': 1405,  # 晋城
    'jian': 3608,  # 吉安
    'jiujiang': 3604,  # 九江
    'jingdezhen': 3602,  # 景德镇
    'jiamusi': 2308,  # 佳木斯
    'jixi': 2303,  # 鸡西
    'jinzhou': 2107,  # 锦州
    'jinzhong': 1407,  # 晋中
    'jiuquan': 6209,  # 酒泉
    'kunming': 5301,  # 昆明
    'kaifeng': 4102,  # 开封
    'kashi': 6531,  # 喀什
    'kelamayi': 6502,  # 克拉玛依
    'kezilesu': 65,  # 克孜勒苏
    'lanzhou': 6201,  # 兰州
    'lasa': 5401,  # 拉萨
    'linyi': 3713,  # 临沂
    'luoyang': 4103,  # 洛阳
    'langfang': 1310,  # 廊坊
    'liaocheng': 3715,  # 聊城
    'luzhou': 5105,  # 泸州
    'leshan': 5111,  # 乐山
    'liangshan': 5134,  # 凉山
    'liupanshui': 5202,  # 六盘水
    'lijiang': 5307,  # 丽江
    'lincang': 5309,  # 临沧
    'linzhi': 5426,  # 林芝
    'longnan': 6212,  # 陇南
    'laibin': 4513,  # 来宾
    'liuzhou': 4502,  # 柳州
    'loudi': 4313,  # 娄底
    'linfen': 1410,  # 临汾
    'lvliang': 1411,  # 吕梁
    'liaoyang': 2110,  # 辽阳
    'liaoyuan': 2204,  # 辽源
    'lianyungang': 3207,  # 连云港
    'lishui': 3311,  # 丽水
    'luan': 3415,  # 六安
    'longyan': 3508,  # 龙岩
    'laiwu': 3712,  # 莱芜
    'luohe': 4111,  # 漯河
    'linxia': 6229,  # 临夏
    'ledong': 6325,  # 乐东
    'lingao': 6325,  # 临高
    'lingshui': 6325,  # 陵水
    'maoming': 4409,  # 茂名
    'mianyang': 5107,  # 绵阳
    'maanshan': 3405,  # 马鞍山
    'meishan': 5114,  # 眉山
    'meizhou': 4414,  # 梅州
    'mudanjiang': 2310,  # 牡丹江
    'nanjing': 3201,  # 南京
    'nanning': 4501,  # 南宁
    'ningbo': 3302,  # 宁波
    'nantong': 3206,  # 南通
    'nanyang': 4113,  # 南阳
    'nanchang': 3601,  # 南昌
    'nanping': 3507,  # 南平
    'naqu': 5424,  # 那曲
    'neijiang': 5110,  # 内江
    'nanchong': 5113,  # 南充
    'ningde': 3509,  # 宁德
    'nujiang': 5333,  # 怒江
    'pingdingshan': 4104,  # 平顶山
    'panjin': 2111,  # 盘锦
    'panzhihua': 5104,  # 攀枝花
    'pingliang': 6208,  # 平凉
    'pingxiang': 3603,  # 萍乡
    'puer': 5311,  # 普洱
    'putian': 3503,  # 莆田
    'puyang': 4109,  # 濮阳
    'qingdao': 3702,  # 青岛
    'quanzhou': 3505,  # 泉州
    'qinhuangdao': 1303,  # 秦皇岛
    'qujing': 5303,  # 曲靖
    'qitaihe': 2309,  # 七台河
    'qiqihaer': 2302,  # 齐齐哈尔
    'qionghai': 4604,  # 琼海
    'qinzhou': 4507,  # 钦州
    'qiandongnan': 5226,  # 黔东南
    'qingyuan': 4418,  # 清远
    'qingyang': 6210,  # 庆阳
    'qianxinan': 5223,  # 黔西南
    'qiannan': 5227,  # 黔南
    'qianjiang': 4230,  # 潜江
    'quzhou': 3308,  # 衢州
    'qiongzhong': 6325,  # 琼中
    'rikaze': 5423,  # 日喀则
    'rizhao': 3711,  # 日照
    'shanghai': 31,  # 上海
    'suzhou': 3205,  # 苏州
    'shenyang': 2101,  # 沈阳
    'shijiazhuang': 1301,  # 石家庄
    'shenzhen': 4403,  # 深圳
    'shaoxing': 3306,  # 绍兴
    'shantou': 4405,  # 汕头
    'shangqiu': 4114,  # 商丘
    'suihua': 2312,  # 绥化
    'shaoguan': 4402,  # 韶关
    'siping': 2203,  # 四平
    'shuozhou': 1406,  # 朔州
    'shanwei': 4415,  # 汕尾
    'sanya': 4602,  # 三亚
    'suining': 5109,  # 遂宁
    'shannan': 5422,  # 山南
    'shangluo': 6110,  # 商洛
    'shizuishan': 6402,  # 石嘴山
    'shaoyang': 4305,  # 邵阳
    'shennongjia': 4232,  # 神农架
    'suqian': 3213,  # 宿迁
    'shuangyashan': 2305,  # 双鸭山
    'suzh': 3413,  # 宿州
    'sanming': 3504,  # 三明
    'shangrao': 3611,  # 上饶
    'sanmenxia': 4112,  # 三门峡
    'songyuan': 2207,  # 松原
    'shiyan': 4203,  # 十堰
    'suizhou': 4213,  # 随州
    'shihezi': 6544,  # 石河子
    'sansha': 6325,  # 三沙
    'tianjin': 12,  # 天津
    'taiyuan': 1401,  # 太原
    'tangshan': 1302,  # 唐山
    'taizhou': 3310,  # 台州
    'taian': 3709,  # 泰安
    'taizh': 3212,  # 泰州
    'tongling': 3407,  # 铜陵
    'tongren': 5222,  # 铜仁
    'tulufan': 6521,  # 吐鲁番
    'tacheng': 6542,  # 塔城
    'tongliao': 1505,  # 通辽
    'tonghua': 2205,  # 通化
    'tongchuan': 6102,  # 铜川
    'tieling': 2112,  # 铁岭
    'tianshui': 6205,  # 天水
    'tianmen': 4231,  # 天门
    'tumushuke': 6546,  # 图木舒克
    'tunchang': 6325,  # 屯昌
    'wuhan': 4201,  # 武汉
    'wulumuqi': 6501,  # 乌鲁木齐
    'wenzhou': 3303,  # 温州
    'wuxi': 3202,  # 无锡
    'weihai': 3710,  # 威海
    'weifang': 3707,  # 潍坊
    'wulanchabu': 1509,  # 乌兰察布
    'wuwei': 6206,  # 武威
    'wuzhong': 6403,  # 吴忠
    'wujiaqu': 6547,  # 五家渠
    'wuhu': 3402,  # 芜湖
    'wanning': 4607,  # 万宁
    'wuhai': 1503,  # 乌海
    'wenshan': 5326,  # 文山
    'wenchang': 4606,  # 文昌
    'weinan': 6105,  # 渭南
    'wuzhou': 4504,  # 梧州
    'wuzhishan': 4603,  # 五指山
    'xian': 6101,  # 西安
    'xiamen': 3502,  # 厦门
    'xuzhou': 3203,  # 徐州
    'xingtai': 1305,  # 邢台
    'xiangfan': 4206,  # 襄樊
    'xuchang': 4110,  # 许昌
    'xinxiang': 4107,  # 新乡
    'xishuangbanna': 5328,  # 西双版纳
    'xiangxi': 4331,  # 湘西
    'xianyang': 6104,  # 咸阳
    'xiangtan': 4303,  # 湘潭
    'xiantao': 4229,  # 仙桃
    'xianning': 4212,  # 咸宁
    'xiaogan': 4209,  # 孝感
    'xinyang': 4115,  # 信阳
    'xinyu': 3605,  # 新余
    'xuancheng': 3418,  # 宣城
    'xilinguole': 15,  # 锡林郭勒
    'xingan': 15,  # 兴安
    'xinzhou': 1409,  # 忻州
    'xining': 6301,  # 西宁
    'yinchuan': 6401,  # 银川
    'yantai': 3706,  # 烟台
    'yancheng': 3209,  # 盐城
    'yangzhou': 3210,  # 扬州
    'yueyang': 4306,  # 岳阳
    'yichang': 4205,  # 宜昌
    'yangquan': 1403,  # 阳泉
    'yulin': 4509,  # 玉林
    'yibin': 5115,  # 宜宾
    'yaan': 5118,  # 雅安
    'yuxi': 5304,  # 玉溪
    'yanan': 6106,  # 延安
    'yul': 6108,  # 榆林
    'yushu': 6327,  # 玉树
    'yunfu': 4453,  # 云浮
    'yangjiang': 4417,  # 阳江
    'yuncheng': 1408,  # 运城
    'yingkou': 2108,  # 营口
    'yanbian': 2224,  # 延边
    'yichun': 2307,  # 伊春
    'yingtan': 3606,  # 鹰潭
    'yich': 3609,  # 宜春
    'yiyang': 4309,  # 益阳
    'yongzhou': 4311,  # 永州
    'yili': 6540,  # 伊犁
    'yangpu': 6325,  # 洋浦
    'zhengzhou': 4101,  # 郑州
    'zhuhai': 4404,  # 珠海
    'zibo': 3703,  # 淄博
    'zhenjiang': 3211,  # 镇江
    'zhangzhou': 3506,  # 漳州
    'zhongshan': 4420,  # 中山
    'zhanjiang': 4408,  # 湛江
    'zhaoqing': 4412,  # 肇庆
    'zhoukou': 4116,  # 周口
    'zaozhuang': 3704,  # 枣庄
    'zhumadian': 4117,  # 驻马店
    'zunyi': 5203,  # 遵义
    'zhaotong': 5306,  # 昭通
    'zhangjiakou': 1307,  # 张家口
    'zhangye': 6207,  # 张掖
    'ziyang': 5120,  # 资阳
    'zigong': 5103,  # 自贡
    'zhangjiajie': 4308,  # 张家界
    'zhuzhou': 4302,  # 株洲
    'zhoushan': 3309,  # 舟山
    'zhongwei': 6405,  # 中卫
}


def get_cate():
    """
    获取分类
    :return:
    """
    s.headers = header_cate
    url = 'http://shanghai.liebiao.com/shenghuo/'
    html = s.get(url).text
    doc = lxml.html.fromstring(html)

    dl = doc.xpath('//div[@class="hover-div"]//tr')
    # 形式一
    # for item in dl:
    #     # dt
    #     cate_code = item.xpath('./th/a/@href')[0].strip('/')
    #     cate_name = item.xpath('./th/a/text()')[0].strip()
    #     print cate_code, cate_name
    #     # dd
    #     dd_list = item.xpath('./td/a')
    #     for dd in dd_list:
    #         cate_code_small = dd.xpath('./@href')[0].strip('/')
    #         cate_name_small = dd.xpath('./text()')[0].strip('')
    #         print '\t', cate_code_small, cate_name_small

    # 形式二
    print 'cate_map = ['
    for item in dl:
        # dt
        cate_code = item.xpath('./th/a/@href')[0].strip('/')
        cate_name = item.xpath('./th/a/text()')[0].strip()
        print '\t# %s' % cate_name
        print '\t{'
        print '\t\t\'code\': \'%s\',' % cate_code
        print '\t\t\'name\': u\'%s\',' % cate_name
        print '\t\t\'small\': ['
        # dd
        dd_list = item.xpath('./td/a')
        for dd in dd_list:
            cate_code_small = dd.xpath('./@href')[0].strip('/')
            cate_name_small = dd.xpath('./text()')[0].strip('')
            print '\t\t\t{'
            print '\t\t\t\t\'code\': \'%s\',' % cate_code_small
            print '\t\t\t\t\'name\': u\'%s\',' % cate_name_small
            # print '\t\t\t\t\'id\': \'%s\',' % cate_map_v4.get(cate_code_small, '')
            print '\t\t\t\t\'id\': \'\','
            print '\t\t\t},'
        print '\t\t]'
        print '\t},'
    print ']'


def get_city():
    """
    获取城市
    :return:
    """
    s.headers = header_city
    url = 'http://www.liebiao.com/'
    html = s.get(url).text
    doc = lxml.html.fromstring(html)
    dd_list = doc.xpath('//div[@class="box w_d"]/dl/dd/a')
    for dd in dd_list:
        city_code = dd.xpath('./@href')[0].replace('http://', '').replace('.liebiao.com/', '')
        city_name = dd.xpath('./text()')[0].strip()
        print city_code, city_name
        yield city_code, city_name


def get_area_list(city_code, city_name, province='', district=''):
    """
    获取区域列表
    :param city_code:
    :param city_name:
    :param province:
    :param district:
    :return:
    """
    url = 'http://%s.liebiao.com/yuesao/' % city_code

    header_area = {
        'Host': '%s.liebiao.com' % city_code,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
    }

    s.headers = header_area

    html = s.get(url).text
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//div[@class="cond-con"]/dl[2]/dd/a[not(@class="current")]')
    area_list = []
    for link_item in link_list:
        city_code_small = link_item.xpath('./@href')[0].strip().split('/')[-3]
        city_name_small = link_item.xpath('./text()')[0].strip()
        area_list.append((city_code_small, city_name_small))
    print area_list

    return {
        'city_code': city_code,
        'city_name': city_name,
        'province': province,
        'district': district,
        'area_list': area_list,
    }


def output_city_area():
    """
    输出城市地区到文件
    :return:
    """
    with open('city_area_lb.py', 'wb') as f:

        f.write("# encoding: utf-8\n\n")

        f.write('city_map = [\n')

        for city_code, city_name in get_city():

            city_info = get_area_list(city_code, city_name)
            city_id = city_map.get(city_code)
            f.write('\t# %s\n' % city_name.encode('utf-8'))
            f.write('\t{\n')
            f.write('\t\t\'code\': \'%s\',\n' % city_code)
            f.write('\t\t\'name\': u\'%s\',\n' % city_name.encode('utf-8'))
            f.write('\t\t\'id\': %s,\n' % city_id)
            f.write('\t\t\'small\': [\n')
            for area in city_info['area_list']:
                f.write('\t\t\t{\n')
                f.write('\t\t\t\t\'code\': \'%s\',\n' % area[0])
                f.write('\t\t\t\t\'name\': u\'%s\',\n' % area[1].encode('utf-8'))
                f.write('\t\t\t\t\'id\': %s\n' % city_id)
                f.write('\t\t\t},\n')
            f.write('\t\t]\n')
            f.write('\t},\n')
            f.flush()
        f.write(']')


if __name__ == '__main__':
    # get_cate()
    # get_city()
    # get_area_list('shanghai', '上海')
    output_city_area()
