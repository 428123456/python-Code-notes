def Merge(dict1,dict2):
    return(dict2.update(dict1))

#2个字典
dict1 = {'a':10,'b':8}
dict2 = {'d':6,'c':4}

#返回 None
print(Merge(dict1,dict2))

#dict2合并dict1
print(dict2)

