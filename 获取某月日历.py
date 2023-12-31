import time

def progress_bar(duration):
    scale = 50
    print("开始".center(scale//2, "-"))

    start = time.time()
    for i in range(scale+1):
        elapsed = time.time() - start
        percent = (i/scale)*100
        a = '*' * i
        b = '.' * (scale-i)
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(percent, a, b, elapsed), end='')
        time.sleep(duration/scale)
    print("\n" + "结束".center(scale//2,'-'))

# 调用函数，进度条持续时间为2秒
progress_bar(2)