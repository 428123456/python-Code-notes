# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/')

# 返回网页内容
print(x.text)

# 返回 http 的状态码
print(x.status_code)

# 响应状态的描述
print(x.reason)

# 返回编码
print(x.apparent_encoding)

# 发送请求
x = requests.get('https://www.runoob.com/try/ajax/json_demo.json')

# 返回 json 数据
print(x.json())

