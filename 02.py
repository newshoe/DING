Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> coding:utf-8
import json
import urllib.request

#1、构建url
url = "https://oapi.dingtalk.com/robot/send?access_token=5304dc23bb9709ab48be0dec1e3829c17e3cca4b803b5625b76a8fe0a80a8c77"   #url为机器人的webhook

#2、构建一下请求头部
header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
}
#3、构建请求数据
data = {
    "msgtype": "text",
    "text": {
        "content": "大家好，你们猜猜我是谁"
    },
    "at": {
         "isAtAll": True     #@全体成员（在此可设置@特定某人）
    }
}

#4、对请求的数据进行json封装
sendData = json.dumps(data)#将字典类型数据转化为json格式
sendData = sendData.encode("utf-8") # python3的Request要求data为byte类型

#5、发送请求
request = urllib.request.Request(url=url, data=sendData, headers=header)

#6、将请求发回的数据构建成为文件格式

opener = urllib.request.urlopen(request)
#7、打印返回的结果
print(opener.read())
--------------------- 
作者：植魂人 
来源：CSDN 
原文：https://blog.csdn.net/m0_37752182/article/details/80200972 
版权声明：本文为博主原创文章，转载请附上博文链接！
