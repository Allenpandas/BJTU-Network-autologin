import re
import requests
from time import strftime
import time

# 校园网登录页
schoolWebURL = 'http://10.10.43.3'  # 10.10.43.3或者10.10.42.3
# 校园网登录的账号（一般是学号或者工号）
user = ''
# 校园网登录的密码
password = ''

# 刷新时间(s)
refreshTime = 30

while(True):
    try:
        response = requests.get(schoolWebURL)

        # 正则表达式，匹配<title>标签中的内容
        pattern = re.compile('<title>(.*?)</title>', re.S)
        title = re.findall(pattern, response.text)
        title = title[0]  # 将格式转为字符串

        if title == '注销页':
            print('%s %s 连接正常' % (strftime('%Y-%m-%d'),strftime('%H:%M:%S')))
            time.sleep(refreshTime)
            pass

        else:
            t = str(int(round(time.time() * 1000)))  # 毫秒级时间戳
            schoolWebLoginURL = schoolWebURL+'/drcom/login?callback=dr'+t+'&DDDDD='+user+'&upass='+password+'&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_='+t
            print('%s %s 登录成功' % (strftime('%Y-%m-%d'),strftime('%H:%M:%S')))
            requests.get(schoolWebLoginURL)
    except:
        print('%s %s WIFI连接异常' % (strftime('%Y-%m-%d'),strftime('%H:%M:%S')))
        print('%s %s %d 秒后重试' % (strftime('%Y-%m-%d'),strftime('%H:%M:%S'), refreshTime))
        time.sleep(refreshTime)