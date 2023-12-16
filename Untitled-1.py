def _sum(arr):
    sum = 0
    for i in arr:
        sum +=i
    return sum

arr = [1,2,3,4]
ans = _sum(arr)
print(ans)