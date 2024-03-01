'''
用for 循环实现1-100求和
'''
sum = 0

for x in range(101):
    sum += x
print(sum)

'''偶数求和'''
sum1 = 0
for x in range(2,101,2):
    sum1 += x
print(sum1)

'''使用分支结构'''
sum2 = 0
for x in range(1,101):
    if x % 2 ==0:
        sum += x
print(sum2)

'''while循环结构
猜出数字大小，以及输出次数
'''
import random

answeat = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入数字：'))
    if number <answeat:
        print('大一点')
    elif number > answeat:
        print('小一点')
    else:
        print('恭喜你猜对了！')
        break
    print('你总共猜 %d 次' % counter)
    if counter >7:
        print('你的智商余额明显不足')

