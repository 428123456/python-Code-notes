test_dict = {"runoob":1,"google":2,"taobao":3,"zhihu":4}

#输出原始字典
print("字典移除后："+str(test_dict))

#使用del移除zhihu
del test_dict['zhihu']

#输出移除后的字典
print("字典移除后："+str(test_dict))

#移除后没有key会报错
#del test_dict['baidu']