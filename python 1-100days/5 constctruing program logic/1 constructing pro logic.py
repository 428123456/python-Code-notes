'''
找出所有水仙花数目
说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
'''

for num in range(100,1000):
    low = num % 10
    mid = num //10 %10
    high = num // 100
    if num == low ** 3 +mid **3 + high ** 3:
        print(num)
print('-------') 
'''
low = num % 10:这行代码计算了输入数字num除以10的余数，也就是个位数。例如，如果num是123,那么low就是3。

mid = num // 10 %10:这行代码首先将num除以10(整除),得到的结果是去掉个位数后的两位数。然后再对这个结果除以10取余数，得到的就是十位数。例如，如果num是123,那么mid就是2。

high = num // 100:这行代码直接将num除以100,得到的结果就是百位数。例如，如果num是123,那么high就是1。
'''
'''正整数反转'''

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
'''
具体解释如下：

reversed_num 是一个变量，用于存储反转后的数字。
num % 10 计算 num 除以 10 的余数，即 num 的个位数。
reversed_num * 10 将 reversed_num 乘以 10,相当于去掉了 reversed_num 的个位数。
reversed_num * 10 + num % 10 将反转后的数字与原数字的个位数相加，得到反转后的数字。
'''