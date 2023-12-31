import urllib.request

myURL1 = urllib.request.urlopen("https://www.runoob.com/")
print(myURL1.getcode())  # 200

try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404) # 404

'''
在对网页进行抓取时，经常需要判断网页是否可以正常访问，
这里我们就可以使用 getcode() 函数获取网页状态码，
返回 200 说明网页正常，返回 404 说明网页不存在:
'''