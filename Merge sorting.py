def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
        '''这段代码是在 Python 中对数组进行操作。`L[i] = arr[l + i]` 这行代码的含义是将 `arr` 数组中索引为 `l + i` 的元素赋值给 `L` 数组中索引为 `i` 的元素。

在 Python 中，数组的索引是从 0 开始的。所以 `arr[l + i]` 表示的是 `arr` 数组中的第 `l + i + 1` 个元素（如果从 1 开始计数的话）。

这段代码可能出现在归并排序算法中。归并排序是一种分治算法，它将一个大问题分解为两个或更多的相同或相似的小问题，然后将小问题的解合并以得到大问题的解。在归并排序中，我们需要创建一个临时数组来存储排序后的元素，这时就可能会用到这样的操作。

需要注意的是，数组的索引必须在有效范围内，即 `0 <= 索引 < 数组长度`，否则会引发 `IndexError` 错误。所以在使用这样的操作时，需要确保 `l + i` 的值不超过 `arr` 的长度。'''

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # merge the temp arrays back into arr[l..r]
    i = 0  # initial index of first subarray
    j = 0  # initial index of second subarray
    k = l  # initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        '''这段代码是一个合并排序算法中的合并步骤。它通过比较两个临时数组L和R中的元素，将较小的元素逐个复制到原数组arr中，并更新对应的索引i、j和k。当其中一个临时数组的所有元素都复制完后，将剩余的另一个数组的元素复制到arr的末尾。'''

    # copy the remaining elements of L[]
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        '''这个函数使用了while循环，当i小于n1时，将L[i]赋值给arr[k]，然后i和k分别增加1。'''

    # copy the remaining elements of R[]
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        '''这个代码片段实现了归并排序算法。mergeSort函数将数组拆分成两部分，分别对左右两部分递归调用mergeSort函数，直到数组长度为1。然后通过调用merge函数将排好序的两部分合并成一个有序的数组。这个过程重复进行，直到整个数组排序完成。'''

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print('给定数组')
for i in range(n):
    print("%d" % arr[i])

mergeSort(arr, 0, n - 1)
print("\n\n排序后的数组")
for i in range(n):
    print("%d" % arr[i])
