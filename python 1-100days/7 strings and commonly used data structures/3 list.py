fruits = ['frape','apple','strawberry','waxberry']
fruits += ['pitaya','pear','mango']
#列表切片
fruits2 = fruits[1:4]
print(fruits2)
#可以通过完整的切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4)
#可以通过反向切片操作获得到钻后的列表拷贝
fruits5 = fruits[::-1]
print(fruits5)

print('-------')
#下面列表实现对列表的排序操作

list6 = ['orange','apple','zoo','internationlization','blueberry']
list7 = sorted(list6)
#sorted函数返回咧白哦排序后的拷贝不会修改传入的列表
#函数的设计就应该向sorted函数一样尽量不产生副作用

list8 = sorted(list6,reverse = True)
#通过key关键字参数指定根据字符串长度进行排序而不是默认字母表顺序
list9 = sorted(list6,key = len)
print(list6)
print(list7)
print(list8)
print(list9)
#给定列表对象发出排序消息直接在列表对象进行排序
list6.sort(reverse = True)
print(list6)