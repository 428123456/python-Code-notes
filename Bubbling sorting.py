def bubbleSort(arr):
    """
    Sorts the given array using the bubble sort algorithm.

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    None. The array is sorted in-place.
    """

    n = len(arr)

    #遍历所有数据元素
    for i in range(n):

        #last i elements are already in place
        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [64,34,25,12,22,11,90]

bubbleSort(arr)
print("排序后的数组")
for i in range(len(arr)):
    print("%d"%arr[i])

'''
这段代码实现了冒泡排序算法。冒泡排序是一种简单的排序算法，它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

在 `bubbleSort` 函数中，首先获取了输入数组 `arr` 的长度 `n`。然后，通过两层循环来实现冒泡排序。外层循环 `for i in range(n):` 用于控制遍历的次数，内层循环 `for j in range(0,n-i-1):` 用于在每次遍历中，通过比较和交换相邻的元素来将最大的元素“冒泡”到数组的末尾。

在内层循环中，如果当前元素 `arr[j]` 大于其相邻的下一个元素 `arr[j+1]`，则交换这两个元素的位置。这样，每一次内层循环结束后，最大的元素都会被移动到数组的末尾。

需要注意的是，每次外层循环结束后，数组末尾的元素都是已经排序好的，因此在内层循环中，我们只需要遍历到 `n-i-1` 的位置即可，这也是为什么内层循环的范围是 `range(0,n-i-1)`。

这个函数没有返回值，因为它直接修改了输入的数组 `arr`，即所谓的“原地排序”。'''