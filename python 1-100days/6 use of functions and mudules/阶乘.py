# 输入M和N计算C(M,N)

m = int(input('m = '))
n = int(input('n = '))

fm = 1
for num in range(1,m+1):
    fm *= num
fn = 1
for num in range(1,n+1):
    fn *= num
fm_n = 1
for num in range(1,m-n+1):
    fm_n *= num
print(fm//fn//fm_n)

#事实上，上面的问题等同于将8个苹果分成四组
#每组至少一个苹果有多少种方案。
#想到这一点问题的答案就呼之欲出了。

#使用函数计算

def fac(num):
    result = 1
    for num in range(1,num+1):
        result *= n
    return result

m = int(input(' m = '))
n = int(input(' n = '))
print(fac(m)//fac(n)//fac(m-n))