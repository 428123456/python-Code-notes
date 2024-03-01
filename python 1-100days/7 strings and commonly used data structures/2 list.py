list1 = [1,3,5,7,100]
print(list1)
list2 = ['hello']*3
print(list2)
print(len(list1))
print(list1[0])
print(list1[4])
print(list1[-1])
print(list1[-3])
list1[2] =300
print(list1)
#通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
#通过for遍历列表元素
for elem in list1:
    print(elem)
#通过enumertate函数处理列表之后在遍历可以同时获得元素的索引和值
for index,elem in enumerate(list1):
    print(index,elem)

print('-------')
#如何向列表中添加元素以及如何让从列表中移除元素
list3 = [1,3,5,7,100]
#添加元素
list3.append(200)
list3.insert(1,400)
#合并2个元素
#list3.extend([1000,2000])
list3 += [1000,2000]
print(list3)
print(len(list3))

#先判断成员运算判断元素是不是在列表中，如果存在删除
if 3 in list3:
    list3.remove(3)

if 1234 in list3:
    list3.remove(1234)

print(list3)
#从指定位置删除元素
list3.pop(0)
list3.pop(len(list3) - 1)
#这段代码的作用是从名为list3的列表中移除最后一个元素。
print(list3)
#清空列表
list3.clear()
print(list3)


