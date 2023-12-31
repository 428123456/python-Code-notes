# 导入 requests 包
import requests

# 发送请求
x = requests.post('https://www.runoob.com/try/ajax/demo_post.php')

# 返回网页内容
print(x.text)

#post请求带参数:
# 导入 requests 包
import requests

# 表单参数，参数名为 fname 和 lname
myobj = {'fname': 'RUNOOB','lname': 'Boy'}

# 发送请求
x = requests.post('https://www.runoob.com/try/ajax/demo_post2.php', data = myobj)

# 返回网页内容
print(x.text)

