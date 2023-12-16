# -*- conding:uft-8 -*-

#用户输入摄氏温度
#接收用户输入
celsius = float(input('请输入温度'))

fahrenheit = (celsius*1.8)+32
print("摄氏度为%.1f度，对应的华氏度为%.1f度"%(celsius,fahrenheit))