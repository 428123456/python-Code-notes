import cmath

num = int(input("请输入一个数字！"))
new_num = cmath.sqrt(num)
print('%d的平方根为 %0.2f + %0.2fj' % (num, new_num.real, new_num.imag))

#print('{0}的平方根为{1：0.3f}+{2:0.3f}j.format(num,new_num.real,num_sqrt.imag))另一种格式化方式，复数
