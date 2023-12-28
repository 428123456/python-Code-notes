def shellSort(arr):

    n = len(arr)
    gap = int(n/2)

    while gap > 0:

        for i in range(gap,n):

            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
                arr[j] =temp
                #这个函数使用插入排序算法中的一个步骤，将元素temp按照升序插入到arr数组中。当遍历到位置j时，如果arr[j]大于temp并且还有足够的位置向前移动，则将arr[j]的元素依次向前移动一个位置，然后将temp插入到该位置。
        gap = int(gap/2)
        #这个函数将变量gap除以2并向下取整，然后将结果赋值给变量gap。
arr = [12,34,54,2,3]

n = len(arr)
print("排序前：")
for i in range(n):
    print(arr[i]),

shellSort(arr)

print("\n排序后:")
for i in range(n):
    print(arr[i])