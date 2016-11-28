# encoding: utf-8
__author__ = 'zhanghe'


import requests
import re
import json


UserAgent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'


def get_city_list():
    """
    获取城市列表
    """
    # 入口页的url
    url = 'http://www.58.com/changecity.aspx'
    header = {
        'Host': 'www.58.com',
        'Referer': 'http://sh.58.com/',
        'User-Agent': UserAgent
    }
    response = requests.get(url, headers=header)
    html = response.text
    rule = '<a href="http://.*?.58.com/" onclick="co\(\'(.*?)\'\)">(.*?)</a>'
    city_list = re.compile(rule, re.S).findall(html)
    city = {}
    for item in city_list:
        city[item[0]] = item[1]
    print json.dumps(city, indent=4).decode('raw_unicode_escape')


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


if __name__ == '__main__':
    # get_city_list()
    get_contacts()
    get_promotion_info()
