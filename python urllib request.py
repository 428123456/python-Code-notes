'''
以上代码使用 urlopen 打开一个 URL，然后使用 read() 函数获取网页的 HTML 实体代码。
read() 是读取整个网页内容，我们可以指定读取的长度：
'''
from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
print(myURL.read())
'''
以上代码使用 urlopen 打开一个 URL，然后使用 read() 函数获取网页的 HTML 实体代码。
read() 是读取整个网页内容，我们可以指定读取的长度：
'''
from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
print(myURL.read(300))

#除read()外，还有readline()和readlines()，readline()是读取一行，readlines()是读取所有行，返回一个列表，每行是列表的一个元素。

from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
print(myURL.readline()) #读取一行

readlines - 读取文件的全部内容，它会把读取内容复制给一个列表变量

from rullib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
lines = myURL.readlines()
for line in lines:
    print(line)
#完结以下为ai总结

import gzip
import io
from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
compressed_file = io.BytesIO(myURL.read())
decompressed_file = gzip.GzipFile(fileobj=compressed_file)

for line in decompressed_file:
    print(line.decode().strip())

'''
这段代码使用 Python 的 urllib 库从指定的 URL（在这种情况下是 "https://www.runoob.com/"）获取数据。然后，它打印出从该 URL 读取的内容。
在你的输出中，你看到的是从该 URL 获取的原始字节数据。这些数据被编码为 gzip 压缩的 HTML，这就是为什么它看起来像一堆无法解读的字符。
如果你想看到人类可读的 HTML,你需要解压缩和解码这些数据。你可以使用以下代码来实现：
这段代码首先读取 URL 的内容到一个 BytesIO 对象中，然后使用 gzip 库的 GzipFile 函数来解压缩这些数据。最后，它逐行打印出解压缩后的数据，每行都被解码为字符串并去除了前后的空格。
'''
