# encoding: utf-8
__author__ = 'zhanghe'

import requests
import time
import json


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    }


ID = '1152617826'
url_p = 'http://item.jd.com/'+ID+'.html'
s = requests.session()


def get_price():
    """
    获取简单的价格信息
    """
    url = 'http://p.3.cn/prices/get'
    payload = {
        'skuid': 'J_'+ID,
        # 'type': '1',
        # 'area': '2_2820_2879',  # 区域，会影响到现货数量
        # 'callback': 'cnp',
    }
    header['Host'] = 'p.3.cn'
    header['Referer'] = 'http://item.jd.com/'+ID+'.html'
    response = s.get(url, params=payload, headers=header)
    print response.url
    print response.text
    # http://p.3.cn/prices/get?skuid=J_1152617826
    # [{"id":"J_1152617826","p":"9.90","m":"15.00"}]


def get_detail():
    """
    获取商品详细信息
    """
    url = 'http://d.jd.com/fittingInfo/get'
    payload = {
        'callback': 'jQuery9305912',
        'skuId': ID,
        '_': time.time()
    }
    header['Host'] = 'd.jd.com'
    header['Referer'] = 'http://item.jd.com/'+ID+'.html'
    response = s.get(url, params=payload, headers=header)
    content = response.text.lstrip('jQuery9305912(').rstrip(')')
    print response.url
    print json.dumps(json.loads(content), indent=4, ensure_ascii=False)
    # http://d.jd.com/fittingInfo/get?callback=jQuery9305912&_=1438014651.47&skuId=1152617826
    # {
    #     "fittings": [],
    #     "master": {
    #         "sort": 12239,
    #         "skuid": "1152617826",
    #         "name": "富爸爸韩国泡菜韩式五福腌渍菜150g袋装正宗韩国",
    #         "price": "9.90",
    #         "pic": "jfs/t148/132/858922143/236699/5f23e1ed/539ab9d3Nf5ccab7f.jpg",
    #         "discount": "0.00"
    #     },
    #     "fittingType": []
    # }


if __name__ == '__main__':
    get_price()
    get_detail()


"""
京东商城数据抓取
http://item.jd.com/1605859857.html

http://p.3.cn/prices/get?skuid=J_1605859857&type=1&area=1_72_2799&callback=cnp
GET

skuid:J_1605859857  # 这个参数必须，后面3个可以不要
type:1
area:1_72_2799  # 这个貌似固定
callback:cnp

cnp([{"id":"J_1605859857","p":"28.00","m":"56.00"}]);


http://d.jd.com/fittingInfo/get?callback=jQuery1159693&skuId=1605859857&_=1437490190965
GET
callback:jQuery1159693
skuId:1605859857
_:1437490190965

jQuery1159693({"master":{"name":"\u97e9\u548f2015\u60c5\u4fa3\u94a5\u5319\u6263\u97e9\u56fd\u521b\u610f\u5408\u91d1\u5de5\u827a\u60c5\u4fa3\u94a5\u5319\u6302\u4ef6\uff08\u8d60\u54c1 \u5355\u4e2a\uff09 \u5e78\u798f \u5355\u4e2a","price":"28.00","discount":"0.00","pic":"jfs/t1666/122/241299161/270356/6e8d1ca7/558391fcNc9843bb8.jpg","skuid":"1605859857","sort":9719},"fittings":[],"fittingType":[]})


图片
http://img12.360buyimg.com/n0/

http://img12.360buyimg.com/n0/jfs/t787/251/1187768978/279676/f17318b0/558391fdN02c5a1cd.jpg
http://img12.360buyimg.com/n0/jfs/t1666/122/241299161/270356/6e8d1ca7/558391fcNc9843bb8.jpg






"""