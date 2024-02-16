numbers = [1,2,3,4,5,6,7,8,9,10]

squared = list(map(lambda x:x**2,numbers))
print(squared)

'''在你的代码中，你提到了 map，这是 Python 的内置函数。map 函数接收一个函数和一个或多个迭代器作为参数，然后返回一个迭代器，该迭代器将输入函数应用于每个给定的迭代器的元素。

在你提供的类声明中，我们可以看到 map 类的多个重载版本。这些重载版本允许 map 函数接收不同数量的迭代器参数。每个重载版本都接收一个函数 __func 和一个或多个迭代器 __iter1、__iter2 等。

__func 是一个可调用对象，它接收与提供的迭代器数量相同的参数。例如，如果你提供了两个迭代器，那么 __func 应该是一个接收两个参数的函数。

__iter1、__iter2 等是迭代器，它们的元素将作为参数传递给 __func。

map 类还定义了 __iter__ 和 __next__ 方法，这使得它成为一个迭代器。__iter__ 方法返回迭代器本身，__next__ 方法返回迭代器的下一个元素。

这是一个使用 map 的简单示例：

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)

for num in squares:
    print(num)
    
在这个示例中，map 函数接收 square 函数和 numbers 列表作为参数，然后返回一个迭代器。当我们遍历这个迭代器时，它会返回 numbers 列表中每个元素的平方。
'''