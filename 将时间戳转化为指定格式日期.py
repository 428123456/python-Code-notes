#firstly
import time
#获取当前时间戳
now = int(time.time())
#转化为其他日期格式，如："%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStylwTime = time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
print(otherStylwTime)

#secondly
import datetime
 
# 获得当前时间
now = datetime.datetime.now()
# 转换为指定的格式
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

#thirdiy
import time
 
timeStamp = 1557502800
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

#fourth
import datetime
 
timeStamp = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)