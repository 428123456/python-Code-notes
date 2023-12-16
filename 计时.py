import time

print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:    
    input("")  # 如果是 python 2.x 版本请使用 raw_input()    
    starttime = time.time()    
    print('开始')    
    try:        
        while True:            
            print('\r计时: ', round(time.time() - starttime, 0), '秒', end="")            
            time.sleep(1)    
    except KeyboardInterrupt:        
        print('\n结束')        
        endtime = time.time()        
        print('总共的时间为:', round(endtime - starttime, 2), 'secs')        
        break

"""
此处的input("")用于等待用户按下回车键，以开始计时。
如果使用的是Python 2.x版本，请使用raw_input()函数代替input()函数。
"""
    