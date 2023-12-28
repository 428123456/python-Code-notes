def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # 使用列表推导式初始化临时数组
    L = arr[l : m + 1]
    R = arr[m + 1 : r + 1]

    # 合并临时数组到原数组
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # 复制剩余元素从L到arr
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # 复制剩余元素从R到arr
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# 测试数据
arr = [12, 11, 13, 5, 6, 7]
print('给定数组')
for i in arr:
    print(i)

# 调用归并排序
n = len(arr)
merge_sort(arr, 0, n - 1)
print("\n排序后的数组")
for i in arr:
    print(i)