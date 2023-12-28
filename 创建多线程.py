#!/usr/bin/python3

import _thread
import time

# 为线程定义一个函数
def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
    _thread.start_new_thread(print_time,("thread-1",2,))
    _thread.start_new_thread(print_time,("thread-2",4,))
except:
    print("Error:无法启动线程")
    
while 1:
    pass
'''
在 Python 中，"bare except" 是指一个没有指定异常类型的 except 语句。这种语句会捕获所有类型的异常，包括系统退出事件和键盘中断事件等。这通常是不推荐的，因为它可能会隐藏真正的错误，使得问题难以调试。

在你的代码中：

你使用了一个 bare except 语句来捕获可能出现的所有异常。如果 _thread.start_new_thread() 函数抛出了一个异常，你的代码会捕获它并打印出一条错误消息。

一个更好的做法是指定你希望捕获的异常类型。例如，如果你知道 _thread.start_new_thread() 可能会抛出 RuntimeError，你可以这样写：

这样，只有 RuntimeError 会被捕获，其他类型的异常会被忽略，这可以帮助你发现和修复代码中的其他问题。


'''