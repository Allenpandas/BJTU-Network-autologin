# BJTU-Network-autologin
北京交通大学校园网自动登录脚本，适用于local.bjtu.edu.cn和web.bjtu.edu.cn。| Beijing Jiaotong University EDU network automatic login script for local.bjtu.edu.cn and web.bjtu.edu.cn.

## 1.工作原理

- 使用while循环语句，控制脚本始终在运行；
- 每次while循环都会发送请求访问`10.10.42.3`登录页，判断当前页面是否为"注销页"。若是"注销页"，说明账号已成功登录，联网正常，则等待5秒后结束本次循环；若不是"注销页"，说明当前未登录或已掉线，则立即发送请求登录账号联网。



## 2.PC使用教程

克隆本仓库代码

```shell
git clone https://github.com/Allenpandas/BJTU-Network-autologin
```

打开autologin.py文件，在user处填写学号（或工号）、在password处填写密码，然后保存autologin.py文件。

```python
# 校园网登录页
schoolWebURL = 'http://10.10.42.3'  # 10.10.43.3或者10.10.42.3
# 校园网登录的账号（一般是学号或者工号）
user = ''
# 校园网登录的密码
password = ''
```

执行python脚本

```shell
# 执行python脚本
python3 autologin.py
```



## 3.服务器持久化教程

将`check_login.sh`文件放在服务器的/home/bjtu/目录下

```
mv ./check_login.sh /home/bjtu/check_login.sh
```

编辑定时任务

```shell
crontab -e
```

设置定时任务，1分钟检查1次脚本执行情况

```shell
*/1 * * * * bash /home/bjtu/check_login.sh
```

