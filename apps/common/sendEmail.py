from apps.common import getInfo_common
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import time
import threading


def filter():
    infoList = getInfo_common.getListInfo()
    strr = ''
    for info in infoList:
        if ('平谷' in info[7] or '平谷' in info[8]) or info[2] > 1000:
            strr += '**************************************\n'
            strr += '起始地:{}\n'.format(info[7])
            strr += '结束地:{}\n'.format(info[8])
            strr += '底价:{}\n'.format(info[0])
            strr += '原始价格:{}\n'.format(info[1])
            strr += '预计收益:{}\n'.format(info[2])
            strr += '全程公里:{}\n'.format(info[3])
            strr += '车辆:{}\n'.format(info[4])
            strr += '车长:{}\n'.format(info[5])
            strr += '油费:{}\n'.format(info[6])
            strr += '开始时间:{}\n'.format(info[9])
            strr += '结束时间:{}\n\n'.format(info[10])

    return strr



def send(title):
    strr = filter()
    if strr != '':
        print(strr)
        sender = "1006573469@qq.com"
        receiver = ['573587128@qq.com']   # 573587128@qq.com   jiangyanchen2@vip.qq.com
        message = MIMEText(strr, 'plain', 'utf-8')
        message['From'] = Header('自动查询助手', 'utf-8')
        message['To'] = Header('有合适订单', 'utf-8')

        message['Subject'] = Header(title, 'utf-8')

        obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
        obj.login('1006573469@qq.com','nlamtdopfqkxbfih')
        obj.sendmail(sender, receiver, message.as_string())


def begin():
    while True:
        try:
            send('有合适订单')
            print('执行成功!!')
        except:
            pass
        finally:
            time.sleep(1800)

def test():
    while True:
        print('fuck!!!!!!!!!!!!!!!!!')
        time.sleep(3)

