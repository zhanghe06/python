# encoding: utf-8
__author__ = 'zhanghe'

import sys
reload(sys)

sys.setdefaultencoding('utf-8')

import requests
import re
import json
import lxml.html
import csv


UserAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'


city_map = {
    'bj': 11,  # 北京
    'sh': 31,  # 上海
    'tj': 12,  # 天津
    'cq': 50,  # 重庆
    'qd': 3702,  # 青岛
    'jn': 3701,  # 济南
    'yt': 3706,  # 烟台
    'wf': 3707,  # 潍坊
    'linyi': 3713,  # 临沂
    'zb': 3703,  # 淄博
    'jining': 3708,  # 济宁
    'ta': 3709,  # 泰安
    'lc': 3715,  # 聊城
    'weihai': 3710,  # 威海
    'zaozhuang': 3704,  # 枣庄
    'dz': 3714,  # 德州
    'rizhao': 3711,  # 日照
    'dy': 3705,  # 东营
    'heze': 3717,  # 菏泽
    'bz': 3716,  # 滨州
    'lw': 3712,  # 莱芜
    'zhangqiu': 3701,  # 章丘
    'kl': 3705,  # 垦利
    'zc': 3707,  # 诸城
    'shouguang': 3707,  # 寿光
    'su': 3205,  # 苏州
    'nj': 3201,  # 南京
    'wx': 3202,  # 无锡
    'cz': 3204,  # 常州
    'xz': 3203,  # 徐州
    'nt': 3206,  # 南通
    'yz': 3210,  # 扬州
    'yancheng': 3209,  # 盐城
    'ha': 3208,  # 淮安
    'lyg': 3207,  # 连云港
    'taizhou': 3212,  # 泰州
    'suqian': 3213,  # 宿迁
    'zj': 3211,  # 镇江
    'shuyang': 3213,  # 沭阳
    'dafeng': 3209,  # 大丰
    'rugao': 3206,  # 如皋
    'qidong': 3206,  # 启东
    'liyang': 3223,  # 溧阳
    'haimen': 3206,  # 海门
    'donghai': 3207,  # 东海
    'yangzhong': 3211,  # 扬中
    'xinghuashi': 3212,  # 兴化
    'xinyishi': 3203,  # 新沂
    'taixing': 3214,  # 泰兴
    'rudong': 3206,  # 如东
    'pizhou': 3203,  # 邳州
    'xzpeixian': 3203,  # 沛县
    'jingjiang': 3216,  # 靖江
    'jianhu': 3209,  # 建湖
    'haian': 3206,  # 海安
    'dongtai': 3209,  # 东台
    'danyang': 3221,  # 丹阳
    'hz': 3301,  # 杭州
    'nb': 3302,  # 宁波
    'wz': 3303,  # 温州
    'jh': 3307,  # 金华
    'jx': 3304,  # 嘉兴
    'tz': 3310,  # 台州
    'sx': 3306,  # 绍兴
    'huzhou': 3305,  # 湖州
    'lishui': 3311,  # 丽水
    'quzhou': 3308,  # 衢州
    'zhoushan': 3309,  # 舟山
    'yueqingcity': 3303,  # 乐清
    'ruiancity': 3303,  # 瑞安
    'yiwu': 3313,  # 义乌
    'yuyao': 3302,  # 余姚
    'zhuji': 3306,  # 诸暨
    'xiangshanxian': 3302,  # 象山
    'wenling': 3310,  # 温岭
    'tongxiang': 3304,  # 桐乡
    'cixi': 3302,  # 慈溪
    'changxing': 3305,  # 长兴
    'jiashanx': 3304,  # 嘉善
    'haining': 3312,  # 海宁
    'deqing': 3305,  # 德清
    'hf': 3401,  # 合肥
    'wuhu': 3402,  # 芜湖
    'bengbu': 3403,  # 蚌埠
    'fy': 3412,  # 阜阳
    'hn': 3404,  # 淮南
    'anqing': 3408,  # 安庆
    'suzhou': 3413,  # 宿州
    'la': 3415,  # 六安
    'huaibei': 3406,  # 淮北
    'chuzhou': 3411,  # 滁州
    'mas': 3405,  # 马鞍山
    'tongling': 3407,  # 铜陵
    'xuancheng': 3418,  # 宣城
    'bozhou': 3416,  # 亳州
    'huangshan': 3410,  # 黄山
    'chizhou': 3417,  # 池州
    'ch': 3414,  # 巢湖
    'hexian': 3405,  # 和县
    'hq': 3415,  # 霍邱
    'tongcheng': 3408,  # 桐城
    'ningguo': 3418,  # 宁国
    'tianchang': 3411,  # 天长
    'sz': 4403,  # 深圳
    'gz': 4401,  # 广州
    'dg': 4419,  # 东莞
    'fs': 4406,  # 佛山
    'zs': 4420,  # 中山
    'zh': 4404,  # 珠海
    'huizhou': 4413,  # 惠州
    'jm': 4407,  # 江门
    'st': 4405,  # 汕头
    'zhanjiang': 4408,  # 湛江
    'zq': 4412,  # 肇庆
    'mm': 4409,  # 茂名
    'jy': 4452,  # 揭阳
    'mz': 4414,  # 梅州
    'qingyuan': 4418,  # 清远
    'yj': 4417,  # 阳江
    'sg': 4402,  # 韶关
    'heyuan': 4416,  # 河源
    'yf': 4453,  # 云浮
    'sw': 4415,  # 汕尾
    'chaozhou': 4451,  # 潮州
    'taishan': 4407,  # 台山
    'yangchun': 4417,  # 阳春
    'sd': 4422,  # 顺德
    'huidong': 4413,  # 惠东
    'boluo': 4413,  # 博罗
    'fz': 3501,  # 福州
    'xm': 3502,  # 厦门
    'qz': 3505,  # 泉州
    'pt': 3503,  # 莆田
    'zhangzhou': 3506,  # 漳州
    'nd': 3509,  # 宁德
    'sm': 3504,  # 三明
    'np': 3507,  # 南平
    'ly': 3508,  # 龙岩
    'wuyishan': 3507,  # 武夷山
    'shishi': 3505,  # 石狮
    'jinjiangshi': 3505,  # 晋江
    'nananshi': 3505,  # 南安
    'nn': 4501,  # 南宁
    'liuzhou': 4502,  # 柳州
    'gl': 4503,  # 桂林
    'yulin': 4509,  # 玉林
    'wuzhou': 4504,  # 梧州
    'bh': 4505,  # 北海
    'gg': 4508,  # 贵港
    'qinzhou': 4507,  # 钦州
    'baise': 4510,  # 百色
    'hc': 4512,  # 河池
    'lb': 4513,  # 来宾
    'hezhou': 4511,  # 贺州
    'fcg': 4506,  # 防城港
    'chongzuo': 4514,  # 崇左
    'haikou': 4601,  # 海口
    'sanya': 4602,  # 三亚
    'wzs': 4603,  # 五指山
    'sansha': 3509,  # 三沙
    'qh': 4604,  # 琼海
    'wenchang': 4606,  # 文昌
    'wanning': 4607,  # 万宁
    'tunchang': 0,  # 屯昌
    'qiongzhong': 0,  # 琼中
    'lingshui': 0,  # 陵水
    'df': 4608,  # 东方
    'da': 0,  # 定安
    'cm': 0,  # 澄迈
    'baoting': 0,  # 保亭
    'baish': 5307,  # 白沙
    'danzhou': 4605,  # 儋州
    'zz': 4101,  # 郑州
    'luoyang': 4103,  # 洛阳
    'xx': 4107,  # 新乡
    'ny': 4113,  # 南阳
    'xc': 4110,  # 许昌
    'pds': 4104,  # 平顶山
    'ay': 4105,  # 安阳
    'jiaozuo': 4108,  # 焦作
    'sq': 4114,  # 商丘
    'kaifeng': 4102,  # 开封
    'puyang': 4109,  # 濮阳
    'zk': 4116,  # 周口
    'xy': 4115,  # 信阳
    'zmd': 4117,  # 驻马店
    'luohe': 4111,  # 漯河
    'smx': 4112,  # 三门峡
    'hb': 4106,  # 鹤壁
    'jiyuan': 4118,  # 济源
    'mg': 4115,  # 明港
    'yanling': 4110,  # 鄢陵
    'yuzhou': 4110,  # 禹州
    'changge': 4110,  # 长葛
    'wh': 4201,  # 武汉
    'yc': 4205,  # 宜昌
    'xf': 4204,  # 襄阳
    'jingzhou': 4210,  # 荆州
    'shiyan': 4203,  # 十堰
    'hshi': 4202,  # 黄石
    'xiaogan': 4209,  # 孝感
    'hg': 4211,  # 黄冈
    'es': 4228,  # 恩施
    'jingmen': 4208,  # 荆门
    'xianning': 4212,  # 咸宁
    'ez': 4207,  # 鄂州
    'suizhou': 4213,  # 随州
    'qianjiang': 4230,  # 潜江
    'tm': 4231,  # 天门
    'xiantao': 4229,  # 仙桃
    'snj': 4232,  # 神农架
    'yidou': 4205,  # 宜都
    'cs': 4301,  # 长沙
    'zhuzhou': 4302,  # 株洲
    'yiyang': 4309,  # 益阳
    'changde': 4307,  # 常德
    'hy': 4304,  # 衡阳
    'xiangtan': 4303,  # 湘潭
    'yy': 4306,  # 岳阳
    'chenzhou': 4310,  # 郴州
    'shaoyang': 4305,  # 邵阳
    'hh': 4312,  # 怀化
    'yongzhou': 4311,  # 永州
    'ld': 4313,  # 娄底
    'xiangxi': 4331,  # 湘西
    'zjj': 4308,  # 张家界
    'nc': 3601,  # 南昌
    'ganzhou': 3607,  # 赣州
    'jj': 3604,  # 九江
    'yichun': 3609,  # 宜春
    'ja': 3608,  # 吉安
    'sr': 3611,  # 上饶
    'px': 3603,  # 萍乡
    'fuzhou': 3610,  # 抚州
    'jdz': 3602,  # 景德镇
    'xinyu': 3605,  # 新余
    'yingtan': 3606,  # 鹰潭
    'yxx': 3608,  # 永新
    'sy': 2101,  # 沈阳
    'dl': 2102,  # 大连
    'as': 2103,  # 鞍山
    'jinzhou': 2107,  # 锦州
    'fushun': 2104,  # 抚顺
    'yk': 2108,  # 营口
    'pj': 2111,  # 盘锦
    'cy': 2113,  # 朝阳
    'dandong': 2106,  # 丹东
    'liaoyang': 2110,  # 辽阳
    'benxi': 2105,  # 本溪
    'hld': 2114,  # 葫芦岛
    'tl': 2112,  # 铁岭
    'fx': 2109,  # 阜新
    'pld': 2102,  # 庄河
    'wfd': 2102,  # 瓦房店
    'hrb': 2301,  # 哈尔滨
    'dq': 2306,  # 大庆
    'qqhr': 2302,  # 齐齐哈尔
    'mdj': 2310,  # 牡丹江
    'suihua': 2312,  # 绥化
    'jms': 2308,  # 佳木斯
    'jixi': 2303,  # 鸡西
    'sys': 2305,  # 双鸭山
    'hegang': 2304,  # 鹤岗
    'heihe': 2311,  # 黑河
    'yich': 2307,  # 伊春
    'qth': 2309,  # 七台河
    'dxal': 2327,  # 大兴安岭
    'cc': 2201,  # 长春
    'jl': 22,  # 吉林
    'sp': 2203,  # 四平
    'yanbian': 2224,  # 延边
    'songyuan': 2207,  # 松原
    'bc': 2208,  # 白城
    'th': 2205,  # 通化
    'baishan': 2206,  # 白山
    'liaoyuan': 2204,  # 辽源
    'cd': 5101,  # 成都
    'mianyang': 5107,  # 绵阳
    'deyang': 5106,  # 德阳
    'nanchong': 5113,  # 南充
    'yb': 5115,  # 宜宾
    'zg': 5103,  # 自贡
    'ls': 5111,  # 乐山
    'luzhou': 5105,  # 泸州
    'dazhou': 5117,  # 达州
    'scnj': 5110,  # 内江
    'suining': 5109,  # 遂宁
    'panzhihua': 5104,  # 攀枝花
    'ms': 5114,  # 眉山
    'ga': 5116,  # 广安
    'zy': 5120,  # 资阳
    'liangshan': 5134,  # 凉山
    'guangyuan': 5108,  # 广元
    'ya': 5118,  # 雅安
    'bazhong': 5119,  # 巴中
    'ab': 5132,  # 阿坝
    'ganzi': 5133,  # 甘孜
    'km': 5301,  # 昆明
    'qj': 5303,  # 曲靖
    'dali': 5329,  # 大理
    'honghe': 5325,  # 红河
    'yx': 5304,  # 玉溪
    'lj': 5307,  # 丽江
    'ws': 5326,  # 文山
    'cx': 5323,  # 楚雄
    'bn': 5328,  # 西双版纳
    'zt': 5306,  # 昭通
    'dh': 5331,  # 德宏
    'pe': 5311,  # 普洱
    'bs': 5305,  # 保山
    'lincang': 5309,  # 临沧
    'diqing': 5334,  # 迪庆
    'nujiang': 5333,  # 怒江
    'gy': 5201,  # 贵阳
    'zunyi': 5203,  # 遵义
    'qdn': 5226,  # 黔东南
    'qn': 5227,  # 黔南
    'lps': 5202,  # 六盘水
    'bijie': 5224,  # 毕节
    'tr': 5222,  # 铜仁
    'anshun': 5204,  # 安顺
    'qxn': 5223,  # 黔西南
    'lasa': 5401,  # 拉萨
    'rkz': 5423,  # 日喀则
    'sn': 5422,  # 山南
    'linzhi': 5426,  # 林芝
    'changdu': 5421,  # 昌都
    'nq': 5424,  # 那曲
    'al': 5425,  # 阿里
    'rituxian': 5425,  # 日土
    'gaizexian': 5425,  # 改则
    'sjz': 1301,  # 石家庄
    'bd': 1306,  # 保定
    'ts': 1302,  # 唐山
    'lf': 1310,  # 廊坊
    'hd': 1304,  # 邯郸
    'qhd': 1303,  # 秦皇岛
    'cangzhou': 1309,  # 沧州
    'xt': 1305,  # 邢台
    'hs': 1311,  # 衡水
    'zjk': 1307,  # 张家口
    'chengde': 1308,  # 承德
    'dingzhou': 1306,  # 定州
    'gt': 1304,  # 馆陶
    'zhangbei': 1307,  # 张北
    'zx': 1301,  # 赵县
    'zd': 1301,  # 正定
    'ty': 1401,  # 太原
    'linfen': 1410,  # 临汾
    'dt': 1402,  # 大同
    'yuncheng': 1408,  # 运城
    'jz': 1407,  # 晋中
    'changzhi': 1404,  # 长治
    'jincheng': 1405,  # 晋城
    'yq': 1403,  # 阳泉
    'lvliang': 1411,  # 吕梁
    'xinzhou': 1409,  # 忻州
    'shuozhou': 1406,  # 朔州
    'linyixian': 1408,  # 临猗
    'qingxu': 1401,  # 清徐
    'hu': 1501,  # 呼和浩特
    'bt': 1502,  # 包头
    'chifeng': 1504,  # 赤峰
    'erds': 1506,  # 鄂尔多斯
    'tongliao': 1505,  # 通辽
    'hlbe': 1507,  # 呼伦贝尔
    'bycem': 1508,  # 巴彦淖尔市
    'wlcb': 1509,  # 乌兰察布
    'xl': 1525,  # 锡林郭勒
    'xam': 1522,  # 兴安盟
    'wuhai': 1503,  # 乌海
    'alsm': 1529,  # 阿拉善盟
    'hlr': 1507,  # 海拉尔
    'xa': 6101,  # 西安
    'xianyang': 6104,  # 咸阳
    'baoji': 6103,  # 宝鸡
    'wn': 6105,  # 渭南
    'hanzhong': 6107,  # 汉中
    'yl': 6108,  # 榆林
    'yanan': 6106,  # 延安
    'ankang': 6109,  # 安康
    'sl': 6110,  # 商洛
    'tc': 6102,  # 铜川
    'xj': 6501,  # 乌鲁木齐
    'changji': 6523,  # 昌吉
    'bygl': 6528,  # 巴音郭楞
    'yili': 6540,  # 伊犁
    'aks': 6529,  # 阿克苏
    'ks': 6531,  # 喀什
    'hami': 6522,  # 哈密
    'klmy': 6502,  # 克拉玛依
    'betl': 6527,  # 博尔塔拉
    'tlf': 6521,  # 吐鲁番
    'ht': 6532,  # 和田
    'shz': 6544,  # 石河子
    'kzls': 6530,  # 克孜勒苏
    'ale': 6545,  # 阿拉尔
    'wjq': 6547,  # 五家渠
    'tmsk': 6546,  # 图木舒克
    'kel': 6528,  # 库尔勒
    'alt': 6543,  # 阿勒泰
    'tac': 6542,  # 塔城
    'lz': 6201,  # 兰州
    'tianshui': 6205,  # 天水
    'by': 6204,  # 白银
    'qingyang': 6210,  # 庆阳
    'pl': 6208,  # 平凉
    'jq': 6209,  # 酒泉
    'zhangye': 6207,  # 张掖
    'wuwei': 6206,  # 武威
    'dx': 6211,  # 定西
    'jinchang': 6203,  # 金昌
    'ln': 6212,  # 陇南
    'linxia': 6229,  # 临夏
    'jyg': 6202,  # 嘉峪关
    'gn': 6230,  # 甘南
    'yinchuan': 6401,  # 银川
    'wuzhong': 6403,  # 吴忠
    'szs': 6402,  # 石嘴山
    'zw': 6405,  # 中卫
    'guyuan': 6404,  # 固原
    'xn': 6301,  # 西宁
    'hx': 6328,  # 海西
    'haibei': 6322,  # 海北
    'guoluo': 6326,  # 果洛
    'haidong': 6321,  # 海东
    'huangnan': 6323,  # 黄南
    'ys': 6327,  # 玉树
    'hainan': 46,  # 海南
    'hk': 81,  # 香港
    'am': 82,  # 澳门
    'tw': 71,  # 台湾
    'quanguo': 0,  # 全国
    'cn': 0,  # 其他
}


def get_city_list():
    """
    获取城市列表
    """
    # 入口页的url
    url = 'http://www.58.com/changecity.aspx'
    header = {
        'Host': 'www.58.com',
        'Referer': 'http://www.58.com/',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    rule = '<a href="http://(.*?).58.com/" onclick="co\(\'.*?\'\)">(.*?)</a>'
    city_list = re.compile(rule, re.S).findall(html)
    city = {}
    for item in city_list:
        city[item[0]] = item[1]
    print json.dumps(city, indent=4).decode('raw_unicode_escape')


def parse_city_list():
    """
    解析城市列表(去除海外城市)
    """
    # 入口页的url
    url = 'http://www.58.com/changecity.aspx'
    header = {
        'Host': 'www.58.com',
        'Referer': 'http://www.58.com/',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)

    # 省份
    province_list = doc.xpath('//dl[@id="clist"]//dt[not(@class)]/text()')[:-1]
    # for i in province_list:
    #     print i

    # 城市
    city_rule = '<a href="http://(.*?).58.com/" onclick="co\(\'.*?\'\)">(.*?)</a>'
    city_list = doc.xpath('//dl[@id="clist"]//dd[not(@class)]')[:-1]

    result = []
    for index, city_item in enumerate(city_list):
        city_link_list = city_item.xpath('./a')
        for city_link in city_link_list:
            city_link_html = lxml.html.tostring(city_link, encoding='utf-8')
            city_result = re.compile(city_rule, re.S).findall(city_link_html)
            print city_result[0][0], city_result[0][1], province_list[index]
            result.append([city_result[0][0], city_result[0][1], province_list[index]])

    # 校验省份城市数量
    # print len(province_list), len(city_list)

    return result


def get_cate_list_shenghuo():
    """
    获取分类列表
    """
    # 入口页的url
    url = 'http://sh.58.com/shenghuo.shtml'  # 家政服务

    header = {
        'Host': 'sh.58.com',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)

    cate_list = doc.xpath('//div[@class="sublist"]//dl[@class="catecss-item"]')

    cate_title_rule = '<dt><a href="http://sh.58.com/(.*?)(.shtml|/)" target="_blank".*?>(.*?)</a>'
    cate_item_rule = '<a href="http://sh.58.com/(.*?)/" target="_blank".*?>(.*?)</a>'

    for i in cate_list:
        cate_title_html = lxml.html.tostring(i.xpath('./dt')[0], encoding='utf-8')
        cate_item_html = lxml.html.tostring(i.xpath('./dd')[0], encoding='utf-8')
        # 标题
        cate_title_result = re.compile(cate_title_rule, re.S).findall(cate_title_html)
        for cate_title_list in cate_title_result:
            print '#', '#', cate_title_list[0], cate_title_list[2]

        # 明细
        cate_item_result = re.compile(cate_item_rule, re.S).findall(cate_item_html)
        cate = {}
        for cate_item_list in cate_item_result:
            cate[cate_item_list[0]] = cate_item_list[1].strip()
            print cate_item_list[0], cate_item_list[1].strip()
        # print json.dumps(cate, indent=4).decode('raw_unicode_escape')


def get_cate_list_zhuangxiujc():
    """
    获取分类列表
    """
    # 入口页的url
    # url = 'http://sh.58.com/hunjiehunqing.shtml'  # 婚庆摄影
    url = 'http://sh.58.com/zhuangxiujc.shtml'  # 装修建材

    header = {
        'Host': 'sh.58.com',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)

    cate_title_list = doc.xpath('//div[@class="banner-cont"]/div[@class="sidebar"]/ul/li//a')
    cate_list = doc.xpath('//div[@class="banner-cont"]/div[@class="sublist"]/div[@class="catecss"]')

    cate_title_rule = '<a href="http://sh.58.com/(.*?)" target="_blank".*?>(.*?)</a>'
    cate_item_rule = '<a href="http://sh.58.com/(.*?)/" target="_blank".*?>(.*?)</a>'

    # 标题
    title_list = []
    for i in cate_title_list:
        cate_title_html = lxml.html.tostring(i, encoding='utf-8')
        cate_title_result = re.compile(cate_title_rule, re.S).findall(cate_title_html)
        for cate_title_list in cate_title_result:
            # print '#', '#', cate_title_list[0], cate_title_list[1]
            title_list.append([cate_title_list[0], cate_title_list[1]])
    # 明细
    for i, m in enumerate(cate_list[:len(title_list)]):
        # 输出标题
        print '#', '#', title_list[i][0], title_list[i][1]
        for n in m.xpath('./a'):
            cate_item_html = lxml.html.tostring(n, encoding='utf-8')
            cate_item_result = re.compile(cate_item_rule, re.S).findall(cate_item_html)
            cate = {}
            # 输出明细
            for cate_item_list in cate_item_result:
                cate[cate_item_list[0]] = cate_item_list[1].strip()
                print cate_item_list[0], cate_item_list[1].strip()


def get_cate_list_shangwu():
    """
    获取分类列表
    """
    # 入口页的url
    url = 'http://sh.58.com/shangwu.shtml'  # 商务服务
    # url = 'http://sh.58.com/lvyouxiuxian.shtml'  # 旅游酒店
    # url = 'http://sh.58.com/zhaoshang.shtml'  # 招商加盟
    # url = 'http://sh.58.com/xiuxianyl.shtml'  # 休闲娱乐

    header = {
        'Host': 'sh.58.com',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)

    cate_list = doc.xpath('//div[@class="sublist"]//div[@class="catecss"]/dl')

    cate_title_rule = '<a href="http://sh.58.com/(.*?)(.shtml|/)" target="_blank".*?>(.*?)</a>'
    cate_item_rule = '<a href="http://sh.58.com/(.*?)/" target="_blank".*?>(.*?)</a>'

    for i in cate_list:
        cate_title_html = lxml.html.tostring(i.xpath('./dt/a')[0], encoding='utf-8')
        cate_item_html = lxml.html.tostring(i.xpath('./dd')[0], encoding='utf-8')
        # 标题
        cate_title_result = re.compile(cate_title_rule, re.S).findall(cate_title_html)
        for cate_title_list in cate_title_result:
            print '#', '#', cate_title_list[0], cate_title_list[2]

        # 明细
        cate_item_result = re.compile(cate_item_rule, re.S).findall(cate_item_html)
        cate = {}
        for cate_item_list in cate_item_result:
            cate[cate_item_list[0]] = cate_item_list[1].strip()
            print cate_item_list[0], cate_item_list[1].strip()


def get_contacts():
    """
    获取联系方式
    :return:
    """
    url = 'http://sh.58.com/hyjk/listAjaxApi/'
    header = {
        'Host': 'sh.58.com',
        'Referer': 'http://sh.58.com/',
        'User-Agent': UserAgent,
        'X-Requested-With': 'XMLHttpRequest'
    }
    s_ajax_param = 's_contact_baojie_196139473193474552186077834_'
    param = '25953277422517_38982245142801_0_adsumplayinfo_8DAA63759947EF47858F8EA3AD3D3F1D'
    form_data = {
        'ajax_param': s_ajax_param + param,
        'lmcate': ''
    }
    response = requests.post(url, data=form_data, headers=header)

    print json.dumps(response.json(), indent=4, ensure_ascii=False)


def get_promotion_info():
    """
    获取会员推广信息
    :return:
    """
    url = 'http://sh.58.com/hyjk/listAjaxApi/'
    header = {
        'Host': 'sh.58.com',
        'Referer': 'http://sh.58.com/',
        'User-Agent': UserAgent,
        'X-Requested-With': 'XMLHttpRequest'
    }
    ajax_param = '{"platform":"pc","infoMethod":["renzheng","wltAge"],"dataParam":"27635365552076_42349714013201_0_adinfo,23978226171963_30110967056649_0_promationinfo,27228545116992_7715319655942_0_promationinfo,24267133521976_31011764_0_promationinfo,26341531878841_39825442758928_0_promationinfo,27537787529538_42349714013201_0_promationinfo,27369765592510_31131127077388_0_promationinfo,26203081582670_39732159639312_0_promationinfo,26852770947242_36265725460496_0_promationinfo,27227627875130_36460206072079_0_promationinfo,26919564208079_34723293059851_0_promationinfo,27297229859020_41908793267472_0_promationinfo,25970724472781_39209928147477_0_promationinfo,9709048675466_2881415678214_0_promationinfo,25526822994222_28276516466439_0_promationinfo,23733432686387_34539145627401_0_promationinfo,23746434952376_34806212995846_0_promationinfo,26428537311295_40089453348885_0_promationinfo,21175695050380_28305155861767_0_promationinfo,25897156976720_38365916388886_0_promationinfo,26760665594574_40165314644754_0_promationinfo,26671643928779_31928151670537_0_promationinfo,25743851768512_38681202520851_0_promationinfo,27374487786958_42065473327117_0_promationinfo,27094804372404_23677654908934_0_promationinfo,26576085167292_40404568069136_0_promationinfo,27646817870019_958976883975_0_promationinfo,26499543940540_40264006853649_0_promationinfo,18697452964869_24568846015751_0_promationinfo,26240781793081_39741342008592_0_promationinfo,27235189567049_41775030971412_0_promationinfo,25847911701436_28254579084295_0_promationinfo,26742286458571_40728598353936_0_promationinfo,27518150853831_42307833403927_0_promationinfo,19997647110789_27265893924870_0_promationinfo,22826141761824_17067318798087_0_promationinfo","dispCateId":168,"dispCateName":"baojie","pageIndex":8,"paramMap":null}'
    form_data = {
        'ajax_param': ajax_param,
        'lmcate': ''
    }
    response = requests.post(url, data=form_data, headers=header)

    print json.dumps(response.json(), indent=4, ensure_ascii=False)


def get_area_list(city_code, city_name, province='', district=''):
    """
    获取区域列表
    :param city_code:
    :param city_name:
    :param province:
    :param district:
    :return:
    """
    url = 'http://%s.58.com/banjia/' % city_code

    header = {
        'Host': '%s.58.com' % city_code,
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//dd[@id="local"]/a')
    link_rule = u'<a href="/(.*?)/banjia/">(.*?)</a>'
    area_list = []
    # print "# %s" % city_name
    # print "'%s': [" % city_code
    # for i, link in enumerate(link_list):
    #     link_html = lxml.html.tostring(link, encoding='utf-8').strip()
    #     link_result = re.compile(link_rule, re.S).findall(link_html.decode('utf-8'))
    #     for v in link_result:
    #         area_list.append((v[0], v[1]))
    #         print "\t'%s'%s  # %s" % (v[0], ',' if (i + 1) < len(link_list) else '', v[1])
    # print "]"

    print '{'
    print '\t\'code\': \'%s\',' % city_code
    print '\t\'name\': u\'%s\',' % city_name
    print '\t\'small\': ['

    for i, link in enumerate(link_list):
        link_html = lxml.html.tostring(link, encoding='utf-8').strip()
        link_result = re.compile(link_rule, re.S).findall(link_html.decode('utf-8'))
        if not link_result:
            continue
        print '\t\t{'
        for v in link_result:
            area_list.append((v[0], v[1]))
            print '\t\t\t\'code\': \'%s\'' % v[0]
            print '\t\t\t\'name\': u\'%s\'' % v[1]
            print '\t\t\t\'id\': \'\''
        print '\t\t},'
    print '\t]'
    print '},'

    return {
        'city_code': city_code,
        'city_name': city_name,
        'province': province,
        'district': district,
        'area_list': area_list,
    }


def print_city_area():
    """
    打印城市地区
    :return:
    """
    city_list = parse_city_list()
    for city_code, city_name, province_name in city_list:
        get_area_list(city_code, city_name)


def get_cate_list(cate_code, cate_name):
    """
    获取分类列表
    :param cate_code:
    :param cate_name:
    :return:
    """
    url = 'http://sh.58.com/%s/' % cate_code

    header = {
        'Host': 'sh.58.com',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//dd[@id="ObjectType" or @id="objecttype"]/a')
    # link_rule = u'<a href="/(.*?)">(.*?)</a>'
    link_rule = u'<a href="http://sh.58.com/(.*?)/">(.*?)</a>'
    area_list = []
    print "# %s" % cate_name
    print "'%s': [" % cate_code
    for i, link in enumerate(link_list):
        link_html = lxml.html.tostring(link, encoding='utf-8').strip()
        # print link_html
        link_result = re.compile(link_rule, re.S).findall(link_html.decode('utf-8'))
        for v in link_result:
            area_list.append((v[0], v[1]))
            print "\t'%s'%s  # %s" % (v[0], ',' if (i + 1) < len(link_list) else '', v[1])
    print "]"


def read_csv(csv_file_path):
    """
    读取csv文件
    :param csv_file_path:
    :return:
    """
    with open(csv_file_path, 'rb') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print json.dumps(row, ensure_ascii=False)
            yield row


def write_csv(csv_file_path, rows):
    """
    写入csv文件
    :param csv_file_path:
    :param rows:
    :return:
    """
    with open(csv_file_path, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in rows:
            csv_writer.writerow(row)


def output_city_area():
    """
    输出城市地区到文件
    :return:
    """
    with open('city_area2.py', 'wb') as f:
        rows = read_csv('city_map_58.csv')
        f.write("# encoding: utf-8\n\n")
        # f.write("area = {\n")
        # for row in rows:
        #     city_code = row['city_code']
        #     city_name = row['city_name']
        #     province = row['province']
        #     district = row['district']
        #     city_info = get_area_list(city_code, city_name, province, district)
        #     f.write("    # %s %s %s\n" % (city_name, province, district))
        #     f.write("    '%s': [\n" % city_code)
        #     for area in city_info['area_list']:
        #         f.write("        '%s',  # %s\n" % (area[0], area[1]))
        #     f.write("    ],\n")
        #     f.flush()
        # f.write("}\n")
        f.write('city_map = [\n')
        for row in rows:
            city_code = row['city_code']
            city_name = row['city_name']
            province = row['province']
            district = row['district']
            city_info = get_area_list(city_code, city_name, province, district)
            city_id = city_map.get(city_code)
            f.write('\t# %s %s %s\n' % (city_name, province, district))
            f.write('\t{\n')
            f.write('\t\t\'code\': \'%s\',\n' % city_code)
            f.write('\t\t\'name\': u\'%s\',\n' % city_name)
            f.write('\t\t\'id\': %s,\n' % city_id)
            f.write('\t\t\'small\': [\n')

            for area in city_info['area_list']:
                f.write('\t\t\t{\n')
                f.write('\t\t\t\t\'code\': \'%s\',\n' % area[0])
                f.write('\t\t\t\t\'name\': u\'%s\',\n' % area[1])
                f.write('\t\t\t\t\'id\': %s\n' % city_id)
                f.write('\t\t\t},\n')
            f.write('\t\t]\n')
            f.write('\t},\n')
            f.flush()
        f.write(']')


if __name__ == '__main__':
    # get_city_list()
    # parse_city_list()
    # get_cate_list_shenghuo()
    # get_cate_list_zhuangxiujc()
    # get_cate_list_shangwu()
    # get_contacts()
    # get_promotion_info()
    # print get_area_list('sh', u'上海')
    # print_city_area()
    # read_csv('city_map_58.csv')
    # write_csv('test.csv', [['一', '二', '三'], [1, 2, 3], [5, 6, 7]])
    output_city_area()
    # get_cate_list('caishui', u'-')
