test_dict = {"runoob":1,"google":2,"taoboa":3,"zhihu":4}
#输出原始字典
print("原始字典："+str(test_dict))

#pop移除zhihu
removed_value = test_dict.pop('zhihu')

#移除后字典
print("移除key对应的value:"+str(removed_value))
print('\r')

#使用pop（）移除没有的key不会发生异常，我们可以自定义提示信息
removed_value = test_dict.pop('baidu','没有该键(key)')

#输出移除后字典
print("字典移除后："+str(test_dict))
print('移除值为：'+str(removed_value))