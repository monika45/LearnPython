from smtplib import SMTP, SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'
mail_pass = 'zzzz1234'
sender = 'hgyu_zhao@163.com'
receivers = ['944479924@qq.com']


def main1():
    """发邮件"""
    message = MIMEText('用python发送邮件的示例代码', 'plain', 'utf-8')
    message['From'] = Header('Sss', 'utf-8')
    message['To'] = Header('Aaa', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.163.com', 25)
    smtper.login(sender, 'zzzz1234')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')



def main2():
    """发送带附件的邮件"""
    pass


if __name__ == '__main__':
    main1()
