# encoding: utf-8
__author__ = 'zhanghe'


def select_best_resume(resume_list):
    '''
    根据相关字段权重取出最优简历
    :param resume_list:
    :return:
    '''
    url_list = {}
    if resume_list is None:
        # 如果简历为空
        url_list['resume'] = None
        return url_list

    for item in resume_list:
        if u'英文' in item:
            resume_list.remove(item)

    # 获取最优简历url
    # 如果只有一个简历，直接返回
    if len(resume_list) == 1:
        url_list['resume'] = resume_list[0]['url']
    else:
        # 如果有多个简历，先取出各字段的最优值
        # 完整度
        integrity_range = []
        for item in resume_list:
            integrity_range.append(item['integrity'])
        max_integrity = max(integrity_range)
        # 更新日期
        update_date_range = []
        for item in resume_list:
            update_date_range.append(item['update_date'])
        max_update_date = max(update_date_range)
        # 开放程度
        openness_range = []
        for item in resume_list:
            openness_range.append(item['openness'])
        if u'开放' in openness_range:
            max_openness = u'开放'
        elif u'委托给智联' in openness_range:
            max_openness = u'委托给智联'
        else:
            max_openness = u'保密'
        # 权重
        weight_range = []
        for item in resume_list:
            item['weight'] = 0
            # 将每条简历与最优值比较，如果存在，则权重自增
            if item['integrity'] == max_integrity:
                item['weight'] += 100
            if item['update_date'] == max_update_date:
                item['weight'] += 10
            if item['openness'] == max_openness:
                item['weight'] += 1
            weight_range.append(item['weight'])
        # 最大权重
        max_weight = max(weight_range)

        for item_max in resume_list:
            # 查询简历列表中有最大权重的一条记录
            if item_max['weight'] == max_weight:
                url_list['resume'] = item_max['url']
    return url_list


def url_join(url_str, host):
    '''
    url拼接
    :param url_str:
    :param host:
    :return:
    '''
    if url_str.startswith(host) or url_str.startswith('http://'):
        return url_str
    return host.rstrip('/') + '/' + url_str.lstrip('/')


if __name__ == '__main__':
    print url_join('http://www.baidu.com/123/fff', 'http://eee.baidu.com')
    print url_join('/123/fff', 'http://eee.baidu.com')
    print url_join('/123/fff', 'http://eee.baidu.com/')