#!/usr/bin/python3

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.delay, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")


'''
这段代码是 Python 中使用 `threading` 模块创建和启动线程的示例。在这个示例中，我们首先定义了一个名为 `myThread` 的类，这个类继承自 `threading.Thread` 类。

在 `myThread` 类中，我们定义了一个构造函数 `__init__`，这个函数接受三个参数：`threadID`、`name` 和 `delay`。这三个参数分别表示线程的 ID、名称和延迟时间。在构造函数中，我们首先调用了父类的构造函数 `threading.Thread.__init__(self)`，然后将传入的参数保存到类的实例变量中。

然后，我们在 `myThread` 类中定义了一个 `run` 方法。这个方法是 `threading.Thread` 类的一个重要方法，当我们调用一个线程的 `start` 方法时，实际上是在调用这个 `run` 方法。在 `run` 方法中，我们首先打印出一条消息表示线程开始，然后调用 `print_time` 函数，最后打印出一条消息表示线程结束。

`print_time` 函数接受三个参数：`threadName`、`delay` 和 `counter`。这个函数在一个循环中打印出当前时间，循环的次数由 `counter` 参数决定。

在主程序中，我们创建了两个 `myThread` 类的实例，然后调用它们的 `start` 方法来启动线程。`start` 方法会调用 `run` 方法，所以线程开始执行的是 `run` 方法中的代码。然后，我们调用 `join` 方法等待线程结束。`join` 方法会阻塞主线程，直到调用 `join` 方法的线程结束。最后，我们打印出一条消息表示主线程结束。
'''