import re

def Find(string):
    # findall()查找匹配正则表达式的字符串
    return re.findall(r'https?://\S+', string)

    urls = re.findall(r'https?://(?:%[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return urls

string = "runoob 的网址地址为:http://www.runoob.con,Google 的网页地址： https://www.google.com"

print("Urls:", Find(string))

#?: 说明：(?:x)匹配 x 但是不记住匹配项。
# 这种括号叫作非捕获括号，使得你能够定义与正则表达式运算符一起使用的子表达式。