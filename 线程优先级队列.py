#!/usr/bin/python3

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")

'''
这段代码是 Python 中使用 threading 模块和 queue 模块创建和管理线程的示例。

首先，我们定义了一个名为 myThread 的类，这个类继承自 threading.Thread 类。在 myThread 类中，我们定义了一个构造函数 __init__，这个函数接受三个参数：threadID、name 和 q。这三个参数分别表示线程的 ID、名称和工作队列。在构造函数中，我们首先调用了父类的构造函数 threading.Thread.__init__(self)，然后将传入的参数保存到类的实例变量中。

然后，我们在 myThread 类中定义了一个 run 方法。这个方法是 threading.Thread 类的一个重要方法，当我们调用一个线程的 start 方法时，实际上是在调用这个 run 方法。在 run 方法中，我们首先打印出一条消息表示线程开始，然后调用 process_data 函数处理数据，最后打印出一条消息表示线程结束。

process_data 函数接受两个参数：threadName 和 q。这个函数在一个循环中从工作队列中获取数据并处理，循环直到全局变量 exitFlag 被设置为 1。在处理数据之前，我们获取了一个线程锁，以确保在同一时间只有一个线程在处理数据。处理完数据后，我们释放了线程锁，允许其他线程处理数据。

在主程序中，我们创建了一个线程锁 queueLock 和一个工作队列 workQueue。然后创建了三个 myThread 类的实例，并调用它们的 start 方法来启动线程。start 方法会调用 run 方法，所以线程开始执行的是 run 方法中的代码。然后，我们将这三个线程添加到线程列表中，然后填充工作队列。最后，我们等待工作队列清空，然后设置 exitFlag 为 1，通知所有线程退出。最后，我们使用一个循环等待所有线程完成。在循环中，我们调用了每个线程的 join 方法，这个方法会阻塞主线程，直到调用 join 方法的线程结束。最后，我们打印出一条消息表示主线程结束。


'''