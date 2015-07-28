# encoding: utf-8
__author__ = 'zhanghe'

import requests
import time
import json

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    }

s = requests.session()


def get_keywords_list(keywords):
    """
    获取
    :param keywords:
    :return:
    """
    print keywords
    url = 'https://suggest.taobao.com/sug'
    payload = {
        'code': 'utf-8',
        'q': keywords,
        '_ksTS': str(int(1000*(time.time())))+'_2550',
        # 'callback': 'jsonp2551',
        'k': '1',
        'area': 'c2c',
        'bucketid': '19',
    }
    header['Host'] = 'suggest.taobao.com'
    header['Referer'] = 'https://top.taobao.com/index.php?spm=a1z5i.1.2.1.hUTg2J&topId=HOME'
    response = s.get(url, params=payload, headers=header)
    print response.url
    content = response.text
    print json.dumps(json.loads(content), indent=4, ensure_ascii=False)


if __name__ == '__main__':
    get_keywords_list('衣服')


"""
测试结果：

衣服
https://suggest.taobao.com/sug?code=utf-8&area=c2c&bucketid=19&k=1&q=%E8%A1%A3%E6%9C%8D&_ksTS=1438097289998_2550
{
    "magic": [
        {
            "index": "1",
            "type": "tag_group",
            "data": [
                [
                    {
                        "title": "修身"
                    },
                    {
                        "title": "学生"
                    },
                    {
                        "title": "春装"
                    },
                    {
                        "title": "显瘦"
                    },
                    {
                        "title": "中长款"
                    },
                    {
                        "title": "打底衫"
                    },
                    {
                        "title": "短袖"
                    },
                    {
                        "type": "hot",
                        "title": "连衣裙"
                    },
                    {
                        "title": "韩国"
                    },
                    {
                        "title": "宽松"
                    }
                ]
            ]
        },
        {
            "index": "2",
            "type": "tag_group",
            "data": [
                [
                    {
                        "title": "外套"
                    },
                    {
                        "title": "学生"
                    },
                    {
                        "title": "常规"
                    },
                    {
                        "type": "hot",
                        "title": "大码"
                    },
                    {
                        "title": "上衣"
                    },
                    {
                        "title": "高中"
                    },
                    {
                        "title": "打底衫"
                    },
                    {
                        "title": "短袖"
                    },
                    {
                        "title": "修身"
                    },
                    {
                        "title": "宽松"
                    }
                ]
            ]
        },
        {
            "index": "3",
            "type": "tag_group",
            "data": [
                [
                    {
                        "title": "挂衣架"
                    },
                    {
                        "type": "hot",
                        "title": "衣撑"
                    }
                ],
                [
                    {
                        "title": "落地"
                    },
                    {
                        "title": "折叠"
                    },
                    {
                        "title": "卧室"
                    },
                    {
                        "title": "布艺"
                    },
                    {
                        "title": "组装"
                    },
                    {
                        "title": "简易"
                    },
                    {
                        "title": "欧式"
                    },
                    {
                        "type": "hot",
                        "title": "实木"
                    }
                ]
            ]
        },
        {
            "index": "4",
            "type": "tag_group",
            "data": [
                [
                    {
                        "title": "整理箱"
                    },
                    {
                        "type": "hot",
                        "title": "箱子"
                    },
                    {
                        "title": "储物箱"
                    }
                ],
                [
                    {
                        "type": "hot",
                        "title": "牛津布"
                    },
                    {
                        "title": "布艺"
                    }
                ],
                [
                    {
                        "title": "宜家"
                    },
                    {
                        "title": "塑料"
                    },
                    {
                        "title": "折叠"
                    },
                    {
                        "type": "hot",
                        "title": "钢架"
                    },
                    {
                        "title": "卧室"
                    }
                ]
            ]
        },
        {
            "index": "5",
            "type": "tag_group",
            "data": [
                [
                    {
                        "title": "干洗店"
                    },
                    {
                        "type": "hot",
                        "title": "服装店"
                    }
                ],
                [
                    {
                        "title": "收纳袋"
                    },
                    {
                        "type": "hot",
                        "title": "挂袋"
                    }
                ],
                [
                    {
                        "title": "塑料"
                    },
                    {
                        "title": "小号"
                    },
                    {
                        "type": "hot",
                        "title": "中号"
                    },
                    {
                        "title": "加厚"
                    },
                    {
                        "title": "一次性"
                    },
                    {
                        "title": "大衣"
                    }
                ]
            ]
        },
        {
            "index": "7",
            "type": "tag_group",
            "data": [
                [
                    {
                        "type": "hot",
                        "title": "雪纺衫"
                    },
                    {
                        "title": "打底衫"
                    }
                ],
                [
                    {
                        "title": "中长款"
                    },
                    {
                        "title": "学生"
                    },
                    {
                        "title": "春装"
                    },
                    {
                        "title": "印花"
                    },
                    {
                        "title": "上衣"
                    },
                    {
                        "type": "hot",
                        "title": "大码"
                    },
                    {
                        "title": "显瘦"
                    },
                    {
                        "title": "短袖"
                    }
                ]
            ]
        },
        {
            "index": "8",
            "type": "tag_group",
            "data": [
                [
                    {
                        "title": "衬衫"
                    },
                    {
                        "type": "hot",
                        "title": "T恤"
                    }
                ],
                [
                    {
                        "title": "常规"
                    },
                    {
                        "type": "hot",
                        "title": "薄款"
                    }
                ],
                [
                    {
                        "title": "夏季"
                    },
                    {
                        "title": "短袖"
                    },
                    {
                        "title": "青春"
                    },
                    {
                        "title": "修身"
                    },
                    {
                        "title": "外套"
                    },
                    {
                        "type": "hot",
                        "title": "联盟"
                    }
                ]
            ]
        },
        {
            "index": "9",
            "type": "tag_group",
            "data": [
                [
                    {
                        "type": "hot",
                        "title": "V领"
                    },
                    {
                        "title": "圆领"
                    }
                ],
                [
                    {
                        "type": "hot",
                        "title": "青春"
                    },
                    {
                        "title": "学生"
                    },
                    {
                        "title": "联盟"
                    },
                    {
                        "title": "短袖"
                    },
                    {
                        "title": "薄款"
                    },
                    {
                        "title": "修身"
                    },
                    {
                        "title": "英雄"
                    },
                    {
                        "title": "宽松"
                    }
                ]
            ]
        }
    ],
    "result": [
        [
            "衣服女夏",
            "911812"
        ],
        [
            "衣服男夏装",
            "864045"
        ],
        [
            "衣服架",
            "194265"
        ],
        [
            "衣服收纳箱",
            "88531"
        ],
        [
            "衣服防尘罩",
            "25904"
        ],
        [
            "衣服挂",
            "303525"
        ],
        [
            "衣服女夏 宽松",
            "131730"
        ],
        [
            "衣服男",
            "1440833"
        ],
        [
            "衣服男夏装 t恤",
            "460215"
        ],
        [
            "判断衣服是否掉色",
            "1"
        ]
    ],
    "cat": [
        [
            "流行男装",
            "50344007",
            "衣服"
        ],
        [
            "女装",
            "50102996",
            "衣服"
        ]
    ]
}
"""