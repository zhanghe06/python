# encoding: utf-8
__author__ = 'zhanghe'


import requests
import random
import json
import time
import re


class WebQQ:
    def __init__(self, qq):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
        }
        self.s = requests.session()
        self.qq_hash = ''
        self.vf_web_qq = ''
        self.user_list_dict = {}
        self.group_list_dict = {}
        self.PSessionID = ''
        self.NAME = int(qq)
        self.AppID = '501004106'
        self.ClientID = 53999199
        self.MsgId = 3030001
        self.qq_cookie = {
            'supertoken': '',
            'skey': '',
            'pt2gguin': '',
            'superuin': '',
            'superkey': '',
            'uin': '',
            'ptisp': '',
            'ptnick_' + str(self.NAME): '',
            'u_' + str(self.NAME): '',
            'ptwebqq': '',
            # 验证
            'pt4_token': '',
            'p_uin': '',
            'p_skey': '',
        }

    def load_config(self):
        pass

    @staticmethod
    def get_hash(x, K):
        """
        获取hash令牌（由js转化过来）
        获取群组信息，好友信息需要用到
        """
        # x += ""
        N = [0, 0, 0, 0]
        for T in range(0, len(K)):
            N[T % 4] ^= ord(K[T])
        U = ["EC", "OK"]
        V = []
        V.append(int(x) >> 24 & 255 ^ ord(U[0][0]))
        V.append(int(x) >> 16 & 255 ^ ord(U[0][1]))
        V.append(int(x) >> 8 & 255 ^ ord(U[1][0]))
        V.append(int(x) & 255 ^ ord(U[1][1]))
        U = []
        for T in range(0, 8):
            U.append(T % 2)
            if U[T] == 0:
                U[T] = N[T >> 1]
            else:
                U[T] = V[T >> 1]
        N = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        V = ""
        for T in range(0, len(U)):
            V += N[U[T] >> 4 & 15]
            V += N[U[T] & 15]
        return V

    def get_login_img(self):
        """
        获取登录二维码图片
        """
        url = 'https://ssl.ptlogin2.qq.com/ptqrshow'
        payload = {
            'appid': self.AppID,
            'e': '0',
            'l': 'M',
            's': '5',
            'd': '72',
            'v': '4',
            't': random.random()
        }
        self.header['Host'] = 'ssl.ptlogin2.qq.com'
        response = self.s.get(url, params=payload, headers=self.header)
        with open('ptqrshow.png', 'wb') as f:
            for item in response:
                f.write(item)

    def check_login_status(self):
        """
        检查登录状态
        """
        url = 'https://ssl.ptlogin2.qq.com/ptqrlogin'
        payload = {
            'webqq_type': '10',
            'remember_uin': '1',
            'login2qq': '1',
            'aid': self.AppID,
            'u1': 'http://w.qq.com/proxy.html?login2qq=1&webqq_type=10',
            'ptredirect': '0',
            'ptlang': '2052',
            'daid': '164',
            'from_ui': '1',
            'pttype': '1',
            'dumy': '',
            'fp': 'loginerroralert',
            'action': '0-0-36375',
            'mibao_css': 'm_webqq',
            't': time.time(),
            'g': '1',
            'js_type': '0',
            'js_ver': '10135',
            'login_sig': '',
            'pt_randsalt': '0'
        }
        self.header['Host'] = 'ssl.ptlogin2.qq.com'
        response = self.s.get(url, params=payload, headers=self.header)
        if 'ptwebqq' in response.cookies:
            # 如果登录成功，保存cookie
            print 'qq_cookie[\'ptwebqq\']:' + response.cookies['ptwebqq']
            self.qq_cookie['ptwebqq'] = response.cookies['ptwebqq']
        return response.content

    def check_sig(self, url):
        """
        二维码扫描后确认签名[并设置相应cookie]
        :param url:
        :return:
        """
        self.header['Host'] = 'ptlogin4.web2.qq.com'
        response = self.s.get(url, headers=self.header)
        # print response.content
        # print response.url
        print response.cookies  # 因302跳转，此处获取不到cookie，如果需要查看cookie，需要设置allow_redirects=False
        print response.history
        # Set-Cookie:uin=o0875270022; PATH=/; DOMAIN=qq.com;
        # Set-Cookie:skey=@uqacxdTvl; PATH=/; DOMAIN=qq.com;
        # Set-Cookie:pt2gguin=o0875270022; EXPIRES=Fri, 02-Jan-2020 00:00:00 GMT; PATH=/; DOMAIN=qq.com;
        # Set-Cookie:p_skey=1Jh*qEUJtSziSC5dQTTDqUALXe7qQcJcujNUHFz8rhs_; PATH=/; DOMAIN=web2.qq.com;
        # Set-Cookie:pt4_token=7rcO74gIW9QiQwa-d9QwSw__; PATH=/; DOMAIN=web2.qq.com;
        # Set-Cookie:p_uin=; EXPIRES=Fri, 02-Jan-1970 00:00:00 GMT; PATH=/; DOMAIN=qq.com;
        # Set-Cookie:p_skey=; EXPIRES=Fri, 02-Jan-1970 00:00:00 GMT; PATH=/; DOMAIN=qq.com;
        # Set-Cookie:pt4_token=; EXPIRES=Fri, 02-Jan-1970 00:00:00 GMT; PATH=/; DOMAIN=qq.com;
        # Set-Cookie:p_uin=o0875270022; PATH=/; DOMAIN=web2.qq.com;
        # todo cookie保存

    @staticmethod
    def read_login_status(status=None):
        """
        读取登录状态
        """
        # login_status = "ptuiCB('66','0','','0','二维码未失效。(3380616416)', '');"
        # login_status = "ptuiCB('0','0','http://ptlogin4.web2.qq.com/check_sig?pttype=1&uin=875270022&service=ptqrlogin&nodirect=0&ptsigx=60659e61c2dfdd3f21e34809d0a2d3baedb5e4f6a7703334382fb29629e6ee623f7295a85c63834cfb8898cbc44ba8f38246d5afcf2140036b83aff7d8a96c37&s_url=http%3A%2F%2Fw.qq.com%2Fproxy.html%3Flogin2qq%3D1%26webqq_type%3D10&f_url=&ptlang=2052&ptredirect=100&aid=501004106&daid=164&j_later=0&low_login_hour=0&regmaster=0&pt_login_type=3&pt_aid=0&pt_aaid=16&pt_light=0&pt_3rd_aid=0','0','登录成功！', '╰微微.ヾ迷╮');"
        login_status_rule = r'ptuiCB\((.*?)\);'
        login_status_list = re.compile(login_status_rule, re.S).findall(status)
        result_list = []
        if login_status_list:
            result_list = [item.strip(' \'') for item in login_status_list[0].split(',')]
        # for item in result_list:
        #     print item
        # return result_list
        if not result_list:
            return None
        else:
            if result_list[0] == '66' and result_list[1] == '0':
                print result_list[4]
                return {'status': result_list[4]}
            elif result_list[0] == '0' and result_list[1] == '0':
                print result_list[2]
                return {'check_url': result_list[2]}
            else:
                return None

    def get_session_id(self):
        """
        获取sessionId
        """
        session_id_url = 'http://d1.web2.qq.com/channel/login2'
        self.header['Host'] = 'd1.web2.qq.com'
        self.header['Origin'] = 'http://d1.web2.qq.com'
        self.header['Referer'] = 'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2'
        session_id_dict = {
            "ptwebqq": self.qq_cookie['ptwebqq'],
            "clientid": self.ClientID,
            "psessionid": "",
            "status": "online"
        }
        session_id_payload = {'r': json.dumps(session_id_dict)}
        response = self.s.post(session_id_url, data=session_id_payload, headers=self.header)
        data = json.loads(response.content)
        self.PSessionID = data['result']['psessionid']
        print 'PSessionID:'+self.PSessionID

    def get_self_info(self):
        """
        获取当前登录用户个人信息
        """
        url_self_info = 'http://s.web2.qq.com/api/get_self_info2?t=1434857217484'
        self.header['Host'] = 's.web2.qq.com'
        self.header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
        response = self.s.get(url_self_info, headers=self.header)
        return json.dumps(response.content, ensure_ascii=False, indent=4)

    def get_vf_web_qq(self):
        """
        获取验证令牌
        :return:
        """
        vf_web_qq_url = 'http://s.web2.qq.com/api/getvfwebqq'
        vf_web_qq_payload = {
            'ptwebqq': self.qq_cookie['ptwebqq'],  # 从cookie中获取
            'clientid': self.ClientID,
            'psessionid': '',
            't': time.time()
        }
        self.header['Host'] = 's.web2.qq.com'
        self.header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
        response = self.s.get(vf_web_qq_url, params=vf_web_qq_payload, headers=self.header)
        print response.url
        print response.content
        return json.loads(response.content)['result']['vfwebqq']

    def get_group_list(self):
        """
        获取群组列表信息
        """
        group_list_url = 'http://s.web2.qq.com/api/get_group_name_list_mask2'
        group_list_payload = {'r': json.dumps({"vfwebqq": self.vf_web_qq, "hash": self.qq_hash})}
        self.header['Host'] = 's.web2.qq.com'
        self.header['Origin'] = 'http://s.web2.qq.com'
        self.header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
        response = self.s.post(group_list_url, data=group_list_payload, headers=self.header)
        group_list = json.loads(response.content)['result']['gnamelist']
        for group_item in group_list:
            self.group_list_dict[group_item['name']] = group_item
        # print json.dumps(self.group_list_dict, ensure_ascii=False, indent=4)
        return json.loads(response.content)

    def get_group_detail(self, group_code):
        """
        获取群组详细信息
        包含群组成员信息
        """
        group_detail_url = 'http://s.web2.qq.com/api/get_group_info_ext2'
        group_detail_payload = {
            'gcode': group_code,
            'vfwebqq': self.vf_web_qq,
            't': time.time()
        }
        self.header['Host'] = 's.web2.qq.com'
        self.header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
        response = self.s.get(group_detail_url, params=group_detail_payload, headers=self.header)
        group_detail = json.loads(response.content)
        return group_detail

    def get_friends_info(self):
        """
        获取好友信息[原始数据，没有关联]
        """
        friends_info_url = 'http://s.web2.qq.com/api/get_user_friends2'
        friends_info_payload = {'r': json.dumps({"vfwebqq": self.vf_web_qq, "hash": self.qq_hash})}
        self.header['Host'] = 's.web2.qq.com'
        self.header['Origin'] = 'http://s.web2.qq.com'
        self.header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
        response = self.s.post(friends_info_url, data=friends_info_payload, headers=self.header)
        return json.loads(response.content)

    def get_friends_qq_info(self):
        """
        合并好友信息[关联uin和qq号码]
        :return:
        """
        friends_info = self.get_friends_info()
        user_info_dict = {}
        user_mark_dict = {}
        for i in friends_info['result']['info']:
            user_info_dict[i['uin']] = i
        for i in friends_info['result']['marknames']:
            user_mark_dict[i['uin']] = i
        # print len(user_info_dict)
        # print len(user_mark_dict)
        user_dict = {}
        for i in user_info_dict:
            for j in user_mark_dict:
                if i == j:
                    user_dict[i] = dict(user_info_dict[i], **user_mark_dict[j])
                    break
                else:
                    user_dict[i] = user_info_dict[i]
        for i in user_dict:
            user_account = self.get_friends_qq_by_uin(i)
            # print 'QQ号码：' + str(user_account)
            self.user_list_dict[user_account] = user_dict[i]
        # print json.dumps(user_list_dict, ensure_ascii=False, indent=4)

    def get_group_uin_by_name(self, group_name):
        """
        根据群组名称获取群组临时编号
        :param group_name:
        :return:
        """
        if group_name in self.group_list_dict:
            print '找到对应群组'
            print self.group_list_dict[group_name]['gid']
            return self.group_list_dict[group_name]['gid']
        print '没有对应群组'

    def send_group_msg(self, group_uin, msg):
        """
        发送群消息
        """
        group_msg_url = 'http://d.web2.qq.com/channel/send_qun_msg2'
        self.header['Host'] = 'd.web2.qq.com'
        self.header['Origin'] = 'http://d.web2.qq.com'
        self.header['Referer'] = 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2'
        group_msg_dict = {
            "group_uin": group_uin,
            "content": "[\"" + msg + "\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]",
            "face": 0,
            "clientid": self.ClientID,
            "msg_id": self.MsgId,
            "psessionid": self.PSessionID
        }
        group_msg_payload = {'r': json.dumps(group_msg_dict)}
        response = self.s.post(group_msg_url, data=group_msg_payload, headers=self.header)
        group_msg_result = json.loads(response.content)
        # {"errCode":0,"msg":"send ok"}
        if group_msg_result.get('errCode') == 0 and group_msg_result.get('msg') == 'send ok':
            print '发送成功'
        else:
            print '发送失败，错误码：%s' % group_msg_result.get('errCode')

    def get_friends_qq_by_uin(self, friends_uin):
        """
        根据uin获取好友QQ号码
        """
        friends_account_url = 'http://s.web2.qq.com/api/get_friend_uin2'
        self.header['Host'] = 's.web2.qq.com'
        self.header['Referer'] = 'http://s.web2.qq.com/proxy.html?v=20130916001&callback=1&id=1'
        friends_account_payload = {
            'tuin': friends_uin,
            'type': 1,
            'vfwebqq': self.vf_web_qq,
            't': time.time(),
        }
        response = self.s.get(friends_account_url, params=friends_account_payload, headers=self.header)
        result_dict = json.loads(response.content)
        return result_dict['result']['account']

    def get_uin_by_qq(self, qq):
        """
        根据QQ号码获取uin
        :param qq:
        :return:
        """
        return self.user_list_dict[qq]['uin']

    def get_nick_by_qq(self, qq):
        """
        根据QQ号码获取昵称
        :param qq:
        :return:
        """
        return self.user_list_dict[qq]['nick']

    def send_qq_msg(self, qq, msg):
        """
        发送QQ好友消息
        :param qq:
        :param msg:
        :return:
        """
        qq_msg_url = 'http://d1.web2.qq.com/channel/send_buddy_msg2'
        self.header['Host'] = 'd1.web2.qq.com'
        self.header['Referer'] = 'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2'
        qq_msg_dict = {
            "to": self.get_uin_by_qq(qq),
            "content": "[\""+str(msg)+"\",[\"font\",{\"name\":\"宋体\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]",
            "face": 0,
            "clientid": self.ClientID,
            "msg_id": self.MsgId,
            "psessionid": self.PSessionID
        }
        qq_msg_payload = {'r': json.dumps(qq_msg_dict)}
        response = self.s.post(qq_msg_url, data=qq_msg_payload, headers=self.header)
        qq_msg_result = json.loads(response.content)
        # {"errCode":0,"msg":"send ok"}
        if qq_msg_result.get('errCode') == 0 and qq_msg_result.get('msg') == 'send ok':
            print '发送成功'
        else:
            print '发送失败，错误码：%s' % qq_msg_result.get('errCode')

    def get_new_msg(self):
        """
        获取最新消息（轮询）
        备注：请求到返回时间大概10S
        """
        new_msg_url = 'http://d1.web2.qq.com/channel/poll2'
        self.header['Host'] = 'd1.web2.qq.com'
        self.header['Referer'] = 'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2'
        new_msg_dict = {
            "ptwebqq": self.qq_cookie['ptwebqq'],
            "clientid": self.ClientID,
            "psessionid": self.PSessionID,
            "key": ""
        }
        new_msg_payload = {'r': json.dumps(new_msg_dict)}
        response = self.s.post(new_msg_url, data=new_msg_payload, headers=self.header)
        content = json.loads(response.content)
        if content['retcode'] == 0:
            for row in content['result']:
                # 接收群组消息
                if row['poll_type'] == 'group_message':
                    group_code = row['value']['group_code']
                    send_uin = row['value']['send_uin']
                    send_qq = self.get_friends_qq_by_uin(send_uin)
                    group_name = ''
                    member_name = ''
                    # 获取群组详细信息
                    group_detail = self.get_group_detail(group_code)
                    if group_detail['retcode'] == 0:
                        group_name = group_detail['result']['ginfo']['name']
                        for group_row in group_detail['result']['minfo']:
                            if group_row['uin'] == send_uin:
                                member_name = group_row['nick']
                    msg = row['value']['content'][1]
                    msg_info = '群组消息：%s\t成员[%s]：%s\t消息：%s\n' % (group_name, send_qq, member_name, msg)
                    print msg_info
                    # yield msg_info
                # 接收好友消息
                if row['poll_type'] == 'message':
                    from_uin = row['value']['from_uin']
                    send_time_stamp = row['value']['time']
                    send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(send_time_stamp))
                    # 获取好友详细信息
                    from_qq = self.get_friends_qq_by_uin(from_uin)
                    nick = self.get_nick_by_qq(from_qq)
                    msg = row['value']['content'][1]
                    msg_info = '好友消息：%s\t好友[%s]：%s\t消息：%s\n' % (send_time, from_qq, nick, msg)
                    print msg_info
                    # yield msg_info

    def run(self):
        """
        启动入口
        """
        self.get_login_img()
        raw_input('扫描完毕请回车')
        login_status = self.read_login_status(self.check_login_status())
        print login_status
        if 'status' in login_status:
            print login_status['status']
            print '请重新扫描'
        if 'check_url' in login_status:
            # print login_status['check_url']
            self.check_sig(login_status['check_url'])
            # print self.get_self_info()
            # 获取验证令牌
            self.vf_web_qq = self.get_vf_web_qq()
            # 获取hash令牌
            self.qq_hash = self.get_hash(self.NAME, self.qq_cookie['ptwebqq'])
            # 获取SessionId
            self.get_session_id()
            # 获取好友信息
            self.get_friends_qq_info()
            # 获取群组信息
            self.get_group_list()

    def run_get_msg(self, sleep_time=2):
        """
        获取最新消息
        :return:
        """
        while 1:
            self.get_new_msg()
            time.sleep(sleep_time)

    def run_send_group_msg(self, group_name, group_msg=None):
        """
        发送群组消息
        :param group_name:
        :return:
        """
        if group_name is None:
            print '请指定群组名称'
            return None
        group_name = str(group_name).decode()
        group_uin = self.get_group_uin_by_name(group_name)
        group_uin = int(group_uin)
        if group_msg is not None:
            self.send_group_msg(group_uin, group_msg)
            self.MsgId += 1
        else:
            while 1:
                group_msg = raw_input("请输入消息: ")
                group_msg += 'This is a test\\nSend by python\\n%s' % time.strftime("%Y-%m-%d %H:%M:%S")
                self.send_group_msg(group_uin, group_msg)
                self.MsgId += 1

    def run_send_friend_msg(self, friend_qq, friend_msg=None):
        """
        发送好友消息
        :param friend_qq:
        :return:
        """
        friend_qq = int(friend_qq)
        if friend_msg is not None:
            self.send_qq_msg(friend_qq, friend_msg)
            self.MsgId += 1
        else:
            while 1:
                raw_input_msg = raw_input("请输入消息: ")
                self.send_qq_msg(friend_qq, raw_input_msg)
                self.MsgId += 1


def test_send_friend_msg():
    """
    测试发送好友消息
    :return:
    """
    my_qq = WebQQ(875270022)
    my_qq.run()
    my_qq.run_send_friend_msg(455091702)


def test_send_group_msg():
    """
    测试发送群组消息
    :return:
    """
    my_qq = WebQQ(875270022)
    my_qq.run()
    my_qq.run_send_group_msg('微妙网官方高级群')


if __name__ == "__main__":
    test_send_friend_msg()
    # test_send_group_msg()


# todo 状态提醒
# {"retcode":0,"result":[{"poll_type":"buddies_status_change","value":{"uin":1166353395,"status":"online","client_type":4}}]}
# {"retcode":0,"result":[{"poll_type":"buddies_status_change","value":{"uin":3019820949,"status":"offline","client_type":1}}]}
# {"retcode":0,"result":[{"poll_type":"buddies_status_change","value":{"uin":3019820949,"status":"online","client_type":21}}]}
