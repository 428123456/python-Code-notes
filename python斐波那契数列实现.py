# python斐波那契数列实现

#获取用户输入数据
nterms = int(input("输出几项？"))

#第一项和第二项
n1 = 0
n2 = 1
count = 2

#判断数据合理？
if nterms <= 0:
    print("请输入一个正整数")
elif nterms ==1:
    print("非波那契数列：")
    print(n1)
else:
    print('斐波那契数列：')
    print(n1,",",n2,end = ',') 
    while count <nterms:
        nth = n1+n2
        print(nth,end=",")
        #更新值
        n1 = n2
        n2 = nth
        count +=1
        
    