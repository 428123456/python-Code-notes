import time

a1 = "2023-12-12 23:40:00"
# 先转化为时间数据
timeArray = time.strptime(a1, "%Y-%m-%d %H:%M:%S")
# 转化为时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

# 格式转化 - 转为/
a2 = "2023/12/12 23:40:00"
# 先转化为时间组，然后转化为其他格式
timeArray = time.strptime(a2, "%Y/%m/%d %H:%M:%S")
otherStyleTime = time.strftime('%Y/%m/%d %H:%M:%S', timeArray)
print(otherStyleTime)

