# coding=utf-8
__author__ = 'zhanghe'

import smtplib
from email.mime.text import MIMEText

from mail_config import from_email_name
from mail_config import from_email
from mail_config import password
from mail_config import smtp_server

from email.header import Header
from email.utils import parseaddr, formataddr

# 邮件内容
email_info = {
    'to_email_name': u'测试收件人',
    'to_email': u'xxxxxx@qq.com',
    'subject': u'这是一封来自python的测试邮件！',
    'content': u'<html><body><h1>Hello</h1>' +
                u'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
                u'</body></html>',
}


def _format_email(s):
    """
    格式化邮件地址
    :param s:
    :return:
    """
    name, email = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), email.encode('utf-8') if isinstance(email, unicode) else email))


def send_mail(to_email, email_format='html'):
    """
    发送邮件
    适用场景：邮件队列
    :return:
    """
    if email_format == 'text':
        msg = MIMEText(email_info['content'], 'plain', 'utf-8')
    else:
        msg = MIMEText(email_info['content'], 'html', 'utf-8')
    msg['From'] = _format_email(u'%s <%s>' % (from_email_name, from_email))
    msg['To'] = _format_email(u'%s <%s>' % (email_info['to_email_name'], email_info['to_email']))
    msg['Subject'] = Header(u'%s' % email_info['subject'], 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    # server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息
    server.login(from_email, password)
    server.sendmail(from_email, [to_email], msg.as_string())
    server.quit()
    # TODO：与队列结合起来


if __name__ == '__main__':
    send_mail(email_info['to_email'])
