x =int(input('x = '))
y =int(input('y = '))

for e in range(x,0,-1):
    if x % e ==0 and y % e ==0:
      print('%d和%d最大公约数%d' %(x,y,e))
      print('%d和%d最小公倍数：%d' %(x,y,x*y//e))
    break

'''
首先找出两个数的最大公约数(Greatest Common Divisor, GCD)。
然后使用公式：lcm(a, b) = a * b / gcd(a, b) 计算最小公倍数。
'''