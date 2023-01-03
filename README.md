# BJTU-edu-network-autologin
北京交通大学校园网自动登录脚本（开机无需输入账号密码，实现自动登录），适用于local.bjtu.edu.cn和web.bjtu.edu.cn



## 使用教程

克隆仓库代码

```shell
git clone https://github.com/wuyalun/BJTU-edu-network-autologin.git
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
# 进入到项目目录
cd BJTU-edu-network-autologin/

# 执行python脚本
python3 autologin.py
```

