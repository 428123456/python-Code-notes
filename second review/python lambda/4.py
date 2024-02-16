number = [1,2,3,4,5,6,7,8,9,10]
even_number = list(filter(lambda x: x%2 == 0, number))
print(even_number)
'''
filter 函数接收一个函数和一个迭代器作为参数，然后返回一个迭代器，该迭代器包含应用输入函数后结果为 True 的原迭代器的元素。

在你提供的类声明中，我们可以看到 filter 类的多个重载版本。这些重载版本允许 filter 函数接收不同类型的函数参数。每个重载版本都接收一个函数 __function 和一个迭代器 __iterable。

__function 是一个可调用对象，它接收一个参数并返回一个布尔值。如果 __function 返回 True，那么对应的元素将被包含在 filter 返回的迭代器中。

__iterable 是一个迭代器，它的元素将作为参数传递给 __function。

filter 类还定义了 __iter__ 和 __next__ 方法，这使得它成为一个迭代器。__iter__ 方法返回迭代器本身，__next__ 方法返回迭代器的下一个元素。

这是一个使用 filter 的简单示例：
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)

for num in even_numbers:
    print(num)
在这个示例中，filter 函数接收 is_even 函数和 numbers 列表作为参数，然后返回一个迭代器。当我们遍历这个迭代器时，它会返回 numbers 列表中的偶数。
'''