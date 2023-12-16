# -*- conding uft-8 -*-

x = input('输入x')
y = input('输入y')

#创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后x的值为{}'.format(x))
print('交换后y的值为{}'.format(y))
#使用temp临时变量
#不使用临时变量方法为：x,y=y,x
