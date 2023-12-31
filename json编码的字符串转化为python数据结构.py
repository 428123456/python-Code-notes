#!/sur/bin.python

import json
import sys

#python 字典类型转化为json对象

data = {
    'no':1,
    'name':"runoob",
    'url':'http//www.runoob.com'
}

json_str = json.dumps(data)
print('python原始数据:',repr(data))
print('json对象:',json_str)