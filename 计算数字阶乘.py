# 获取用户输入的数字
num = int(input("请输入一个数字"))

factorial = 1
#判断数字正反
if num < 0:
    print("负数没有阶乘")
elif num == 0:
    print("0的阶乘为0")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("%d的阶乘为%d" %(num,factorial))
    