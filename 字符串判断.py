#测试实例一
print("测试实例1")
str = "runoob.com"
print(str.isalnum()) #判断所有字符都是数字或首字母
print(str.isalpha()) #判断所有字符是字母
print(str.isdigit()) #判断所有字符都是数字
print(str.isupper()) #判断所有字符都是大写
print(str.istitle()) #判断所有单词都是首字母大写，像标题
print(str.isspace()) #判断所有字符都是空白字符、\t、\n、\r

print('--------------------------------')
#测试实例二
print("测试实例2")
str = "runoob"
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.istitle())
print(str.isspace())