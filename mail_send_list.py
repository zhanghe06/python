# coding=utf-8
__author__ = 'zhanghe'

import smtplib
from email.mime.text import MIMEText

from mail_config import from_email_name
from mail_config import from_email
from mail_config import password
from mail_config import smtp_server
from mail_config import to_email_name
from mail_config import to_email

from email.header import Header
from email.utils import parseaddr, formataddr


def _format_email(s):
    """
    格式化邮件地址
    :param s:
    :return:
    """
    name, email = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), email.encode('utf-8') if isinstance(email, unicode) else email))


# 实际收件人地址（列表格式，可以群发）:
email_list = ['455091702@qq.com', 'zhang_he06@163.com']

# 邮件主题
subject = u'来自邮件列表的问候……'

# 邮件内容（默认html格式）
email_content = '''<html>
<body>
    <h1>Hello你好</h1>
    <p>send by <a href="http://www.python.org">Python</a>...</p>
</body>
</html>'''


def send_mail(to_email_list, email_format='html'):
    """
    发送邮件
    适用场景：邮件列表，EDM邮件营销，群发（特点：邮件内容统一）
    :return:
    """
    if email_format == 'text':
        msg = MIMEText(email_content, 'plain', 'utf-8')
    else:
        msg = MIMEText(email_content, 'html', 'utf-8')
    msg['From'] = _format_email(u'%s <%s>' % (from_email_name, from_email))
    msg['To'] = _format_email(u'%s <%s>' % (to_email_name, to_email))
    msg['Subject'] = Header(subject, 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    # server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息
    server.login(from_email, password)
    server.sendmail(from_email, to_email_list, msg.as_string())
    server.quit()


if __name__ == '__main__':
    send_mail(email_list)
