def countSort(arr):
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]
    '''这个函数创建了两个长度为256的列表output和count,并初始化为0。'''
    ans = ['' for _ in arr]
    #这个函数创建了一个包含与列表arr一样数量的空字符串的列表。循环变量_表示不关心循环变量的值。
    for i in arr:
        count[ord(i)] += 1
        #这个函数count[ord(i)]将字符i的ASCII码转换为整数，并将对应位置的元素加1。
    for i in range(256):
        count[i] += count[i-1]
        #该函数通过将count[i]的值增加count[i-1]的值，实现对列表count中每个元素的累加。
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
        #这个函数的作用是将输入列表arr中的元素按照ASCII码进行排序，并将排序后的结果存储在output列表中。函数首先通过count列表记录每个ASCII码出现的次数，然后遍历arr列表，将元素按照ASCII码存储到output列表中，并将对应的ASCII码次数减1。
    for i in range(len(arr)):
        ans[i] = output[i]
        #这个函数将变量output的第i个元素赋值给变量ans的第i个元素。
    return ans

arr = "wwwrunoobcom"
ans = countSort(arr)
print("字符数组排序%s"%("".join(ans)))
