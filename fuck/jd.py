# encoding: utf-8
__author__ = 'zhanghe'



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