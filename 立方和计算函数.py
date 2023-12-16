#立方和计算函数
def sumOfseries(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i*i*i
    return sum

#调用函数
n = 4
print(sumOfseries(n))