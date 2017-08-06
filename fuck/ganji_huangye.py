#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: ganji_huangye.py
@time: 2017/8/16 上午10:37
"""


import lxml.html
import requests


header_cate = {
    'Host': 'sh.ganji.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

header_city = {
    'Host': 'www.ganji.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
}

s = requests.session()


cate_map = {
    # 电脑维修 http://sh.ganji.com/weixiu/
    'diannaoweixiu': '(138)',  # 台式机维修
    'bijiben': '(138)',  # 笔记本维修
    'sujuhuifu': '(183),(138)',  # 数据恢复
    'xianshiqiweixiu': '(138)',  # 电脑显示器维修
    'pingbanweixiu': '(138)',  # ipad/平板电脑维修
    'serverweixiu': '(138)',  # 服务器维修/维护
    'wangluoweixiu': '(138)',  # 网络维修
    'xitonganzhuang': '(138)',  # 系统安装
    'itwaibaowx': '(138)',  # it外包
    'diannaozujianwx': '(138)',  # 电脑组件维修
    'qitaweixiu': '(138)',  # 其他电脑维修

    # 手机维修 http://sh.ganji.com/shumashoujiweixiu/
    # 220 | 手机维修
    # 262 | 影音家电维修
    'shoujiweixiu': '(220)',  # 手机维修
    'pingguoshoujiweixiu': '(220)',  # 苹果
    'sanxingshoujiweixiu': '(220)',  # 三星
    'nuojiyashoujiweixiu': '(220)',  # 诺基亚
    'htcshoujiweixiu': '(220)',  # HTC
    'motuoluolashoujiweixiu': '(220)',  # 摩托罗拉
    'suoaishoujiweixiu': '(220)',  # 索爱
    'heimeishoujiweixiu': '(220)',  # 黑莓
    'lgshoujiweixiu': '(220)',  # LG
    'guochanshoujiweixiu': '(220)',  # 国产
    'xiapushoujwx': '(220)',  # 夏普
    'duopudashoujwx': '(220)',  # 多普达
    'lianxiangshoujwx': '(220)',  # 联想
    'xiaomiweixiu': '(220)',  # 小米
    'meizuweixiu': '(220)',  # 魅族
    'huaweiweixiu': '(220)',  # 华为
    'zteweixiu': '(220)',  # 中兴
    'coolpadweixiu': '(220)',  # 酷派
    'tianyuweixiu': '(220)',  # 天语
    'jinliweixiu': '(220)',  # 金立


    'shumaweixiu': '(262)',  # 数码维修
    'shumaxiangjiwx': '(262)',  # 数码相机维修
    'shexiangjiwx': '(262)',  # 摄像机维修
    'danfanwx': '(262)',  # 单反相机/单反配件维修
    'dandianwx': '(262)',  # 单电/微单相机维修
    'youxijiwx': '(262)',  # 游戏机维修
    'shumaxiangkuangwx': '(262)',  # 数码相框维修
    'qitashumaweixiu': '(262)',  # 其他数码维修

    'zufang': '(224)',  # 房屋租赁
    'fang1': '(224)',  # 房屋租赁

    # 家政
    'yuesao': '(124),(301)',  # 月嫂
    'baomu': '(125),(301)',  # 保姆
    'zhongdiangong': '(126),(301)',  # 钟点工
    'peihugong': '(129),(301)',  # 护工
    'shewaijiazheng': '(128)',  # 涉外家政
    'yuyingshi': '(130)',  # 育婴师/育儿嫂
    'jiazhengcuiru': '(127)',  # 催乳师
    'guanjia': '(301)',  # 管家
    'jujiayanglao': '(129),(301)',  # 居家养老
    'yanglaoyuan': '(129),(301)',  # 养老院
    'jiazhengqita': '(126),(301)',  # 其他家政服务

    # 保洁
    'jiatingbaojie': '(131)',  # 家庭保洁
    'gongchengbaojie': '(132)',  # 公司保洁
    'kaihuangbaojie': '(131),(133)',  # 家庭开荒保洁
    'gongchengkaihuang': '(132),(133)',  # 工程开荒保洁
    'shangchangkaihuang': '(132),(133)',  # 商场开荒保洁
    'changfangkaihuang': '(132),(133)',  # 厂房开荒保洁
    'yiyuankaihuang': '(132),(133)',  # 医院开荒保洁
    'chuchongchuyi': '(134)',  # 除虫除蚁
    'kongqijinghua': '(182)',  # 空气净化
    'shicaifanxin': '(135)',  # 石材翻新>
    'bizhiqingxi': '(135)',  # 壁纸清洗
    'gaokongqingxi': '(136)',  # 高空清洗
    'zhanhuibaojie': '(132)',  # 展会保洁
    'dengjuqingxi': '(137)',  # 灯具清洗
    'qitabaojie': '(131),(132),(200),(296)',  # 其他保洁

    # 搬家
    'zhuzhaibanjia': '(106)',  # 居民搬家
    'jinbeixiaomianbanjia': '(335)',  # 金杯/小面搬家
    'bangongshibanjia': '(107)',  # 办公室搬家
    'qizhongdiaozhuang': '(110)',  # 起重吊装
    'changtubanjia': '(108)',  # 长途搬家
    'shebeibanqian': '(109)',  # 设备搬迁>
    'duantulahuo': '(335)',  # 短途拉货>
    'gangqinbanyun': '(111)',  # 钢琴搬运
    'chaizhuangjiaju': '(114)',  # 家具拆装
    'kongtiaochaizhuang': '(112)',  # 空调移机
    'guojibanjia': '(252)',  # 国际搬家
    'qitabanjia': '(106),(107)',  # 其他搬家

    # 装修
    'jiatingzhuangxiu': '(100),(199),(197),(101)',  # 家庭装修
    'bangongshizhuangxiu': '(192),(193)',  # 办公室装修
    'dianmianzhuangxiu': '(195),(196)',  # 店面装修
    'jubuzhuangxiui': '(193),(197)',  # 局部装修
    'bieshuzhuangxiu': '(191)',  # 别墅装修
    'fangwugaizao': '(104)',  # 房屋改造
    'ershoufangfanxin': '(105)',  # 二手房翻新
    'zhuangshisheji': '(103)',  # 装修设计
    'shangyezhuangxiu': '(195),(102)',  # 商业装修
    'diping': '(198)',  # 地坪
    'qitazhuangxiu': '(103)',  # 其他

    # 家电维修
    'bingxiangweixiu': '(141),(263)',  # 冰箱维修
    'dianshijiweixiu': '(141),(264)',  # 电视机维修
    'kongtiaoyiji': '(141),(294)',  # 空调移机
    'kongtiaoweixiu': '(141),(294)',  # 空调维修
    'kongtiaoqingxi': '(141),(294)',  # 空调清洗
    'xiyijiweixiu': '(265)',  # 洗衣机维修
    'reshuiqiweixiu': '(266)',  # 热水器维修
    'lengku': '(141)',  # 冷库安装/维修
    'yinshuijiweixiu': '(141)',  # 饮水机维修
    'bigualuweixiu': '(141)',  # 壁挂炉维修
    'jingshuijiweixiu': '(141)',  # 净水机维修
    'yinxiangweixiu': '(141),(262)',  # 音响/功放维修
    'diandongcheweixiu': '(141)',  # 电动车维修
    'taiyangnengweixiu': '(141)',  # 太阳能维修
    'xiaojiadianweixiu': '(141)',  # 小家电维修
    'chufangdianqiweixiu': '(141)',  # 厨房电器维修
    'zhongyangkongtiaoweixiu': '(141),(294)',  # 中央空调维修
    'qitajiadianweixiu': '(141)',  # 其他

    # 物流
    'tongchengkuaidi': '(335)',  # 同城快递
    'guoneikuaidi': '(335)',  # 国内快递
    'guojikuaidi': '(335),(252)',  # 国际快递
    'xiaojianwuliu': '(335)',  # 小件物流
    'guoneiwuliu': '(335)',  # 国内物流
    'guojiwuliu': '(335),(252)',  # 国际物流
    'baoguan': '(335)',  # 报关
    'cangchu': '(335)',  # 仓储
    'huowuyunshu': '(335)',  # 货物运输
    'baocheyunshu': '(335)',  # 包车运输
    'huoyundaili': '(335)',  # 货运代理
    'tuoyun': '(335)',  # 托运
    'qitawuliu': '(335)',  # 其他

    # 房屋维修
    'menchuangweixiu': '(143),(309)',  # 门窗维修/安装
    'fangshuibulou': '(310),(185)',  # 防水补漏
    'dianluweixiu': '(143)',  # 电路维修/安装
    'weiyujiejuwx': '(143)',  # 卫浴洁具维修
    'nuanqishuiguanwx': '(310),(185)',  # 暖气水管维修/安装
    'dengjuanzhuangwx': '(143)',  # 灯具维修/安装
    'shuiguanshuilongtouwx': '(310),(185)',  # 水管/水龙头维修
    'fenshuafangfu': '(311)',  # 粉刷/防腐
    'qitajiajuweixiu': '(143)',  # 其他家居维修

}


city_map = {
    'anshan': 2103,  # 鞍山
    'anyang': 4105,  # 安阳
    'anqing': 3408,  # 安庆
    'ankang': 6109,  # 安康
    'akesu': 6529,  # 阿克苏
    'anshun': 5204,  # 安顺
    'aletai': 6543,  # 阿勒泰
    'alashan': 15,  # 阿拉善
    'aba': 5132,  # 阿坝
    'ali': 5425,  # 阿里
    'alaer': 6545,  # 阿拉尔
    'aomen': 82,  # 澳门
    'bj': 11,  # 北京
    'baoding': 1306,  # 保定
    'binzhou': 3716,  # 滨州
    'baotou': 1502,  # 包头
    'baoji': 6103,  # 宝鸡
    'benxi': 2105,  # 本溪
    'bengbu': 3403,  # 蚌埠
    'beihai': 4505,  # 北海
    'bayannaoer': 1508,  # 巴彦淖尔
    'baicheng': 2208,  # 白城
    'baishan': 2206,  # 白山
    'bozhou': 3416,  # 亳州
    'bazhong': 5119,  # 巴中
    'baiyin': 6204,  # 白银
    'baise': 4510,  # 百色
    'bijie': 5224,  # 毕节
    'bayinguoleng': 6528,  # 巴音郭楞
    'baoshan': 5305,  # 保山
    'boertala': 6527,  # 博尔塔拉
    'cd': 5101,  # 成都
    'cq': 50,  # 重庆
    'cs': 4301,  # 长沙
    'cc': 2201,  # 长春
    'changzhou': 3204,  # 常州
    'cangzhou': 1309,  # 沧州
    'chifeng': 1504,  # 赤峰
    'chengde': 1308,  # 承德
    'changde': 4307,  # 常德
    'changzhi': 1404,  # 长治
    'chenzhou': 4310,  # 郴州
    'chuzhou': 3411,  # 滁州
    'chaohu': 3414,  # 巢湖
    'chaozhou': 4451,  # 潮州
    'changji': 6523,  # 昌吉
    'chizhou': 3417,  # 池州
    'chuxiong': 5323,  # 楚雄
    'chongzuo': 4514,  # 崇左
    'changdu': 5421,  # 昌都
    'chaoyang': 2113,  # 朝阳
    'changshu': 3219,  # 常熟
    'cixi': 3302,  # 慈溪
    'dl': 2102,  # 大连
    'dg': 4419,  # 东莞
    'dezhou': 3714,  # 德州
    'dongying': 3705,  # 东营
    'daqing': 2306,  # 大庆
    'datong': 1402,  # 大同
    'dandong': 2106,  # 丹东
    'danzhou': 4605,  # 儋州
    'deyang': 5106,  # 德阳
    'dazhou': 5117,  # 达州
    'dali': 5329,  # 大理
    'daxinganling': 2327,  # 大兴安岭
    'dingxi': 6211,  # 定西
    'dehong': 5331,  # 德宏
    'diqing': 5334,  # 迪庆
    'eerduosi': 1506,  # 鄂尔多斯
    'enshi': 4228,  # 恩施
    'ezhou': 4207,  # 鄂州
    'fz': 3501,  # 福州
    'foshan': 4406,  # 佛山
    'fushun': 2104,  # 抚顺
    'fuyang': 3412,  # 阜阳
    'fuxin': 2109,  # 阜新
    'jxfuzhou': 3610,  # 抚州
    'fangchenggang': 4506,  # 防城港
    'gz': 4401,  # 广州
    'gy': 5201,  # 贵阳
    'gl': 4503,  # 桂林
    'ganzhou': 3607,  # 赣州
    'guangyuan': 5108,  # 广元
    'guangan': 5116,  # 广安
    'guigang': 4508,  # 贵港
    'guyuan': 6404,  # 固原
    'gannan': 6230,  # 甘南
    'ganzi': 5133,  # 甘孜
    'guoluo': 6326,  # 果洛
    'hz': 3301,  # 杭州
    'huizhou': 4413,  # 惠州
    'hrb': 2301,  # 哈尔滨
    'hf': 3401,  # 合肥
    'nmg': 1501,  # 呼和浩特
    'hn': 4601,  # 海口
    'handan': 1304,  # 邯郸
    'heze': 3717,  # 菏泽
    'hengshui': 1311,  # 衡水
    'huaian': 3208,  # 淮安
    'hengyang': 4304,  # 衡阳
    'huludao': 2114,  # 葫芦岛
    'huainan': 3404,  # 淮南
    'hanzhong': 6107,  # 汉中
    'huaihua': 4312,  # 怀化
    'huaibei': 3406,  # 淮北
    'huanggang': 4211,  # 黄冈
    'huzhou': 3305,  # 湖州
    'huangshi': 4202,  # 黄石
    'hulunbeier': 1507,  # 呼伦贝尔
    'heyuan': 4416,  # 河源
    'hebi': 4106,  # 鹤壁
    'hegang': 2304,  # 鹤岗
    'huangshan': 3410,  # 黄山
    'honghe': 53,  # 红河
    'hechi': 4512,  # 河池
    'hami': 6522,  # 哈密
    'heihe': 2311,  # 黑河
    'hezhou': 4511,  # 贺州
    'haixi': 6328,  # 海西
    'hetian': 6532,  # 和田
    'haibei': 6322,  # 海北
    'haidong': 6321,  # 海东
    'huangnan': 6323,  # 黄南
    'jn': 3701,  # 济南
    'jining': 3708,  # 济宁
    'jilin': 22,  # 吉林
    'jinzhou': 2107,  # 锦州
    'jinhua': 3307,  # 金华
    'jiaxing': 3304,  # 嘉兴
    'jiangmen': 4407,  # 江门
    'jingzhou': 4210,  # 荆州
    'jiaozuo': 4108,  # 焦作
    'jinzhong': 1407,  # 晋中
    'jiamusi': 2308,  # 佳木斯
    'jiujiang': 3604,  # 九江
    'jincheng': 1405,  # 晋城
    'jingmen': 4208,  # 荆门
    'jixi': 2303,  # 鸡西
    'jian': 3608,  # 吉安
    'jieyang': 4452,  # 揭阳
    'jingdezhen': 3602,  # 景德镇
    'jiyuan': 4118,  # 济源
    'jiuquan': 6209,  # 酒泉
    'jinchang': 6203,  # 金昌
    'jiayuguan': 6202,  # 嘉峪关
    'jiaozhou': 3702,  # 胶州
    'jimo': 3702,  # 即墨
    'km': 5301,  # 昆明
    'kaifeng': 4102,  # 开封
    'kashi': 6531,  # 喀什
    'kelamayi': 6502,  # 克拉玛依
    'kuerle': 15,  # 库尔勒
    'kezilesu': 15,  # 克孜勒苏
    'kunshan': 3218,  # 昆山
    'lz': 6201,  # 兰州
    'xz': 5401,  # 拉萨
    'langfang': 1310,  # 廊坊
    'linyi': 3713,  # 临沂
    'luoyang': 4103,  # 洛阳
    'liaocheng': 3715,  # 聊城
    'liuzhou': 4502,  # 柳州
    'lianyungang': 3207,  # 连云港
    'linfen': 1410,  # 临汾
    'luohe': 4111,  # 漯河
    'liaoyang': 2110,  # 辽阳
    'leshan': 5111,  # 乐山
    'luzhou': 5105,  # 泸州
    'luan': 3415,  # 六安
    'loudi': 4313,  # 娄底
    'laiwu': 3712,  # 莱芜
    'longyan': 3508,  # 龙岩
    'lvliang': 1411,  # 吕梁
    'lishui': 3311,  # 丽水
    'liangshan': 5134,  # 凉山
    'lijiang': 5307,  # 丽江
    'liupanshui': 5202,  # 六盘水
    'liaoyuan': 2204,  # 辽源
    'laibin': 4513,  # 来宾
    'lincang': 5309,  # 临沧
    'longnan': 6212,  # 陇南
    'linxia': 6229,  # 临夏
    'linzhi': 5426,  # 林芝
    'mianyang': 5107,  # 绵阳
    'mudanjiang': 2310,  # 牡丹江
    'maoming': 4409,  # 茂名
    'meizhou': 4414,  # 梅州
    'maanshan': 3405,  # 马鞍山
    'meishan': 5114,  # 眉山
    'nj': 3201,  # 南京
    'nb': 3302,  # 宁波
    'nn': 4501,  # 南宁
    'nc': 3601,  # 南昌
    'nantong': 3206,  # 南通
    'nanyang': 4113,  # 南阳
    'nanchong': 5113,  # 南充
    'neijiang': 5110,  # 内江
    'nanping': 3507,  # 南平
    'ningde': 3509,  # 宁德
    'nujiang': 5333,  # 怒江
    'naqu': 5424,  # 那曲
    'pingdingshan': 4104,  # 平顶山
    'puyang': 4109,  # 濮阳
    'panjin': 2111,  # 盘锦
    'putian': 3503,  # 莆田
    'panzhihua': 5104,  # 攀枝花
    'pingxiang': 3603,  # 萍乡
    'pingliang': 6208,  # 平凉
    'puer': 5311,  # 普洱
    'pixian': 510112,  # 郫县
    'qd': 3702,  # 青岛
    'qh': 4604,  # 琼海
    'qinhuangdao': 1303,  # 秦皇岛
    'quanzhou': 3505,  # 泉州
    'qiqihaer': 2302,  # 齐齐哈尔
    'qingyuan': 4418,  # 清远
    'qujing': 5303,  # 曲靖
    'quzhou': 3308,  # 衢州
    'qingyang': 6210,  # 庆阳
    'qitaihe': 2309,  # 七台河
    'qinzhou': 4507,  # 钦州
    'qianjiang': 4230,  # 潜江
    'qiandongnan': 5226,  # 黔东南
    'qiannan': 5227,  # 黔南
    'qianxinan': 5223,  # 黔西南
    'rizhao': 3711,  # 日照
    'rikaze': 5423,  # 日喀则
    'sh': 31,  # 上海
    'sz': 4403,  # 深圳
    'sy': 2101,  # 沈阳
    'sjz': 1301,  # 石家庄
    'su': 3205,  # 苏州
    'shantou': 4405,  # 汕头
    'shangqiu': 4114,  # 商丘
    'sanya': 4602,  # 三亚
    'suqian': 3213,  # 宿迁
    'shaoxing': 3306,  # 绍兴
    'shiyan': 4203,  # 十堰
    'siping': 2203,  # 四平
    'sanmenxia': 4112,  # 三门峡
    'shaoyang': 4305,  # 邵阳
    'shangrao': 3611,  # 上饶
    'suining': 5109,  # 遂宁
    'sanming': 3504,  # 三明
    'suihua': 2312,  # 绥化
    'shihezi': 6544,  # 石河子
    'ahsuzhou': 3413,  # 宿州
    'shaoguan': 4402,  # 韶关
    'songyuan': 2207,  # 松原
    'suizhou': 4213,  # 随州
    'shanwei': 4415,  # 汕尾
    'shuangyashan': 2305,  # 双鸭山
    'shuozhou': 1406,  # 朔州
    'shizuishan': 6402,  # 石嘴山
    'shangluo': 6110,  # 商洛
    'shennongjia': 4232,  # 神农架
    'shannan': 5422,  # 山南
    'shuangliu': 5101,  # 双流
    'tj': 12,  # 天津
    'ty': 1401,  # 太原
    'tangshan': 1302,  # 唐山
    'taian': 3709,  # 泰安
    'zjtaizhou': 3310,  # 台州
    'jstaizhou': 3212,  # 泰州
    'tieling': 2112,  # 铁岭
    'tongliao': 1505,  # 通辽
    'tonghua': 2205,  # 通化
    'tianshui': 6205,  # 天水
    'tongling': 3407,  # 铜陵
    'tongchuan': 6102,  # 铜川
    'tongren': 5222,  # 铜仁
    'tianmen': 4231,  # 天门
    'tacheng': 6542,  # 塔城
    'tulufan': 6521,  # 吐鲁番
    'tumushuke': 6546,  # 图木舒克
    'wh': 4201,  # 武汉
    'wx': 3202,  # 无锡
    'xj': 6501,  # 乌鲁木齐
    'wei': 3710,  # 威海
    'weifang': 3707,  # 潍坊
    'wenzhou': 3303,  # 温州
    'wuhu': 3402,  # 芜湖
    'weinan': 6105,  # 渭南
    'wuhai': 1503,  # 乌海
    'wuzhou': 4504,  # 梧州
    'wulanchabu': 1509,  # 乌兰察布
    'wuwei': 6206,  # 武威
    'wenshan': 5326,  # 文山
    'wuzhong': 6403,  # 吴忠
    'wujiaqu': 6547,  # 五家渠
    'wuzhishan': 4603,  # 五指山
    'xa': 6101,  # 西安
    'xm': 3502,  # 厦门
    'xn': 6301,  # 西宁
    'xuzhou': 3203,  # 徐州
    'xianyang': 6104,  # 咸阳
    'xingtai': 1305,  # 邢台
    'xiangyang': 4204,  # 襄阳
    'xinxiang': 4107,  # 新乡
    'xiangtan': 4303,  # 湘潭
    'xuchang': 4110,  # 许昌
    'xinyang': 4115,  # 信阳
    'xiaogan': 4209,  # 孝感
    'xinzhou': 1409,  # 忻州
    'xianning': 4212,  # 咸宁
    'xinyu': 3605,  # 新余
    'xuancheng': 3418,  # 宣城
    'xiantao': 4229,  # 仙桃
    'xilinguole': 15,  # 锡林郭勒
    'xiangxi': 4331,  # 湘西
    'xingan': 4503,  # 兴安
    'xishuangbanna': 5328,  # 西双版纳
    'xianggang': 81,  # 香港
    'yc': 6401,  # 银川
    'yichang': 4205,  # 宜昌
    'yantai': 3706,  # 烟台
    'yangzhou': 3210,  # 扬州
    'yancheng': 3209,  # 盐城
    'yingkou': 2108,  # 营口
    'yueyang': 4306,  # 岳阳
    'yuncheng': 1408,  # 运城
    'sxyulin': 6108,  # 榆林
    'yibin': 5115,  # 宜宾
    'yangquan': 1403,  # 阳泉
    'yanan': 6106,  # 延安
    'yiyang': 4309,  # 益阳
    'yongzhou': 4311,  # 永州
    'gxyulin': 4509,  # 玉林
    'jxyichun': 3609,  # 宜春
    'yangjiang': 4417,  # 阳江
    'yanbian': 2224,  # 延边
    'yuxi': 5304,  # 玉溪
    'yili': 6540,  # 伊犁
    'yunfu': 4453,  # 云浮
    'hljyichun': 2307,  # 伊春
    'yaan': 5118,  # 雅安
    'yingtan': 3606,  # 鹰潭
    'yushu': 6327,  # 玉树
    'yiwu': 3313,  # 义乌
    'zz': 4101,  # 郑州
    'zhuhai': 4404,  # 珠海
    'zibo': 3703,  # 淄博
    'zhongshan': 4420,  # 中山
    'zaozhuang': 3704,  # 枣庄
    'zhangjiakou': 1307,  # 张家口
    'zhuzhou': 4302,  # 株洲
    'zhenjiang': 3211,  # 镇江
    'zhoukou': 4116,  # 周口
    'zhanjiang': 4408,  # 湛江
    'zhumadian': 4117,  # 驻马店
    'zhaoqing': 4412,  # 肇庆
    'zigong': 5103,  # 自贡
    'zunyi': 5203,  # 遵义
    'zhangzhou': 3506,  # 漳州
    'zhoushan': 3309,  # 舟山
    'zhangye': 6207,  # 张掖
    'ziyang': 5120,  # 资阳
    'zhangjiajie': 4308,  # 张家界
    'zhaotong': 5306,  # 昭通
    'zhongwei': 6405,  # 中卫
}


def get_cate():
    """
    获取分类
    :return:
    """
    s.headers = header_cate
    url = 'http://sh.ganji.com/huangye/'
    html = s.get(url).text
    doc = lxml.html.fromstring(html)

    dl = doc.xpath('//div[@class="s-class"]/dl')
    # 形式一
    for item in dl:
        # dt
        cate_code = item.xpath('./dt/a/@href')[0].strip('/')
        cate_name = item.xpath('./dt/a/text()')[0].strip()
        print cate_code, cate_name
        # dd
        dd_list = item.xpath('./dd/a')
        for dd in dd_list:
            cate_code_small = dd.xpath('./@href')[0].strip('/')
            cate_name_small = dd.xpath('./text()')[0].strip('')
            print '\t', cate_code_small, cate_name_small

    # 形式二
    print 'cate_map = ['
    for item in dl:
        # dt
        cate_code = item.xpath('./dt/a/@href')[0].strip('/')
        cate_name = item.xpath('./dt/a/text()')[0].strip()
        print '\t# %s' % cate_name
        print '\t{'
        print '\t\t\'code\': \'%s\',' % cate_code
        print '\t\t\'name\': u\'%s\',' % cate_name
        print '\t\t\'small\': ['
        # dd
        dd_list = item.xpath('./dd/a')
        for dd in dd_list:
            cate_code_small = dd.xpath('./@href')[0].strip('/')
            cate_name_small = dd.xpath('./text()')[0].strip('')
            print '\t\t\t{'
            print '\t\t\t\t\'code\': \'%s\',' % cate_code_small
            print '\t\t\t\t\'name\': u\'%s\',' % cate_name_small
            print '\t\t\t\t\'id\': \'%s\',' % cate_map.get(cate_code_small, '')
            print '\t\t\t},'
        print '\t\t]'
        print '\t},'
    print ']'


def get_area_list(city_code, city_name, province='', district=''):
    """
    获取区域列表
    :param city_code:
    :param city_name:
    :param province:
    :param district:
    :return:
    """
    url = 'http://%s.ganji.com/banjia/' % city_code

    header_area = {
        'Host': '%s.ganji.com' % city_code,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
    }

    s.headers = header_area

    html = s.get(url).text
    doc = lxml.html.fromstring(html)
    link_list = doc.xpath('//dd[@class="posrelative w-area"]/a[contains(@class, "a-area")]')
    area_list = []
    for link_item in link_list:
        city_code_small = link_item.xpath('./@href')[0].strip().split('/')[-2]
        city_name_small = link_item.xpath('./em/text()')[0].strip()
        area_list.append((city_code_small, city_name_small))

    return {
        'city_code': city_code,
        'city_name': city_name,
        'province': province,
        'district': district,
        'area_list': area_list,
    }


def get_city():
    """
    获取城市
    :return:
    """
    s.headers = header_city
    url = 'http://www.ganji.com/index.htm'
    html = s.get(url).text
    doc = lxml.html.fromstring(html)
    dd_list = doc.xpath('//div[@class="all-city"]/dl/dd/a')
    for dd in dd_list:
        city_code = dd.xpath('./@href')[0].replace('http://', '').replace('.ganji.com/', '')
        city_name = dd.xpath('./text()')[0].strip()
        print city_code, city_name


def output_city_area():
    """
    输出城市地区到文件
    :return:
    """
    with open('city_area_gj.py', 'wb') as f:

        f.write("# encoding: utf-8\n\n")

        f.write('city_map = [\n')

        s.headers = header_city
        url = 'http://www.ganji.com/index.htm'
        html = s.get(url).text
        doc = lxml.html.fromstring(html)
        dd_list = doc.xpath('//div[@class="all-city"]/dl/dd/a')
        for dd in dd_list:
            city_code = dd.xpath('./@href')[0].replace('http://', '').replace('.ganji.com/', '')
            city_name = dd.xpath('./text()')[0].strip()
            print city_code, city_name

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


class Main(object):
    def __init__(self):
        pass


if __name__ == '__main__':
    # get_cate()
    # get_city()
    output_city_area()
