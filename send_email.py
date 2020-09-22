from smtplib import SMTP, SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

mail_host = 'smtp.163.com'
mail_port = 465
mail_pass = '*****'
sender = '***@163.com'
sender_name = 'Sina'
receiver = '***@qq.com'
receiver_name = 'Monika'
title = '测试发送邮件'
# html
content = 'python学习'


def main1():
    """发邮件"""
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = formataddr((sender_name, sender))
    message['To'] = formataddr((receiver_name, receiver))
    message['Subject'] = title
    # 当with语句结束时，smtp的quit()会自动执行
    with SMTP_SSL(mail_host, mail_port) as smtp:
        smtp.login(sender, mail_pass)
        smtp.sendmail(sender, [receiver], message.as_string())


def main2():
    """发送带附件的邮件"""
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = formataddr((sender_name, sender))
    message['To'] = formataddr((receiver_name, receiver))
    message['Subject'] = title

    # 邮件正文内容
    message.attach(MIMEText(content, 'plain', 'utf-8'))

    # 构造附件1
    att1 = MIMEText(open('./res/img/conpon1.png', 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="1.png"'
    message.attach(att1)

    # 构造附件1
    att1 = MIMEText(open('./res/1.txt', 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment; filename="1.txt"'
    message.attach(att1)

    with SMTP_SSL(mail_host, mail_port) as smtp:
        smtp.login(sender, mail_pass)
        smtp.sendmail(sender, [receiver], message.as_string())


if __name__ == '__main__':
    main2()
