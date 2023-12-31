#python 实列
#add(),sub(),mul()

#导入 operator 模块
import operator

#初始化变量
a = 4
b = 3
#使用add()函数相加2值

print("add()运算结果：",end="")
print(operator.add(a,b))

#使用sub()函数相减2值
print("sub()运算结果：",end="")
print(operator.sub(a,b))

#使用mul()函数相乘2值
print("mul()运算结果：,"end="")
print(operator.mul(a,b))
